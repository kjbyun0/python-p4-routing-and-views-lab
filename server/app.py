#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:str_content>')
def print_string(str_content):
    print(str_content)
    return str_content

@app.route('/count/<int:ubound>')
def count(ubound):
    return '\n'.join([str(c) for c in range(ubound)]) + '\n'

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(int(num1) + int(num2))
    elif operation == '-':
        return str(int(num1) - int(num2))
    elif operation == '*':
        return str(int(num1) * int(num2))
    elif operation == 'div':
        return str(int(num1) / int(num2))
    elif operation == '%':
        return str(int(num1) % int(num2))
    else:
        return None

if __name__ == '__main__':
    app.run(port=5555, debug=True)
