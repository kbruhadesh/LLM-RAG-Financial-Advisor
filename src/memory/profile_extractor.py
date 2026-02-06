import re

def extract_profile(text: str):
    text = text.lower()

    age = None
    duration = None
    risk = None

    # AGE
    age_match = re.search(r'\b(\d{2})\b', text)
    if age_match:
        age = int(age_match.group(1))

    # DURATION
    if "year" in text:
        duration_match = re.search(r'(\d+)\s*year', text)
        if duration_match:
            duration = duration_match.group(1)

    # RISK
    if any(w in text for w in ["safe", "low risk", "secure", "stable"]):
        risk = "low"
    elif any(w in text for w in ["moderate", "balanced"]):
        risk = "medium"
    elif any(w in text for w in ["high return", "aggressive", "risky"]):
        risk = "high"

    return age, duration, risk
