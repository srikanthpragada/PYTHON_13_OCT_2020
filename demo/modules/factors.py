# Take a number on command line and display factors of the number
import sys

if len(sys.argv) < 2:
    print("Missing number!")
    exit()  # Stop program

num = int(sys.argv[1])

for i in range(2, num//2 + 1):
    if num % i == 0:
        print(i, end=' ')






