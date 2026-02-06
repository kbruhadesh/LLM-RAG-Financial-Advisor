from embeddings import get_embeddings

embed = get_embeddings()

DOMAINS = {
    "faq": [
        "debit card pin reset",
        "bank procedures",
        "loan requirements",
        "card blocked what to do"
    ],
    "investment": [
        "investment profile",
        "risk tolerance",
        "financial planning based on age",
        "portfolio allocation"
    ],
    "news": [
        "recent financial news",
        "company updates this week",
        "market events",
        "what happened to a company"
    ]
}

DOMAIN_VECTORS = {
    domain: embed.embed_documents(texts)
    for domain, texts in DOMAINS.items()
}
