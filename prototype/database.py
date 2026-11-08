# database.py
import json
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = "sqlite:///alpha_quest.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, index=True)
    xp = Column(Integer, default=0)
    avatar = Column(String, default="🦊") 
    last_bonus_date = Column(String, default="") 
    buildings = relationship("Building", back_populates="owner")

class Building(Base):
    __tablename__ = "buildings"
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    building_type = Column(String)
    position_x = Column(Integer, default=0) 
    position_y = Column(Integer, default=0) 
    owner = relationship("Player", back_populates="buildings")

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)
    prompt = Column(String)
    options = Column(String)
    correct_answer = Column(String)
    explanation = Column(String)

class Attempt(Base):
    __tablename__ = "attempts"
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    is_correct = Column(Integer) 

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def seed_data():
    db = SessionLocal()
    print("Checking for new questions...")
    
    try:
        with open("questions.json", "r", encoding="utf-8") as file:
            questions_data = json.load(file)
    except FileNotFoundError:
        print("questions.json not found. Skipping seed.")
        db.close()
        return
        
    existing_prompts = [q.prompt for q in db.query(Question).all()]
    
    new_added_count = 0
    for q in questions_data:
        if q["prompt"] not in existing_prompts:
            new_question = Question(
                subject=q["subject"],
                prompt=q["prompt"],
                options=q["options"],
                correct_answer=q["correct_answer"],
                explanation=q["explanation"]
            )
            db.add(new_question)
            new_added_count += 1
            
    db.commit()
    db.close()
    
    if new_added_count > 0:
        print(f"Successfully added {new_added_count} new questions to the database!")
    else:
        print("Database is up to date. No new questions to add.")

# Run the seed function when this file loads
seed_data()