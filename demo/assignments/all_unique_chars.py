
uchars = set()
while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break
    # for c in name:
    #     uchars.add(c)
    uchars.update(set(name))

print(uchars)


