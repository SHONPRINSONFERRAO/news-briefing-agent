import os
import json
import logging
import os, json, requests
from mcp.server.fastmcp import FastMCP
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
mcp = FastMCP("news-server")
@mcp.tool()
def fetch_news(topic: str, num_articles: int = 5) -> str:
    """Fetch latest news."""
    logger.info(f"Tool fetch_news called with topic='{topic}' and num_articles={num_articles}")
    key = os.environ.get("NEWS_API_KEY", "")
    try:
        r = requests.get("https://newsapi.org/v2/everything", params={"q": topic, "apiKey": key, "pageSize": num_articles, "language": "en"}, timeout=10)
        r.raise_for_status()
        logger.info(f"Successfully fetched news for topic='{topic}'")
        articles = [{"title": a.get("title"), "source": a.get("source", {}).get("name"), "url": a.get("url")} for a in r.json().get("articles", [])]
        return json.dumps({"topic": topic, "articles": articles}, indent=2)
    except Exception as e: 
        logger.error(f"Error in fetch_news for topic='{topic}': {str(e)}")
        return json.dumps({"error": str(e)})
if __name__ == "__main__": mcp.run(transport="stdio")
