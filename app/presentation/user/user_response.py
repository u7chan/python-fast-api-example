from typing import List

from pydantic import BaseModel


class UserModel(BaseModel):
    id: str
    name: str
    email: str
    updated_at: str


class UserResponse(BaseModel):
    data: List[UserModel]
