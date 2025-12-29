import streamlit as st

st.set_page_config(page_title="SSE Bank & ATM", layout="centered")
st.title("SSE Bank System")

# ---------------- SESSION STATE ----------------
if "pin" not in st.session_state:
    st.session_state.pin = None

if "balance" not in st.session_state:
    st.session_state.balance = 0

if "attempts" not in st.session_state:
    st.session_state.attempts = 3

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ---------------- TABS ----------------
bank_tab, atm_tab = st.tabs(["Bank", "ATM"])

# ---------------- BANK TAB ----------------
with bank_tab:
    st.header("Bank Setup")

    pin = st.text_input("Set your PIN", type="password")
    balance = st.number_input("Set initial balance", min_value=0, step=100)

    if st.button("Save Account"):
        if pin.isdigit():
            st.session_state.pin = int(pin)
            st.session_state.balance = balance
            st.session_state.attempts = 3
            st.session_state.authenticated = False
            st.success("Account created successfully")
        else:
            st.error("PIN must contain only numbers")

# ---------------- ATM TAB ----------------
with atm_tab:
    st.header("ATM")

    if st.session_state.pin is None:
        st.warning("Please create an account in the Bank tab first.")

    else:
        card_inserted = st.checkbox("Insert Card")

        if card_inserted:

            # ---------- PIN CHECK ----------
            if not st.session_state.authenticated:

                if st.session_state.attempts > 0:
                    user_try = st.text_input("Enter PIN", type="password")

                    if st.button("Submit PIN"):
                        if user_try.isdigit() and int(user_try) == st.session_state.pin:
                            st.session_state.authenticated = True
                            st.success("Access granted")
                        else:
                            st.session_state.attempts -= 1
                            st.error("Wrong PIN")
                            st.write("Attempts left:", st.session_state.attempts)
                else:
                    st.error("Card blocked due to 3 wrong attempts")

            # ---------- WITHDRAW ----------
            else:
                st.success("Logged in")
                st.write("Current balance:", st.session_state.balance)

                with st.form("withdraw_form"):
                    withdraw_amt = st.number_input(
                        "Enter withdrawal amount",
                        min_value=0,
                        step=100
                    )
                    submit = st.form_submit_button("Withdraw")

                if submit:
                    if withdraw_amt <= st.session_state.balance:
                        st.session_state.balance -= withdraw_amt
                        st.success(f"Withdrawn amount: {withdraw_amt}")
                        st.write("Remaining balance:", st.session_state.balance)
                    else:
                        st.error("Insufficient balance")

                if st.button("Exit ATM"):
                    st.session_state.authenticated = False
                    st.session_state.attempts = 3
