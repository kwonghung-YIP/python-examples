from pydantic import BaseModel

class User(BaseModel):
    title: str
    firstName: str
    lastName: str

def main():
    user = User(title="Mr",firstName="John",lastName="Doe")
    user.model_validate(user)

if __name__ == "__main__":
    main()