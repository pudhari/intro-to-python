import streamlit as st
import json
import os
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Organised Life", layout="centered")

# ---------------- THEME ----------------
st.markdown("""
<style>
body {
    background-color: #ffecec;
}
.task-card {
    background-color: #fff5f5;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
    color: black;
}
.done {
    text-decoration: line-through;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

st.title("🗓️ Organised Life")
st.write("Plan your day. Stay consistent.")
st.markdown("---")

# ---------------- FILE STORAGE ----------------
FILE_NAME = "tasks.json"

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f)

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# ---------------- SESSION STATE ----------------
if "tasks" not in st.session_state:
    raw_tasks = load_tasks()
    st.session_state.tasks = [
        {
            "task": t["task"],
            "time": datetime.strptime(t["time"], "%I:%M %p"),
            "done": t["done"]
        }
        for t in raw_tasks
    ]

# ---------------- ADD TASK ----------------
st.subheader("➕ Add a Task")

task_name = st.text_input("Task")
time_input = st.text_input("Time (HH:MM AM/PM)", placeholder="6:30 PM")

if st.button("Add Task"):
    if not task_name or not time_input:
        st.error("Please enter task and time")
    else:
        try:
            time_obj = datetime.strptime(time_input.upper(), "%I:%M %p")

            st.session_state.tasks.append({
                "task": task_name,
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
            st.error("Invalid time format. Use HH:MM AM/PM")

# ---------------- SORT TASKS ----------------
st.session_state.tasks.sort(key=lambda x: x["time"])

# ---------------- SHOW TASKS ----------------
st.markdown("---")
st.subheader("📋 Your Tasks")

if not st.session_state.tasks:
    st.info("No tasks yet. Add one above ☝️")

for index, t in enumerate(st.session_state.tasks):
    time_str = t["time"].strftime("%I:%M %p")
    task_style = "done" if t["done"] else ""

    st.markdown(f"""
        <div class="task-card">
            <span class="{task_style}">
                <b>{time_str}</b> → {t['task']}
            </span>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Mark Done", key=f"done_{index}"):
            st.session_state.tasks[index]["done"] = True

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
        if st.button("🗑 Remove", key=f"remove_{index}"):
            st.session_state.tasks.pop(index)

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
st.write("💪 Stay organised. Small steps daily.")
