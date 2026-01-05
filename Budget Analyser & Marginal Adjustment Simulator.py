import streamlit as st
import plotly.express as px

st.title("Budget Analyser & Marginal Adjustment Simulator")

# -------------------- INPUT SECTION --------------------
st.header("Budget Analyser")

goal = st.number_input("Monthly savings target (₹)", min_value=0, step=500)
income = st.number_input("Monthly income (₹)", min_value=0, step=1000)

st.subheader("Monthly Expenditure")
expenses = {
    "food": st.number_input("Food (₹)", min_value=0),
    "rent": st.number_input("Rent (₹)", min_value=0),
    "transport": st.number_input("Transport (₹)", min_value=0),
    "education": st.number_input("Education (₹)", min_value=0),
    "entertainment": st.number_input("Entertainment (₹)", min_value=0),
    "health": st.number_input("Health (₹)", min_value=0),
    "clothing": st.number_input("Clothing (₹)", min_value=0),
    "others": st.number_input("Others (₹)", min_value=0)
}

# -------------------- ANALYSIS --------------------
total_expense = sum(expenses.values())
savings = income - total_expense

st.divider()
st.subheader("Summary")

st.write(f"**Total Expenditure:** ₹{total_expense}")
st.write(f"**Savings:** ₹{savings}")

if total_expense <= income:
    st.success("Expenditure is within income limit")
else:
    st.error("Expenditure exceeds income")

if savings >= goal:
    st.success("Savings target achieved 🎯")
else:
    st.warning(f"Shortfall from goal: ₹{goal - savings}")

# -------------------- PIE CHART --------------------
st.subheader("Expense Distribution")

fig = px.pie(
    names=expenses.keys(),
    values=expenses.values(),
    hole=0.4
)
st.plotly_chart(fig, use_container_width=True)

# -------------------- MARGINAL ADJUSTMENT --------------------
st.divider()
st.header("Marginal Adjustment Simulator")
st.caption("Simulates small (5–15%) reductions in expenses to show their effect")

category = st.selectbox("Select category to reduce", expenses.keys())
percent = st.slider("Reduction percentage", 5, 15)

if st.button("Apply Adjustment"):
    old_total = total_expense
    old_savings = savings

    reduction = expenses[category] * percent / 100
    expenses[category] -= reduction

    total_expense = sum(expenses.values())
    savings = income - total_expense

    st.success(f"{category.capitalize()} reduced by ₹{round(reduction,2)}")

    st.subheader("Updated Impact")
    st.write(f"**New Total Expenditure:** ₹{round(total_expense,2)}")
    st.write(f"**New Savings:** ₹{round(savings,2)}")

    st.write(f"**Expenditure Reduced By:** ₹{round(old_total - total_expense,2)}")
    st.write(f"**Savings Increased By:** ₹{round(savings - old_savings,2)}")

    fig2 = px.pie(
        names=expenses.keys(),
        values=expenses.values(),
        hole=0.4
    )
    st.plotly_chart(fig2, use_container_width=True)

