from kafka import KafkaAdminClient
from kafka.admin import NewTopic

topics = [
    {"name": "messages.all"},
    {"name": "messages.hostage"},
    {"name": "messages.explosive"},
]


def init_topics():
    admin_client = KafkaAdminClient(bootstrap_servers='localhost:9092')
    topic_list = [
        NewTopic(
                name=topic["name"],
                num_partitions=3,
                replication_factor=3
            ) for topic in topics
    ]

    try:
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
        print("Topics created successfully!")
    except Exception as e:
        print(f"Error creating topics: {e}")
    finally:
        admin_client.close()