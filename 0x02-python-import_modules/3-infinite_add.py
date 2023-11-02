#!/usr/bin/python3
# Calculates the sum of the command-line arguments.
import sys

if __name__ != "__main__":
    exit()

argc = len(sys.argv) - 1
# Skip the script name.

result = 0
for i, arg in enumerate(sys.argv):
    if i != 0:
        result += int(arg)
# Add each argument to the result.

print(result)
