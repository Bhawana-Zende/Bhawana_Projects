import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("CSV Data Upload and Visualization")

# Sidebar for CSV upload
uploaded_file = st.sidebar.file_uploader("Upload a CSV", type="csv")

# Function to read CSV and return a DataFrame
def load_csv(file):
    return pd.read_csv(file)

# Display extracted data and allow user to generate graphs
if uploaded_file is not None:
    # Reading the CSV file
    df = load_csv(uploaded_file)
    
    # Display the uploaded CSV file content
    st.write("Uploaded Data:")
    st.write(df)

    # Display the column names in the uploaded file
    st.write("Columns in the uploaded CSV:")
    st.write(df.columns)

    # Let the user select the Category and Values columns from the uploaded data
    category_col = st.selectbox("Select the 'Category' column", df.columns)
    value_col = st.selectbox("Select the 'Values' column", df.columns)
    
    # Data for Visualization
    st.write("Data for Visualization:")
    st.write(df[[category_col, value_col]])

    # Bar chart visualization
    st.subheader('Bar Chart')
    st.bar_chart(df.set_index(category_col)[value_col])

    # Line chart visualization
    st.subheader('Line Chart')
    st.line_chart(df.set_index(category_col)[value_col])

    # Matplotlib Pie chart
    st.subheader('Pie Chart')
    fig, ax = plt.subplots()
    ax.pie(df[value_col], labels=df[category_col], autopct='%1.1f%%')
    st.pyplot(fig)

else:
    st.write("Please upload a CSV file to visualize the data.")
