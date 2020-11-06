a = 10  # Global variable


def f1():
    global a
    a = a + 10
    b = 20  # Enclosing variable

    def f2():
        nonlocal b
        b = b + 1
        c = 30  # Local variable
        print(a, b, c)

    f2()


f1()
