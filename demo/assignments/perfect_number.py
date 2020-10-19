
num = int(input("Enter a number :"))

total = 0
for i in range(1, num//2 + 1):
    if num % i == 0:
        total += i

if num == total:
    print("Perfect Number!")
else:
    print("Not a perfect number!")

