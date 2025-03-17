import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 1000)

st.subheader("Instant Cash Generator")

if st.button("Generate Money"):
    st.write("Counting Your Money...")
    time.sleep(1)
    money= generate_money()
    st.success(f"Congratulations! You have generated ${money}!")


def fetch_tech_and_digital():
    try:
        response = requests.get("http://127.0.0.1:8000/tech_and_digital")
        if response.status_code == 200:
            tech= response.json()
            return tech
        else:
            return ("Web Development")
    
    except:
        return ("Something went wrong")
    
st.subheader("Tech and Digital Idea")
if st.button("Get Idea"):
    st.write("Fetching Idea...")
    time.sleep(1)
    idea= fetch_tech_and_digital()
    st.success(f"Your Idea is: {idea}")



def fetch_money_qoutes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            qoutes = response.json()
            return qoutes 
        else:
            return ("Money is the root of all evil")
    except:
        return ("Something went wrong")
    

st.subheader("Money Making Motivation")
if st.button("Get Inspired"):
    st.write("Fetching Quote...")
    time.sleep(1)
    qoute= fetch_money_qoutes()
    st.success(f"Your Quote is: {qoute}")
