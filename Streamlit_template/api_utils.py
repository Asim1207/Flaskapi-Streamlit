import requests


def fetch_leave_info(employee_id):
    response = requests.get(
        f"http://localhost:5000/get_leave_info?EmployeeID={employee_id}")

    if response.status_code == 200:
        employee_data = response.json()
        return employee_data, 200
    else:
        return None, response.status_code

# def llm_chat():
#     return None
