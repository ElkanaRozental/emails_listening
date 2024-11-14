from app.models.Device import Device
from app.models.Location import Location
from app.models.User import User
from app.models.SentenceExplosive import SentenceExplosive
from app.models.SentenceHostage import SentenceHostage
from app.repository.device_repository import insert_device
from app.repository.explosive_sentence_repository import insert_explosive_sentence
from app.repository.hostage_sentence_repository import insert_hostage_sentence
from app.repository.location_repository import insert_location
from app.db.postgres_database import session_factory
from app.repository.user_repository import insert_user
from app.services.email_service import is_contain_hostage, is_contain_explosive


def insert_hostage_data(message: dict):
    try:
        print(message, "insert value")
        device = message['device_info']
        location = message['location']
        with session_factory() as session:
            user_to_insert = User(
                name=message['username'],
                email=message['email'],
                ip_address=message['ip_address'],
                location=Location(
                    latitude=location['latitude'],
                    longitude=location['longitude'],
                    city=location['city'],
                    country=location['country'],
                ),
                device=Device(
                    browser=device['browser'],
                    os=device['os'],
                    device_id=device['device_id'],
                ),
                hostage_sentences=[
                    SentenceHostage(
                        sentence=sentence,
                        created_at=message['created_at'],
                    )
                    for sentence in message['sentences']
                    if is_contain_hostage(message)
                ]
            )
            session.add(user_to_insert)
            session.commit()

    except Exception as e:
        print(str(e))


def insert_explosive_data(message: dict):
    try:
        print(message, "insert value")
        device = message['device_info']
        location = message['location']
        with session_factory() as session:
            user_to_insert = User(
                name=message['username'],
                email=message['email'],
                ip_address=message['ip_address'],
                location=Location(
                    latitude=location['latitude'],
                    longitude=location['longitude'],
                    city=location['city'],
                    country=location['country'],
                ),
                device=Device(
                    browser=device['browser'],
                    os=device['os'],
                    device_id=device['device_id'],
                ),
                explosive_sentences=[
                    SentenceExplosive(
                        sentence=sentence,
                        created_at=message['created_at'],
                    )
                    for sentence in message['sentences']
                    if is_contain_explosive(message)
                ]
            )
            session.add(user_to_insert)
            session.commit()

    except Exception as e:
        print(str(e))

