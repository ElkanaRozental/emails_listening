from app.db.mongo_database import emails_collection


def get_all_emails():
    return list(emails_collection.find())


def insert_email_to_mongo(email):
    if email not in get_all_emails():
        emails_collection.insert_one(email)
    else:
        return