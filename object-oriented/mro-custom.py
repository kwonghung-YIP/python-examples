class C3:
    def f1(self):
        print ("C3")

class C2:
    def f1(self):
        print ("C2")

class C1(C2):
    def f1(self):
        print ("C1")

class C(C1,C3):
    def __init__(self):
        self.__mro__ = (C,C3,C1)

    def f1(self):
        print("C")


print(C.mro())

obj = C()
obj.f1()