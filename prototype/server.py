# server.py
# Our FastAPI web server.

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from prototype.questions import QUESTIONS

app = FastAPI()

# API endpoints go first
@app.get("/api/questions")
def get_questions():
    return {"questions": QUESTIONS}

# Mount the frontend folder to serve index.html, app.js, and styles
# The html=True argument makes it automatically serve index.html at the root URL
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")