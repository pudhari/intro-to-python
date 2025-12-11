import streamlit as st

# ---- DATA (song info: artist + album cover) ----
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
    }
}

# ---- SESSION STATE FOR SONG LIST ----
if "shopping_cart" not in st.session_state:
    st.session_state.shopping_cart = ["Work", "Mona Lisa", "Sunflower", "intentions"]


# ---- PAGE CONFIG ----
st.set_page_config(page_title="Spotify Liked Songs", layout="wide")

# ---- HEADER ----
st.markdown("""
    <h1 style='color:#1DB954; font-size:48px;'>🎵 Spotify Liked Songs</h1>
    <p style='font-size:20px; color:#ccc;'>Your saved tracks — Streamlit Edition</p>
    <hr style='border:1px solid #1DB954;'>
""", unsafe_allow_html=True)


# ---- ADD SONG UI ----
st.subheader("➕ Add a Song")
add_option = st.selectbox("Select Song to Add", list(song_data.keys()))
if st.button("Add to Liked Songs"):
    if add_option not in st.session_state.shopping_cart:
        st.session_state.shopping_cart.append(add_option)
        st.success(f"Added **{add_option}** to your liked songs")
    else:
        st.warning("This song is already in your list.")


# ---- REMOVE SONG UI ----
st.subheader("➖ Remove a Song")
remove_option = st.selectbox("Select Song to Remove", st.session_state.shopping_cart)
if st.button("Remove from Liked Songs"):
    st.session_state.shopping_cart.remove(remove_option)
    st.error(f"Removed **{remove_option}** from your liked songs")


st.write("---")


# ---- DISPLAY SONG CARDS ----
cols = st.columns(3)

for index, song in enumerate(st.session_state.shopping_cart):
    with cols[index % 3]:
        st.image(song_data[song]["cover"], width=250)
        st.markdown(f"""
            <div style="padding:10px; background-color:#111; border-radius:10px; margin-top:-10px;">
                <h3 style="color:white;">{song}</h3>
                <p style="color:#1DB954;">{song_data[song]['artist']}</p>
            </div>
        """, unsafe_allow_html=True)


# ---- FOOTER ----
st.markdown("""
    <center><p style='color:#888; margin-top:40px;'>Built with ❤️ using Streamlit</p></center>
""", unsafe_allow_html=True)

