# Entry point for FastAPI backend
from fastapi import FastAPI

app = FastAPI(title="AI-Powered Stock Sentiment Analyzer")

@app.get("/")
async def root():
    return {"message": "Welcome to the AI-Powered Stock Sentiment Analyzer"}
