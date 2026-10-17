# test_game.py
# Automated tests for Alpha Quest prototype

from questions import QUESTIONS

def test_question_bank_loads():
    # Check that we actually have questions in our list
    assert len(QUESTIONS) > 0

def test_question_structure():
    # Check that the first question has all the keys we need for the game
    first_question = QUESTIONS[0]
    assert "id" in first_question
    assert "subject" in first_question
    assert "prompt" in first_question
    assert "correct_answer" in first_question