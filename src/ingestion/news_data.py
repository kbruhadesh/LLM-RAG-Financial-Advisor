import pandas as pd
from datetime import datetime, timedelta
from newsapi import NewsApiClient
from langchain_core.documents import Document
from config import NEWS_DAYS_LOOKBACK, NEWS_PAGE_SIZE, NEWS_LANGUAGE

from config import NEWS_API_KEY

if not NEWS_API_KEY:
    raise RuntimeError(
        "NEWS_API_KEY not set. Please set it as an environment variable."
    )


def load_news_documents(
    query: str,
    api_key: str,
    days: int | None = None
):
    days = days or NEWS_DAYS_LOOKBACK

    newsapi = NewsApiClient(api_key=api_key)

    to_date = datetime.utcnow()
    from_date = to_date - timedelta(days=days)

    response = newsapi.get_everything(
        q=query,
        from_param=from_date.strftime("%Y-%m-%d"),
        to=to_date.strftime("%Y-%m-%d"),
        language=NEWS_LANGUAGE,
        sort_by="relevancy",
        page_size=NEWS_PAGE_SIZE,
    )

    articles = response.get("articles", [])
    documents = []

    for art in articles:
        if not art.get("title") or not art.get("description"):
            continue

        content = (
            f"Title: {art['title']}\n"
            f"Source: {art['source']['name']}\n"
            f"Published: {art['publishedAt']}\n\n"
            f"{art['description']}"
        )

        documents.append(
            Document(
                page_content=content,
                metadata={
                    "dataset": "News",
                    "source": art["source"]["name"],
                    "published": art["publishedAt"]
                }
            )
        )

    return documents
