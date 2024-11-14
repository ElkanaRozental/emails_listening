from returns.maybe import Maybe
from returns.result import Result, Failure, Success
from sqlalchemy.exc import SQLAlchemyError

from app.db.postgres_database import session_factory
from app.models.Device import Device
from app.models.User import User


def get_user_by_user_id(user_id: int):
    with session_factory() as session:
        return Maybe.from_optional(
            session.get(User, user_id)
        )


def insert_user(user: User) -> Result[User, str]:
    with session_factory() as session:
        try:
            session.add(user)
            session.commit()
            session.refresh(user)
            return Success(user)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))


