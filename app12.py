from langchain_community.llms import Ollama
import streamlit as st

# Initialize the language model
llm = Ollama(model="ollama run llama3.2")

# Fun and creative app title
st.title("✨ Llama the Knowledge Genie ✨")

# Ask for the user's name
user_name = st.text_input("Hey there! What's your name?", placeholder="Your name here")

# Initialize session state for conversation history and user input
if 'messages' not in st.session_state:
    st.session_state.messages = []  # To hold the conversation history
if 'input' not in st.session_state:
    st.session_state.input = ""  # To store the user's current input
if 'welcome_message_shown' not in st.session_state:
    st.session_state.welcome_message_shown = False  # Flag to track welcome message

# Display conversation history
if st.session_state.messages:
    for msg in st.session_state.messages:
        st.markdown(msg)

# Only show the welcome message once after the user enters their name
if user_name and not st.session_state.welcome_message_shown:
    welcome_message = f"👋 Hi {user_name}! I'm Llama, your friendly genie chatbot here to grant your wishes! 🦙✨"
    st.markdown(welcome_message)
    st.session_state.messages.append(welcome_message)  # Add welcome message to history
    st.session_state.welcome_message_shown = True  # Set flag to true

# Input area for user prompts
st.session_state.input = st.text_area("What would you like to ask me?", placeholder="Ask your question here...", value=st.session_state.input)

# Button to generate response
if st.button("Ask Llama!"):
    if st.session_state.input.strip():  # Check if the prompt is provided
        with st.spinner("Llama is thinking... 🤔"):
            try:
                # Generate response from the model
                response = llm(st.session_state.input)  # Call the model directly with the prompt
                
                # Create message strings for display
                user_message = f"👤 {user_name}: {st.session_state.input}"
                llama_response = f"✨ Llama: {response} ✨"

                # Update session state with new messages
                st.session_state.messages.append(user_message)  # Add user's message
                st.session_state.messages.append(llama_response)  # Add Llama's response

                # Clear the input for a new question
                st.session_state.input = ""  # Reset input for the next question
            except Exception as e:  # Handle potential errors
                st.error(f"Eror generating response: {str(e)}")
                st.error("hey000l")
