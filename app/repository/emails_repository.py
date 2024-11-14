from sqlalchemy import Result

from app.db.mongo_database import emails_collection
from app.db.postgres_database import session_factory
from app.models.User import User


def get_all_emails():
    try:
        return list(emails_collection.find())
    except Exception as e:
        print(str(e))


def insert_email_to_mongo(email):
    if email not in get_all_emails():
        emails_collection.insert_one(email)
    else:
        return



