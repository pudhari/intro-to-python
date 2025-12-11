import streamlit as st
import hashlib
import textwrap

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Liked Songs — Clean UI + Audio", layout="wide", page_icon="🎧")

# ---------------- DATA ----------------
song_data = {
    "Work": {"artist": "Rihanna ft. Drake"},
    "Mona Lisa": {"artist": "Lil Wayne ft. Kendrick Lamar"},
    "Sunflower": {"artist": "Post Malone & Swae Lee"},
    "intentions": {"artist": "Justin Bieber ft. Quavo"},
    "Closer": {"artist": "The Chainsmokers ft. Halsey"},
    "My Mind & Me": {"artist": "Selena Gomez"},
    "Girls Like You": {"artist": "Maroon 5 ft. Cardi B"},
    "Come Around Me": {"artist": "Justin Bieber"},
    "Let Me": {"artist": "Zayn"},
    "Back To You": {"artist": "Selena Gomez"}
}

# ---- Audio previews (public example mp3s) ----
# Replace these URLs with real preview mp3 URLs when you have them.
song_previews = {
    "Work": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "Mona Lisa": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "Sunflower": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
    "intentions": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
    "Closer": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3",
    "My Mind & Me": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3",
    "Girls Like You": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3",
    "Come Around Me": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3",
    "Let Me": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3",
    "Back To You": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3"
}

# ---------------- SESSION STATE ----------------
if "liked" not in st.session_state:
    st.session_state.liked = [
        "My Mind & Me", "Girls Like You", "Come Around Me", "Let Me", "Back To You",
        "Work", "Mona Lisa", "Sunflower", "intentions"
    ]

# Keep track of which song's audio player should be visible
if "playing_song" not in st.session_state:
    st.session_state.playing_song = None

# ---------------- HELPER: color by name ----------------
BASE_COLORS = [
    "#1DB954", "#5B9BD5", "#F39C12", "#8E44AD", "#E74C3C",
    "#16A085", "#2C3E50", "#D35400", "#7F8C8D", "#27AE60"
]

def color_for(text: str) -> str:
    """Return a deterministic color based on the string hash."""
    h = int(hashlib.md5(text.encode("utf-8")).hexdigest()[:8], 16)
    return BASE_COLORS[h % len(BASE_COLORS)]

def initials(name: str, length: int = 2) -> str:
    parts = name.split()
    if len(parts) == 1:
        return (parts[0][:length]).upper()
    return (parts[0][0] + parts[-1][0]).upper()

# ---------------- STYLES ----------------
st.markdown(
    """
    <style>
    /* page */
    .top-row { display:flex; justify-content:space-between; align-items:center; gap:16px; }
    .title { font-size:34px; color:#0f172a; font-weight:700; margin:0; }
    .subtitle { color:#6b7280; margin:0; font-size:14px; }

    /* grid */
    .grid { display:flex; flex-wrap:wrap; gap:20px; align-items:flex-start; }
    .card {
        min-width:220px;
        max-width:320px;
        border-radius:16px;
        padding:18px;
        box-shadow: 0 8px 24px rgba(15,23,42,0.06);
        transition: transform .14s ease, box-shadow .14s ease;
        background: white;
    }
    .card:hover { transform: translateY(-6px); box-shadow: 0 18px 40px rgba(15,23,42,0.12); }
    .avatar {
        height:72px; width:72px; border-radius:14px;
        display:flex; align-items:center; justify-content:center;
        font-weight:800; font-size:20px; color:white;
        margin-bottom:12px;
    }
    .song-title { font-size:18px; margin:0 0 6px 0; color:#0b1220; font-weight:700; }
    .artist { font-size:13px; margin:0; color:#475569; }

    .controls { display:flex; gap:10px; margin-top:14px; }
    .small-btn { padding:8px 12px; border-radius:10px; border:none; cursor:pointer; font-weight:600; }
    .remove-btn { background:transparent; color:#ef4444; border:1px solid rgba(239,68,68,0.12); }
    .play-btn { background:#111827; color:white; border:1px solid rgba(0,0,0,0.04); }

    /* responsive tweaks */
    @media (max-width:900px) {
        .grid { justify-content:center; }
    }
    </style>
    """, unsafe_allow_html=True
)

