class A:
    def fly(self):
        print("Летит A")

    def swim(self):
        print("Плывёт A ")

class B:
    def swim(self):
        print("Плывёт B")

    def fly(self):
        print("Летит B")


class C(A, B):

    def fly(self):
        print("CCCCCC")
        super().fly()


c = C()

c.fly()
# c.swim()
#
# print(C.mro())
#
# print(int.mro())
# print(str.mro())
# print(tuple.mro())
# print(dict.mro())