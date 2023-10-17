from typing import List

from pydantic import BaseModel


class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    updated_at: str


class UsersResponse(BaseModel):
    data: List[UserResponse]
