from modules.send_email import send_email
import streamlit as st


# Webpage configuration
st.set_page_config(
    page_title="Contact Us", 
    page_icon=":email:",
    layout="centered"
)

st.title("Contact Me")
# Create a Form with some elements
with st.form(key="email_forms"):
    user_email = st.text_input(label="Your email address")
    raw_message = st.text_area(label="Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}

{raw_message}
"""
    button = st.form_submit_button(label="Submit", use_container_width=True)
    # If button is clicked will send the email a show a message
    if button:
        send_email(message=message)
        st.success(body="Your email was sent successfully!", icon="✅") # Shortcodes are not allowed here!