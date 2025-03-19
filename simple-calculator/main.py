import streamlit as st

def main():
    st.title("Simple Calculator 🔢")
    st.write("Enter two numbers and select an operation to perform")

    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number", value=0.0)
    with col2:
        num2 = st.number_input("Enter second number", value=0.0)

    operation = st.selectbox("Select operation", ["Addition ➕", "Subtraction ➖", "Multiplication ✖️", "Division ➗"])

    if st.button("Calculate"):
        try:
            if operation == "Addition ➕":
                result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction ➖":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication ✖️":
                result = num1 * num2
                symbol = "×"
            else:
                if num1 == 0 or num2 == 0:
                    st.error("Division by zero is not allowed")
                    return
                result = num1 / num2
                symbol = "÷"
                
            st.success(f"{num1} {symbol} {num2} = {result}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")


    st.write("Made by with ❤️ by [Ahmed Raza](https://www.linkedin.com/in/irazaahmed/)")

#Run the main function when the page is loaded
if __name__ == "__main__":
    main()
