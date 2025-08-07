from flask import Flask, render_template, request

app = Flask(__name__)

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return "Cannot divide by zero!" if b == 0 else a / b
def floor_division(a, b): return "Cannot divide by zero!" if b == 0 else a // b
def modulus(a, b): return "Cannot divide by zero!" if b == 0 else a % b

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ''
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)
        elif operation == 'floor_division':
            result = floor_division(num1, num2)
        elif operation == 'modulus':
            result = modulus(num1, num2)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
