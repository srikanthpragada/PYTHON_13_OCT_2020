def add(n1, n2):
    return n1 + n2


def avg(a, b):
    total = add(a, b)
    return total / 2


def iseven(n):
    if n % 2 == 0:
        return True
    else:
        return False


v = add(10, 20)
print(add('abc', 'xyz'))
#print(add('abc', 10))
