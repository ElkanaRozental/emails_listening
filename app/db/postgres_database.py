from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.settings.postgers_config import DB_POSTGRES_URL

engine = create_engine(DB_POSTGRES_URL)
# use session_factory() to get a new Session
_session_factory = sessionmaker(bind=engine)

Base = declarative_base()

from app.models import User, SentenceHostage, SentenceExplosive, Device, Location


def session_factory():
    return _session_factory()


def init_db():
    Base.metadata.create_all(engine)
