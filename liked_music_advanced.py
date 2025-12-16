import streamlit as st

st.set_page_config(page_title="Liked Music Player", layout="wide")

# ---- INIT SONG DATA IN SESSION STATE ----
if "song_data" not in st.session_state:
    st.session_state.song_data = {
        "Flute": {
            "artist": "Krishna",
            "youtube": "https://youtu.be/yRrU0zCUVJg"
        },
        "Mona Lisa": {
            "artist": "Dominic Fike",
            "youtube": "https://youtu.be/XiqN3pOIVIw"
        },
        "Sunflower": {
            "artist": "Post Malone & Swae Lee",
            "youtube": "https://youtu.be/ApXoWvfEYVU"
        },
        "Intentions": {
            "artist": "Justin Bieber ft. Quavo",
            "youtube": "https://youtu.be/3AyMjyHu1bA"
        },
        "Girls Like You": {
            "artist": "Maroon 5 ft. Cardi B",
            "youtube": "https://youtu.be/aJOTlE1K90k"
        }
    }

# ---- INIT LIKED SONGS ----
if "liked" not in st.session_state:
    st.session_state.liked = list(st.session_state.song_data.keys())

# ---- HEADER ----
st.markdown("""
    <h1 style='color:#FF69B4; font-size:48px; text-align:center;'>🎧 Your Liked Music</h1>
    <p style='text-align:center; font-size:18px; color:#1E90FF;'>Paste YouTube links & play instantly</p>
    <hr>
""", unsafe_allow_html=True)

# ---- SHOW LIKED MUSIC ----
cols = st.columns(3)

for index, song in enumerate(st.session_state.liked):
    with cols[index % 3]:
        st.markdown(f"""
            <div style="
              background-color:#1E90FF; 
              padding:20px; 
              border-radius:15px; 
              margin-bottom:20px;
              border-left:6px solid #FF69B4;">
                <h3 style="color:white;">{song}</h3>
                <p style="color:#eee;">{st.session_state.song_data[song]['artist']}</p>
            </div>
        """, unsafe_allow_html=True)

        play = st.button(f"▶ Play {song}", key=f"play_{song}")
        remove = st.button(f"🗑 Remove {song}", key=f"remove_{song}")

        if play:
            st.video(st.session_state.song_data[song]["youtube"])

        if remove:
            st.session_state.liked.remove(song)
            st.experimental_rerun()

# ---- ADD FROM YOUTUBE ----
st.markdown("## ➕ Add Music from YouTube")

song_name = st.text_input("🎵 Song Name")
artist_name = st.text_input("🎤 Artist Name")
youtube_link = st.text_input("🔗 YouTube Link")

if st.button("Add Song"):
    if not song_name or not artist_name or not youtube_link:
        st.error("Fill all fields")
    elif song_name in st.session_state.song_data:
        st.warning("Song already exists")
    else:
        st.session_state.song_data[song_name] = {
            "artist": artist_name,
            "youtube": youtube_link
        }
        st.session_state.liked.append(song_name)
        st.success("Song added successfully 🎶")
        st.experimental_rerun()

