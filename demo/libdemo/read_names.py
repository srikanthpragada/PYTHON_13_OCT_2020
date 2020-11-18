# Read names form names.txt

try:
    with open("names.txt", "rt") as f:
        for name in f.readlines():
            print(name, end='')
except:
    print("Sorry! Could not open file!")
