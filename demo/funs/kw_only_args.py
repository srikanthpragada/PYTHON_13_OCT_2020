# Keyword-only arguments
def fun(*, age, name):
    pass


fun(name='Abc', age=20)
fun(age=30, name='Abc')
# fun('Abc', 25)
