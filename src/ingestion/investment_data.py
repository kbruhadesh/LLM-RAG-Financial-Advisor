import pandas as pd
from langchain_core.documents import Document


def load_investment_documents(csv_path: str):
    df = pd.read_csv(csv_path)
    records = df.to_dict(orient="records")

    documents = []

    for entry in records:
        prompt = (
            f"I'm a {entry['age']}-year-old {entry['gender']} looking to invest in "
            f"{entry['Avenue']} for {entry['Purpose']} over the next {entry['Duration']}."
        )

        response = (
            f"Mutual Funds: {entry['Mutual_Funds']}\n"
            f"Equity Market: {entry['Equity_Market']}\n"
            f"Debentures: {entry['Debentures']}\n"
            f"Government Bonds: {entry['Government_Bonds']}\n"
            f"Fixed Deposits: {entry['Fixed_Deposits']}\n"
            f"PPF: {entry['PPF']}\n"
            f"Gold: {entry['Gold']}\n"
            f"Objective: {entry['Objective']}\n"
            f"Expected Returns: {entry['Expect']}\n"
            f"Monitoring: {entry['Invest_Monitor']}"
        )

        content = f"Prompt:\n{prompt}\n\nResponse:\n{response}"
        documents.append(Document(page_content=content))

    return documents
