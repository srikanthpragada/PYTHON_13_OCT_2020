def fun():
    print("In fun()")

def fun2():
    print("Second fun()")

def process(f):
    print("About to start!")
    f()
    print("End of task!")

process(fun2)
