from bs4 import BeautifulSoup
import logging
from ..config import NEWS_SOURCES

def parse_reuters(html_content):
    """Extracts news articles from Reuters."""
    soup = BeautifulSoup(html_content, "html.parser")
    articles = []
    base_url = NEWS_SOURCES["reuters"]["base_url"]

    for item in soup.select("article.story")[:5]:  # Get top 5 articles
        try:
            title_tag = item.find("h3")
            link_tag = item.find("a", href=True)
            date_tag = item.find("time", datetime=True)  # Look for date

            if not title_tag or not link_tag:
                continue  # Skip incomplete entries

            # Ensure full URL
            full_url = link_tag["href"]
            if not full_url.startswith("http"):
                full_url = base_url + full_url

            # Extract date if available, otherwise mark as 'Unknown'
            date = date_tag["datetime"] if date_tag else "Unknown"

            articles.append({
                "title": title_tag.get_text(strip=True),
                "url": full_url,
                "date": date,
                "source": "Reuters"
            })

        except Exception as e:
            logging.error(f"❌ Error parsing Reuters article: {e}")

    return articles
