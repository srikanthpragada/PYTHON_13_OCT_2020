class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


p1 = Person("Abc", 22)
p2 = Person("Abc", 20)
print(p1 == p2)  # p1.__eq__(p2)
print(p1)  # p1.__str__()
# print(p1 > p2)  # p1.__gt__(p2)

persons = [Person('Abc', 20), Person('Xyz', 15), Person('Pqr', 10)]
for p in sorted(persons):
    print(p)
