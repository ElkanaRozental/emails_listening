from app.models.Device import Device
from app.models.Location import Location
from app.models.User import User


def insert_all_data(message: dict):
    device = message['device_info']
    location = message['location']

    user_to_insert = User(
        user_id=message['id'],
        name=message['username'],
        ip_address=message['ip_address'],
        location=Location(
            latitude=location['latitude'],
            longitude=location['longitude'],
            city=location['city'],
            country=location['country']
        ),
        device=Device(
            browser=device['browser'],
            os=device['os'],
            device_id=device['device_id']
        ))

