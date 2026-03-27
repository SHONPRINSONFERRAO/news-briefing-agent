import os, json, requests
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("news-server")
@mcp.tool()
def fetch_news(topic: str, num_articles: int = 5) -> str:
    """Fetch latest news."""
    key = os.environ.get("NEWS_API_KEY", "")
    try:
        r = requests.get("https://newsapi.org/v2/everything", params={"q": topic, "apiKey": key, "pageSize": 5, "language": "en"}, timeout=10)
        r.raise_for_status()
        articles = [{"title": a.get("title"), "source": a.get("source", {}).get("name"), "url": a.get("url")} for a in r.json().get("articles", [])]
        return json.dumps({"topic": topic, "articles": articles}, indent=2)
    except Exception as e: return json.dumps({"error": str(e)})
if __name__ == "__main__": mcp.run(transport="stdio")
