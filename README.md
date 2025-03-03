# AI-Powered Stock Sentiment Analyzer

## 📌 Project Overview
The **AI-Powered Stock Sentiment Analyzer** is a web application that scrapes financial news, social media posts, and financial reports to analyze stock sentiment in real time. Using **GPT-4o, LangChain v0.3, and Pinecone**, it provides sentiment insights to help traders and investors make informed decisions. 

## 🚀 Features
- **Real-time Data Scraping**: Aggregates stock-related news from major sources.
- **Social Media Sentiment Analysis**: Extracts stock sentiment from Twitter (X), LinkedIn, and stock market forums.
- **LLM-Powered Sentiment Scoring**: Uses GPT-4o and FinBERT for accurate sentiment classification.
- **Stock-Specific Sentiment Dashboard**: Provides sentiment trends and analysis over time.
- **Custom Alerts & Notifications**: Notifies users about sudden sentiment shifts.
- **Scalable & Modular Architecture**: Built with FastAPI, ReactJS, and Next.js.

## 📂 Project Structure
```bash
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── endpoints/
│   │   │   │   ├── news.py  # API routes for news
│   │   │   │   ├── social.py  # API routes for social media
│   │   │   │   ├── reports.py  # API routes for financial reports
│   │   │   │   ├── sentiment.py  # API routes for sentiment analysis
│   │   │   │   ├── stocks.py  # API routes for stock-related endpoints
│   │   │   │   ├── alerts.py  # API routes for alerts
│   │   ├── core/
│   │   │   ├── config.py  # Configuration settings
│   │   │   ├── logging_config.py  # Logging configuration
│   │   │   ├── security.py  # Security configurations
│   │   │   ├── exceptions.py  # Custom exception handling
│   │   ├── models/
│   │   │   ├── base.py  # SQLAlchemy base model
│   │   │   ├── news.py  # News model
│   │   │   ├── social.py  # Social media model
│   │   │   ├── reports.py  # Financial reports model
│   │   │   ├── sentiment.py  # Sentiment model
│   │   │   ├── alerts.py  # Alerts model
│   │   │   ├── stocks.py  # Stocks metadata model
│   │   ├── services/
│   │   │   ├── scraper/
│   │   │   │   ├── news_scraper.py  # Web scraper for news
│   │   │   │   ├── social_scraper.py  # Web scraper for social media
│   │   │   │   ├── report_scraper.py  # Scraper for financial reports
│   │   │   │   ├── utils.py  # Utility functions for scraping
│   │   │   ├── ai/
│   │   │   │   ├── openai_analysis.py  # OpenAI GPT-4o sentiment analysis
│   │   │   │   ├── azure_nlp.py  # Azure Cognitive Services NLP
│   │   │   │   ├── finbert.py  # FinBERT sentiment analysis
│   │   │   │   ├── summarization.py  # AI-driven text summarization
│   │   │   ├── storage/
│   │   │   │   ├── azure_blob.py  # Azure Blob Storage operations
│   │   │   │   ├── azure_cosmos.py  # Azure CosmosDB operations
│   │   │   │   ├── azure_sql.py  # Azure SQL Database operations
│   │   │   │   ├── vector_db.py  # Pinecone vector search integration
│   │   │   │   ├── cache.py  # Redis caching system
│   │   │   ├── alerts/
│   │   │   │   ├── alert_engine.py  # Alert system logic
│   │   │   │   ├── push_notifications.py  # Send alerts via email/SMS/WhatsApp
│   │   ├── workers/
│   │   │   ├── fetch_data.py  # Fetch latest news and social posts
│   │   │   ├── analyze_data.py  # Process and analyze sentiment
│   │   │   ├── schedule_tasks.py  # Task scheduler for periodic jobs
│   │   │   ├── queue_handler.py  # Message queue handling (RabbitMQ, Azure Service Bus)
│   │   ├── tests/
│   │   │   ├── test_news.py  # Unit test for news scraper & API
│   │   │   ├── test_social.py  # Unit test for social media API
│   │   │   ├── test_reports.py  # Unit test for financial reports parsing
│   │   │   ├── test_sentiment.py  # Unit test for sentiment analysis models
│   │   │   ├── test_storage.py  # Unit test for Azure storage & DB interactions
│   │   │   ├── test_alerts.py  # Unit test for alerting mechanisms
│   │   ├── main.py  # Entry point for FastAPI backend
│   ├── config/
│   ├── scripts/
│
├── frontend/  # ReactJS & Next.js application
│   ├── src/
│   ├── pages/
│   ├── components/
│   ├── public/
│   ├── package.json
│   └── next.config.js
│
├── README.md  # Documentation
├── .gitignore
└── docker-compose.yml
```

## 🔧 Installation & Setup
### **1. Clone the Repository**
```bash
git clone https://github.com/jatindera/stocks-sentiments-analyzer.git
cd stocks-sentiments-analyzer
```

### **2. Backend Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### **3. Frontend Setup**
```bash
cd frontend
npm install
npm run dev
```

### **4. Run with Docker (Optional)**
```bash
docker-compose up --build
```

## 📞 Contact
For any queries, reach out via **your-email@example.com** or create an issue on GitHub.

