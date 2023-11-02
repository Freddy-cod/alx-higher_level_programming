#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

# Check if the script is being run as the main program
if __name__ != "__main__":
    exit()

# Calculate the number of command-line arguments
argc = len(argv) - 1

# Check if the correct number of arguments is provided
if argc != 3:
    print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
    exit(1)
elif argv[2] == '+':
    func = add
elif argv[2] == '-':
    func = sub
elif argv[2] == '*':
    func = mul
elif argv[2] == '/':
    func = div
else:
    print("Unknown operator. Available operators: +, -, *, and /")
    exit(1)

# Perform the calculation using the selected operator function
result = func(int(argv[1]), int(argv[3]))

# Display the calculation result
print("{:d} {:s} {:d} = {:d}".format(int(argv[1]), argv[2],
                                     int(argv[3]), result))

