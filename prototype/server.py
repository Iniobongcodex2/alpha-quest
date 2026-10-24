# server.py
import random
import ast
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from prototype.database import SessionLocal, Player, Building, Question, Attempt

app = FastAPI()

# --- Models ---
class ScoreData(BaseModel):
    nickname: str
    xp: int

class SpendData(BaseModel):
    nickname: str
    amount: int

class AttemptData(BaseModel):
    nickname: str
    question_id: int
    is_correct: bool

# --- API ROUTES ---

@app.get("/api/questions")
def get_questions(nickname: str = None):
    db = SessionLocal()
    all_questions = db.query(Question).all()
    
    if nickname:
        player = db.query(Player).filter(Player.nickname == nickname).first()
        if player:
            # MEMORY VAULT LOGIC: Find questions this player previously got wrong
            wrong_attempts = db.query(Attempt).filter(
                Attempt.player_id == player.id, 
                Attempt.is_correct == 0
            ).all()
            
            wrong_q_ids = list(set([a.question_id for a in wrong_attempts]))
            
            # Separate into "needs review" and "other"
            review_questions = [q for q in all_questions if q.id in wrong_q_ids]
            other_questions = [q for q in all_questions if q.id not in wrong_q_ids]
            
            random.shuffle(review_questions)
            random.shuffle(other_questions)
            
            # Priority: Put the ones they got wrong first!
            questions = review_questions + other_questions
            questions = questions[:10] 
        else:
            # New player, just shuffle and pick 10
            random.shuffle(all_questions)
            questions = all_questions[:10]
    else:
        # No nickname provided, just shuffle
        random.shuffle(all_questions)
        questions = all_questions[:10]

    db.close()
    
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
    else:
        player = Player(nickname=data.nickname, xp=data.xp)
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
    return {"message": "Attempt saved to Memory Vault"}

@app.get("/api/player/{nickname}")
def get_player(nickname: str):
    db = SessionLocal()
    player = db.query(Player).filter(Player.nickname == nickname).first()
    db.close()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return {"nickname": player.nickname, "xp": player.xp}

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
    new_building = Building(player_id=player.id, building_type="Library")
    db.add(new_building)
    
    db.commit()
    new_xp = player.xp
    db.close()
    
    return {"message": "XP spent and library built!", "new_xp": new_xp}

@app.get("/api/buildings/{nickname}")
def get_buildings(nickname: str):
    db = SessionLocal()
    player = db.query(Player).filter(Player.nickname == nickname).first()
    if not player:
        db.close()
        raise HTTPException(status_code=404, detail="Player not found")
    
    buildings = db.query(Building).filter(Building.player_id == player.id).all()
    db.close()
    return {"buildings": [b.building_type for b in buildings]}

@app.get("/api/leaderboard")
def get_leaderboard():
    db = SessionLocal()
    top_players = db.query(Player).order_by(Player.xp.desc()).limit(10).all()
    db.close()
    
    leaderboard_data = [
        {"nickname": p.nickname, "xp": p.xp} for p in top_players
    ]
    
    return {"leaderboard": leaderboard_data}

# --- STATIC FILES (Must be the VERY LAST line) ---
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")