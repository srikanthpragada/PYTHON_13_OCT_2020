# Take number and length on command line and print table
import sys

if len(sys.argv) < 2:
    print("Missing number!")
    exit()  # Stop program

num = int(sys.argv[1])

if len(sys.argv) == 2:
    length = 10    # default length
else: # Third parameter is given
    length = int(sys.argv[2])

for i in range(1, length + 1):
    print(f"{num:3} * {i:2} = {num * i:5}")






