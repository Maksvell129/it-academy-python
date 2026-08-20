class A:
    def hello(self):
        print("A")


class B(A):
    pass
    # def hello(self):
    #     print("B")


class C(A):
    def hello(self):
        print("C")


class D(B, C):
    pass


d = D()

d.hello()

print(D.__mro__)