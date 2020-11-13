class A:
    def processing(self):
        print("A process()")


class B(A):
    pass


class C:
    def process(self):
        print("C process()")


class D(B, C):
    pass


obj = D()
obj.process()
