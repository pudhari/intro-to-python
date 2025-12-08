import streamlit as st

st.title("Simple Calculator")

# Input numbers
num1 = st.number_input("Tell me 1st number", value=0.0)
num2 = st.number_input("Tell me your 2nd number", value=0.0)

# When user clicks button
if st.button("Calculate"):
    # Calculations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    
    # Avoid division by zero error
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Cannot divide by zero"

    # Display results
    st.write("### Results:")
    st.write("Addition =", addition)
    st.write("Subtraction =", subtraction)
    st.write("Multiplication =", multiplication)
    st.write("Division =", division)
