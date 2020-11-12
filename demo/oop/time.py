class Time:
    def __init__(self, h=0, m=0, s=0):
        self.__h = h
        self.__m = m
        self.__s = s

    @property
    def hours(self):
        return self.__h

    @hours.setter
    def hours(self, value):
        if value >= 0 and value <= 23:
            self.__h = value
        else:
            raise ValueError('Invalid Hours')


t = Time(10, 20, 30)
t.hours = 20  # Setter method of property
print(t.hours)  # Getter method

print(isinstance(t, Time))
print(isinstance("Abc", str))
print(isinstance("Abc", object))
print(isinstance([1, 2, 3], object))
