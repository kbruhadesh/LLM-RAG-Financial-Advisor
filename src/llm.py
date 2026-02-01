from langchain_community.llms import Ollama
from config import OLLAMA_MODEL

def get_llm():
    return Ollama(
        model=OLLAMA_MODEL,
        temperature=0.2
    )
