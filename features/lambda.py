def deco(prefix,suffix):
    return lambda s: f"{prefix}{s}{suffix}"

decoWithBrace = deco('{','}')
decoWithTilde = deco('~','~')
decoWithDollar = deco('$','$')


if __name__ == "__main__":
    print(type(deco)) # function
    print(type(decoWithBrace)) # function
    print(decoWithBrace("John"))
    print(decoWithTilde("John"))
    print(decoWithDollar("John"))
    for n in filter(lambda n: n%2==0,range(1,11)):
        print(n)