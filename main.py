import json

from flask import Flask

app = Flask(__name__)

employees = [{"id": 1, "firstName": "John", "lastName": "Doe", "department": 1, "designation": 1},
             {"id": 2, "firstName": "Maven", "lastName": "Luke", "department": 2, "designation": 1},
             {"id": 3, "firstName": "Anna", "lastName": "Marie", "department": 1, "designation": 2}]
departments = [{"id": 1, "deptName": "account"},
               {"id": 2, "deptName": "inventory"}]
designations = [{"id": 1, "position": "Developer"},
                {"id": 2, "position": "Designer"}]

emps = [{"empID": "A", "skill": "X", "department": "D1"},
        {"empID": "B", "department": "D2"},
        {"empID": "C", "department": "D2"}]

depts = [{"deptName": "D1", "skill": "Z", "course": "java"},
         {"deptName": "D2", "skill": "Y", "course": "python"}]


@app.route('/', methods=['GET'])
def index():
    return "Dummy Service is running"


@app.route('/getEmployee/<emp_id>', methods=['GET'])
def get_employee(emp_id):
    return json.dumps([emp for emp in employees if emp['id'] == int(emp_id)][0])


@app.route('/getDepartment/<dept_id>', methods=['GET'])
def get_department(dept_id):
    return json.dumps([dept for dept in departments if dept['id'] == int(dept_id)][0])


@app.route('/getDesignation/<pos_id>', methods=['GET'])
def get_designation(pos_id):
    return json.dumps([position for position in designations if position['id'] == int(pos_id)][0])


@app.route('/getSkilledEmployees', methods=['GET'])
def get_skilled_employee():
    return json.dumps(emps)


@app.route('/getAllDepartments', methods=['GET'])
def get_all_dept():
    return json.dumps(depts)


@app.route('/getDepartmentDetail/<dept_name>', methods=['GET'])
def get_dept_details(dept_name):
    return json.dumps([dept for dept in depts if dept['deptName'] == dept_name][0])


if __name__ == "__main__":
    app.debug = True
    app.run()
