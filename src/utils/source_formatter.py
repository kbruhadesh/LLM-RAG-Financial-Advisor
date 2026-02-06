def format_sources(source_documents, max_sources=3):
    formatted = []

    for doc in source_documents[:max_sources]:
        dataset = doc.metadata.get("dataset", "unknown")
        category = doc.metadata.get("category", "unknown")

        text = doc.page_content.strip()
        preview = text[:300] + "..." if len(text) > 300 else text

        formatted.append(
            f"**Dataset:** {dataset}\n"
            f"**Category:** {category}\n\n"
            f"{preview}"
        )

    return formatted
