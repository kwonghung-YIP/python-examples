from domain.common import Person

class C:
    def __init__(self):
        self.__readWritePpty:int = 0
        self.__readOnlyPpty:str = "ro"

    @property
    def readWritePpty(self):
        """read write property for class C"""
        print("@property")
        return self.__readWritePpty #without the getter method, this return is used instead
    
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

obj = C()
print(obj.readWritePpty)
obj.readWritePpty = 10
print(obj.readWritePpty)
obj.readWritePpty = "string value" #no type check here
print(obj.readWritePpty)

try:
    print(obj.readOnlyPpty)
    obj.readOnlyPpty = "hello world!"
except AttributeError as e:
    print(f"catch {e}")

try:
    print(obj.__readWritePpty)
except AttributeError as e:
    print(f"catch {e}")

try:
    del obj.readWritePpty
    print(obj.readWritePpty)
except AttributeError as e:
    print(f"catch {e}")

person = Person("John","Doe")
print(person._firstName)