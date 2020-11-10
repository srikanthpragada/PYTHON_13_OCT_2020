class SavingsAccount:
    # Class attribute
    minbal = 5000
    # Constructor
    def __init__(self, acno, ahname, balance=0):
        # Object attributes
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    # Method
    def details(self):
        print(self.acno)
        print(self.ahname)
        print(self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - SavingsAccount.minbal >= amount:
            self.balance -= amount
        else:
            print("Sorry! Insufficient balance!")


s1 = SavingsAccount(1001, 'Scott', 10000)  # create object, call __init__()
s1.deposit(20000)
s1.withdraw(40000)
s1.details()  # Call method
# s2 = SavingsAccount(1002, 'Mike')  # object
# print(s2.balance)
