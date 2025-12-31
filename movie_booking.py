import streamlit as st

# session state initialization
if "available_seats" not in st.session_state:
    st.session_state.available_seats = 5

if "price" not in st.session_state:
    st.session_state.price = 150

if "choice" not in st.session_state:
    st.session_state.choice = None

password = "abcd"  # admin password

st.title("🎬 Movie Booking System")
st.write("=" * 47)

st.write("### Press a number to choose:")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("1"):
        st.session_state.choice = 1

with col2:
    if st.button("2"):
        st.session_state.choice = 2

with col3:
    if st.button("3"):
        st.session_state.choice = 3

with col4:
    if st.button("4"):
        st.session_state.choice = 4

st.write("=" * 47)

# Choice 1
if st.session_state.choice == 1:
    st.write("### 1. Check available seats and ticket price")
    st.write("Available seats:", st.session_state.available_seats)
    st.write("Ticket price:", st.session_state.price)

# Choice 2
elif st.session_state.choice == 2:
    st.write("### 2. Book tickets")
    how_many = st.number_input(
        "How many seats do you want to book?",
        min_value=1,
        step=1,
    )

    if st.button("Confirm Booking"):
        if st.session_state.available_seats >= how_many:
            st.session_state.available_seats -= how_many
            st.success("Tickets booked")
            st.write("Remaining seats:", st.session_state.available_seats)
            st.write("Your bill:", how_many * st.session_state.price)
        else:
            st.error("Sorry, not enough seats available")

# Choice 3
elif st.session_state.choice == 3:
    st.write("### 3. Admin: Add seats and change price")
    admin_password = st.text_input("Enter admin password", type="password")

    if admin_password == password:
        new_seats = st.number_input(
            "How many seats do you want to add?",
            min_value=0,
            step=1,
        )

        if st.button("Add Seats"):
            st.session_state.available_seats += new_seats
            st.success("Seats added successfully")
            st.write("Current seats:", st.session_state.available_seats)

        new_price = st.number_input(
            "Set new ticket price",
            min_value=0,
            step=10,
        )

        if st.button("Change Price"):
            st.session_state.price = new_price
            st.success("Price updated")
            st.write("New price:", st.session_state.price)
    else:
        if admin_password != "":
            st.error("Wrong password")

# Choice 4
elif st.session_state.choice == 4:
    st.write("### 4. Exit")
    st.write("Exiting application")

