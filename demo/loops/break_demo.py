total = 0
for i in range(1, 6):
    num = int(input("Enter number [0 to stop]:"))
    if num == 0:
        break  # Terminate loop
    total += num

print(total)
