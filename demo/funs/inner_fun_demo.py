def outer():
    def inner():
        print('Inner function!')

    def inner2():
        print('Inner function!')

    print('Outer function')
    inner()


outer()
