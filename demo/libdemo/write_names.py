names = set()  # Empty set
while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break

    names.add(name)

# Write names in sorted order into file
f = open("names.txt", "wt")

for name in sorted(names):
    f.write(name + "\n")

f.close()
