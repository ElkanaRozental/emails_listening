import json
import os

from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaProducer

from app.services.email_service import check_suspect_email, change_sentence_index, is_contain_hostage, \
    is_contain_explosive

load_dotenv(verbose=True)

app = Flask(__name__)


def produce_email(email):
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    message_to_send = change_sentence_index(email)
    producer.send(
        os.environ['TOPIC_ALL_MESSAGE_NAME'],
        value=message_to_send,
        key=message_to_send['email'].encode('utf-8')
    )
    producer.flush()

    if is_contain_hostage(message_to_send):
        producer.send(
            os.environ['TOPIC_HOSTAGE_MESSAGE_NAME'],
            value=message_to_send,
            key=message_to_send['email'].encode('utf-8')
        )
        print(message_to_send)

        producer.flush()

    if is_contain_explosive(message_to_send):

        producer.send(
            os.environ['TOPIC_EXPLOSIVE_MESSAGE_NAME'],
            value=message_to_send,
            key=message_to_send['email'].encode('utf-8')
        )
        print(message_to_send)

        producer.flush()


if __name__ == '__main__':
    app.run()