from pydantic import BaseModel, Field

from app.domain.exception.duplication_exception import DuplicationException


class ErrorMessageAccountAlreadyExists(BaseModel):
    detail: str = Field(example=DuplicationException.message)


class AccountResponse(BaseModel):
    user_id: str
