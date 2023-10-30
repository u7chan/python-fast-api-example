from pydantic import BaseModel, Field


class AccountRequest(BaseModel):
    name: str = Field()
    email: str = Field()
    password: str = Field()
