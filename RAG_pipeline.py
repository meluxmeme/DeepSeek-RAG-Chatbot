from langchain_groq import ChatGroq
from vector_database import faiss_db
from langchain_core.prompts import ChatPromptTemplate


llm_model=ChatGroq(model="deepseek-r1-distill-llama-70b", api_key = "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")


def retrieve_docs(query):
    return faiss_db.similarity_search(query)

def get_context(documents):
    context = "\n\n".join([doc.page_content for doc in documents])
    return context


custom_prompt_template = """
Use the pieces of information provided in the context to answer user's question.
If you dont know the answer, just say that you dont know, dont try to make up an answer. 
Dont provide anything out of the given context
Question: {question} 
Context: {context} 
Answer:
"""

def answer_query(documents, model, query):
    context = get_context(documents)
    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    chain = prompt | model
    return chain.invoke({"question": query, "context": context})

question = "who is PSS ?"
retrieved_docs = retrieve_docs(question)
print("Answer:", answer_query(documents=retrieved_docs, model=llm_model, query=question))
