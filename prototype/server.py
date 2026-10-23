# server.py
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from prototype.questions import QUESTIONS
from prototype.database import SessionLocal, Player

app = FastAPI()

# --- Schemas for incoming data ---
class ScoreData(BaseModel):
    nickname: str
    xp: int

class SpendData(BaseModel):
    nickname: str
    amount: int

# --- API Endpoints ---

@app.get("/api/questions")
def get_questions():
    return {"questions": QUESTIONS}

@app.post("/api/save-score")
def save_score(data: ScoreData):
    db = SessionLocal()
    # Find the player or create a new one
    player = db.query(Player).filter(Player.nickname == data.nickname).first()
    
    if player:
        player.xp += data.xp
    else:
        player = Player(nickname=data.nickname, xp=data.xp)
        db.add(player)
    
    db.commit()
    db.close()
    return {"message": "Score saved successfully!"}

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
    db.commit()
    new_xp = player.xp
    db.close()
    
    return {"message": "XP spent successfully", "new_xp": new_xp}

@app.get("/api/player/{nickname}")
def get_player(nickname: str):
    db = SessionLocal()
    player = db.query(Player).filter(Player.nickname == nickname).first()
    db.close()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return {"nickname": player.nickname, "xp": player.xp}

# --- Serve the frontend ---
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")