import streamlit as st

st.title('My First Streamlit App')

user_input = st.text_input('Enter your name')
# st.write('Hello', user_input)
if st.button("Show Text"):
    st.write('Hello', user_input)
