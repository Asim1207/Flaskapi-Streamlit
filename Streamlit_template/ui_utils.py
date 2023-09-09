import streamlit as st


def display_leave_information(employee_data):
    
    st.subheader("Leave Information")
    st.write(f"Employee ID: {employee_data['EmployeeID']}")
    st.write(f"Total Leaves: {employee_data['TotalLeaves']}")
    st.write(f"Leaves Availed: {employee_data['LeavesAvailed']}")

def display_medical_information(medical_data):
    st.subheader("Medical Information")
    st.write(f"Employee ID: {medical_data['EmployeeID']}")
    st.write(f"Total Medical Limit: {medical_data['TotalMedicalLimit']}")
    st.write(
        f"Remaining Medical Balance: {medical_data['RemainingMedicalBalance']}")
    st.write(f"Medical Bill Claimed: {medical_data['MedicalBillClaimed']}")


def display_error_message(message):
    st.error(message)
