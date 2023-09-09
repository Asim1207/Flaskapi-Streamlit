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