import json
import os

from dotenv import load_dotenv
from kafka import KafkaConsumer

from app.repository.postgres_repository import insert_all_data

load_dotenv(verbose=True)


def consume_explosive_email():
    consumer = KafkaConsumer(
        os.environ['TOPIC_EXPLOSIVE_MESSAGE_NAME'],
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='latest'
    )
    print(consumer)

    for message in consumer:
        print(f"Received: {message.key}: {message.value}")
        insert_all_data(message.value)


if __name__ == '__main__':
    consume_explosive_email()
