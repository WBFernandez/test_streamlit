import streamlit as st

# Retrieve the password from secrets
PASSWORD = st.secrets["password"]

# Password prompt
password = st.text_input("Enter the password:", type="password")

if password == PASSWORD:
    st.write("Welcome to the app!")
    # Add your app content here
else:
    st.warning("Invalid password, please try again.")
