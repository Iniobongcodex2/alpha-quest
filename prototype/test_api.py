# test_api.py
from fastapi.testclient import TestClient
from prototype.server import app

client = TestClient(app)

def test_read_homepage():
    # Test that the home page loads and returns a 200 OK status
    response = client.get("/")
    assert response.status_code == 200
    assert "ALPHA QUEST" in response.text

def test_get_questions():
    # Test that the questions API returns a list of questions
    response = client.get("/api/questions")
    assert response.status_code == 200
    data = response.json()
    assert "questions" in data
    assert len(data["questions"]) > 0

def test_leaderboard():
    # Test that the leaderboard API returns data
    response = client.get("/api/leaderboard")
    assert response.status_code == 200
    assert "leaderboard" in response.json()