import streamlit as st

st.set_page_config(page_title="Liked Music Player", layout="wide")

# ---- INIT SONG DATA ----
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
        }
    }

# ---- INIT LIKED ----
if "liked" not in st.session_state:
    st.session_state.liked = list(st.session_state.song_data.keys())

# ✅ BEST PRACTICE SYNC (FIX)
st.session_state.liked = [
    song for song in st.session_state.liked
    if song in st.session_state.song_data
]

# ---- HEADER ----
st.markdown("""
<h1 style='color:#FF69B4; text-align:center;'>🎧 Your Liked Music</h1>
<hr>
""", unsafe_allow_html=True)

# ---- SHOW SONGS ----
cols = st.columns(3)

for index, song in enumerate(st.session_state.liked):
    with cols[index % 3]:
        st.markdown(f"""
            <div style="
                background:#1E90FF;
                padding:20px;
                border-radius:15px;
                margin-bottom:20px;">
                <h3 style="color:white;">{song}</h3>
                <p style="color:#eee;">
                    {st.session_state.song_data[song]['artist']}
                </p>
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

song_name = st.text_input("Song name")
artist_name = st.text_input("Artist name")
youtube_link = st.text_input("YouTube link")

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
        st.success("Song added 🎶")
        st.experimental_rerun()
