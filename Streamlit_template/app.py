import streamlit as st
from api_utils import fetch_leave_info
from api_utils import fetch_medical_info
from ui_utils import display_leave_information, display_medical_information, display_error_message

def main():
    st.title("Employee Leave and Medical Information")

    employee_id = st.number_input("Enter Employee ID", min_value=1, value=1)

    if st.button("Fetch Leave Information"):
        leave_response = fetch_leave_info(employee_id)

        if leave_response.status_code == 200:
            leave_data = leave_response.json()
            display_leave_information(leave_data)
        elif leave_response.status_code == 404:
            display_error_message("Leave Information: Employee not found.")
        elif leave_response.status_code == 400:
            display_error_message("Leave Information: Invalid Employee ID format.")

    if st.button("Fetch Medical Information"):
        medical_response = fetch_medical_info(employee_id)

        if medical_response.status_code == 200:
            medical_data = medical_response.json()
            display_medical_information(medical_data)
        elif medical_response.status_code == 404:
            display_error_message("Medical Information: Employee not found.")
        elif medical_response.status_code == 400:
            display_error_message("Medical Information: Invalid Employee ID format.")

    st.sidebar.markdown("Note: Make sure both Flask APIs are running. Leave API on http://localhost:5000 and Medical API on http://localhost:5001.")

if __name__ == "__main__":
    main()


# to run app streamlit run app.py
