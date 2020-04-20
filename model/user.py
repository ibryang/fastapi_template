from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    age: int = None
    nickname: str = None
    is_active: bool = True


class UserUpdate(User, UserCreate):
    pass
