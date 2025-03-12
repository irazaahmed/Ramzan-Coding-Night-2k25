import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon=":lock:", layout="wide")

st.title("🔒 Password Strength Checker")
st.markdown("""
## Welcome to Password Strength Checker 👋
This app checks the strength of your password.
Enter your **password** below to get started.
            
**Created by: [Ahmed Raza](https://www.linkedin.com/in/irazaahmed/)**
""")

password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one number.")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character.")
    
    if score == 4:
        st.success("✅ Your Password is strong!")
    elif score == 3:
        st.warning("⚠️ Your Password is medium!")
    else:
        st.error("🔴 Your Password is weak, please improve it!")

    if feedback:
        st.markdown("### Imporment Suggestions:")
        for tip in feedback:
            st.write(tip)

else:
    st.info("Please enter your password to check its strength.")


