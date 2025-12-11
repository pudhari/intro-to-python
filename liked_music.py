import streamlit as st

# ---- SONG DATABASE ----
song_data = {
    "Work": {
        "artist": "Rihanna ft. Drake",
        "cover": "https://i.scdn.co/image/ab67616d0000b273c687ea51ce5e0790871b49a8"
    },
    "Mona Lisa": {
        "artist": "Lil Wayne ft. Kendrick Lamar",
        "cover": "https://i.scdn.co/image/ab67616d0000b273fa5cbe2ad65379b3f90d4b0d"
    },
    "Sunflower": {
        "artist": "Post Malone & Swae Lee",
        "cover": "https://i.scdn.co/image/ab67616d0000b27338a5c6c2c6f0efa3d2d1e4f1"
    },
    "intentions": {
        "artist": "Justin Bieber ft. Quavo",
        "cover": "https://i.scdn.co/image/ab67616d0000b2738d0683be57c8f2c1fe50c2b7"
    },
    "Closer": {
        "artist": "The Chainsmokers ft. Halsey",
        "cover": "https://i.scdn.co/image/ab67616d0000b27308c8c64c1e57a7ed29c2a793"
    },
    "My Mind & Me": {
        "artist": "Selena Gomez",
        "cover": "https://i.scdn.co/image/ab67616d0000b273e0d3cf492819e93915c93d95"
    },
    "Girls Like You": {
        "artist": "Maroon 5 ft. Cardi B",
        "cover": "https://i.scdn.co/image/ab67616d0000b27348eac0c3d5da5a0eab7e2b0b"
    },
    "Come Around Me": {
        "artist": "Justin Bieber",
        "cover": "https://i.scdn.co/image/ab67616d0000b2732b93926ab9dd98ec6053b457"
    },
    "Let Me": {
        "artist": "Zayn",
        "cover": "https://i.scdn.co/image/ab67616d0000b273a623a5a563b7c030546be9e5"
    },
    "Back To You": {
        "artist": "Selena Gomez",
        "cover": "https://i.scdn.co/image/ab67616d0000b273665fb692e8a54915d805885c"
    }
}


# ---- SESSION STATE ----
if "liked" not in st.session_state:
    st.session_state.liked = [
        "Work", "Mona Lisa", "Sunflower", "intentions",
        "My Mind & Me", "Girls Like You", "Come Around Me",
        "Let Me", "Back To You"
    ]


# ---- PAGE CONFIG ----
st.set_page_config(page_title="Spotify Liked Songs", layout="wide")

# ---- HEADER ----
st.markdown("""
    <h1 style='color:#1DB954; font-size:48px;'>🎵 Spotify Liked Songs</h1>
    <p style='font-size:20px; color:#ccc;'>Your favourite tracks — Streamlit Edition</p>
    <hr style='border:1px solid #1DB954;'>
""", unsafe_allow_html=True)


# -------------------------------------
# 1️⃣ SHOW LIKED SONGS FIRST
# -------------------------------------
st.subheader("💚 Your Liked Songs")

cols = st.columns(3)

for i, song in enumerate(st.session_state.liked):
    with cols[i % 3]:
        st.image(song_data[song]["cover"], width=250)
        st.markdown(f"""
        <div style="padding:10px; background-color:#111; border-radius:10px; margin-top:-10px;">
            <h3 style="color:white;">{song}</h3>
            <p style="color:#1DB954;">{song_data[song]["artist"]}</p>
        </div>
        """, unsafe_allow_html=True)


st.write("---")


# -------------------------------------
# 2️⃣ ADD SONG SECTION
# -------------------------------------
st.subheader("➕ Add a Song to Liked List")

add_choice = st.selectbox("Select a song:", list(song_data.keys()))

if st.button("Add to Liked"):
    if add_choice not in st.session_state.liked:
        st.session_state.liked.append(add_choice)
        st.success(f"Added **{add_choice}**!")
    else:
        st.warning("This song is already in your liked list.")


# -------------------------------------
# 3️⃣ REMOVE SONG SECTION
# -------------------------------------
st.subheader("➖ Remove a Song From Liked List")

remove_choice = st.selectbox("Select a song to remove:", st.session_state.liked)

if st.button("Remove"):
    st.session_state.liked.remove(remove_choice)
    st.error(f"Removed **{remove_choice}**")


# -------------------------------------
# FOOTER
# -------------------------------------
st.markdown("""
    <center><p style='color:#666; margin-top:40px;'>Built with ❤️ using Streamlit</p></center>
""", unsafe_allow_html=True)
