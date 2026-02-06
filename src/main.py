from ingestion.investment_data import load_investment_documents
from vectorstore.investment_store import build_investment_store
from pipelines.investment_advisor import investment_advisor_pipeline

docs = load_investment_documents("Finance_data.csv")
vectordb = build_investment_store(docs)
advisor = investment_advisor_pipeline(vectordb)

query = (
    "I'm a 34-year-old female looking to invest in mutual funds "
    "for wealth creation over the next 1-3 years. What are my options?"
)

result = advisor({"query": query})
print(result["result"])
