from pymongo import MongoClient

from app.settings.mongo_config import DB_URL

client = MongoClient(DB_URL)

db = client['hamas_emails']
emails_collection = db['all_emails_data']

