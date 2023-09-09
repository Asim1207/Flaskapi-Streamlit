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
    app.run(debug=True)
