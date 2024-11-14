from returns.maybe import Nothing
from returns.result import Result, Failure, Success
from sqlalchemy.exc import SQLAlchemyError

from app.db.postgres_database import session_factory
from app.models.Location import Location
from app.repository.user_repository import get_user_by_user_id


def insert_location(location: Location) -> Result[Location, str]:
    # maybe_user = get_user_by_user_id(location.user_id)
    # if maybe_user is Nothing:
    #     return Failure(f"Missing user")
    with session_factory() as session:
        try:
            session.add(location)
            session.commit()
            session.refresh(location)
            return Success(location)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))