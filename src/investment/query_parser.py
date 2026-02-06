import re

def parse_investment_query(query: str):
    age_match = re.search(r'(\d+)\s*year', query.lower())
    duration_match = re.search(r'(\d+\s*year|\d+\-\d+\s*year)', query.lower())

    age = int(age_match.group(1)) if age_match else None
    duration = duration_match.group(1) if duration_match else None

    avenue = None
    if "mutual" in query.lower():
        avenue = "Mutual"
    elif "safe" in query.lower() or "low risk" in query.lower():
        avenue = "Fixed"

    return age, duration, avenue
