#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    res = 0
    if operator == "+":
        res = add(a, b)
    elif operator == "-":
        res = sub(a, b)
    elif operator == "*":
        res = mul(a, b)
    elif operator == "/":
        res = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print(f"{a} {operator} {b} = {res}")
