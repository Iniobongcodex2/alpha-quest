# server.py
# Our FastAPI web server.

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from prototype.questions import QUESTIONS
from prototype.database import SessionLocal, Player

app = FastAPI()

# Define the data structure we expect from the frontend
class ScoreSubmission(BaseModel):
    nickname: str
    xp: int

# --- API Endpoints ---

@app.get("/api/questions")
def get_questions():
    return {"questions": QUESTIONS}

@app.post("/api/save-score")
def save_score(submission: ScoreSubmission):
    # 1. Open a database session
    db = SessionLocal()
    
    # 2. Create a new player entry
    new_player = Player(nickname=submission.nickname, xp=submission.xp)
    
    # 3. Save to the database
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    
    # 4. Close the connection
    db.close()
    
    return {"message": f"Successfully saved {submission.xp} XP for {submission.nickname}!"}

# --- Frontend Serving ---
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")