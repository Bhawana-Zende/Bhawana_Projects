import streamlit as st
import requests
import json

# Initialize session state
if 'progress' not in st.session_state:
    st.session_state['progress'] = 0
if 'level' not in st.session_state:
    st.session_state['level'] = 'Beginner'
if 'questions' not in st.session_state:
    st.session_state['questions'] = []
if 'answers' not in st.session_state:
    st.session_state['answers'] = []

# Define a function to query the Ollama model
def query_llm(prompt):
    # The local Ollama API is typically running at this address
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "gpt-3.5",  # Adjust the model name as per your local setup, e.g., "llama2" or any other model
        "prompt": prompt
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        return response.json()["text"].strip()
    else:
        st.error("Failed to get response from the local LLM. Make sure Ollama is running.")
        return ""

# Function to ask the user questions based on their progress and level
def ask_question(level, topic):
    prompt = f"Generate a {level} level question about {topic}."
    question = query_llm(prompt)
    return question

# Function to handle user progress and content delivery
def deliver_content(level, topic):
    prompt = f"Explain {topic} for a {level} learner. Break it into smaller chunks."
    content = query_llm(prompt)
    st.write(content)
    st.session_state['progress'] += 1

# Dynamic interaction based on user input and level
def dynamic_interaction(level, topic):
    st.write(f"You are currently learning about {topic} at the {level} level.")
    if st.session_state['progress'] == 0:
        deliver_content(level, topic)
    else:
        question = ask_question(level, topic)
        st.write(question)
        user_answer = st.text_input("Your answer: ")
        if user_answer:
            # Evaluate user answer using LLM
            feedback_prompt = f"Evaluate the user's answer: '{user_answer}' for the question: '{question}'."
            feedback = query_llm(feedback_prompt)
            st.write(feedback)
            st.session_state['answers'].append(user_answer)
            st.session_state['questions'].append(question)

            if "correct" in feedback.lower():
                st.session_state['progress'] += 1
                st.success("Great job! Moving to the next question or level.")
            else:
                st.warning("Try again or ask for clarification.")
                if st.button("Clarification"):
                    clarification = query_llm(f"Explain the correct answer to: '{question}'")
                    st.write(clarification)

# Main app structure
st.title("Interactive Learning with GPT (Ollama)")
st.subheader("Learn concepts step-by-step with personalized questions and feedback")

# User onboarding
st.write("Welcome! Let’s start by understanding your knowledge level.")
topic = st.text_input("What topic would you like to learn about?", "Python")
level = st.selectbox("How much do you know about this topic?", ["Beginner", "Intermediate", "Advanced"])

if st.button("Start Learning"):
    st.session_state['level'] = level
    dynamic_interaction(level, topic)

# Display user progress
if st.session_state['progress'] > 0:
    st.write(f"Progress: {st.session_state['progress']} lessons completed.")
    if st.session_state['progress'] % 5 == 0:
        st.balloons()

# Option to continue learning or review
if st.session_state['progress'] > 0:
    if st.button("Review Incorrect Answers"):
        for q, a in zip(st.session_state['questions'], st.session_state['answers']):
            st.write(f"Question: {q}")
            st.write(f"Your Answer: {a}")

    if st.button("Advance to Next Level"):
        st.session_state['level'] = "Intermediate" if level == "Beginner" else "Advanced"
        dynamic_interaction(st.session_state['level'], topic)

# Display motivational badges
if st.session_state['progress'] >= 10:
    st.success("Congratulations! You’ve earned a badge for mastering the beginner level.")
