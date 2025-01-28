from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response

@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref') # get the parameter from url
  if pref:
    for student in data: # iterate dataset
      if student['pref'] == pref: # select only the students with a given meal preference
        result.append(student) # add match student to the result
    return jsonify(result) # return filtered set if parameter is supplied
  return jsonify(data) # return entire dataset if no parameter supplied

@app.route('/students/<id>')
def get_student(id):
  for student in data: 
    if student['id'] == id: # filter out the students without the specified id
      return jsonify(student)
  
@app.route('/stats')
def get_stats():
    stats = {
        "Chicken": 0,
        "Computer Science (Major)": 0,
        "Computer Science (Special)": 0,
        "Fish": 0,
        "Information Technology (Major)": 0,
        "Information Technology (Special)": 0,
        "Vegetable": 0
    }

    for student in data:
        # Count food preferences
        if student['pref'] == 'Chicken':
            stats["Chicken"] += 1
        elif student['pref'] == 'Fish':
            stats["Fish"] += 1
        elif student['pref'] == 'Vegetable':
            stats["Vegetable"] += 1

        # Count programmes
        if "Computer Science (Major)" in student['programme']:
            stats["Computer Science (Major)"] += 1
        elif "Computer Science (Special)" in student['programme']:
            stats["Computer Science (Special)"] += 1
        elif "Information Technology (Major)" in student['programme']:
            stats["Information Technology (Major)"] += 1
        elif "Information Technology (Special)" in student['programme']:
            stats["Information Technology (Special)"] += 1
    return jsonify(stats)

# Route to add two numbers
@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    result = a + b
    return jsonify({'Result': result})

# Route to subtract two numbers
@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    result = a - b
    return jsonify({'Result': result})

# Route to multiply two numbers
@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    result = a * b
    return jsonify({'Result': result})

# Route to divide two numbers
@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    if b == 0:
        return jsonify({'Error': 'Division by zero is not allowed'})
    result = a / b
    return jsonify({'Result': result})

app.run(host='0.0.0.0', port=8080, debug=True)
