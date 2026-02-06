import os

# ---------- Vector / Embeddings ----------
VECTOR_DIR = "vector_store/investment"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ---------- LLM ----------
OLLAMA_MODEL = "mistral"

# ---------- News ----------
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

NEWS_DAYS_LOOKBACK = 7
NEWS_PAGE_SIZE = 30
NEWS_LANGUAGE = "en"
