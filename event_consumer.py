import enum
from kafka import KafkaConsumer
import backend_cli
from os import getenv

# KAFKA_ENDPOINT = getenv('KAFKA_ENDPOINT')
KAFKA_ENDPOINT = '185.204.197.207:9092'


class Topics(enum.Enum):
    EVENTS = "events"


maximum_try_count = 10

consumer = KafkaConsumer(
    Topics.EVENTS.value,
    bootstrap_servers=KAFKA_ENDPOINT,
    # enable_auto_commit=False,
    # group_id='gateway-test',
    auto_offset_reset='earliest'
)

print("consumer ready...")

for message in consumer:
    try:
        data = message.value.decode("utf-8")
        print(data)
    except Exception as e:
        print(f'error in read message: {message}, err: {e}')
        continue
    result = backend_cli.BackendCli.send_event(data)
    # if result:
    #     consumer.commit()
    # else:
    #     try_count = 0
    #     while not backend_cli.BackendCli.send_event(data) and try_count < maximum_try_count:
    #         try_count += 1
    #         time.sleep(try_count)
    #     consumer.commit()
