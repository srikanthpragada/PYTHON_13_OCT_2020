def iseven(n):
    """
    Determines whether a number is even or odd
    :param n: number
    :return: True for even, False for odd
    """
    return n % 2 == 0


def largest(n1, n2):
    return n1 if n1 > n2 else n2


if __name__ == '__main__':   # if module is executed
    print("Executing math_funs")
else:  # if module is imported
    print("Importing math_funs")
