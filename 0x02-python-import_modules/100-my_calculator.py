#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit
n = len(argv)
sum = 0
if n == 4:
    x1 = int(argv[1])
    x2 = int(argv[3])
    if argv[2] == '+':
       sum = add(x1, x2)
    elif argv[2] == '-':
        sum = sub(x1, x2)
    elif argv[2] == '*':
        sum = mul(x1, x2)
    elif argv[2] == '/':
        sum = div(x1, x2)
else:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
print(sum)