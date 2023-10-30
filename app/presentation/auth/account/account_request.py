from pydantic import BaseModel, Field


class AccountRequest(BaseModel):
    login_id: str = Field()
    password: str = Field()
    name: str = Field()
