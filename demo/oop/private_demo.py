class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute

    def print_details(self):
        print(self.name, self.__salary)


e = Employee('Andy', 50000)
#e._Employee__salary = 60000
print(e.__dict__)
# print(e.__salary)

