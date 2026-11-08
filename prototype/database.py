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
    last_bonus_date = Column(String, default="") # <-- NEW: Tracks daily bonus
    buildings = relationship("Building", back_populates="owner")

class Building(Base):
    __tablename__ = "buildings"
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    building_type = Column(String)
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
    
    # ONLY seed if the database is completely empty
    if db.query(Question).count() == 0:
        print("Database is empty. Loading questions from JSON...")
        
        # Open and read the questions.json file
        with open("questions.json", "r", encoding="utf-8") as file:
            questions_data = json.load(file)
            
        # Add each question from the JSON to the database
        for q in questions_data:
            new_question = Question(
                subject=q["subject"],
                prompt=q["prompt"],
                options=q["options"],
                correct_answer=q["correct_answer"],
                explanation=q["explanation"]
            )
            db.add(new_question)
            
        db.commit()
        print("Successfully loaded questions from JSON into the database!")
    
    db.close()

# Run the seed function when this file loads
seed_data()