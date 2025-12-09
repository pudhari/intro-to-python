import streamlit as st

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Attendance System",
    page_icon="📘",
    layout="centered"
)

# -------------------- PAGE STYLING (Moodle-like) --------------------
st.markdown("""
    <style>
        body {
            background-color: #f2f5f9;
        }
        .main-title {
            text-align: center;
            font-size: 38px;
            font-weight: 700;
            color: #1a237e;
            margin-bottom: 10px;
        }
        .card {
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 4px 14px rgba(0,0,0,0.12);
            width: 500px;
            margin: auto;
        }
        .btn-style button {
            width: 100%;
            border-radius: 12px !important;
            padding: 10px 0px !important;
            font-size: 18px !important;
            background-color: #1a237e !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------- MAIN TITLE --------------------
st.markdown("<div class='main-title'>📘 Attendance </div>", unsafe_allow_html=True)

# -------------------- CARD UI --------------------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    division = st.text_input("Division")
    teacher = st.text_input("Teacher Name")
    subject = st.text_input("Subject")

    password_by_teacher = 24565
    student_password = st.text_input("Enter Attendance Password", type="password")

    submit = st.button("Submit", help="Click to process attendance", key="submit_btn")

    if submit:
        if not division or not teacher or not subject or not student_password:
            st.warning("⚠️ Please fill all fields.")
        else:
            st.write("### **Attendance **")
            st.write(f"- **Division:** {division}")
            st.write(f"- **Teacher:** {teacher}")
            st.write(f"- **Subject:** {subject}")

            try:
                student_password = int(student_password)
                if student_password == password_by_teacher:
                    st.success("✅ Attendance Given")
                else:
                    st.error("❌ Attendance Not Given (Wrong Password)")
            except:
                st.error("❌ Password must be a number")

    st.markdown("</div>", unsafe_allow_html=True)
