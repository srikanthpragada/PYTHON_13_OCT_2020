class A:
    def process(self):
        print("A process()")


class B:
    def process(self):
        print("B process()")


class C(A, B):
    pass


obj = C()
obj.process()
