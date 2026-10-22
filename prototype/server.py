# server.py
# Our FastAPI web server.

from fastapi import FastAPI
from fastapi.responses import FileResponse
from prototype.questions import QUESTIONS

app = FastAPI()

# Serve the frontend HTML file at the root URL
@app.get("/")
def read_root():
    return FileResponse("frontend/index.html")

# The API endpoint to get the questions
@app.get("/api/questions")
def get_questions():
    return {"questions": QUESTIONS}