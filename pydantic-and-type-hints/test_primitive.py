from pydantic import BaseModel

class SimpleModel(BaseModel):
    intField: int

def test_convert():
    obj = SimpleModel(intField="1")
    assert isinstance(obj.intField,int)
    # convertion only apply for contructor, but not for property assignment
    obj.intField="1"
    assert isinstance(obj.intField,str)
    setattr(obj,"intField","1")
    assert isinstance(obj.intField,str)