# Positional-only arguments  - 3.8
def fun(name, age, /):
    pass


fun('Abc', 20)
fun(name= 'Abc', age = 20)
