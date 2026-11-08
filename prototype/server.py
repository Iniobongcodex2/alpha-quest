# server.py
import random
import ast
import csv
import io
from fastapi.responses import StreamingResponse
from datetime import date
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from prototype.database import SessionLocal, Player, Building, Question, Attempt

app = FastAPI()

# --- Models ---
class ScoreData(BaseModel):
    nickname: str
    xp: int
    avatar: str = "🦊"

class SpendData(BaseModel):
    nickname: str
    amount: int
    building_type: str 
    position_x: int = 0 # <-- NEW
    position_y: int = 0 # <-- NEW

class AttemptData(BaseModel):
    nickname: str
    question_id: int
    is_correct: bool

# --- API ROUTES ---

@app.get("/api/questions")
def get_questions(nickname: str = None, subject: str = None, mode: str = None):
    db = SessionLocal()
    
    # 1. Boss Battle and Brain Rush Logic
    question_limit = 10
    if mode == "boss":
        question_limit = 15
        subject = "All" 
    elif mode == "rush":
        question_limit = 10
        subject = "All"
        
    # 2. Filter by selected world/subject
    if subject and subject != "All":
        all_questions = db.query(Question).filter(Question.subject == subject).all()
    else:
        all_questions = db.query(Question).all()
    
    # 3. Memory Vault Logic
    if nickname:
        player = db.query(Player).filter(Player.nickname == nickname).first()
        if player:
            # Find questions this player got wrong
            wrong_attempts = db.query(Attempt).filter(
                Attempt.player_id == player.id, 
                Attempt.is_correct == 0
            ).all()
            
            wrong_q_ids = list(set([a.question_id for a in wrong_attempts]))
            
            # Separate and shuffle
            review_questions = [q for q in all_questions if q.id in wrong_q_ids]
            other_questions = [q for q in all_questions if q.id not in wrong_q_ids]
            
            random.shuffle(review_questions)
            random.shuffle(other_questions)
            
            # Put wrong answers first, then fill with others
            questions = review_questions + other_questions
            questions = questions[:question_limit] 
        else:
            random.shuffle(all_questions)
            questions = all_questions[:question_limit]
    else:
        random.shuffle(all_questions)
        questions = all_questions[:question_limit]

    db.close()
    
    # 4. Format for frontend
    formatted_questions = []
    for q in questions:
        try:
            parsed_options = ast.literal_eval(q.options)
        except:
            parsed_options = q.options.split(", ")
            
        formatted_questions.append({
            "id": q.id,
            "subject": q.subject,
            "prompt": q.prompt,
            "options": parsed_options,
            "correct_answer": q.correct_answer,
            "explanation": q.explanation
        })
        
    return {"questions": formatted_questions}

@app.post("/api/save-score")
def save_score(data: ScoreData):
    db = SessionLocal()
    player = db.query(Player).filter(Player.nickname == data.nickname).first()
    if player:
        player.xp += data.xp
        player.avatar = data.avatar
    else:
        player = Player(nickname=data.nickname, xp=data.xp, avatar=data.avatar)
        db.add(player)
    db.commit()
    db.close()
    return {"message": "Score saved successfully!"}

@app.post("/api/save-attempt")
def save_attempt(data: AttemptData):
    db = SessionLocal()
    player = db.query(Player).filter(Player.nickname == data.nickname).first()
    
    if not player:
        player = Player(nickname=data.nickname, xp=0)
        db.add(player)
        db.commit()
        db.refresh(player)
        
    new_attempt = Attempt(
        player_id=player.id,
        question_id=data.question_id,
        is_correct=1 if data.is_correct else 0
    )
    db.add(new_attempt)
    db.commit()
    db.close()
    return {"message": "Attempt saved"}

@app.get("/api/player/{nickname}")
def get_player(nickname: str):
    db = SessionLocal()
    player = db.query(Player).filter(Player.nickname == nickname).first()
    db.close()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return {"nickname": player.nickname, "xp": player.xp, "avatar": player.avatar}

@app.post("/api/spend-xp")
def spend_xp(data: SpendData):
    db = SessionLocal()
    player = db.query(Player).filter(Player.nickname == data.nickname).first()
    
    if not player:
        db.close()
        raise HTTPException(status_code=404, detail="Player not found")
    
    if player.xp < data.amount:
        db.close()
        raise HTTPException(status_code=400, detail="Not enough XP")
    
    player.xp -= data.amount
    
    # SAVE COORDINATES
    new_building = Building(
        player_id=player.id, 
        building_type=data.building_type,
        position_x=data.position_x,
        position_y=data.position_y
    )
    db.add(new_building)
    
    db.commit()
    new_xp = player.xp
    db.close()
    
    return {"message": f"{data.building_type} built successfully!", "new_xp": new_xp}

@app.get("/api/buildings/{nickname}")
def get_buildings(nickname: str):
    db = SessionLocal()
    player = db.query(Player).filter(Player.nickname == nickname).first()
    if not player:
        db.close()
        raise HTTPException(status_code=404, detail="Player not found")
    
    buildings = db.query(Building).filter(Building.player_id == player.id).all()
    db.close()
    
    # RETURN COORDINATES
    return {"buildings": [
        {"type": b.building_type, "x": b.position_x, "y": b.position_y} for b in buildings
    ]}

