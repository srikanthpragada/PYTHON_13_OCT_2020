
total = 0
count = 0

while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    if num < 0:
        continue

    total += num
    count += 1

print("Average =", total / count)

