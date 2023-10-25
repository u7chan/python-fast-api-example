from app.domain.entity.login import Login
from app.domain.entity.session import Session
from app.domain.repository.session_repository import SessionRepository
from app.domain.usecase.auth.login_usecase import LoginUseCase


class LoginUseCaseImpl(LoginUseCase):
    def __init__(self, session_repository: SessionRepository):
        self.session_repository = session_repository

    def execute(self, login: Login) -> Session:
        session = self.session_repository.create(user_id=login.id)
        return session
