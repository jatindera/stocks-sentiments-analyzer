from bs4 import BeautifulSoup
from ..config import NEWS_SOURCES

def parse_economic_times(html_content):
    """Extracts news articles from Economic Times."""
    soup = BeautifulSoup(html_content, "html.parser")
    articles = []
    base_url = NEWS_SOURCES["economic_times"]["base_url"]

    for item in soup.select(".eachStory")[:5]:  # Get top 5 articles
        title_tag = item.find("h3")
        link_tag = item.find("a", href=True)

        if not title_tag or not link_tag:
            continue

        # Ensure we always get a full URL
        full_url = link_tag["href"]
        if not full_url.startswith("http"):
            full_url = base_url + full_url

        articles.append({
            "title": title_tag.get_text(strip=True),
            "url": full_url,
            "date": "Today",
            "source": "Economic Times"
        })

    return articles