# ---------------- HEADER ----------------
col1, col2 = st.columns([3,1])
with col1:
    st.markdown("<div class='top-row'><div><h1 class='title'>Liked Songs</h1><p class='subtitle'>Clean cards • no images • colorful and professional</p></div></div>", unsafe_allow_html=True)
with col2:
    # compact stats box
    st.markdown(f"<div style='text-align:right;color:#374151'><strong>{len(st.session_state.liked)}</strong><br><span style='font-size:12px;color:#9ca3af'>songs</span></div>", unsafe_allow_html=True)

st.write("")  # spacing

# ---------------- ADD / REMOVE UI (compact) ----------------
with st.expander("Manage songs", expanded=True):
    cols = st.columns([3,1,1])
    with cols[0]:
        available_to_add = [s for s in song_data.keys() if s not in st.session_state.liked]
        if available_to_add:
            to_add = st.selectbox("Add a song to liked list", available_to_add)
        else:
            to_add = None
            st.info("No more songs available to add.")
    with cols[1]:
        if st.button("Add") and to_add:
            if to_add and to_add not in st.session_state.liked:
                st.session_state.liked.insert(0, to_add)  # add to top (liked shown first)
                st.success(f"Added '{to_add}' to liked songs")
            else:
                st.warning("Please select a valid song.")
    with cols[2]:
        if st.session_state.liked:
            to_remove = st.selectbox("Remove a song", st.session_state.liked, key="remove_dropdown")
            if st.button("Remove"):
                if to_remove in st.session_state.liked:
                    st.session_state.liked.remove(to_remove)
                    # stop any playing audio if that song was playing
                    if st.session_state.playing_song == to_remove:
                        st.session_state.playing_song = None
                    st.experimental_rerun()
        else:
            st.info("No liked songs to remove.")

st.write("---")

# ---------------- SHOW LIKED SONGS GRID ----------------
st.markdown("<div class='grid'>", unsafe_allow_html=True)

# We'll display cards in columns using Streamlit layout to keep interactivity (remove button)
cols = st.columns(3)
for idx, song in enumerate(list(st.session_state.liked)):  # copy list to avoid mutation issues
    col = cols[idx % 3]
    with col:
        col_color = color_for(song)
        avatar_html = f"<div class='avatar' style='background:{col_color};'>{initials(song)}</div>"
        # Safe f-string expression for artist (fixed bug by using {} literal inside expression)
        artist_text = song_data.get(song, {}).get('artist', 'Unknown Artist')
        card_html = textwrap.dedent(f"""
            <div class='card'>
                {avatar_html}
                <div>
                    <p class='song-title'>{song}</p>
                    <p class='artist'>{artist_text}</p>
                </div>
        """)
        st.markdown(card_html, unsafe_allow_html=True)

        # action buttons under each card
        r_col1, r_col2 = st.columns([2,1])
        with r_col1:
            if st.button("Play", key=f"play_{song}"):
                # set the playing song so we can show a player
                st.session_state.playing_song = song
                # don't rerun here; player will appear below
        with r_col2:
            if st.button("Remove", key=f"remove_{song}"):
                if song in st.session_state.liked:
                    st.session_state.liked.remove(song)
                    if st.session_state.playing_song == song:
                        st.session_state.playing_song = None
                    st.experimental_rerun()

        # close card div
        st.markdown("</div>", unsafe_allow_html=True)

        # If this song is selected for play, show audio player
        if st.session_state.playing_song == song:
            preview_url = song_previews.get(song)
            if preview_url:
                st.audio(preview_url)
            else:
                st.info("Preview not available for this song.")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.write("")
st.markdown("<div style='color:#6b7280; font-size:13px;'>Tip: Click Play to open the audio preview for a song. Replace the preview URLs with real song preview links when available.</div>", unsafe_allow_html=True)
