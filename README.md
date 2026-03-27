[![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![Gemini](https://img.shields.io/badge/Gemini_2.5_Flash-8E75B2?style=for-the-badge&logo=google-gemini&logoColor=white)](https://deepmind.google/technologies/gemini/)
# 📰 News Briefing AI Agent (Track 2)
An AI-powered news briefing agent built with **Google ADK**, **MCP (Model Context Protocol)**, and **Vertex AI (Gemini 2.5 Flash)**.
## 🎯 Project Goal
Demonstrate a real-world data-to-agent integration using the Model Context Protocol to fetch live news and generate AI-curated summaries.
## 🛠️ Architecture
- **Agent Framework:** Google ADK
- **Intelligence:** Gemini 2.5 Flash (via Vertex AI)
- **Tool Protocol:** MCP 
- **Data Source:** NewsAPI.org

## ✨ Key Features
- **Topic-Based Search:** Ask about AI, Tech, Sports, or any interest.
- **AI Bulletins:** Structured briefings with headlines, sources, and links.
- **MCP Integration:** Standardized tool-calling for real-world data.

```mermaid
graph LR
    A[User / UI] -- "Interaction" --> B(Cloud Run)
    B -- "Invoke" --> C(ADK Agent)
    C -- "Request" --> D{Gemini 2.5 Flash}
    C -- "Call Tool" --> E[MCP News Server]
    E -- "Fetch" --> F((NewsAPI))
    F -- "Articles" --> E
    E -- "JSON" --> C
    D -- "Briefing" --> C
    C -- "Response" --> B
    B -- "UI Update" --> A
    
    style D fill:#8E75B2,stroke:#fff,color:#fff
    style C fill:#34A853,stroke:#fff,color:#fff
    style B fill:#4285F4,stroke:#fff,color:#fff
    style E fill:#FBBC04,stroke:#fff,color:#333
```

## 🚀 Usage Examples

#### Request: 
What is the latest AI news?

#### Response: 
* Wall Street Has AI Psychosis - Wired (https://www.wired.com/story/wall-street-has-ai-psychosis/)
* Why people really hate AI - The Verge (https://www.theverge.com/podcast/897900/ai-trust-gap-killer-app-vergecast)
* Wikipedia bans AI-generated articles - The Verge (https://www.theverge.com/tech/901461/wikipedia-ai-generated-article-ban)
* AI companies want to harvest improv actors’ skills to train AI on human emotion - The Verge (https://www.theverge.com/ai-artificial-intelligence/893931/ai-companies-handshake-improv-actors-training-data)
* Signal’s Creator Is Helping Encrypt Meta AI - Wired (https://www.wired.com/story/signals-creator-is-helping-encrypt-meta-ai/)

## Created by Shon Ferrao

