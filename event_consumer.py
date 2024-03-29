import enum
from tokenize import group
from kafka import KafkaConsumer
import backend_cli
from os import getenv
from datetime import datetime
import json

KAFKA_ENDPOINT = getenv('KAFKA_ENDPOINT')


class Topics(enum.Enum):
    EVENTS = getenv('KAFKA_TOPIC')

print(KAFKA_ENDPOINT, getenv('KAFKA_TOPIC'))

maximum_try_count = 10

consumer = KafkaConsumer(
    Topics.EVENTS.value,
    bootstrap_servers=KAFKA_ENDPOINT,
    auto_offset_reset='earliest'
)

print("consumer ready...")

for message in consumer:
    try:
        data = message.value.decode("utf-8")
        data = json.loads(data)
    except Exception as e:
        print(f'error in read message: {message}, err: {e}')
        continue
    result = backend_cli.BackendCli.send_event(data)
