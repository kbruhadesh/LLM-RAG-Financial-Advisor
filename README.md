# 💰 Finance Intelligence Assistant (LLM + RAG)

A **local-first, privacy-preserving Finance Intelligence Assistant** built using
Retrieval-Augmented Generation (RAG), open-source embeddings, and a locally hosted LLM
(Mistral-7B via Ollama).

This system integrates multiple finance-related capabilities—banking FAQs and
investment advisory—into a **single conversational interface** with **intent-aware
query routing**.

---

## 🚀 Key Features

- ✅ **Local LLM (Mistral-7B via Ollama)** — no cloud inference
- ✅ **RAG-based Banking FAQ Assistant**
- ✅ **RAG-based Investment Advisor (case-based reasoning)**
- ✅ **Intent-aware query routing**
- ✅ **Single chat interface (Streamlit UI)**
- ✅ **Vector database persistence using Chroma**
- ✅ **Modular, backend-ready architecture**

---

## 🧠 System Architecture

```
┌─────────────────────────────────────┐
│   User (Streamlit Chat UI)         │
└────────────────┬────────────────────┘
                 │
                 ▼
         ┌───────────────────┐
         │ Intent Classifier │
         │      (LLM)        │
         └────────┬──────────┘
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
┌───────────────┐   ┌───────────────┐
│   FAQ RAG     │   │ Investment    │
│  (BankFAQs)   │   │  RAG (CSV)    │
└───────┬───────┘   └───────┬───────┘
        │                   │
        └─────────┬─────────┘
                  ▼
      ┌─────────────────────┐
      │   Mistral-7B via    │
      │   Ollama (Local)    │
      └─────────────────────┘
```


---

## 📁 Project Structure

```
LLM-RAG_Finance_UseCases/
├── src/                          # Backend & UI source code
│   ├── app.py                    # Main CLI-based entry point
│   ├── ui.py                     # Streamlit web interface
│   ├── main.py                   # Testing script for advisory pipeline
│   ├── config.py                 # Central configuration
│   ├── llm.py                    # LLM (Ollama) wrapper
│   ├── embeddings.py             # Embedding model loader
│   │
│   ├── ingestion/                # Data loading & processing
│   │   ├── faq_data.py           # Bank FAQ ingestion
│   │   ├── investment_data.py    # Investment dataset ingestion
│   │   └── news_data.py          # News dataset ingestion
│   │
│   ├── vectorstore/              # Vector DB management logic
│   │   ├── faq_store.py          # FAQ vector DB
│   │   ├── investment_store.py   # Investment vector DB
│   │   └── news_store.py         # News vector DB
│   │
│   ├── pipelines/                # RAG pipelines
│   │   ├── faq_qa.py             # FAQ RAG logic
│   │   ├── investment_advisor.py # Investment advisory pipeline
│   │   └── news_qa.py            # News RAG pipeline
│   │
│   └── router/                   # Query routing
│       ├── intent_router.py      # LLM intent classification
│       └── domain_embeddings.py  # Semantic routing
│
├── vector_store/                 # Persistent ChromaDB data
│   ├── faqs/                     # FAQ vector index
│   ├── investment/               # Investment vector index
│   └── investment_news/          # News vector index
│
├── BankFAQs.csv                  # Banking FAQ dataset
├── Finance_data.csv              # Investment preference dataset
├── LLM_+_RAG_for_Finance.ipynb   # Development notebook (V1-V4)
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```


---

## 📊 Data Sources

- **BankFAQs.csv**
  - ~1,700 real-world banking FAQs
  - Topics: debit/credit cards, OTP, loans, security, procedures

- **Finance_data.csv**
  - Investment preference dataset (Kaggle)
  - Used for case-based investment advice via RAG

---

## ⚙️ Setup Instructions

### 1️⃣ Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Install & run Ollama
```bash
ollama pull mistral
ollama run mistral
```

### 4️⃣ (Optional) Set Hugging Face token
```bash
setx HF_TOKEN "your_huggingface_token"
```

---

## 🖥️ Run the Application

### CLI mode
```bash
python src/app.py
```

### Streamlit Chat UI
```bash
streamlit run src/ui.py
```

---

## 🧪 Example Queries

### Banking FAQ

```
How do I reset my debit card PIN?
```

### Investment Advice

```
I want to invest in mutual funds for 3 years with moderate risk
```

The system automatically detects intent and routes the query.

---

## 🧩 Design Philosophy

- **Local-first & private** — no user data leaves the machine
- **Modular pipelines** — easy to extend with new domains
- **LLM as reasoning engine, not knowledge base**
- **RAG for grounding & reliability**
- **Simple UX, intelligent backend**

---

## 🛣️ Future Extensions

- Market & news RAG
- Source citation in UI
- FastAPI backend
- Dockerized deployment
- Migration to modern LangChain (RunnableSequence)

---

## 📌 Status

- **Current State:** Fully functional multi-domain RAG assistant
- **Target Use:** Learning, demos, and foundation for production systems