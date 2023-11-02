#!/usr/bin/python3
# Import arithmetic functions from calculator_1.
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    # Declare variables a and b.
    a = 10
    b = 5

    # Perform basic arithmetic operations and print results.
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")

