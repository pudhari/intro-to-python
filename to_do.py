import streamlit as st
import json
import os
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Organised Life", layout="centered")

# ---------------- BASIC THEME ----------------
st.markdown("""
<style>
body { background-color: #ffecec; }
.card {
    background-color: #fff5f5;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}
.done {
    text-decoration: line-through;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# ---------------- USER AUTH (BASIC) ----------------
USERS = {
    "alice": "1234",
    "bob": "abcd",
    "admin": "admin"
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# ---------------- LOGIN SCREEN ----------------
if not st.session_state.logged_in:
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.error("Invalid username or password")

    st.stop()

# ---------------- LOGOUT ----------------
st.sidebar.write(f"👤 Logged in as **{st.session_state.username}**")
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.rerun()

# ---------------- USER-SPECIFIC FILE ----------------
FILE_NAME = f"tasks_{st.session_state.username}.json"

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f)

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# ---------------- LOAD TASKS ----------------
if "tasks" not in st.session_state:
    raw = load_tasks()
    st.session_state.tasks = [
        {
            "task": t["task"],
            "time": datetime.strptime(t["time"], "%I:%M %p"),
            "done": t["done"]
        }
        for t in raw
    ]

# ---------------- APP UI ----------------
st.title("🗓️ Organised Life")
st.write("Your personal to-do list")
st.markdown("---")

# ---------------- ADD TASK ----------------
task = st.text_input("Task")
time_input = st.text_input("Time (HH:MM AM/PM)", placeholder="6:30 PM")

if st.button("Add Task"):
    try:
        time_obj = datetime.strptime(time_input.upper(), "%I:%M %p")
        st.session_state.tasks.append({
            "task": task,
            "time": time_obj,
            "done": False
        })

        save_tasks([
            {
                "task": t["task"],
                "time": t["time"].strftime("%I:%M %p"),
                "done": t["done"]
            }
            for t in st.session_state.tasks
        ])

        st.success("Task added ✅")
        st.rerun()

    except ValueError:
        st.error("Invalid time format")

# ---------------- SORT ----------------
st.session_state.tasks.sort(key=lambda x: x["time"])

# ---------------- SHOW TASKS ----------------
st.markdown("---")
st.subheader("📋 Your Tasks")

if not st.session_state.tasks:
    st.info("No tasks yet")

for i, t in enumerate(st.session_state.tasks):
    time_str = t["time"].strftime("%I:%M %p")
    style = "done" if t["done"] else ""

    st.markdown(
        f"<div class='card'><span class='{style}'><b>{time_str}</b> → {t['task']}</span></div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Done", key=f"done_{i}"):
            st.session_state.tasks[i]["done"] = True
            save_tasks([
                {
                    "task": t["task"],
                    "time": t["time"].strftime("%I:%M %p"),
                    "done": t["done"]
                }
                for t in st.session_state.tasks
            ])
            st.rerun()

    with col2:
        if st.button("🗑 Remove", key=f"remove_{i}"):
            st.session_state.tasks.pop(i)
            save_tasks([
                {
                    "task": t["task"],
                    "time": t["time"].strftime("%I:%M %p"),
                    "done": t["done"]
                }
                for t in st.session_state.tasks
            ])
            st.rerun()

st.markdown("---")
st.write("🔒 Your tasks are private to your account")
