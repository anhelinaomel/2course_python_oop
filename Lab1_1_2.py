# Write a Python-script that performs the standard math functions on the data.
# The name of function and data are set on the command line when the script is run.
# The script should be launched like this: $ python my_task.py add 1 2
# Notes: Function names must match the standard math functions from the built-in libraries. 
# operator.mul(a, b), operator.add(a, b), truediv, sub(a, b)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('operator', nargs=1)
parser.add_argument('x', nargs=1, type=float)
parser.add_argument('y', nargs=1, type=float)
args = parser.parse_args()

def add(x, y):      # addition
    return (x + y)

def sub(x, y):      # subtraction
    return (x - y)

def mul(x, y):
    return (x * y)  # multiplication

def truediv(x, y):  # division
    if y == 0:
        print('Error: division by zero!')
    else:
        return (x / y)

if args.operator[0] == "add":
    print(add(args.x[0], args.y[0]))
elif args.operator[0] == "sub":
    print(sub(args.x[0], args.y[0]))
elif args.operator[0] == "mul":
    print(mul(args.x[0], args.y[0]))
elif args.operator[0] == "truediv":
    print(truediv(args.x[0], args.y[0]))
else:
    print("Error! Run with parameters: add/sub/mul/truediv and two numbers.")