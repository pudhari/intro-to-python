import streamlit as st
import json
import os
import hashlib
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Organised Life", layout="centered")

# ---------------- STYLE ----------------
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

# ---------------- FILES ----------------
USERS_FILE = "users.json"

# ---------------- HELPERS ----------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def save_tasks(username, tasks):
    with open(f"tasks_{username}.json", "w") as f:
        json.dump(tasks, f)

def load_tasks(username):
    file = f"tasks_{username}.json"
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return []

# ---------------- SESSION INIT ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# ---------------- AUTH UI ----------------
st.title("🗓️ Organised Life")

auth_choice = st.radio("Choose action", ["Login", "Sign Up"])

users = load_users()

# ---------------- SIGN UP ----------------
if auth_choice == "Sign Up":
    st.subheader("🆕 Create Account")

    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")

    if st.button("Create Account"):
        if not new_user or not new_pass:
            st.error("All fields required")
        elif new_user in users:
            st.error("Username already exists")
        else:
            users[new_user] = hash_password(new_pass)
            save_users(users)
            save_tasks(new_user, [])
            st.success("Account created! Please login.")

# ---------------- LOGIN ----------------
if auth_choice == "Login":
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == hash_password(password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
        else:
            st.error("Invalid username or password")

# ---------------- STOP IF NOT LOGGED IN ----------------
if not st.session_state.logged_in:
    st.stop()

# ---------------- LOGOUT ----------------
st.sidebar.write(f"👤 {st.session_state.username}")
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.rerun()

# ---------------- LOAD USER TASKS ----------------
raw_tasks = load_tasks(st.session_state.username)
tasks = [
    {
        "task": t["task"],
        "time": datetime.strptime(t["time"], "%I:%M %p"),
        "done": t["done"]
    }
    for t in raw_tasks
]

# ---------------- ADD TASK ----------------
st.subheader("➕ Add Task")
task_name = st.text_input("Task")
time_input = st.text_input("Time (HH:MM AM/PM)", placeholder="6:30 PM")

if st.button("Add Task"):
    try:
        time_obj = datetime.strptime(time_input.upper(), "%I:%M %p")
        tasks.append({"task": task_name, "time": time_obj, "done": False})

        save_tasks(st.session_state.username, [
            {
                "task": t["task"],
                "time": t["time"].strftime("%I:%M %p"),
                "done": t["done"]
            }
            for t in tasks
        ])
        st.success("Task added")
        st.rerun()
    except:
        st.error("Invalid time format")

# ---------------- SHOW TASKS ----------------
tasks.sort(key=lambda x: x["time"])

st.subheader("📋 Your Tasks")

for i, t in enumerate(tasks):
    style = "done" if t["done"] else ""
    time_str = t["time"].strftime("%I:%M %p")

    st.markdown(
        f"<div class='card'><span class='{style}'><b>{time_str}</b> → {t['task']}</span></div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Done", key=f"d{i}"):
            tasks[i]["done"] = True

    with col2:
        if st.button("🗑 Remove", key=f"r{i}"):
            tasks.pop(i)

# ---------------- SAVE CHANGES ----------------
save_tasks(st.session_state.username, [
    {
        "task": t["task"],
        "time": t["time"].strftime("%I:%M %p"),
        "done": t["done"]
    }
    for t in tasks
])

