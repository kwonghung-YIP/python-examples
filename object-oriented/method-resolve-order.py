# method resolve order (MRO) example

class C8:
    def f1(self):
        print("C8")

class C7(C8):
    def f1(self):
        print("C7")

class C6:
    def f1(self):
        print("C6")

class C5(C6):
    def f1(self):
        print("C5")

class C4:
    def f1(self):
        print("C4")

class C3(C4):
    def f1(self):
        print("C3")

class C2:
    def f1(self):
        print("C2")

class C1(C2,C3):
    def f1(self):
        print("C1")

#    C4
#    |
# C2 C3 C6 C8
# |  /  |  |
# C1    C5 C7
# |     /  /
# C 

class C(C1,C5,C7):
    def f1(self):
        # the super() lookup the next available class in self.mro(), right after C4
        # therefore expected searching order below is C5,C6,C7,C8 
        super(C4,self).f1()

# expected order: depth first, then left to right
# C,C1,C2,C3,C4,C5,C6,C7,C8,object

print(C.mro())

obj = C()

# expected C5
obj.f1()

print(isinstance(obj,C5))
print(issubclass(C,C8))
