from typing import Dict
print(">>> NEW RULE-BASED ADVISOR LOADED <<<")

def risk_band(age: int, risk: str, duration: int) -> str:
    risk = risk.lower()

    if risk in ["low", "safe", "conservative"]:
        return "conservative"

    if risk in ["medium", "balanced"]:
        return "balanced"

    if risk in ["high", "aggressive"]:
        return "aggressive"

    # fallback by age + duration
    if age > 50 or duration < 3:
        return "conservative"
    if duration > 7:
        return "aggressive"
    return "balanced"


def allocation_model(band: str) -> Dict[str, int]:

    if band == "conservative":
        return {
            "Bonds": 40,
            "Fixed Deposits": 30,
            "Gold": 15,
            "Large Cap Equity": 15
        }

    if band == "balanced":
        return {
            "Bonds": 25,
            "Fixed Deposits": 15,
            "Large Cap Equity": 35,
            "Index Funds": 15,
            "Gold": 10
        }

    if band == "aggressive":
        return {
            "Mid/Small Cap Equity": 45,
            "Index Funds": 25,
            "International Equity": 20,
            "Gold": 10
        }


def explanation(age, risk, duration, band):
    return (
        f"Based on age {age}, a {duration}-year horizon, "
        f"and {risk} risk tolerance, you fall into a {band} investor category. "
        "The allocation prioritizes stability vs growth accordingly."
    )


# -------- MAIN PIPELINE --------
def investment_advisor_pipeline(_):

    class Advisor:
        def invoke(self, inputs):

            profile = inputs["profile"]
            age = profile["age"]
            duration = profile.get("duration", 5)
            risk = profile.get("risk", "medium")

            band = risk_band(age, risk, duration)
            allocation = allocation_model(band)

            alloc_text = "\n".join(
                [f"- {k}: {v}%" for k, v in allocation.items()]
            )

            result = f"""
### Investor Profile
Age: {age}
Horizon: {duration} years
Risk Appetite: {risk}
Category: {band.capitalize()}

### Recommended Portfolio Allocation
{alloc_text}

### Rationale
{explanation(age, risk, duration, band)}
"""

            return {"result": result}

    return Advisor()
