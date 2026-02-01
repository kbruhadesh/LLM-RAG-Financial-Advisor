from ingestion.faq_data import load_faq_documents
from vectorstore.faq_store import build_faq_store
from pipelines.faq_qa import faq_qa_pipeline

docs = load_faq_documents("BankFAQs.csv")
vectordb = build_faq_store(docs)
faq_bot = faq_qa_pipeline(vectordb)

query = "How can I reset my debit card PIN?"
result = faq_bot({"query": query})

print(result["result"])
