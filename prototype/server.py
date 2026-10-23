# server.py
import ast
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from prototype.database import SessionLocal, Player, Building, Question

app = FastAPI()

# --- Models ---
class ScoreData(BaseModel):
    nickname: str
    xp: int

class SpendData(BaseModel):
    nickname: str
    amount: int

# --- API ROUTES (Must be above app.mount) ---

@app.get("/api/questions")
def get_questions():
    # Fetch questions from the database
    db = SessionLocal()
    questions = db.query(Question).all()
    db.close()
    
    formatted_questions = []
    for q in questions:
        try:
            # This safely turns the text "['A) Mars', 'B) Earth']" back into a real Python list
            parsed_options = ast.literal_eval(q.options)
        except Exception:
            # If there's an error, fallback to a simple split
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

# --- STATIC FILES (Must be the VERY LAST line) ---
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")