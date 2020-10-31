def unique_digits(*nums):
    digits = set()
    for n in nums:
        digits |= set(str(n))

    return "".join(sorted(digits))


def unique_digits_v2(*nums):
    digits = set()
    for n in nums:
        while n > 0:
            d = n % 10
            digits.add(str(d))
            n //= 10

    return "".join(sorted(digits))


print(unique_digits(10, 11, 56, 78, 96, 34))
print(unique_digits_v2(10, 11, 56, 78, 96, 34))
