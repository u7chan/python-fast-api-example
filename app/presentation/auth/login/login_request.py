from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    login: str = Field()
    password: str = Field()
