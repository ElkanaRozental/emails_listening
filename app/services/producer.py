import json
import os

from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaProducer

from app.services.email_service import check_suspect_email

load_dotenv(verbose=True)

app = Flask(__name__)


def produce_email(email):
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    if check_suspect_email(email) == 'clear':
        producer.send(
            os.environ['TOPIC_ALL_MESSAGE_NAME'],
            value=email,
            key=email['email'].encode('utf-8')
        )
        producer.flush()

    if check_suspect_email(email) == 'hostage':
        producer.send(
            os.environ['TOPIC_HOSTAGE_MESSAGE_NAME'],
            value=email,
            key=email['email'].encode('utf-8')
        )
        producer.flush()

    if check_suspect_email(email) == 'hostage':
        producer.send(
            os.environ['TOPIC_EXPLOSIVE_MESSAGE_NAME'],
            value=email,
            key=email['email'].encode('utf-8')
        )
        producer.flush()


if __name__ == '__main__':
    app.run()