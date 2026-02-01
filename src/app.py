from ingestion.faq_data import load_faq_documents
from vectorstore.faq_store import build_faq_store
from pipelines.faq_qa import faq_qa_pipeline

from ingestion.investment_data import load_investment_documents
from vectorstore.investment_store import build_investment_store
from pipelines.investment_advisor import investment_advisor_pipeline

from router.intent_router import classify_intent

# Build pipelines once
faq_docs = load_faq_documents("BankFAQs.csv")
faq_db = build_faq_store(faq_docs)
faq_bot = faq_qa_pipeline(faq_db)

inv_docs = load_investment_documents("Finance_data.csv")
inv_db = build_investment_store(inv_docs)
inv_bot = investment_advisor_pipeline(inv_db)

print("Finance Assistant Ready. Type 'exit' to quit.\n")

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    intent = classify_intent(query)

    if intent == "faq":
        result = faq_bot.invoke({"query": query})
    elif intent == "investment":
        result = inv_bot.invoke({"query": query})
    else:
        result = {"result": "Sorry, I could not classify your query."}

    print("\nAssistant:", result["result"], "\n")
