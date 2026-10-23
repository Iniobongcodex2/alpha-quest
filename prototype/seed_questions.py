# seed_questions.py
import json
from database import SessionLocal, Question
from questions import QUESTIONS

db = SessionLocal()

# Check if we already seeded to avoid duplicates
existing = db.query(Question).first()
if existing:
    print("Questions already in database!")
else:
    for q in QUESTIONS:
        new_q = Question(
            subject=q["subject"],
            prompt=q["prompt"],
            options=json.dumps(q["options"]), # Convert list to text
            correct_answer=q["correct_answer"],
            explanation=q["explanation"]
        )
        db.add(new_q)
    db.commit()
    print(f"Successfully saved {len(QUESTIONS)} questions to the database!")

db.close()