class A:
    def process(self):
        print("A process()")


class B:
    def task(self):
        print("B task()")


class C(A, B):
    pass


obj = C()
obj.process()
obj.task()
