import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Organised Life", layout="centered")

# ---------- THEME ----------
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
st.markdown("Plan your day. Stay disciplined.")
st.markdown("---")

# ---------- SESSION STATE ----------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# ---------- ADD TASK ----------
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
            st.success("Task added ✅")
        except ValueError:
            st.error("Invalid time format")

# ---------- SORT TASKS ----------
st.session_state.tasks.sort(key=lambda x: x["time"])

st.markdown("---")
st.subheader("📋 Your Tasks")

# ---------- SHOW TASKS ----------
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
            st.experimental_rerun()

    with col2:
        if st.button("🗑 Remove", key=f"remove_{index}"):
            st.session_state.tasks.pop(index)
            st.experimental_rerun()

st.markdown("---")
st.write("Stay organised 💪")
