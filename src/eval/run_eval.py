from ingestion.faq_data import load_faq_documents
from ingestion.investment_data import load_investment_documents
from vectorstore.faq_store import build_faq_store
from vectorstore.investment_store import build_investment_store
from pipelines.faq_qa import faq_qa_pipeline
from pipelines.investment_advisor import investment_advisor_pipeline
from eval.golden_set import FAQ_TESTS, INVESTMENT_TESTS


def evaluate_pipeline(bot, tests, label):
    print(f"\n=== Evaluating {label} ===")

    for test in tests:
        result = bot.invoke({"query": test["query"]})
        answer = result["result"].lower()
        sources = result["source_documents"]

        keyword_score = sum(
            kw in answer for kw in test["expected_keywords"]
        )

        source_ok = any(
            doc.metadata.get("dataset") == test["dataset"]
            for doc in sources
        )

        print(f"\nQuery: {test['query']}")
        print(f"Keyword match: {keyword_score}/{len(test['expected_keywords'])}")
        print(f"Correct source used: {source_ok}")
        print(f"Answer preview: {answer[:150]}...")


def main():
    faq_bot = faq_qa_pipeline(
        build_faq_store(load_faq_documents("BankFAQs.csv"))
    )

    inv_bot = investment_advisor_pipeline(
        build_investment_store(load_investment_documents("Finance_data.csv"))
    )

    evaluate_pipeline(faq_bot, FAQ_TESTS, "FAQ RAG")
    evaluate_pipeline(inv_bot, INVESTMENT_TESTS, "Investment RAG")


if __name__ == "__main__":
    main()
