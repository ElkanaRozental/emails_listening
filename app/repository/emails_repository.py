from sqlalchemy import Result

from app.db.mongo_database import emails_collection
from app.db.postgres_database import session_factory
from app.models.Device import Device
from app.models.Location import Location
from app.models.SentenceHostage import SentenceHostage
from app.models.SentenceExplosive import SentenceExplosive

from app.models.User import User


def get_all_emails():
    try:
        return list(emails_collection.find())
    except Exception as e:
        print(str(e))


def insert_email_to_mongo(email):
    try:
        if email in get_all_emails():
            return
        else:
            emails_collection.insert_one(email)
    except Exception as e:
        print(str(e))


from sqlalchemy.orm import joinedload

def get_all_details_by_email(email):
    with session_factory() as session:
        data = session.query(User).options(
            joinedload(User.device),
            joinedload(User.location),
            joinedload(User.hostage_sentences),
            joinedload(User.explosive_sentences)
        ).filter(User.email == email).first()
        return data

