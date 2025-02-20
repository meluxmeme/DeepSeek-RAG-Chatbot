import streamlit as st 
from RAG_pipeline import answer_query,llm_model, retrieve_docs

file = st.file_uploader("Please upload files before", type ="pdf", accept_multiple_files = True)

question_from_user = st.text_area("Write your question here:", height = 200, placeholder="what's on your brain?")
ask_button = st.button("click here for response")

if ask_button:    
    if question_from_user:
        # for uploaded_file in file:
            # code to process uploaded_file goes here
            st.write("Response")
            st.chat_message("Laxmi").write(question_from_user)
            retrieved_docs = retrieve_docs(question_from_user)
            response = answer_query(documents=retrieved_docs, model=llm_model, query = question_from_user)
            # static_chat = "this is a static message for checking"
            st.chat_message("System").write(response)
    else:
        st.write("You have not ask anything, please type in the field")