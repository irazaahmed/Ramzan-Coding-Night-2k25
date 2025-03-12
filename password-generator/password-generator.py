import streamlit as st
import random
import string

def generat_password(length, use_degits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation #add special characters e.g !@#$%^&*()
    
    return ''.join(random.choice(characters) for _ in range (length))



st.title('🔐 Password Generator')

length = st.slider('Select length of password',min_value=4, max_value= 24,  value=12)

use_digits = st.checkbox('Use digits')
use_special = st.checkbox('Use special characters')


if st.button('Generate Password'):
    password = generat_password(length, use_digits, use_special)
    st.write(f"Generated Password: {password}")


st.write('''
    ## About
    This is a simple password generator app built with Streamlit.
    It uses the `random` and `string` modules to generate random passwords.
''')


st.write("---------------------------------")
st.write ("Build with 💖 👨‍💻 [Ahmed Raza]('https://www.linkedin.com/in/irazaahmed/')")

