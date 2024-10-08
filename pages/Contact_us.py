import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key="email_form"):
	user_email = st.text_input("Your email address")
	message = st.text_area("Message")
	submit_button = st.form_submit_button("Submit") #Boolean returns : Default Fals
	if submit_button:
		send_email(user_email, message)
		st.info("Your email was sent successfully!!")

