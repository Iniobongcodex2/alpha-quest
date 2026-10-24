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

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def seed_data():
    db = SessionLocal()
    
    # Wipe old easy questions
    db.query(Question).delete()
    
    new_questions = [
        # Advanced Math
        {"subject": "Math World", "prompt": "If 4x - 7 = 2x + 9, what is the value of x?", "options": "['A) 2', 'B) 4', 'C) 8', 'D) 16']", "correct_answer": "C", "explanation": "Subtract 2x from both sides (2x - 7 = 9). Add 7 to both sides (2x = 16). Divide by 2 (x = 8)."},
        {"subject": "Math World", "prompt": "A right-angled triangle has legs of 6cm and 8cm. What is the length of the hypotenuse?", "options": "['A) 10cm', 'B) 12cm', 'C) 14cm', 'D) 16cm']", "correct_answer": "A", "explanation": "Pythagorean theorem: a² + b² = c². 6² + 8² = 36 + 64 = 100. The square root of 100 is 10."},
        {"subject": "Math World", "prompt": "What is the probability of rolling a sum of 7 with two standard 6-sided dice?", "options": "['A) 1/6', 'B) 1/8', 'C) 1/12', 'D) 7/36']", "correct_answer": "A", "explanation": "There are 6 ways to roll a 7 out of 36 possible outcomes (6/36 = 1/6)."},
        
        # Advanced English
        {"subject": "English Kingdom", "prompt": "Identify the underlined clause (or phrase) in meaning: 'Because it was raining, we stayed inside.' What type of clause is 'Because it was raining'?", "options": "['A) Independent clause', 'B) Dependent (subordinate) clause', 'C) Prepositional phrase', 'D) Gerund phrase']", "correct_answer": "B", "explanation": "It has a subject and verb but cannot stand alone as a complete sentence, making it a dependent clause."},
        {"subject": "English Kingdom", "prompt": "Which sentence is written in the passive voice?", "options": "['A) The dog chased the ball.', 'B) The ball was chased by the dog.', 'C) The dog is chasing the ball.', 'D) The dog will chase the ball.']", "correct_answer": "B", "explanation": "In passive voice, the subject (the ball) receives the action, rather than doing it."},
        {"subject": "English Kingdom", "prompt": "What is the meaning of the idiom 'to bite the bullet'?", "options": "['A) To eat something hard', 'B) To endure a painful or difficult situation', 'C) To speak angrily', 'D) To make a loud noise']", "correct_answer": "B", "explanation": "It means to face a difficult or unpleasant situation with courage."},

        # Advanced Science
        {"subject": "Science Lab", "prompt": "Which of Newton's Laws states that 'for every action, there is an equal and opposite reaction'?", "options": "['A) First Law', 'B) Second Law', 'C) Third Law', 'D) Law of Gravitation']", "correct_answer": "C", "explanation": "Newton's Third Law of Motion explains action-reaction pairs."},
        {"subject": "Science Lab", "prompt": "What is the primary greenhouse gas emitted by human activities?", "options": "['A) Oxygen', 'B) Carbon Dioxide', 'C) Nitrogen', 'D) Helium']", "correct_answer": "B", "explanation": "Carbon dioxide (CO2) is the primary greenhouse gas emitted through human activities like burning fossil fuels."},
        {"subject": "Science Lab", "prompt": "Which part of the human brain controls balance and coordination?", "options": "['A) Cerebrum', 'B) Brainstem', 'C) Cerebellum', 'D) Hypothalamus']", "correct_answer": "C", "explanation": "The cerebellum is located at the back of the brain and coordinates voluntary movements and balance."},

        # Advanced Logic & Discovery
        {"subject": "Logic Temple", "prompt": "If 5 machines take 5 minutes to make 5 widgets, how long would it take 100 machines to make 100 widgets?", "options": "['A) 5 minutes', 'B) 20 minutes', 'C) 100 minutes', 'D) 1 minute']", "correct_answer": "A", "explanation": "If 5 machines make 5 widgets in 5 minutes, 1 machine makes 1 widget in 5 minutes. Therefore, 100 machines make 100 widgets in 5 minutes."},
        {"subject": "Logic Temple", "prompt": "A farmer has 17 sheep. All but 9 run away. How many sheep does he have left?", "options": "['A) 8', 'B) 9', 'C) 17', 'D) 0']", "correct_answer": "B", "explanation": "The phrase 'all but 9' means exactly 9 did not run away. So he has 9 left."},
        {"subject": "Discovery World", "prompt": "What is the longest river in the world?", "options": "['A) The Amazon', 'B) The Nile', 'C) The Yangtze', 'D) The Mississippi']", "correct_answer": "B", "explanation": "While the Amazon is the largest by volume, the Nile is traditionally considered the longest river in the world."}
    ]

    for q in new_questions:
        db.add(Question(**q))
        
    db.commit()
    db.close()
    print("Successfully seeded 12 Grade 6+ hard questions to the database!")

# Run the seed function when this file loads
seed_data()