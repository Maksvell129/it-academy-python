class A:
    def hello(self):
        print("A")


class B(A):
    def hello(self):
        print("B")
        super().hello()


class C(B):
    def hello(self):
        print("C")
        super().hello()


obj = C()
obj.hello()
