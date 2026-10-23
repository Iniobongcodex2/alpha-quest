# database.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = "sqlite:///./alpha_quest.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()

# 1. Player Table
class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, index=True)
    xp = Column(Integer, default=0)
    
    # Relationship to buildings
    buildings = relationship("Building", back_populates="owner")

    def __repr__(self):
        return f"<Player(nickname='{self.nickname}', xp={self.xp})>"

# 2. Building Table
class Building(Base):
    __tablename__ = "buildings"
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    building_type = Column(String)

    owner = relationship("Player", back_populates="buildings")

    def __repr__(self):
        return f"<Building(type='{self.building_type}')>"

# 3. Question Table
class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String, index=True)
    prompt = Column(String)
    options = Column(String) 
    correct_answer = Column(String)
    explanation = Column(String)

    def __repr__(self):
        return f"<Question(prompt='{self.prompt}')>"

# 4. Create the tables
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

print("Database and tables created successfully using SQLAlchemy!")