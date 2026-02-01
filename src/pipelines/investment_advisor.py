from langchain.chains import RetrievalQA
from llm import get_llm

def investment_advisor_pipeline(vectordb):
    retriever = vectordb.as_retriever(search_kwargs={"k": 5})

    qa = RetrievalQA.from_chain_type(
        llm=get_llm(),
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False
    )

    return qa
