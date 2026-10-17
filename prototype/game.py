
# game.py
# This is the main engine that runs the quiz.

from questions import QUESTIONS

def play_game():
    score = 0
    total_xp = 0
    total_questions = len(QUESTIONS)
    
    print("===================================")
    print("       WELCOME TO ALPHA QUEST      ")
    print("===================================")
    
    for q in QUESTIONS:
        print(f"\nSubject: {q['subject']}")
        print(f"Question: {q['prompt']}")
        
        # Print the multiple choice options
        for option in q['options']:
            print(option)
            
        # Get the player's answer
        answer = input("\nEnter your answer (A, B, C, or D): ").strip().upper()
        
        # Check if the answer is correct
        if answer == q['correct_answer']:
            print("\n✅ Correct!")
            score += 1
            total_xp += 20  # Award 20 XP for a correct answer
            print("✨ +20 XP")
        else:
            print(f"\n❌ Incorrect. The correct answer was {q['correct_answer']}.")
            
        # Always show the explanation
        print(f"Explanation: {q['explanation']}")
        print("-" * 35)

    # Calculate Explorer Level (1 level for every 50 XP)
    explorer_level = (total_xp // 50) + 1

    # Show final score and XP
    print(f"\n🏆 Game Over! You scored {score} out of {total_questions}.")
    print(f"⭐ Total XP Earned: {total_xp}")
    print(f"🛡️ Explorer Level: {explorer_level}")

if __name__ == "__main__":
    play_game()