# Write a Python-script that determines whether the input string is the correct entry for the 'formula' according EBNF syntax 
# (without using regular expressions).

import argparse

parser = argparse.ArgumentParser(description='Formula string')
parser.add_argument('my_string', action='store', type=str, help='String to parse')

args = parser.parse_args()

def process( accum, op, number ):
    if op == '+':
        return accum + number
    elif op == '-':
        return accum - number
    elif op == '0':
        return number

def parse(expression):
    if not expression:
        return (False, None)
    accum = 0
    number = 0
    pending = '0'
    for char in expression:
        if char.isdigit():
            if number is None:
                number = 0
            number = number * 10 + int(char)
        elif char in "+-":
            if number is None:
                return False, None
            accum = process( accum, pending, number )
            pending = char
            number = None
        else:
            return False, None
    return True, process( accum, pending, number )

print(parse(args.my_string))