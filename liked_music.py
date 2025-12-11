import streamlit as st

st.set_page_config(page_title="Liked Music Player", layout="wide")

# ---- YOUTUBE PREVIEW LINKS ----
song_data = {
    "Work": {
        "artist": "Rihanna ft. Drake",
        "youtube": "https://youtu.be/HL1UzIK-flA"
    },
    "Mona Lisa": {
        "artist": "Dominic Fike",
        "youtube": "https://youtu.be/XiqN3pOIVIw?si=E-aXA86iS2Z-cV07"
    },
    "Sunflower": {
        "artist": "Post Malone & Swae Lee",
        "youtube": "https://youtu.be/ApXoWvfEYVU?si=TrRfsWimtAbPfZck"
    },
    "Intentions": {
        "artist": "Justin Bieber ft. Quavo",
        "youtube": "https://youtu.be/3AyMjyHu1bA?si=KQ3kGF0l4GphAe2P"
    },
    "Girls Like You": {
        "artist": "Maroon 5 ft. Cardi B",
        "youtube": "https://youtu.be/aJOTlE1K90k"
    },
    "Come Around Me": {
        "artist": "Justin Bieber",
        "youtube": "https://youtu.be/GtDwH6fPRMA?si=RbSvZT3OLHZf6C9t"
    },
    "Let Me": {
        "artist": "Zayn",
        "youtube": "https://youtu.be/17ozSeGw-fU"
    },
    "Back To You": {
        "artist": "Selena Gomez",
        "youtube": "https://youtu.be/RQc77zvkaB8"
    },
    "My Mind & Me": {
        "artist": "Selena Gomez",
        "youtube": "https://youtu.be/IOqNz8aNC2g"
    },
    "Closer": {
        "artist": "The Chainsmokers ft. Halsey",
        "youtube": "https://youtu.be/PT2_F-1uJ4I"
    }
}

# ---- DEFAULT LIKED SONGS ----
if "liked" not in st.session_state:
    st.session_state.liked = [
        "Work",
        "Mona Lisa",
        "Sunflower",
        "Intentions",
        "Girls Like You",
        "Come Around Me",
        "Let Me",
        "Back To You",
        "My Mind & Me",
        "Closer"
    ]

st.markdown("""
    <h1 style='color:#FF69B4; font-size:48px; text-align:center;'>🎧 Your Liked Music</h1>
    <p style='text-align:center; font-size:18px; color:#1E90FF;'>Click play to listen</p>
    <hr>
""", unsafe_allow_html=True)

# ---- SHOW LIKED MUSIC ----
cols = st.columns(3)

for index, song in enumerate(st.session_state.liked):
    with cols[index % 3]:
        st.markdown(f"""
            <div style="
              background-color:#3F0028; 
              padding:20px; 
              border-radius:15px; 
              margin-bottom:20px;
              border-left: 6px solid #FF69B4;">
                <h3 style="color:white;">{song}</h3>
                <p style="color:#bbb;">{song_data[song]['artist']}</p>
            </div>
        """, unsafe_allow_html=True)

        play = st.button(f"▶ Play {song}", key=f"play_{song}")
        remove = st.button(f"🗑 Remove {song}", key=f"remove_{song}")

        if play:
            st.video(song_data[song]["youtube"])

        if remove:
            st.session_state.liked.remove(song)
            st.experimental_rerun()


# ---- ADD A SONG ----
st.markdown("## ➕ Add a Song to Liked List")
new_song = st.selectbox("Pick a song:", list(song_data.keys()))

if st.button("Add"):
    if new_song not in st.session_state.liked:
        st.session_state.liked.append(new_song)
        st.success(f"{new_song} added!")
        st.experimental_rerun()
    else:
        st.warning("Already in liked list!")
