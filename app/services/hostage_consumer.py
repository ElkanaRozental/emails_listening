import json
import os
from threading import Thread

from dotenv import load_dotenv
from kafka import KafkaConsumer

from app.repository.emails_repository import insert_email_to_mongo
from app.repository.postgres_repository import insert_hostage_data

load_dotenv(verbose=True)


def consume_hostages_email():
    consumer = KafkaConsumer(
        os.environ['TOPIC_HOSTAGE_MESSAGE_NAME'],
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='latest'
    )
    print(consumer)

    for message in consumer:
        print(f"Received: {message.key}: {message.value}")
        insert_hostage_data(message.value)


if __name__ == '__main__':
    consume_hostages_email()
