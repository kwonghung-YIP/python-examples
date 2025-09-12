class Iteratable:
    def __init__(self,start,max):
        self.__counter = start
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        current = self.__counter
        if current > self.max:
            raise StopIteration
        self.__counter += 1
        return current
    
    def hasNext(self):
        return self.__counter <= self.max
    
if __name__ == "__main__":
    list = [1,2,3,4,5]
    # iterable : any object can return iterator
    print(type(list)) # list
    # iterator : object to perform operation
    print(type(iter(list))) # list_iterator

    for x in Iteratable(1,5):
        print(x)

    it = Iteratable(1,3)
    print(next(it))
    print(next(it))
    print(next(it))
    try:
        print(next(it)) #StopIteration
    except StopIteration as e:
        print("StopIteration")

    it2 = Iteratable(1,5)
    while(it2.hasNext()):
        print(next(it2))

    print([ x**2 for x in Iteratable(1,5) ])
    print(sum(Iteratable(1,5)))