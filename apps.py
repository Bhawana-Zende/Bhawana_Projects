import streamlit as st

st.title("Welcome App")
name = st.text_input("What is your name?")
if name:
    st.write(f"Hello, {name}! Welcome to Streamlit!")
    st.write(f"Hell, {name}! Welcome to Streamlit!")

