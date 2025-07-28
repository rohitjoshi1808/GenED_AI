import streamlit as st
from app import generate_question
from evaluate import evaluate_questions

st.title("Topic based AI question")
st.write("Please give your best answer,so evaluate your understanding")

tab1, tab2 = st.tabs(["Question_Generator", "Evaluator"])

with tab1:
    st.header("Question_Generator")
    with st.form("my_form_1"):
        st.write("Please Enter Word: ")
        word = st.text_input("Enter your Topic: ")

        submitted = st.form_submit_button("Enter")

        if submitted:
            list_of_Questions = generate_question(word)
            st.text_area("list_of_Questions",list_of_Questions, height=400)
        

    if submitted:
       
        st.download_button(label="📥 Download Questions",
            data=list_of_Questions,
            file_name="questions.txt",
            mime="text/plain"
            )

with tab2:
    st.header("Evaluator")
    with st.form("my_form_2"):
        answer = st.text_area("Please enter your answer", height=200)

        submitted = st.form_submit_button("Submit")

        if submitted:
            result = evaluate_questions(answer)
            st.text_area("result",result, height=1000)







