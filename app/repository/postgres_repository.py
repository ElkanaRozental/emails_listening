from app.models.Device import Device
from app.models.Location import Location
from app.models.User import User
from app.models.SentenceExplosive import SentenceExplosive
from app.models.SentenceHostage import SentenceHostage
from app.repository.device_repository import insert_device
from app.repository.explosive_sentence_repository import insert_explosive_sentence
from app.repository.hostage_sentence_repository import insert_hostage_sentence
from app.repository.location_repository import insert_location

from app.repository.user_repository import insert_user
from app.services.email_service import is_contain_hostage, is_contain_explosive


def insert_all_data(message: dict):
    try:
        print(message,"insert value")
        device = message['device_info']
        location = message['location']

        user_to_insert = User(
            name=message['username'],
            email=message['email'],
            ip_address=message['ip_address']
        )
        user_id = insert_user(user_to_insert)

        location_to_insert = Location(
            latitude=location['latitude'],
            longitude=location['longitude'],
            city=location['city'],
            country=location['country'],
            user_id=user_id
        )
        insert_location(location_to_insert)

        device_to_insert = Device(
            browser=device['browser'],
            os=device['os'],
            device_id=device['device_id'],
            user_id=user_id
        )
        insert_device(device_to_insert)

        for sentence in message['sentences']:
            hostage_sentence_to_insert = SentenceHostage(
                sentence=sentence,
                created_at=message['created_at'],
                user_id=user_id
            )
            if is_contain_hostage(message):
                insert_hostage_sentence(hostage_sentence_to_insert)

            explosive_sentence_to_insert = SentenceExplosive(
                sentence=sentence,
                created_at=message['created_at'],
                user_id=user_id
            )
            if is_contain_explosive(message):
                insert_explosive_sentence(explosive_sentence_to_insert)
    except Exception as e:
        print(str(e))


