# database.py
# This file sets up our SQLite database and defines our tables.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Create the database engine (this creates a file named alpha_quest.db)
DATABASE_URL = "sqlite:///./alpha_quest.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# 2. Create a base class for our models
Base = declarative_base()

# 3. Define our first table: Players
class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, index=True)
    xp = Column(Integer, default=0)

    # This special method tells Python how to print the object nicely
    def __repr__(self):
        return f"<Player(nickname='{self.nickname}', xp={self.xp})>"

# 4. Create the tables in the database
Base.metadata.create_all(bind=engine)

# 5. Set up a session to interact with the database later
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

print("Database and tables created successfully using SQLAlchemy!")