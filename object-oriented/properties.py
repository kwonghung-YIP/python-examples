class C:
    __counter = 0

    @staticmethod
    def toUpperCase(value:str) -> str:
        return value.upper()

    @classmethod
    def increment(cls):
        cls.__counter += 1

    @classmethod
    def getCounter(cls):
        return cls.__counter

    def __init__(self):
        self.__readWritePpty:int = 0
        self.__readOnlyPpty:str = "ro"
        self.__x = 9.999

    @property
    def readWritePpty(self):
        """read write property for class C"""
        print("@property")
        # return statement is required only if no @getter is defined
        # return self.__readWritePpty #without the getter method, this return is used instead
    
    @readWritePpty.getter
    def readWritePpty(self) -> int:
        print("@getter")
        return self.__readWritePpty #use @getter method instead of @property if it is defined

    @readWritePpty.setter
    def readWritePpty(self,value:int):
        print("@setter")
        self.__readWritePpty = value

    @readWritePpty.deleter
    def readWritePpty(self):
        print("@deleter")
        del self.__readWritePpty

    @property
    def readOnlyPpty(self) -> str:
        return self.__readOnlyPpty
    
    def x_fget(self):
        return self.__x

    def x_fset(self,value):
        self.__x = value

    def x_fdel(self):
        del self.__x

    # define x property with function instead of annotation
    x = property(x_fget,x_fset,x_fdel,"property x")

obj = C()
print(obj.readWritePpty)
obj.readWritePpty = 10
print(obj.readWritePpty)
obj.readWritePpty = "string value" #no type check here
print(obj.readWritePpty)

# get, set, del attribute with property name
print(getattr(obj,"x"))
setattr(obj,"x",88.8888888)
print(getattr(obj,"x"))
delattr(obj,"x")
print(hasattr(obj,"x"))

print(dir(obj))


print(C.toUpperCase("abc"))
C.increment()
print(C.getCounter())

try:
    print(obj.readOnlyPpty)
    # cannot assign value to a read-only property
    obj.readOnlyPpty = "hello world!"
except AttributeError as e:
    print(f"catch {e}")

try:
    # cannot read the private attribute directly
    print(obj.__readWritePpty)
except AttributeError as e:
    print(f"catch {e}")

try:
    # cannot del an attribute without defined a @deleter
    del obj.readWritePpty
    # cannot read the attribute after delete it
    print(obj.readWritePpty)
except AttributeError as e:
    print(f"catch {e}")
