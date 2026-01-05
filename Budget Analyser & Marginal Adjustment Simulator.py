import streamlit as st
import matplotlib.pyplot as plt

st.title("Budget Analyser & Marginal Adjustment Simulator")
st.caption("Simulates small (5–15%) reductions in expenses to show their effect on savings.")

st.divider()

# ---------- INPUTS ----------
goal = st.number_input("Monthly savings target (₹)", min_value=0, step=500)
income = st.number_input("Monthly income (₹)", min_value=0, step=1000)

st.subheader("Monthly Expenditure")
food = st.number_input("Food (₹)", min_value=0)
rent = st.number_input("Rent (₹)", min_value=0)
transport = st.number_input("Transport (₹)", min_value=0)
education = st.number_input("Education (₹)", min_value=0)
entertainment = st.number_input("Entertainment (₹)", min_value=0)
health = st.number_input("Health (₹)", min_value=0)
clothing = st.number_input("Clothing & Footwear (₹)", min_value=0)
others = st.number_input("Others (₹)", min_value=0)

# ---------- STORE EXPENSES ----------
if "expenses" not in st.session_state:
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

expenses = st.session_state.expenses
total_expense = sum(expenses.values())
savings = income - total_expense

# ---------- SUMMARY ----------
st.divider()
st.subheader("Budget Summary")

st.write(f"**Total Expenditure:** ₹{round(total_expense,2)}")

if total_expense <= income:
    st.success("Expenditure is within income limit.")
else:
    st.error("Expenditure exceeds income.")

if savings > 0:
    percent = round((savings / income) * 100, 2)
    st.write(f"**Savings:** ₹{round(savings,2)} ({percent}%)")
    if savings >= goal:
        st.success("Savings target achieved.")
    else:
        st.warning(f"Shortfall from goal: ₹{goal - savings}")
else:
    st.warning("No savings made this month.")

# ---------- PIE CHART ----------
st.divider()
st.subheader("Expense Distribution")

fig, ax = plt.subplots()
ax.pie(expenses.values(), labels=expenses.keys(), autopct="%1.1f%%", startangle=90)
ax.axis("equal")
st.pyplot(fig)

# ---------- MARGINAL ADJUSTMENT ----------
st.divider()
st.subheader("Marginal Adjustment Simulator")

category = st.selectbox("Select category to reduce", list(expenses.keys()))
reduction = st.slider("Reduction percentage", 5, 15)

if st.button("Apply Adjustment"):
    previous_total = total_expense
    previous_savings = savings

    change = expenses[category] * reduction / 100
    expenses[category] -= change

    st.success(f"{category.capitalize()} reduced by ₹{round(change,2)}")

    new_total = sum(expenses.values())
    new_savings = income - new_total

    st.write(f"**New Total Expenditure:** ₹{round(new_total,2)}")
    st.write(f"**Change in Savings:** ₹{round(new_savings - previous_savings,2)}")

    # Update session state
    st.session_state.expenses = expenses
