import os
import json
import time
import datetime
import random
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from azure.storage.blob import BlobServiceClient
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Load environment variables from .env
load_dotenv("config/.env")

# Azure Blob Storage Configuration
AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
AZURE_BLOB_CONTAINER = os.getenv("AZURE_BLOB_CONTAINER")

# Define user agents to rotate
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/537.36",
]

# News sources to scrape
NEWS_SOURCES = {
    "moneycontrol": "https://www.moneycontrol.com/news/business/markets/",
    "economic_times": "https://economictimes.indiatimes.com/markets/stocks"
}

# Function to scrape news using requests and BeautifulSoup
def scrape_news(url):
    """Scrapes financial news articles from the given URL."""
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Error fetching {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    # Extract articles based on site-specific HTML structure
    if "moneycontrol" in url:
        articles = scrape_moneycontrol(soup)
    elif "indiatimes" in url:
        articles = scrape_economic_times(soup)

    return articles

# Function to extract articles from Moneycontrol
def scrape_moneycontrol(soup):
    """Extracts news articles from Moneycontrol."""
    articles = []
    for item in soup.select("li.clearfix")[:10]:  # Limit to 10 articles
        title_tag = item.find("h2")
        link_tag = item.find("a", href=True)

        if not title_tag or not link_tag:
            continue  # Skip if missing required elements

        title = title_tag.get_text(strip=True)
        link = link_tag["href"]
        date = datetime.datetime.utcnow().isoformat()

        articles.append({"title": title, "url": link, "source": "Moneycontrol", "date": date})

    return articles

# Function to extract articles from Economic Times
def scrape_economic_times(soup):
    """Extracts news articles from Economic Times."""
    articles = []
    for item in soup.select(".eachStory")[:10]:  # Limit to 10 articles
        title_tag = item.find("h3")
        link_tag = item.find("a", href=True)

        if not title_tag or not link_tag:
            continue

        title = title_tag.get_text(strip=True)
        link = "https://economictimes.indiatimes.com" + link_tag["href"]
        date = datetime.datetime.utcnow().isoformat()

        articles.append({"title": title, "url": link, "source": "Economic Times", "date": date})

    return articles

# Function to scrape JavaScript-heavy sites using Selenium
def scrape_with_selenium(url):
    """Uses Selenium to scrape JavaScript-heavy sites."""
    options = Options()
    options.headless = True  # Run in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(url)
        time.sleep(5)  # Allow JavaScript to load
        soup = BeautifulSoup(driver.page_source, "html.parser")
    finally:
        driver.quit()

    return scrape_news(url)  # Reuse existing parsing logic

# Function to upload scraped news to Azure Blob Storage
def upload_to_blob(news_data):
    """Uploads a JSON file of scraped news to Azure Blob Storage."""
    if not news_data:
        print("❌ No news articles found, skipping upload.")
        return

    blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
    container_client = blob_service_client.get_container_client(AZURE_BLOB_CONTAINER)

    now = datetime.datetime.utcnow()
    year, month, day = now.strftime("%Y"), now.strftime("%m"), now.strftime("%d")
    timestamp = now.strftime("%Y-%m-%dT%H-%M-%S")
    
    file_name = f"{year}/{month}/{day}/news_{timestamp}.json"
    json_data = json.dumps(news_data, indent=4)

    blob_client = container_client.get_blob_client(file_name)
    blob_client.upload_blob(json_data, overwrite=True)

    print(f"✅ News articles uploaded: {file_name}")

# Main function to run the scraper
def main():
    """Main execution function to scrape news from multiple sources."""
    all_articles = []

    for source, url in NEWS_SOURCES.items():
        print(f"🔍 Scraping {source}...")
        articles = scrape_news(url) if "moneycontrol" in url else scrape_with_selenium(url)
        all_articles.extend(articles)

    upload_to_blob(all_articles)

if __name__ == "__main__":
    main()
