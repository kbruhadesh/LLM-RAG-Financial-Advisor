from langchain.chains import RetrievalQA
from llm import get_llm

def faq_qa_pipeline(vectordb):
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    qa = RetrievalQA.from_chain_type(
        llm=get_llm(),
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False
    )

    return qa
