import requests
import json
import datetime
import logging
from .config import NEWS_SOURCES, HEADERS
from .parsers.moneycontrol import parse_moneycontrol
from .parsers.economic_times import parse_economic_times
from .parsers.reuters import parse_reuters
from .utils import upload_to_blob

# Mapping sites to their respective parsers
PARSERS = {
    "moneycontrol": parse_moneycontrol,
    "economic_times": parse_economic_times,
    "reuters": parse_reuters
}

def fetch_news():
    """Scrapes news articles from multiple sources."""
    all_articles = []

    for source, details in NEWS_SOURCES.items():
        url = details["news_url"]

        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            logging.error(f"❌ Error fetching {url}: {e}")
            continue  # Skip to the next source

        parser = PARSERS.get(source)
        if parser:
            articles = parser(response.text)
            all_articles.extend(articles)

    return all_articles
