from app.domain.entity.login import Login
from app.domain.repository.session_repository import SessionRepository
from app.domain.usecase.login_usecase import LoginUseCase


class LoginUseCaseImpl(LoginUseCase):
    def __init__(self, session_repository: SessionRepository):
        self.session_repository = session_repository

    def execute(self, login: Login) -> str:
        session_id = self.session_repository.create(user_id=login.id)
        return session_id
