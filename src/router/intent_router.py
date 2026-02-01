from llm import get_llm

INTENT_PROMPT = """
Classify the following user query into ONE of the categories below.

Categories:
- faq : banking, debit card, credit card, PIN, loan rules, procedures
- investment : investing, mutual funds, wealth, returns, portfolio

Query:
{query}

Respond with ONLY the category name.
"""

def classify_intent(query: str) -> str:
    llm = get_llm()
    response = llm.invoke(INTENT_PROMPT.format(query=query))
    return response.strip().lower()
