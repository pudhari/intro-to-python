import streamlit as st

# initial values (session state)
if "available_seats" not in st.session_state:
    st.session_state.available_seats = 5

if "price" not in st.session_state:
    st.session_state.price = 150

password = "abcd"  # admin password

st.title("🎬 Movie Booking System")
st.write("=" * 47)

choice = st.selectbox(
    "What do you want to do?",
    (
        "Check available seats and ticket price",
        "Book tickets",
        "Admin: add seats and change price",
        "Exit",
    ),
)

st.write("=" * 47)

# Option 1
if choice == "Check available seats and ticket price":
    st.write("Available seats:", st.session_state.available_seats)
    st.write("Ticket price:", st.session_state.price)

# Option 2
elif choice == "Book tickets":
    how_many = st.number_input(
        "How many seats do you want to book?",
        min_value=1,
        step=1,
    )

    if st.button("Book"):
        if st.session_state.available_seats >= how_many:
            st.session_state.available_seats -= how_many
            st.success("Tickets booked successfully!")
            st.write("Remaining seats:", st.session_state.available_seats)
            st.write("Your bill:", how_many * st.session_state.price)
        else:
            st.error("Sorry, not enough seats available")

# Option 3
elif choice == "Admin: add seats and change price":
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
            st.write("Current available seats:", st.session_state.available_seats)

        new_price = st.number_input(
            "Set new ticket price",
            min_value=0,
            step=10,
        )

        if st.button("Change Price"):
            st.session_state.price = new_price
            st.success("Price updated successfully")
            st.write("New ticket price:", st.session_state.price)
    else:
        if admin_password != "":
            st.error("Wrong password")

# Option 4
elif choice == "Exit":
    st.write("Exiting application")
