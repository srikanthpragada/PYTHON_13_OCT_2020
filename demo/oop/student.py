class Student:
    # Class attributes or static attribute/variable
    gst = 15
    courses = {'python': 8000, 'java': 10000, 'ds': 15000, 'angular': 3000}

    @staticmethod
    def change_gst(newgst):
        Student.gst = newgst

    def __init__(self, name, course, feepaid):
        # Object attributes
        if course not in Student.courses:
            raise ValueError('Invalid course -> ' + course)

        self.name = name
        self.course = course
        self.feepaid = feepaid

    def totalfee(self):
        fee = Student.courses[self.course]
        return fee + fee * Student.gst / 100

    def payment(self, amount):
        if amount <= self.due():
            self.feepaid += amount
        else:
            print('Sorry! Amount is more than due amount!')

    def due(self):
        return self.totalfee() - self.feepaid


Student.change_gst(12)
s = Student("Jack", "java", 3000)
s.payment(3000)
print(s.due())
