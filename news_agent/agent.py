import os, sys
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
_SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mcp_news_server.py")
root_agent = LlmAgent(
    model="gemini-2.5-flash", name="news_briefing_agent",
    instruction="Summarize news articles beautifully into a briefing.",
    tools=[McpToolset(connection_params=StdioConnectionParams(server_params=StdioServerParameters(
        command=sys.executable, args=[_SCRIPT], env={**os.environ, "NEWS_API_KEY": os.environ.get("NEWS_API_KEY", "")}
    )))]
)
