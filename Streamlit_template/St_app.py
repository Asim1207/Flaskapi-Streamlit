import streamlit as st
import requests
import pandas as pd
import openai  # Make sure you have the 'openai' library installed and your API key configured

# Streamlit UI elements
st.title("Employee Leave Information")

# Input for Employee ID
employee_id = st.number_input("Enter Employee ID", min_value=1, value=1)

# Button to fetch leave information
if st.button("Fetch Leave Information"):
    # Make a GET request to the Flask API
    response = requests.get(f"http://localhost:5000/get_leave_info?EmployeeID={employee_id}")
    
    if response.status_code == 200:
        employee_data = response.json()
        st.subheader("Leave Information")
        st.write(f"Employee ID: {employee_data['EmployeeID']}")
        st.write(f"Total Leaves: {employee_data['TotalLeaves']}")
        st.write(f"Leaves Availed: {employee_data['LeavesAvailed']}")
        
        # Example GPT-3 usage
        st.subheader("GPT-3 Generated Text")
        
        # Use the 'employee_data' in a GPT-3 call
        gpt_response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Employee {employee_id} has {employee_data['TotalLeaves']} total leaves and has availed {employee_data['LeavesAvailed']} leaves. Generate a message for this employee.",
            max_tokens=50  # Adjust the number of tokens as needed
        )
        
        generated_text = gpt_response.choices[0].text
        st.write(generated_text)
    elif response.status_code == 404:
        st.error("Employee not found.")
    elif response.status_code == 400:
        st.error("Invalid Employee ID format.")

# Note to the user
st.sidebar.markdown("Note: Make sure the Flask API is running on http://localhost:5000.")
