if __name__ == "__main__":
    # with expression and condition
    print([f"{n:2}" for n in range(1,101) if n%2==0])

    # loop char in string
    print([c for c in "abcde"])

    # 3D looping
    print([sum([x,y,z]) for x in range(10) for y in range(10) for z in range(10) if x < y and y < z])

    m = [[x,y] for x in 'AB' for y in '123']
    print(m)
    # nested
    print(sorted({ element for set in m for element in set }))