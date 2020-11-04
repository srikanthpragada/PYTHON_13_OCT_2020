def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10

    return total


nums = {192, 3939, 882, 33, 34}

for n in map(sum_of_digits, nums):
    print(n)
