class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Abc", 20)
p2 = Person("Abc", 20)
s1 = "Abc"
s2 = "Abc"
print(s1 == s2)
print(s1)
print(p1 == p2)
print(p1)
