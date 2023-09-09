"""
Flask API for Employee Leave Information

This Flask application provides an API to retrieve leave information for employees based on their EmployeeID.

It uses a sample DataFrame containing EmployeeID, TotalLeaves, and LeavesAvailed data as a data source.

Endpoints:
    - /get_leave_info: Retrieve leave information for a specific employee by providing their EmployeeID as a query parameter.

Usage:
    1. Start the application by running this script.
    2. Make GET requests to the '/get_leave_info' endpoint with the 'EmployeeID' parameter to fetch leave information for specific employees.

Example:
    GET http://localhost:5000/get_leave_info?EmployeeID=1

    Response:
    {
        "EmployeeID": 1,
        "TotalLeaves": 20,
        "LeavesAvailed": 5
    }

Note:
    - You can replace the sample data in the 'data' dictionary with your own data source.
"""

from flask import Flask, request, jsonify
import pandas as pd
import numpy as np

# Create a Flask app
app = Flask(__name__)

# Sample employee leave data in a DataFrame (you can replace this with your data source)
data = {
    'EmployeeID': [1, 2, 3, 4, 5],
    'TotalLeaves': [20, 25, 18, 22, 30],
    'LeavesAvailed': [5, 10, 2, 12, 15]
}

df = pd.DataFrame(data)

# API endpoint to get leave information by Employee ID
@app.route('/get_leave_info', methods=['GET'])
def get_leave_info():
    try:
        employee_id = int(request.args.get('EmployeeID'))
        employee_data = df[df['EmployeeID'] == employee_id].to_dict('records')

        if not employee_data:
            return jsonify({'error': 'Employee not found'}), 404

        return jsonify(employee_data[0])
    except ValueError:
        return jsonify({'error': 'Invalid EmployeeID format'}), 400

if __name__ == '__main__':
    print('App in operation: Example to call \n http://localhost:5000/get_leave_info?EmployeeID=1')
    app.run(debug=True)
