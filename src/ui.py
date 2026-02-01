import streamlit as st

from ingestion.faq_data import load_faq_documents
from vectorstore.faq_store import build_faq_store
from pipelines.faq_qa import faq_qa_pipeline

from ingestion.investment_data import load_investment_documents
from vectorstore.investment_store import build_investment_store
from pipelines.investment_advisor import investment_advisor_pipeline

from router.intent_router import classify_intent

st.set_page_config(
    page_title="Finance Assistant",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Finance Intelligence Assistant")
st.caption("Local • Private • Powered by Mistral")

# ---------- Load pipelines once ----------
@st.cache_resource
def load_pipelines():
    faq_docs = load_faq_documents("BankFAQs.csv")
    faq_db = build_faq_store(faq_docs)
    faq_bot = faq_qa_pipeline(faq_db)

    inv_docs = load_investment_documents("Finance_data.csv")
    inv_db = build_investment_store(inv_docs)
    inv_bot = investment_advisor_pipeline(inv_db)

    return faq_bot, inv_bot

faq_bot, inv_bot = load_pipelines()

# ---------- Chat state ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- Display chat history ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- User input ----------
user_input = st.chat_input("Ask a finance or banking question")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Classify intent
    intent = classify_intent(user_input)

    # Route query
    if intent == "faq":
        response = faq_bot.invoke({"query": user_input})["result"]
    elif intent == "investment":
        response = inv_bot.invoke({"query": user_input})["result"]
    else:
        response = "Sorry, I couldn't understand your request."

    # Show assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
