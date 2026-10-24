from database import SessionLocal, Question

db = SessionLocal()

# 1. Clear out old questions (so we don't get duplicates)
db.query(Question).delete()
db.commit()

# 2. Our expanded question bank
new_questions = [
    # Math
    {"subject": "Math World", "prompt": "What is 8 x 4?", "options": "['A) 24', 'B) 32', 'C) 36', 'D) 40']", "correct_answer": "B", "explanation": "8 times 4 is 32."},
    {"subject": "Math World", "prompt": "What is 100 - 45?", "options": "['A) 45', 'B) 55', 'C) 65', 'D) 75']", "correct_answer": "B", "explanation": "100 minus 45 leaves 55."},
    
    # English
    {"subject": "English Kingdom", "prompt": "Which word is an adjective?", "options": "['A) Run', 'B) Quickly', 'C) Beautiful', 'D) Dog']", "correct_answer": "C", "explanation": "An adjective describes a noun. 'Beautiful' describes something."},
    {"subject": "English Kingdom", "prompt": "What is the plural of 'Child'?", "options": "['A) Childs', 'B) Childes', 'C) Children', 'D) Child']", "correct_answer": "C", "explanation": "The plural of child is children."},
    
    # Science
    {"subject": "Science Lab", "prompt": "What gas do plants breathe in?", "options": "['A) Oxygen', 'B) Carbon Dioxide', 'C) Nitrogen', 'D) Hydrogen']", "correct_answer": "B", "explanation": "Plants absorb carbon dioxide to make food."},
    {"subject": "Science Lab", "prompt": "What is H2O commonly known as?", "options": "['A) Salt', 'B) Water', 'C) Air', 'D) Sugar']", "correct_answer": "B", "explanation": "H2O is the chemical formula for water."},
    
    # Logic
    {"subject": "Logic Temple", "prompt": "What comes next in the sequence? 2, 4, 6, 8, __", "options": "['A) 9', 'B) 10', 'C) 11', 'D) 12']", "correct_answer": "B", "explanation": "The pattern is counting by 2s."},
    {"subject": "Logic Temple", "prompt": "If all birds can fly, and a robin is a bird, can a robin fly?", "options": "['A) Yes', 'B) No', 'C) Maybe', 'D) Only at night']", "correct_answer": "A", "explanation": "Based on the rule, since a robin is a bird, it can fly."},
    
    # Discovery
    {"subject": "Discovery World", "prompt": "What is the largest ocean on Earth?", "options": "['A) Atlantic', 'B) Indian', 'C) Arctic', 'D) Pacific']", "correct_answer": "D", "explanation": "The Pacific Ocean is the largest and deepest."},
    {"subject": "Discovery World", "prompt": "Which continent is Egypt located in?", "options": "['A) Asia', 'B) Africa', 'C) Europe', 'D) South America']", "correct_answer": "B", "explanation": "Egypt is located in the northeast corner of Africa."}
]

# 3. Save to database
for q in new_questions:
    new_q = Question(
        subject=q["subject"],
        prompt=q["prompt"],
        options=q["options"],
        correct_answer=q["correct_answer"],
        explanation=q["explanation"]
    )
    db.add(new_q)

db.commit()
db.close()

print(f"Successfully saved {len(new_questions)} questions to the database!")