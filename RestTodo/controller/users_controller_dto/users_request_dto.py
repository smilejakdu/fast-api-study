from pydantic import BaseModel
from typing import Optional


class CreateUser(BaseModel):
    username: str
    email: Optional[str]
    img_url: str
    first_name: str
    last_name: str
    password: str


class UpdateUser(BaseModel):
    username: str
    email: Optional[str]
    img_url: str
    first_name: str
    last_name: str
    password: str


class FindUserById(BaseModel):
    id: int


class FindUserByEmail(BaseModel):
    email: str
