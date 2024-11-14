import json
import os

from dotenv import load_dotenv
from kafka import KafkaConsumer

from app.repository.emails_repository import insert_email_to_mongo

load_dotenv(verbose=True)


def consume_non_filter_email():
    consumer = KafkaConsumer(
        os.environ['TOPIC_ALL_MESSAGE_NAME'],
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='latest'
    )

    for message in consumer:
        print(f"Received: {message.key}: {message.value}")
        insert_email_to_mongo(message.value)


def consume_hostages_email():
    consumer = KafkaConsumer(
        os.environ['TOPIC_HOSTAGE_MESSAGE_NAME'],
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='latest'
    )

    for message in consumer:
        print(f"Received: {message.key}: {message.value}")
        insert_email_to_mongo(message.value)


def consume_explosive_email():
    consumer = KafkaConsumer(
        os.environ['TOPIC_EXPLOSIVE_MESSAGE_NAME'],
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='latest'
    )

    for message in consumer:
        print(f"Received: {message.key}: {message.value}")
        insert_email_to_mongo(message.value)


if __name__ == '__main__':
    consume_non_filter_email()
