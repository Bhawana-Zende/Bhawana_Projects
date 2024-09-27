import streamlit as st

# Title of the app
st.title("Welcome App")

# Asking for the user's name
name = st.text_input("Hi! What's your name?")

# If the user enters their name
if name:
    st.write(f"Hello, {name}! Welcome to Streamlit!")

    # Food options
    food_options = ["Pizza", "Burger", "Pasta"]
    selected_food = st.selectbox("Please select your food:", food_options)

    # Confirmation message
    st.write(f"You have selected: {selected_food}")
    st.write("Your food is going to be ready in 15 minutes!")


