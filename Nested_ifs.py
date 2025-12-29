import streamlit as st

st.set_page_config(page_title="SSE Bank & ATM", layout="centered")

st.title("SSE Bank ")

# Initialize session state
if "pin" not in st.session_state:
    st.session_state.pin = None

if "balance" not in st.session_state:
    st.session_state.balance = 0

if "attempts" not in st.session_state:
    st.session_state.attempts = 3

# Tabs
bank_tab, atm_tab = st.tabs(["🏦 Bank", "🏧 ATM"])

# ---------------- BANK TAB ----------------
with bank_tab:
    st.header("Bank Setup")

    pin = st.number_input("Set your PIN", type="password", step=1)
    balance = st.number_input("Set initial balance", min_value=0, step=100)

    if st.button("Save Account"):
        st.session_state.pin = pin
        st.session_state.balance = balance
        st.session_state.attempts = 3
        st.success("Account created successfully")

# ---------------- ATM TAB ----------------
with atm_tab:
    st.header("ATM")

    if st.session_state.pin is None:
        st.warning("Please create an account in the Bank tab first.")
    else:
        card_inserted = st.checkbox("Insert Card")

        if card_inserted:
            st.info("Card detected")

            if st.session_state.attempts > 0:
                user_try = st.number_input(
                    "Enter PIN",
                    type="password",
                    step=1,
                    key="atm_pin"
                )

                if st.button("Submit PIN"):
                    if user_try == st.session_state.pin:
                        st.success("Access granted")
                        st.write("Current balance:", st.session_state.balance)

                        withdraw_amt = st.number_input(
                            "Enter withdrawal amount",
                            min_value=0,
                            step=100
                        )

                        if st.button("Withdraw"):
                            if withdraw_amt <= st.session_state.balance:
                                st.session_state.balance -= withdraw_amt
                                st.success("Withdrawal successful")
                                st.write("Remaining balance:", st.session_state.balance)
                            else:
                                st.error("Insufficient balance")
                    else:
                        st.session_state.attempts -= 1
                        st.error("Wrong PIN")
                        st.write("Attempts left:", st.session_state.attempts)
            else:
                st.error("Card blocked due to 3 wrong attempts")
