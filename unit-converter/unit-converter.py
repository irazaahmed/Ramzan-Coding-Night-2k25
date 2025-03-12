import streamlit as st

# Custom CSS for better design and responsiveness
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        max-width: 600px;
        margin: auto;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    @media (max-width: 600px) {
        .main {
            padding: 10px;
        }
        .stButton button {
            width: 100%;
            padding: 15px;
        }
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        color: black;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    h1 {
        color: #4CAF50;
        text-align: center;
    }
    .stNumberInput input {
        border: 2px solid #4CAF50;
        border-radius: 5px;
    }
    .stSelectbox select {
        border: 2px solid #4CAF50;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

def convert_units(value, unit_from, unit_to):
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
    }

    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not available"

st.title("Unit Converter")

value = st.number_input("Enter the value you want to convert: ", min_value=1.0, step=1.0)

unit_from = st.selectbox("Select the unit you want to convert from: ", ["meter", "kilometer", "gram", "kilogram"])

unit_to = st.selectbox("Select the unit you want to convert to: ", ["meter", "kilometer", "gram", "kilogram"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"{value} {unit_from} is equal to {result} {unit_to}")

# Add footer
st.markdown("""
    <div class="footer">
        Created by Ahmed Raza
    </div>
""", unsafe_allow_html=True)






# import streamlit as st #import streamlit

# def convert_units(value, unit_from, unit_to): #function to convert units

#     conversions = {
#         "meter_kilometer" : 0.001, #1 meter = 0.001 kilometer
#         "kilometer_meter": 1000, #1 kilometer = 1000 meters
#         "gram_kilogram" : 0.001, #1 gram = 0.001 kilogram
#         "kilogram_gram" : 1000, #1 kilogram = 1000 grams
#     }

#     key = f"{unit_from}_{unit_to}" #generate a key based on the input and output units

#     #check if the key exists in the conversions dictionary
#     if key in conversions:
#         conversion = conversions[key]
#         return value * conversion
#     else:
#         return "Conversion not available"
    
# st.title("Unit Converter")

# value = st.number_input("Enter the value you want to convert: ", min_value=1.0, step=1.0)

# unit_from = st.selectbox("Select the unit you want to convert from: ", ["meter", "kilometer", "gram", "kilogram"])

# unit_to = st.selectbox("Select the unit you want to convert to: ", ["meter", "kilometer", "gram", "kilogram"])

# if st.button("Convert"):
#     result = convert_units(value, unit_from, unit_to)
#     st.write(f"{value} {unit_from} is equal to {result} {unit_to}")


