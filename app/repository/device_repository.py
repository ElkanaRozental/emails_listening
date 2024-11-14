from returns.maybe import Nothing
from returns.result import Result, Failure, Success
from sqlalchemy.exc import SQLAlchemyError

from app.db.postgres_database import session_factory
from app.models.Device import Device
from app.repository.user_repository import get_user_by_user_id


def insert_device(device: Device) -> Result[Device, str]:
    maybe_user = get_user_by_user_id(device.user_id)
    if maybe_user is Nothing:
        return Failure(f"Missing user")
    with session_factory() as session:
        try:
            session.add(device)
            session.commit()
            session.refresh(device)
            return Success(device)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))