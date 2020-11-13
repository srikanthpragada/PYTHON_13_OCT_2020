class A:
    def process(self):
        print("A process()")


class B:
    def process(self):
        print("B process()")


class C(A, B):
    def process(self):
        print("C process()")


obj = C()
obj.process()
