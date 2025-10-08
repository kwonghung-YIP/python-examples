from pydantic import BaseModel
from datetime import datetime

class SimpleModel(BaseModel):
    intField: int
    floatField: float
    complexField: complex
    strField: str
    bytesField: bytes
    #bytearrayField: bytearray
    boolField: bool
    datetimeField: datetime

def main():
    obj = SimpleModel(
        intField = 9_999_999,
        floatField = 9_999.9999,
        complexField = 2 + 3j,
        strField = 'abcd1234',
        bytesField = b'Hello world!',
        boolField = True,
        datetimeField = datetime.now()
    )
    obj.intField = 0b1111 #binary value
    obj.intField = int("0b1111",base=2)
    #obj.intField = "15"
    #obj.intField = "0b1111"
    #print(obj.intField + 1)
    #obj.intField = b"\b1111"
    #print(obj.intField + 1)
    obj.intField = 0o7777 #octal value
    obj.intField = int("0o7777",base=8)
    obj.intField = 0xFFFF #hex value
    obj.intField = int("0xFFFF",base=16)
    obj.intField = int.from_bytes(b"\xff")
    print(obj.intField + 1)
    print(f"{(13).bit_count()}, {(13).bit_length()}")
    print((255).to_bytes())

    obj.bytesField = bytes("Hello world!",encoding="utf-8")
    
    SimpleModel.model_validate(obj)

if __name__ == "__main__":
    main()