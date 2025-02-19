import streamlit as st 
file = st.file_uploader("Please upload files before", type ="pdf", accept_multiple_files = True)

question_from_user = st.text_area("Write your question here:", height = 200, placeholder="what's on your brain?")
ask_button = st.button("click here for response")

if ask_button:    
    if file:
        for uploaded_file in file:
            # code to process uploaded_file goes here
            st.write("Answer: This is where the answer would be displayed.")
    else:
        st.write("Please upload a PDF file before asking a question.")