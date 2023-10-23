from pydantic import BaseModel


class LoginResponse(BaseModel):
    session_id: str
