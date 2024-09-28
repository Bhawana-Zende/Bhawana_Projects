import openai
import streamlit as st

# Set your OpenAI API key
openai.api_key = "your-openai-api-key"

# Streamlit app layout
st.title("LLM-powered Job Search Assistant")

# Input for job title
job_title = st.text_input("Enter the job title you're looking for (e.g., Product Manager):", "")

# Button to trigger the job search
if st.button("Search Jobs"):
    if job_title:
        # Use ChatCompletion instead of Completion for the new OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the appropriate model like "gpt-3.5-turbo" or "gpt-4"
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Give me a brief summary of what skills a {job_title} typically needs."}
            ]
        )
        
        # Display the LLM-generated job summary
        job_summary = response['choices'][0]['message']['content'].strip()
        st.write(f"Job Summary for {job_title}:")
        st.write(job_summary)
