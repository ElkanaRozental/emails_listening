from returns.maybe import Nothing
from returns.result import Result, Failure, Success
from sqlalchemy.exc import SQLAlchemyError

from app.db.postgres_database import session_factory
from app.models.SentenceHostage import SentenceHostage
from app.repository.user_repository import get_user_by_user_id


def insert_hostage_sentence(sentence: SentenceHostage) -> Result[SentenceHostage, str]:
    # maybe_user = get_user_by_user_id(sentence.user_id)
    # if maybe_user is Nothing:
    #     return Failure(f"Missing user")
    with session_factory() as session:
        try:
            session.add(sentence)
            session.commit()
            session.refresh(sentence)
            return Success(sentence)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))