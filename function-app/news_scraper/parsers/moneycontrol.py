from bs4 import BeautifulSoup
import logging
from ..config import NEWS_SOURCES

def parse_moneycontrol(html_content):
    """Extracts news articles from Moneycontrol."""
    soup = BeautifulSoup(html_content, "html.parser")
    articles = []
    base_url = NEWS_SOURCES["moneycontrol"]["base_url"]

    for item in soup.select("li.clearfix")[:5]:  # Get top 5 articles
        try:
            title_tag = item.find("h2")
            link_tag = item.find("a", href=True)
            date_tag = item.find("span", class_="timing")  # Example: "1 hour ago"

            if not title_tag or not link_tag:
                continue  # Skip if essential data is missing

            # Ensure full URL
            full_url = link_tag["href"]
            if not full_url.startswith("http"):
                full_url = base_url + full_url

            # Extract date if available, otherwise default to "Unknown"
            date = date_tag.get_text(strip=True) if date_tag else "Unknown"

            articles.append({
                "title": title_tag.get_text(strip=True),
                "url": full_url,
                "date": date,
                "source": "Moneycontrol"
            })

        except Exception as e:
            logging.error(f"❌ Error parsing Moneycontrol article: {e}")

    return articles
