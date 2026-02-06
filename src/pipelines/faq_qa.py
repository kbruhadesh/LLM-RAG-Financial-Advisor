from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from llm import get_llm
from prompts.rag_prompt import RAG_SYSTEM_PROMPT


def faq_qa_pipeline(vectordb):
    llm = get_llm()

    prompt = PromptTemplate(
        template=RAG_SYSTEM_PROMPT,
        input_variables=["context", "question"]
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever(search_kwargs={"k": 4}),
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )

    return qa
