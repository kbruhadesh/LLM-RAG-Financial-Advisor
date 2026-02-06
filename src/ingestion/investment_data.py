import pandas as pd
from langchain_core.documents import Document


def load_investment_documents(csv_path: str):
    df = pd.read_csv(csv_path)
    documents = []

    for _, row in df.iterrows():

        # 🔹 Retrieval-focused content
        content = (
            f"Investment Scenario:\n"
            f"Age: {row['age']}\n"
            f"Gender: {row['gender']}\n"
            f"Duration: {row['Duration']}\n"
            f"Purpose: {row['Purpose']}\n"
            f"Avenue: {row['Avenue']}\n\n"
            f"Recommended Options:\n"
            f"- Mutual Funds: {row['Mutual_Funds']}\n"
            f"- Equity Market: {row['Equity_Market']}\n"
            f"- Debentures: {row['Debentures']}\n"
            f"- Government Bonds: {row['Government_Bonds']}\n"
            f"- Fixed Deposits: {row['Fixed_Deposits']}\n"
            f"- PPF: {row['PPF']}\n"
            f"- Gold: {row['Gold']}\n\n"
            f"Factors: {row['Factor']}\n"
            f"Objective: {row['Objective']}\n"
            f"Expected Returns: {row['Expect']}\n"
            f"Monitoring: {row['Invest_Monitor']}\n\n"
            f"Reasons:\n"
            f"- Equity: {row['Reason_Equity']}\n"
            f"- Mutual Funds: {row['Reason_Mutual']}\n"
            f"- Bonds: {row['Reason_Bonds']}\n"
            f"- Fixed Deposits: {row['Reason_FD']}\n\n"
            f"Source: {row['Source']}"
        )

        documents.append(
            Document(
                page_content=content,
                metadata={
                    "dataset": "InvestmentCases",
                    "age": int(row["age"]),
                    "gender": str(row["gender"]),
                    "duration": str(row["Duration"]),
                    "avenue": str(row["Avenue"])
                }
            )
        )

    return documents
