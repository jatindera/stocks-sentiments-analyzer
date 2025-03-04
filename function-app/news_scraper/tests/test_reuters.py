import pytest
from news_scraper.parsers.reuters import parse_reuters


# Sample HTML for testing (simplified)
SAMPLE_HTML = """
<html>
    <body>
        <article class="story">
            <h3>Market rallies amid AI boom</h3>
            <a href="/business/markets/article1.html">Read more</a>
            <time datetime="2024-03-01T12:00:00Z"></time>
        </article>
        <article class="story">
            <h3>Tech stocks surge as earnings beat estimates</h3>
            <a href="/business/markets/article2.html">Read more</a>
            <time datetime="2024-03-02T14:30:00Z"></time>
        </article>
    </body>
</html>
"""

@pytest.fixture
def sample_html():
    """Returns sample HTML content for testing."""
    return SAMPLE_HTML

def test_parse_reuters(sample_html):
    """Tests the Reuters news parser for extracting article details."""
    articles = parse_reuters(sample_html)

    # Ensure at least 2 articles are found
    assert len(articles) == 2

    # Validate the extracted data
    assert articles[0]["title"] == "Market rallies amid AI boom"
    assert articles[0]["url"].endswith("/business/markets/article1.html")
    assert articles[0]["date"] == "2024-03-01T12:00:00Z"
    assert articles[0]["source"] == "Reuters"

    assert articles[1]["title"] == "Tech stocks surge as earnings beat estimates"
    assert articles[1]["url"].endswith("/business/markets/article2.html")
    assert articles[1]["date"] == "2024-03-02T14:30:00Z"
    assert articles[1]["source"] == "Reuters"
