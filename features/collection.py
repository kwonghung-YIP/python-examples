if __name__ == "__main__":
    listInst = [1,2,3]
    tupleInst = (1,2,3)
    setInst = {1,2,3}
    dictInst = {"a":123}

    print("=== simple instances ===")
    print(f"expected type: list  {type(listInst)}") #list
    print(f"expected type: tuple {type(tupleInst)}") #tuple
    print(f"expected type: set   {type(setInst)}") #set
    print(f"expected type: dict  {type(dictInst)}") #dict 

    emptyList = []
    emptyTuple = ()
    emptySet = set()
    emptyDict = {}

    print("=== empty ===")
    print(f"expected type: list  {type(emptyList)}") #list
    print(f"expected type: tuple {type(emptyTuple)}") #tuple
    print(f"expected type: set   {type(emptySet)}") #set
    print(f"expected type: dict  {type(emptyDict)}") #dict 

    listBuiltin = list([1,2,3])
    tupleBuiltin = tuple([1,2,3])
    setBuiltin = set([1,2,3])
    dictBuiltin = dict(a=123)

    print("=== builtin ===")
    print(f"expected type: list  {type(listBuiltin)}") #list
    print(f"expected type: tuple {type(tupleBuiltin)}") #tuple
    print(f"expected type: set   {type(setBuiltin)}") #set
    print(f"expected type: dict  {type(dictBuiltin)}") #dict 

    # slice notation [start:stop:step]
    list2 = [1,2,3,4,5,6,7,8,9,10]
    print(list2[1:4]) #[2,3,4] exclude the end index
    print(list2[:3])  #[1,2,3]
    print(list2[8:])  #[9,10]
    print(list2[::2])  #[1,3,5,7,9]
    print(list2[1::2])  #[2,4,6,8,10]

    # sequence unpacking, number of parameters in both sides must be matched
    a,b = list2[2:6:3]
    print([a,b]) #[3,6]

    setA = {'A','B','C','E'}
    setB = {'B','C','F','Z'}

    print(f"\nSet A: {setA}\nSet B: {setB}\n")
    print(f"     intersection: {setA.intersection(setB)}")
    print(f"      operator(&): {setA & setB}") #{B,C}

    print(f"            union: {setA.union(setB)}")
    print(f"      operator(|): {setA | setB}") #{Z,E,A,B,F,C}

    print(f"difference(minus): {setA.difference(setB)}")
    print(f"      operator(-): {setA - setB}") #{E,A}

    print(f"   symmetric_diff: {setA.symmetric_difference(setB)}")
    print(f"      operator(^): {setA ^ setB}") #{Z,E,A,F} #(A-B)|(B-A)

    # looping
    dict2 = dict(a=1,b=2,c=3,d=4)
    for k,v in dict2.items():
        print(f"key:{k},value:{v}")

    for i,e in enumerate(list2):
        print(f"index:{i},element:{e}") #index started by 0

    list3 = ['a','b','c','d']
    list4 = [1,2,3,4]
    list5 = [1,2,3]
    list6 = [1,2,3,4,5]
    for a,b in zip(list3,list4):
        print(f"{a},{b}")

    for a,b in zip(list3,list5):
        print(f"{a},{b}")

    for a,b in zip(list3,list6,strict=True): #when strict=True, raise ValueError is both length are not equal
        print(f"{a},{b}")