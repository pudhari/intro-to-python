import streamlit as st

st.set_page_config(page_title="SSE Bank & ATM", layout="centered")
st.title("SSE Bank System")

# ---------- SESSION STATE (acts like variables that remember values) ----------
if "pin" not in st.session_state:
    st.session_state.pin = None

if "balance" not in st.session_state:
    st.session_state.balance = 0

if "attempts" not in st.session_state:
    st.session_state.attempts = 3

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ---------- TABS ----------
bank_tab, atm_tab = st.tabs(["Bank", "ATM"])


# ================= BANK TAB =================
with bank_tab:
    st.header("Bank")

    pin_input = st.text_input("Set your PIN", type="password")
    balance_input = st.number_input("Set your balance", min_value=0, step=100)

    if st.button("Create Account"):
        if pin_input.isdigit():
            st.session_state.pin = int(pin_input)
            st.session_state.balance = balance_input
            st.session_state.attempts = 3
            st.session_state.logged_in = False
            st.success("Account created successfully")
        else:
            st.error("PIN must be numeric")


# ================= ATM TAB =================
with atm_tab:
    st.header("ATM")

    if st.session_state.pin is None:
        st.warning("Please create an account in Bank tab first")

    else:
        card_inserted = st.checkbox("Insert Card")

        if card_inserted:
            st.info("Card detected")

            # ---------- PIN CHECK ----------
            if not st.session_state.logged_in:

                if st.session_state.attempts > 0:
                    entered_pin = st.text_input("Enter your PIN", type="password")

                    if st.button("Submit PIN"):
                        if entered_pin.isdigit() and int(entered_pin) == st.session_state.pin:
                            st.session_state.logged_in = True
                            st.success("Access granted")
                        else:
                            st.session_state.attempts -= 1
                            st.error("Wrong password")
                            st.write("Attempts left:", st.session_state.attempts)
                else:
                    st.error("Card blocked due to 3 wrong attempts")

            # ---------- WITHDRAW ----------
            else:
                st.write("Your balance is:", st.session_state.balance)

                withdraw_amt = st.number_input(
                    "How much do you want to withdraw?",
                    min_value=0,
                    step=100
                )

                if st.button("Withdraw"):
                    st.write("Withdrawn Amount:", withdraw_amt)

                    if withdraw_amt <= st.session_state.balance:
                        st.session_state.balance -= withdraw_amt
                        st.success("Current balance: " + str(st.session_state.balance))
                    else:
                        st.error("You don't have enough balance")

                if st.button("Exit ATM"):
                    st.session_state.logged_in = False
                    st.session_state.attempts = 3
                    st.info("Card removed")
