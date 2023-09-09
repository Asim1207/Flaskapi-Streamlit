import streamlit as st
from api_utils import fetch_leave_info
from ui_utils import display_leave_information, display_error_message

def main():
    st.title("Employee Leave Information")

    employee_id = st.number_input("Enter Employee ID", min_value=1, value=1)

    if st.button("Fetch Leave Information"):
        employee_data, response_status = fetch_leave_info(employee_id)

        if response_status == 200:
            display_leave_information(employee_data)
        elif response_status == 404:
            display_error_message("Employee not found.")
        elif response_status == 400:
            display_error_message("Invalid Employee ID format.")

    st.sidebar.markdown("Note: Make sure the Flask API is running on http://localhost:5000.")

if __name__ == "__main__":
    main()
