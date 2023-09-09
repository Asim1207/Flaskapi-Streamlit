import streamlit as st


def display_leave_information(employee_data):
    
    st.subheader("Leave Information")
    st.write(f"Employee ID: {employee_data['EmployeeID']}")
    st.write(f"Total Leaves: {employee_data['TotalLeaves']}")
    st.write(f"Leaves Availed: {employee_data['LeavesAvailed']}")


def display_error_message(message):
    st.error(message)
