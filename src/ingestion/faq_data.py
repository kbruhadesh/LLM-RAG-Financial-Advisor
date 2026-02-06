import pandas as pd
from langchain_core.documents import Document

def load_faq_documents(csv_path: str):
    df = pd.read_csv(csv_path)

    documents = []

    for _, row in df.iterrows():
        question = row["Question"]
        answer = row["Answer"]
        category = row.get("Class", "general")

        content = (
            f"Category: {category}\n"
            f"Question: {question}\n"
            f"Answer: {answer}"
        )

        documents.append(
            Document(
                page_content=content,
                metadata={
                    "dataset": "BankFAQs",
                    "category": category
                }
            )
        )

    return documents
