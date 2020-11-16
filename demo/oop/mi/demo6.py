class A:
    def process(self):
        print("A process()")


class B(A):
    def process(self):
        print("B process()")


class C(A, B):
    pass


print(C.mro())
obj = C()
obj.process()
