from pydantic import BaseModel

from app.domain.entity.user import User


class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    updated_at: str

    @staticmethod
    def from_entity(user: User) -> "UserResponse":
        return UserResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            updated_at=user.updated_at or "NA",
        )
