import streamlit as st
 
# import the class already wrote in server.py
from server import OllamaEGchatbot
 

st.set_page_config(page_title="Email Generator", page_icon="✉️", layout="centered")
st.title("AI Email Generator")
st.caption("Fill in the details below and get a ready‑to‑send email body.")
 
# initialise the chatbot (same model & history file)
bot = OllamaEGchatbot()
 

with st.form("email_form"):
    email_type     = st.text_input("Email Type", placeholder="apology / request / follow‑up")
    tone           = st.selectbox("Tone", ["formal", "casual", "friendly"])
    recipient_role = st.text_input("Recipient Role", placeholder="manager / HR / client")
    key_points     = st.text_area("Purpose", height=100)
 
    submitted = st.form_submit_button("Generate Email")
 

if submitted:
    if not all([email_type, tone, recipient_role, key_points]):
        st.warning("Please fill in every field.")
        st.stop()
 
    user_data = {
        "email_type": email_type.strip(),
        "tone": tone.strip(),
        "recipient_role": recipient_role.strip(),
        "key_points": key_points.strip(),
    }
 
    with st.spinner("Generating email…"):
        try:
            email_body = bot.chat(user_data)
        except Exception as exc:
            st.error(f"Failed to generate email: {exc}")
            st.stop()
 
    st.success("Generated Email")
    st.text_area("Email Body", value=email_body, height=250)