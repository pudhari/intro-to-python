import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="SSE Productions", layout="centered")

# ---------------- CINEMA THEME ----------------
st.markdown("""
<style>
body {
    background-color: #ffe5e5;
}
.movie-card {
    background-color: #ffcccc;
    padding: 15px;
    border-radius: 10px;
    color: black;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("🎬 Welcome to SSE Productions")
st.markdown("---")

# ---------------- SESSION STATE ----------------
if "movies" not in st.session_state:
    st.session_state.movies = ["spiderman", "avengers", "inception", "lilo and stitch"]

if "bookings" not in st.session_state:
    st.session_state.bookings = {}

# ---------------- AVAILABLE MOVIES ----------------
st.subheader("🎥 Available Movies")
st.write(st.session_state.movies)

# ---------------- ADD MOVIE ----------------
st.markdown("### ➕ Add Movie")
new_movie = st.text_input("Enter movie name to add")

if st.button("Add Movie"):
    if new_movie:
        st.session_state.movies.append(new_movie.lower())
        st.success("Movie added successfully 🎉")

# ---------------- REMOVE MOVIE ----------------
st.markdown("### ➖ Remove Movie")
movie_to_remove = st.text_input("Enter movie name to remove")

if st.button("Remove Movie"):
    if movie_to_remove in st.session_state.movies:
        st.session_state.movies.remove(movie_to_remove)
        st.success("Movie removed successfully ✅")
    else:
        st.error("Movie not found ❌")

st.markdown("---")

# ---------------- SEATS ----------------
seats = ("a1", "a2", "a3", "a4", "a5", "a6")
st.subheader("💺 Available Seats")
st.write(seats)

st.markdown("---")

# ---------------- BOOKING ----------------
st.subheader("🎟️ Book Your Ticket")

movie_to_watch = st.selectbox("Select movie", st.session_state.movies)
seat = st.selectbox("Select seat", seats)
qty = st.number_input("Number of seats", min_value=1, max_value=6, step=1)

if st.button("Book Ticket"):
    booking_key = movie_to_watch + "-" + seat
    st.session_state.bookings[booking_key] = "BOOKED"

    st.success("Booking Successful 🎉")

    # ---------------- BILL ----------------
    price = 500
    total = price * qty

    st.markdown("## 🧾 Your Bill")
    st.markdown(f"""
    <div class="movie-card">
        <p><b>Movie:</b> {movie_to_watch}</p>
        <p><b>Seat:</b> {seat}</p>
        <p><b>Tickets:</b> {qty}</p>
        <p><b>Price per ticket:</b> ₹{price}</p>
        <hr>
        <p><b>Total Amount:</b> ₹{total}</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- SHOW BOOKINGS ----------------
st.markdown("---")
st.subheader("📌 Current Bookings")
st.write(st.session_state.bookings)
