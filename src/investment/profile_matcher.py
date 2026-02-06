import pandas as pd


# ---------------- AGE RANGE LOGIC ----------------
def _age_band(age: int):
    """
    Dataset ages are discrete (20, 21, 22...).
    We match within a realistic band instead of exact equality.
    """
    if age <= 25:
        return (18, 25)
    elif age <= 35:
        return (26, 35)
    elif age <= 50:
        return (36, 50)
    else:
        return (51, 70)


# ---------------- RISK FILTER ----------------
def _risk_filter(df: pd.DataFrame, risk: str):
    """
    Maps human risk preference → dataset investment avenue
    """

    if risk is None:
        return df

    risk = risk.lower()

    if risk == "low":
        # safe instruments
        return df[
            (df["Fixed_Deposits"] == 1)
            | (df["Government_Bonds"] == 1)
            | (df["PPF"] == 1)
        ]

    elif risk == "medium":
        return df[
            (df["Mutual_Funds"] == 1)
            | (df["Gold"] == 1)
        ]

    elif risk == "high":
        return df[
            (df["Equity_Market"] == 1)
        ]

    return df


# ---------------- MAIN MATCH FUNCTION ----------------
def find_matching_profiles(df: pd.DataFrame, age: int, duration=None, risk=None):
    """
    Returns rows from dataset that resemble the user profile.
    Not exact matching — similarity matching.
    """

    if age is None:
        return pd.DataFrame()

    # 1️⃣ Age band match
    low, high = _age_band(age)
    candidates = df[(df["age"] >= low) & (df["age"] <= high)]

    # 2️⃣ Duration match (optional)
    if duration:
        candidates = candidates[candidates["Duration"].str.contains(str(duration), case=False, na=False)]

    # 3️⃣ Risk filtering
    candidates = _risk_filter(candidates, risk)

    # 4️⃣ Fallback if too strict
    if candidates.empty:
        # Relax duration first
        candidates = df[(df["age"] >= low) & (df["age"] <= high)]
        candidates = _risk_filter(candidates, risk)

    # 5️⃣ Final fallback — only age
    if candidates.empty:
        candidates = df[(df["age"] >= low) & (df["age"] <= high)]

    return candidates.head(5)
