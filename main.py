import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
	st.image("images/Lee_Dong_Geun.png")

with col2:
	st.title("Andrew Lee")
	contents = """
	Hello, I am Andrew Lee. I am a python developer, and managing director of Hanon Systems Thailand and South Africa. 
	I was on board in Thailand in 2021 and I used to work as planning director in Seoul, Korea.
	Currently, I am in the live project of office automation powered by Python, MySQL and PowerBI and
	this project due is the end of 2024. It will give me a lot of skillsets and improve my operation efficiencies significantly.
	All of apps are dedicated to my project purpose either actual project or training.
	"""
	st.info(contents)