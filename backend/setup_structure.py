import os

# Define the folder structure
folders = [
    "app/api/endpoints",
    "app/core",
    "app/models",
    "app/services/scraper",
    "app/services/ai",
    "app/services/storage",
    "app/services/alerts",
    "app/workers",
    "app/tests",
    "config",
    "scripts",
]

# Define the files to create
files = {
    "app/api/__init__.py": "",
    "app/api/endpoints/__init__.py": "",
    "app/api/endpoints/news.py": "# API routes for news",
    "app/api/endpoints/social.py": "# API routes for social media",
    "app/api/endpoints/reports.py": "# API routes for financial reports",
    "app/api/endpoints/sentiment.py": "# API routes for sentiment analysis",
    "app/api/endpoints/stocks.py": "# API routes for stock-related endpoints",
    "app/api/endpoints/alerts.py": "# API routes for alerts",

    "app/core/__init__.py": "",
    "app/core/config.py": "# Configuration settings",
    "app/core/logging_config.py": "# Logging configuration",
    "app/core/security.py": "# Security configurations",
    "app/core/exceptions.py": "# Custom exception handling",

    "app/models/__init__.py": "",
    "app/models/base.py": "# SQLAlchemy base model",
    "app/models/news.py": "# News model",
    "app/models/social.py": "# Social media model",
    "app/models/reports.py": "# Financial reports model",
    "app/models/sentiment.py": "# Sentiment model",
    "app/models/alerts.py": "# Alerts model",
    "app/models/stocks.py": "# Stocks metadata model",

    "app/services/__init__.py": "",
    "app/services/scraper/__init__.py": "",
    "app/services/scraper/news_scraper.py": "# Web scraper for news",
    "app/services/scraper/social_scraper.py": "# Web scraper for social media",
    "app/services/scraper/report_scraper.py": "# Scraper for financial reports",
    "app/services/scraper/utils.py": "# Utility functions for scraping",

    "app/services/ai/__init__.py": "",
    "app/services/ai/openai_analysis.py": "# OpenAI GPT-4o sentiment analysis",
    "app/services/ai/azure_nlp.py": "# Azure Cognitive Services NLP",
    "app/services/ai/finbert.py": "# FinBERT sentiment analysis",
    "app/services/ai/summarization.py": "# AI-driven text summarization",

    "app/services/storage/__init__.py": "",
    "app/services/storage/azure_blob.py": "# Azure Blob Storage operations",
    "app/services/storage/azure_cosmos.py": "# Azure CosmosDB operations",
    "app/services/storage/azure_sql.py": "# Azure SQL Database operations",
    "app/services/storage/vector_db.py": "# Pinecone vector search integration",
    "app/services/storage/cache.py": "# Redis caching system",

    "app/services/alerts/__init__.py": "",
    "app/services/alerts/alert_engine.py": "# Alert system logic",
    "app/services/alerts/push_notifications.py": "# Send alerts via email/SMS/WhatsApp",

    "app/workers/__init__.py": "",
    "app/workers/fetch_data.py": "# Fetch latest news and social posts",
    "app/workers/analyze_data.py": "# Process and analyze sentiment",
    "app/workers/schedule_tasks.py": "# Task scheduler for periodic jobs",
    "app/workers/queue_handler.py": "# Message queue handling (RabbitMQ, Azure Service Bus)",

    "app/tests/__init__.py": "",
    "app/tests/test_news.py": "# Unit test for news scraper & API",
    "app/tests/test_social.py": "# Unit test for social media API",
    "app/tests/test_reports.py": "# Unit test for financial reports parsing",
    "app/tests/test_sentiment.py": "# Unit test for sentiment analysis models",
    "app/tests/test_storage.py": "# Unit test for Azure storage & DB interactions",
    "app/tests/test_alerts.py": "# Unit test for alerting mechanisms",

    "app/__init__.py": "",
    "app/main.py": """# Entry point for FastAPI backend
from fastapi import FastAPI

app = FastAPI(title="AI-Powered Stock Sentiment Analyzer")

@app.get("/")
async def root():
    return {"message": "Welcome to the AI-Powered Stock Sentiment Analyzer"}
""",
    "app/dependencies.py": "# Dependency injection setup",

    "config/.env": "# Environment variables",
    "config/settings.json": "{\n  \"db_url\": \"\",\n  \"openai_api_key\": \"\",\n  \"azure_storage_account\": \"\"\n}",

    "scripts/__init__.py": "",
    "scripts/init_db.py": "# Initialize database schema",
    "scripts/migrate_db.py": "# Database migration script",
    "scripts/load_test_data.py": "# Load test data for development",
    "scripts/deploy_azure_resources.py": "# Deploy Azure resources script",

    "Dockerfile": """# Dockerfile for FastAPI backend
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
""",
    "docker-compose.yml": """version: '3.8'
services:
  backend:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - config/.env
    depends_on:
      - db
  db:
    image: postgres:latest
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: stock_sentiment
    ports:
      - "5432:5432"
""",
    "requirements.txt": """# Python dependencies
fastapi
uvicorn
sqlalchemy
pydantic
tweepy
requests
beautifulsoup4
openai
azure-cosmos
azure-storage-blob
pymupdf
""",
    "README.md": "# AI-Powered Stock Sentiment Analyzer",
    ".gitignore": """__pycache__/
*.pyc
.env
/.vscode/
logs/
data/
"""
}

# Function to create folders
def create_folders():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    print("✅ Folders created successfully.")

# Function to create files
def create_files():
    for file, content in files.items():
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
    print("✅ Files created successfully.")

if __name__ == "__main__":
    create_folders()
    create_files()
    print("🚀 Backend project structure has been successfully created!")
