class SavingsAccount:
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


s1 = SavingsAccount(1001, 'Scott', 10000)  # create object, call __init__()
s1.deposit(20000)
s1.details()  # Call method
s2 = SavingsAccount(1002, 'Mike')  # object
print(s2.balance)
