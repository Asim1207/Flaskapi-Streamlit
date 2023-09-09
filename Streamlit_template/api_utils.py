import requests


def fetch_leave_info(employee_id):
    leave_response = requests.get(
        f"http://localhost:5000/get_leave_info?EmployeeID={employee_id}")
    return leave_response


def fetch_medical_info(employee_id):
    medical_response = requests.get(
        f"http://localhost:5001/get_medical_info?EmployeeID={employee_id}")
        
    return medical_response
