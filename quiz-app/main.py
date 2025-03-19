import streamlit as st
import random
import time

st.title("📝 Quiz App")

questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Karachi", "Islamabad", "Lahore", "Quetta"],
        "answer": "Islamabad"
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": ["Allama Iqbal", "Quaid-e-Azam", "Liaquat Ali Khan", "Fatima Jinnah"],
        "answer": "Quaid-e-Azam"
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Euro", "Dinar"],
        "answer": "Rupee"
    },
    {
        "question": "What is the largest city in Pakistan?",
        "options": ["Karachi", "Islamabad", "Lahore", "Quetta"],
        "answer": "Karachi"
    },
    {
        "question": "What is the national animal of Pakistan?",
        "options": ["Leopard", "Elephant", "Tiger", "Lion"],
        "answer": "Lion"
    },
    {
        "question": "What is the national flower of Pakistan?",
        "options": ["Rose", "Jasmine", "Lotus", "Marigold"],
        "answer": "Rose"
    },
    {
        "question": "What is the national sport of Pakistan?",
        "options": ["Cricket", "Football", "Hockey", "Badminton"],
        "answer": "Cricket"
    },
    {
        "question": "What is the national language of Pakistan?",
        "options": ["Urdu", "English", "Sindhi", "Punjabi"],
        "answer": "Urdu"
    },
    {
        "question": "Which city is know as the 'City of Lights'?",
        "options": ["Karachi", "Islamabad", "Lahore", "Quetta"],
        "answer": "Karachi"
    },
    {
        "question": "What is the national tree of Pakistan?",
        "options": ["Neem", "Banyan", "Pine", "Deodar"],
        "answer": "Deodar"
    },
    {
        "question": "What is the national bird of Pakistan?",
        "options": ["Peacock", "Pigeon", "Eagle", "Owl"],
        "answer": "Peacock"
    },
    {
        "question": "what is the national fruit of Pakistan?",
        "options": ["Mango", "Apple", "Banana", "Orange"],
        "answer": "Mango"
    },
]

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question

st.subheader(question["question"])

selected_option = st.radio("Choose your answer", question["options"], key="answer")

if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("Correct Answer! 🎉")
    else:
        st.error("Incorrect Answer! 😢, The Correct answer is "  + question["answer"])
    

    time.sleep(3)

    st.session_state.current_question = random.choice(questions)

    st.rerun()


st.write("Made with ❤️ by [Ahmed Raza](www.linkedin.com/in/irazaahmed/)") 