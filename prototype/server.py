# server.py
# Our FastAPI web server.

from fastapi import FastAPI
from prototype.questions import QUESTIONS

app = FastAPI()

# The home page endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Alpha Quest API!"}

# A new endpoint to get the questions
@app.get("/api/questions")
def get_questions():
    return {"questions": QUESTIONS}