import streamlit as st

from ingestion.faq_data import load_faq_documents
from vectorstore.faq_store import build_faq_store
from pipelines.faq_qa import faq_qa_pipeline

from pipelines.investment_advisor import investment_advisor_pipeline

from router.intent_router import classify_intent
from utils.source_formatter import format_sources

from ingestion.news_data import load_news_documents
from vectorstore.news_store import build_news_store
from pipelines.news_qa import news_qa_pipeline

from memory.profile_extractor import extract_profile
from memory.session_memory import update_memory, get_profile

from config import NEWS_API_KEY


# ================= PAGE =================
st.set_page_config(page_title="Finance Assistant", page_icon="💰")
st.title("💰 Finance Intelligence Assistant")
st.caption("Local • Private • Powered by Mistral")

# ================= LOAD PIPELINES =================
@st.cache_resource
def load_pipelines():
    # FAQ
    faq_docs = load_faq_documents("BankFAQs.csv")
    faq_db = build_faq_store(faq_docs)
    faq_bot = faq_qa_pipeline(faq_db)

    # Investment (structured)
    inv_bot = investment_advisor_pipeline(None)

    # News
    news_docs = load_news_documents(
        query="technology OR finance",
        api_key=NEWS_API_KEY
    )
    news_db = build_news_store(news_docs)
    news_bot = news_qa_pipeline(news_db)

    return faq_bot, inv_bot, news_bot


faq_bot, inv_bot, news_bot = load_pipelines()


# ================= CHAT STATE =================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "profile" not in st.session_state:
    st.session_state.profile = {"age": None, "duration": None, "risk": None}


# ================= DISPLAY HISTORY =================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# ================= INPUT =================
user_input = st.chat_input("Ask anything about banking, investing, or markets")


if user_input:

    # show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # ---- Extract profile info ----
    age, duration, risk = extract_profile(user_input)
    update_memory(age, duration, risk)
    profile = get_profile()

    # ---- Intent ----
    intent = classify_intent(user_input)

    # ================= ROUTING =================

    # ---------- FAQ ----------
    if intent == "faq":
        result = faq_bot.invoke({"query": user_input})


    # ---------- INVESTMENT ----------
    elif intent == "investment":

        if profile["age"] is None:
            result = {"result": "Tell me your age first so I can tailor investments."}

        elif profile["risk"] is None:
            result = {"result": "Do you prefer low, medium, or high risk investments?"}

        elif profile["duration"] is None:
            result = {"result": "For how many years do you plan to invest?"}

        else:
            result = inv_bot.invoke({"profile": profile})



    # ---------- NEWS ----------
    elif intent == "news":
        result = news_bot.invoke({"query": user_input})


    # ---------- UNKNOWN ----------
    else:
        result = {"result": "I can help with banking questions, investments, or market news."}


    # ================= OUTPUT =================
    response = result.get("result", "Something went wrong.")
    sources = format_sources(result.get("source_documents", []))

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)

        if sources:
            with st.expander("Sources"):
                for i, src in enumerate(sources, 1):
                    st.markdown(f"**Source {i}**\n{src}")
