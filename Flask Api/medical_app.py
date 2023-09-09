from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Generate sample employee data
employee_data = []
for employee_id in range(1, 11):
    total_medical_limit = random.randint(5000, 10000)
    remaining_medical_balance = total_medical_limit
    medical_bill_claimed = random.choice([True, False])

    employee = {
        'EmployeeID': employee_id,
        'TotalMedicalLimit': total_medical_limit,
        'RemainingMedicalBalance': remaining_medical_balance,
        'MedicalBillClaimed': medical_bill_claimed,
    }

    employee_data.append(employee)

# API endpoint to get medical information by Employee ID
@app.route('/get_medical_info', methods=['GET'])
def get_medical_info():
    try:
        employee_id = int(request.args.get('EmployeeID'))
        employee = next((e for e in employee_data if e['EmployeeID'] == employee_id), None)

        if not employee:
            return jsonify({'error': 'Employee not found'}), 404

        return jsonify(employee)
    except ValueError:
        return jsonify({'error': 'Invalid EmployeeID format'}), 400

if __name__ == '__main__':
    app.run(debug=True, 
    port=5001)
