# database.py
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

# Create the tables
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# --- AUTO-SEED DATABASE ---
def seed_data():
    db = SessionLocal()
    # Check if empty
    if db.query(Question).count() == 0:
        print("Database is empty. Seeding questions...")
        new_questions = [
            {"subject": "Math World", "prompt": "What is 8 x 4?", "options": "['A) 24', 'B) 32', 'C) 36', 'D) 40']", "correct_answer": "B", "explanation": "8 times 4 is 32."},
            {"subject": "Math World", "prompt": "What is 100 - 45?", "options": "['A) 45', 'B) 55', 'C) 65', 'D) 75']", "correct_answer": "B", "explanation": "100 minus 45 leaves 55."},
            {"subject": "English Kingdom", "prompt": "Which word is an adjective?", "options": "['A) Run', 'B) Quickly', 'C) Beautiful', 'D) Dog']", "correct_answer": "C", "explanation": "An adjective describes a noun. 'Beautiful' describes something."},
            {"subject": "English Kingdom", "prompt": "What is the plural of 'Child'?", "options": "['A) Childs', 'B) Childes', 'C) Children', 'D) Child']", "correct_answer": "C", "explanation": "The plural of child is children."},
            {"subject": "Science Lab", "prompt": "What gas do plants breathe in?", "options": "['A) Oxygen', 'B) Carbon Dioxide', 'C) Nitrogen', 'D) Hydrogen']", "correct_answer": "B", "explanation": "Plants absorb carbon dioxide to make food."},
            {"subject": "Science Lab", "prompt": "What is H2O commonly known as?", "options": "['A) Salt', 'B) Water', 'C) Air', 'D) Sugar']", "correct_answer": "B", "explanation": "H2O is the chemical formula for water."},
            {"subject": "Logic Temple", "prompt": "What comes next in the sequence? 2, 4, 6, 8, __", "options": "['A) 9', 'B) 10', 'C) 11', 'D) 12']", "correct_answer": "B", "explanation": "The pattern is counting by 2s."},
            {"subject": "Logic Temple", "prompt": "If all birds can fly, and a robin is a bird, can a robin fly?", "options": "['A) Yes', 'B) No', 'C) Maybe', 'D) Only at night']", "correct_answer": "A", "explanation": "Based on the rule, since a robin is a bird, it can fly."},
            {"subject": "Discovery World", "prompt": "What is the largest ocean on Earth?", "options": "['A) Atlantic', 'B) Indian', 'C) Arctic', 'D) Pacific']", "correct_answer": "D", "explanation": "The Pacific Ocean is the largest and deepest."},
            {"subject": "Discovery World", "prompt": "Which continent is Egypt located in?", "options": "['A) Asia', 'B) Africa', 'C) Europe', 'D) South America']", "correct_answer": "B", "explanation": "Egypt is located in the northeast corner of Africa."}
        ]
        for q in new_questions:
            db.add(Question(**q))
        db.commit()
    db.close()

seed_data()
print("Database and tables created successfully!")