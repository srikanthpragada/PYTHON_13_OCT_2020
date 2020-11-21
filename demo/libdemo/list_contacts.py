import re

contacts = {}
with open("contacts.txt", 'rt') as f:
    for line in f:
        # Look for name, which is one or more alpha + space
        name = re.search("[A-Za-z ]+", line)
        if name is None:
            continue

        # Look for number
        number = re.search(r"\d+", line)
        if number is None or len(number.group()) != 10:
            continue

        contacts[name.group().strip()] = number.group()

for name, number in sorted(contacts.items()):
    print(f"{name:15} {number}")
