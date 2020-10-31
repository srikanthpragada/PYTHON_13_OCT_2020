def highest_factor(n):
    for i in range(n // 2, 1, -1):
        if n % i == 0:
            return i
    else:
        return 1


# Raise error for 1
def highest_factor_v2(n):
    i = n // 2
    while True:
        if n % i == 0:
            return i
        n -= 1


print(highest_factor(30))
print(highest_factor(255))
print(highest_factor(29))
print(highest_factor_v2(1))
