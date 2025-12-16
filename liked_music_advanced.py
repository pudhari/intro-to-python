import streamlit as st

st.set_page_config(page_title="Liked Music Player", layout="wide")

# ---- YOUTUBE PREVIEW LINKS ----
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
        # (keep the rest if you want)
    }


# ---- DEFAULT LIKED SONGS ----
if "liked" not in st.session_state:
    st.session_state.liked = [
        "Flute",
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
              background-color:#1E90FF; 
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
st.markdown("## ➕ Add a Song from YouTube")

song_name = st.text_input("Song name")
artist_name = st.text_input("Artist name")
youtube_link = st.text_input("YouTube link")

if st.button("Add from YouTube"):
    if song_name and artist_name and youtube_link:
        if song_name not in st.session_state.song_data:
            st.session_state.song_data[song_name] = {
                "artist": artist_name,
                "youtube": youtube_link
            }
            st.session_state.liked.append(song_name)
            st.success("Song added successfully 🎶")
            st.experimental_rerun()
        else:
            st.warning("Song already exists!")
    else:
        st.error("Please fill all fields")
