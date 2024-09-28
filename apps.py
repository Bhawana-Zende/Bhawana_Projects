import openai
import streamlit as st
import requests
from bs4 import BeautifulSoup

# Set your OpenAI API key
openai.api_key = "your-openai-api-key"

# Streamlit app layout
st.title("LLM-powered Job Search Assistant")

# Input for job title
job_title = st.text_input("Enter the job title you're looking for (e.g., Product Manager):", "")

# Button to trigger the job search
if st.button("Search Jobs"):
    if job_title:
        # Use GPT-3 to generate a job search summary or job-related advice
        response = openai.Completion.create(
            engine="text-davinci-003",  # GPT-3 engine
            prompt=f"Give me a brief summary of what skills a {job_title} typically needs.",
            max_tokens=100
        )
        
        # Display the LLM-generated job summary
        job_summary = response.choices[0].text.strip()
        st.write(f"Job Summary for {job_title}:")
        st.write(job_summary)

        # Proceed to scrape jobs related to the input job title
        st.write(f"Searching for {job_title} jobs...")

        # Example scraping logic (for demo purposes, Google Jobs scraping)
        url = f"https://www.indeed.com/jobs?q={job_title.replace(' ', '+')}&l="
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            jobs = soup.find_all('a', class_='tapItem')
            if jobs:
                st.write(f"Found {len(jobs)} job listings:")
                for idx, job in enumerate(jobs[:5]):  # Show top 5 results
                    job_title = job.find('h2', class_='jobTitle').text.strip()
                    job_link = "https://www.indeed.com" + job['href']
                    st.write(f"**Job Title**: {job_title}")
                    st.write(f"[Apply here]({job_link})")
                    st.write("---")
            else:
                st.write(f"No jobs found for **{job_title}**.")
        else:
            st.write("Unable to access job listings. Please try again later.")
    else:
        st.write("Please enter a job title.")
