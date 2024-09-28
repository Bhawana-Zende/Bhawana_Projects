import streamlit as st

# Title of the app
st.title("Welcome to the Fun Zone! 🎉")

# Greeting message
st.write("🎉 Hi Xinlue! Are you ready for a super awesome game? 🎈")

# Silly questions and their "correct" answers
questions = {
    "If Xinlue could be a vegetable, what would you be? (And why?) 🥦": "Carrot",
    "If you could have any animal as a pet, which animal would you choose? 🎩": "Red Panda",
    "whats xinlues famous sentence 💃🕺": "Play with me ",
    "If you were a character in a cartoon, what would your catchphrase be? 📺": "The Big Ear Tutu!"
}

# Initialize session state to track questions
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0

# Function to display the current question
def display_question():
    question = list(questions.keys())[st.session_state.question_index]
    answer = st.text_input(question)

    if st.button("Submit"):
        if answer:
            correct_answer = questions[question]
            if answer.lower() == correct_answer.lower():
                st.write("🎉 Right! You totally nailed it! 🏆")
            else:
                st.write(f"Oops! That's not quite right. The correct answer is: **{correct_answer}** 😄")
            
            # Move to the next question
            st.session_state.question_index += 1

# Check if there are more questions to ask
if st.session_state.question_index < len(questions):
    display_question()
else:
    st.write("Bhawana loves you, silly boy! 💖 Thanks for playing! Remember, the world needs more fun and laughter!")
    # Reset for another round if desired
    if st.button("Play Again"):
        st.session_state.question_index = 0
