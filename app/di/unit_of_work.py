from fastapi import Depends
from sqlalchemy.orm import Session

from app.infrastructure.database.session import get_session
from app.domain.unitofwork.unit_of_work import UnitOfWork
from app.infrastructure.database.unitofwork.unit_of_work_impl import UnitOfWorkImpl


def inject_unit_of_work(session: Session = Depends(get_session)) -> UnitOfWork:
    return UnitOfWorkImpl(session=session)
