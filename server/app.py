#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    return f'<p>{parameter}</p>'

@app.route('/count/<int:numgiven>')
def count(numgiven:int):
    the_string = ""
    for n in range(numgiven):
        the_string += f"{n}<br/>"
    return the_string

@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, operation, num2):
    total = ''
    if operation == '+':
        total = f'{num1} + {num2}'
    elif operation == '-':
        total = f'{num1} - {num2}'
    elif operation == '*':
        total = f'{num1} * {num2}'
    elif operation == 'div':
        total = f'{num1} / {num2}'
    elif operation == '%':
        total = f'{num1} % {num2}'
    return total
    




# @app.route