@app.get("/api/leaderboard")
def get_leaderboard():
    db = SessionLocal()
    top_players = db.query(Player).order_by(Player.xp.desc()).limit(10).all()
    db.close()
    
    leaderboard_data = [
        {"nickname": p.nickname, "xp": p.xp, "avatar": p.avatar} for p in top_players
    ]
    
    return {"leaderboard": leaderboard_data}

@app.get("/api/badges/{nickname}")
def get_badges(nickname: str):
    db = SessionLocal()
    player = db.query(Player).filter(Player.nickname == nickname).first()
    
    if not player:
        db.close()
        return {"badges": []}
        
    earned_badges = []
    
    if player.xp >= 100:
        earned_badges.append({"name": "Bronze Explorer", "icon": "🥉", "description": "Earned 100 XP"})
    if player.xp >= 500:
        earned_badges.append({"name": "Silver Scholar", "icon": "🥈", "description": "Earned 500 XP"})
    if player.xp >= 1000:
        earned_badges.append({"name": "Gold Master", "icon": "🥇", "description": "Earned 1000 XP"})
    if player.xp >= 400:
        earned_badges.append({"name": "Boss Slayer", "icon": "👹", "description": "Proved your mastery in a Boss Battle"})
        
    buildings = db.query(Building).filter(Building.player_id == player.id).all()
    if len(buildings) > 0:
        earned_badges.append({"name": "Builder", "icon": "🏗️", "description": "Built your first structure"})

    db.close()
    return {"badges": earned_badges}

# --- TEACHER STUDIO API ---
@app.get("/api/teacher/students")
def get_all_students():
    db = SessionLocal()
    players = db.query(Player).order_by(Player.xp.desc()).all()
    db.close()
    
    student_list = [
        {"id": p.id, "nickname": p.nickname, "xp": p.xp, "avatar": p.avatar} for p in players
    ]
    
    return {"students": student_list}

@app.get("/api/teacher/report/{nickname}")
def get_student_report(nickname: str):
    db = SessionLocal()
    player = db.query(Player).filter(Player.nickname == nickname).first()
    
    if not player:
        db.close()
        raise HTTPException(status_code=404, detail="Student not found")
        
    wrong_attempts = db.query(Attempt).filter(
        Attempt.player_id == player.id,
        Attempt.is_correct == 0
    ).all()
    
    report_data = []
    seen_questions = set() 
    
    for attempt in wrong_attempts:
        if attempt.question_id not in seen_questions:
            question = db.query(Question).filter(Question.id == attempt.question_id).first()
            if question:
                report_data.append({
                    "subject": question.subject,
                    "prompt": question.prompt,
                    "correct_answer": question.correct_answer
                })
                seen_questions.add(question.id)
                
    db.close()
    return {"report": report_data}

@app.get("/api/teacher/export")
def export_students_csv():
    db = SessionLocal()
    players = db.query(Player).order_by(Player.xp.desc()).all()
    
    output = io.StringIO()
    writer = csv.writer(output)
    
    writer.writerow(["Student ID", "Nickname", "Total XP", "Avatar"])
    
    for p in players:
        writer.writerow([p.id, p.nickname, p.xp, p.avatar])
        
    db.close()
    
    output.seek(0)
    
    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=alpha_quest_roster.csv"}
    )

# --- DAILY BONUS API ---
@app.get("/api/daily-bonus/{nickname}")
def check_daily_bonus(nickname: str):
    db = SessionLocal()
    player = db.query(Player).filter(Player.nickname == nickname).first()
    
    if not player:
        db.close()
        raise HTTPException(status_code=404, detail="Player not found")
        
    today = str(date.today()) 
    
    if player.last_bonus_date != today:
        player.xp += 50
        player.last_bonus_date = today
        db.commit()
        db.close()
        return {"status": "success", "message": "Daily bonus claimed!", "xp_earned": 50}
    else:
        db.close()
        return {"status": "already_claimed", "message": "Come back tomorrow!", "xp_earned": 0}

# --- MEMORY VAULT DASHBOARD API ---
@app.get("/api/vault/{nickname}")
def get_vault(nickname: str):
    db = SessionLocal()
    player = db.query(Player).filter(Player.nickname == nickname).first()
    
    if not player:
        db.close()
        raise HTTPException(status_code=404, detail="Player not found")
        
    wrong_attempts = db.query(Attempt).filter(
        Attempt.player_id == player.id, 
        Attempt.is_correct == 0
    ).all()
    
    vault_data = []
    seen_questions = set()
    
    for attempt in wrong_attempts:
        if attempt.question_id not in seen_questions:
            question = db.query(Question).filter(Question.id == attempt.question_id).first()
            if question:
                vault_data.append({
                    "id": question.id,
                    "subject": question.subject,
                    "prompt": question.prompt,
                    "correct_answer": question.correct_answer,
                    "explanation": question.explanation
                })
                seen_questions.add(question.id)
                
    db.close()
    return {"vault": vault_data}

# --- STATIC FILES (Must be the VERY LAST line) ---
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")