import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# News Sources with Base URLs
NEWS_SOURCES = {
    "moneycontrol": {
        "base_url": "https://www.moneycontrol.com",
        "news_url": "https://www.moneycontrol.com/news/business/markets/"
    },
    "economic_times": {
        "base_url": "https://economictimes.indiatimes.com",
        "news_url": "https://economictimes.indiatimes.com/markets/stocks"
    },
    "reuters": {
        "base_url": "https://www.reuters.com",
        "news_url": "https://www.reuters.com/business/markets/"
    }
}

# Headers for requests (to prevent blocking)
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )
}

# Azure Storage Config
AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
AZURE_BLOB_CONTAINER = os.getenv("AZURE_BLOB_CONTAINER")
