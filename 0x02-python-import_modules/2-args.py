#!/usr/bin/python3
# This script prints the number of command-line arg

if __name__ != "__main__":
    exit()

# Define a string that will be used to format the output.
argStr = "{:d} argument"

# Get the number of command-line arguments passed.
argc = len(sys.argv) - 1

# Modify the format string based on the number of 
if argc == 0:
    argStr += 's.'
elif argc == 1:
    argStr += ':'
else:
    argStr += 's:'

# Print the number of arguments.
print(argStr.format(argc))

# Iterate over the command-line arguments and print 
i = 0
for arg in sys.argv:
    if i != 0:
        print("{:d}: {:s}".format(i, arg))
    i += 1
