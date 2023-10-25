from sqlalchemy.orm.session import Session

from app.domain.unitofwork.unit_of_work import UnitOfWork


class UnitOfWorkImpl(UnitOfWork):
    def __init__(self, session: Session):
        self.session = session

    def begin(self):
        self.session.begin()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
