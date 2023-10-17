from pydantic import BaseModel, Field


class UserRequest(BaseModel):
    name: str = Field()
    email: str = Field()
