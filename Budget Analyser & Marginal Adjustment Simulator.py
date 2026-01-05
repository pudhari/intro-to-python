import streamlit as st
import pandas as pd

st.set_page_config(page_title="Budget Analyser", layout="centered")

st.title("Budget Analyser & Marginal Adjustment Simulator")
st.write("Analyze your monthly budget and see how small expense reductions affect savings.")

# ------------------ SESSION STATE ------------------
if "expenses" not in st.session_state:
    st.session_state.expenses = {}

if "income" not in st.session_state:
    st.session_state.income = 0

if "goal" not in st.session_state:
    st.session_state.goal = 0

# ------------------ BUDGET ANALYSER ------------------
st.header("Budget Analyser")

st.session_state.goal = st.number_input("Monthly savings target (₹)", min_value=0, step=500)
st.session_state.income = st.number_input("Monthly income (₹)", min_value=0, step=1000)

st.subheader("Monthly Expenses")

food = st.number_input("Food ₹", min_value=0, step=500)
rent = st.number_input("Rent ₹", min_value=0, step=1000)
transport = st.number_input("Transport ₹", min_value=0, step=500)
education = st.number_input("Education ₹", min_value=0, step=500)
entertainment = st.number_input("Entertainment ₹", min_value=0, step=500)
health = st.number_input("Health ₹", min_value=0, step=500)
clothing = st.number_input("Clothing ₹", min_value=0, step=500)
others = st.number_input("Others ₹", min_value=0, step=500)

if st.button("Analyze Budget"):
    st.session_state.expenses = {
        "food": food,
        "rent": rent,
        "transport": transport,
        "education": education,
        "entertainment": entertainment,
        "health": health,
        "clothing": clothing,
        "others": others
    }

    total_expense = sum(st.session_state.expenses.values())
    savings = st.session_state.income - total_expense

    st.subheader("Budget Summary")
    st.write("Total expenditure: ₹", total_expense)

    if total_expense <= st.session_state.income:
        st.success("Expenditure is within income.")
    else:
        st.error("Expenditure exceeds income.")

    if savings > 0:
        percent = round((savings / st.session_state.income) * 100, 2)
        st.write("Savings: ₹", savings)
        st.write("Savings rate:", percent, "%")

        if savings >= st.session_state.goal:
            st.success("Savings target achieved.")
        else:
            st.warning("You are short of your target by ₹" + str(st.session_state.goal - savings))
    else:
        st.error("No savings this month.")

    # -------- BAR CHART (SAFE) --------
    st.subheader("Expense Distribution")
    df = pd.DataFrame({
        "Category": st.session_state.expenses.keys(),
        "Amount": st.session_state.expenses.values()
    })
    st.bar_chart(df.set_index("Category"))

# ------------------ MARGINAL ADJUSTMENT ------------------
st.header("Marginal Adjustment Simulator")
st.write("Simulates small (5–15%) reductions in expenses to show their effect on savings.")

if st.session_state.expenses:
    category = st.selectbox("Select category to reduce", st.session_state.expenses.keys())
    percent = st.slider("Reduction percentage", 5, 15)

    if st.button("Apply Adjustment"):
        old_total = sum(st.session_state.expenses.values())
        old_savings = st.session_state.income - old_total

        reduction = st.session_state.expenses[category] * percent / 100
        st.session_state.expenses[category] -= reduction

        new_total = sum(st.session_state.expenses.values())
        new_savings = st.session_state.income - new_total

        st.subheader("Adjustment Result")
        st.write("Reduced", category, "by ₹", round(reduction, 2))
        st.write("New total expenditure: ₹", round(new_total, 2))
        st.write("Savings increased by: ₹", round(new_savings - old_savings, 2))

        # Updated chart
        df = pd.DataFrame({
            "Category": st.session_state.expenses.keys(),
            "Amount": st.session_state.expenses.values()
        })
        st.bar_chart(df.set_index("Category"))
else:
    st.info("Please analyze your budget first.")
