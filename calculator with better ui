import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")

# ---- HEADER ----
st.markdown("<h1 style='text-align: center; color:#4CAF50;'>🧮 Simple Calculator</h1>", unsafe_allow_html=True)
st.write("### Enter your numbers and choose an operation:")

# ---- INPUTS ----
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("First Number", value=0.0)

with col2:
    num2 = st.number_input("Second Number", value=0.0)

# ---- SELECT OPERATION ----
operation = st.selectbox(
    "Choose Operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"]
)

# ---- CALCULATE BUTTON ----
if st.button("Calculate", type="primary"):
    if operation == "Addition (+)":
        result = num1 + num2

    elif operation == "Subtraction (-)":
        result = num1 - num2

    elif operation == "Multiplication (×)":
        result = num1 * num2

    elif operation == "Division (÷)":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "❌ Cannot divide by zero"

    # ---- RESULT CARD ----
    st.markdown(
        f"""
        <div style="
            border-radius: 12px;
            padding: 20px;
            margin-top: 20px;
            background-color: #f0f8ff;
            border-left: 6px solid #4CAF50;
            font-size: 20px;">
            <strong>Result: </strong> {result}
        </div>
        """,
        unsafe_allow_html=True
    )
