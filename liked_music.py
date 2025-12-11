import streamlit as st

# ---- DATA (fake album covers for demo) ----
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

# ---- INITIAL SONG LIST ----
shopping_cart = ["Work", "Mona Lisa", "Sunflower", "intentions"]

# Apply your code logic:
add_item = "Closer"
shopping_cart.append(add_item)

remove_item = "Work"
shopping_cart.remove(remove_item)

# ---- STREAMLIT UI ----
st.set_page_config(page_title="Spotify Liked Songs", layout="wide")

# Header
st.markdown("""
    <h1 style='color:#1DB954; font-size:48px;'>🎵 Spotify Liked Songs</h1>
    <p style='font-size:20px; color:#ccc;'>Your saved tracks — Streamlit Edition</p>
    <hr style='border:1px solid #1DB954;'>
""", unsafe_allow_html=True)


# Display songs
cols = st.columns(3)  # grid layout

for index, song in enumerate(shopping_cart):
    with cols[index % 3]:
        st.image(song_data[song]["cover"], width=250)
        st.markdown(f"""
            <div style="padding:10px; background-color:#111; border-radius:10px; margin-top:-10px;">
                <h3 style="color:white;">{song}</h3>
                <p style="color:#1DB954;">{song_data[song]['artist']}</p>
            </div>
        """, unsafe_allow_html=True)


# Footer
st.markdown("""
    <br><br>
    <center>
    <p style='color:#888;'>Built with ❤️ using Streamlit</p>
    </center>
""", unsafe_allow_html=True)
