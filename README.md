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

User (Streamlit Chat UI)
|
v
Intent Classifier (LLM)
|
v
┌───────────────┬────────────────┐
│ FAQ RAG │ Investment RAG │
│ (BankFAQs) │ (Finance CSV) │
└───────────────┴────────────────┘
|
v
Mistral-7B (Ollama, Local)



---

## 📁 Project Structure




src/
├── app.py # CLI-based unified assistant
├── ui.py # Streamlit chat UI
├── config.py # Central configuration
├── llm.py # LLM (Ollama) wrapper
├── embeddings.py # Embedding model loader
│
├── ingestion/
│ ├── faq_data.py # Bank FAQ ingestion
│ └── investment_data.py # Investment dataset ingestion
│
├── vectorstore/
│ ├── faq_store.py # FAQ vector DB
│ └── investment_store.py # Investment vector DB
│
├── pipelines/
│ ├── faq_qa.py # FAQ RAG pipeline
│ └── investment_advisor.py
│
├── router/
│ └── intent_router.py # Query intent classification


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
python app.py
```

### Streamlit Chat UI
```bash
streamlit run ui.py
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
