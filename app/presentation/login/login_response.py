from pydantic import BaseModel


class LoginResponse(BaseModel):
    expires: str
