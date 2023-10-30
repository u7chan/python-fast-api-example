from pydantic import BaseModel


class AccountResponse(BaseModel):
    user_id: str
