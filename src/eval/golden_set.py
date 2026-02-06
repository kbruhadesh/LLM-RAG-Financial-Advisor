FAQ_TESTS = [
    {
        "query": "How do I reset my debit card PIN?",
        "expected_keywords": ["PIN", "reset", "debit"],
        "dataset": "BankFAQs"
    },
    {
        "query": "What documents are required for a business loan?",
        "expected_keywords": ["loan", "documents"],
        "dataset": "BankFAQs"
    }
]

INVESTMENT_TESTS = [
    {
        "query": "I am a 30-year-old male looking to invest for 3 years",
        "expected_keywords": ["mutual", "investment", "risk"],
        "dataset": "InvestmentCases"
    },
    {
        "query": "I want low-risk investment options for short term",
        "expected_keywords": ["fixed", "debt", "low"],
        "dataset": "InvestmentCases"
    }
]
