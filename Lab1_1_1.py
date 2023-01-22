# Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'. 
# The type of operator and data are set on the command line when the script is run.
# The script should be launched like this: $ python my_task.py 1 * 2
# Notes: Use the argparse module to parse command line arguments, shouldn't require entering any parameters (like -f or --function).

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('x', type=float)
parser.add_argument('operator')
parser.add_argument('y', type=float)
args = parser.parse_args()

if args.operator == '+':
    print(args.x + args.y)
elif args.operator == '-':
    print(args.x - args.y)
elif args.operator == '*':
    print(args.x * args.y)
elif args.operator == '/':
    if args.y == 0:
        print('Error: division by zero!')
    else:
        print(args.x / args.y)
else:
    print("Error! Run with parameters: a number, operator (+, -, *, /) and another number.")
