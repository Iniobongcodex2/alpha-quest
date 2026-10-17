# game.py
# This is the main engine that runs the quiz.

from questions import QUESTIONS

def play_game():
    score = 0
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
        else:
            print(f"\n❌ Incorrect. The correct answer was {q['correct_answer']}.")
            
        # Always show the explanation
        print(f"Explanation: {q['explanation']}")
        print("-" * 35)

    # Show final score
    print(f"\n🏆 Game Over! You scored {score} out of {total_questions}.")

# This makes sure the game only runs if we execute this file directly
if __name__ == "__main__":
    play_game()