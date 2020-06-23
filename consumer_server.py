from pykafka import KafkaClient
from pykafka.simpleconsumer import OffsetType
import logging

logging.getLogger("pykafka.broker").setLevel('WARN')

client = KafkaClient(hosts='localhost:9092')
topic = client.topics['police.calls.service']
consumer = topic.get_balanced_consumer(
    consumer_group='group-A', 
    auto_commit_enable=False, 
    auto_offset_reset=OffsetType.EARLIEST,
    zookeeper_connect='localhost:2181'
)

for message in consumer:
    if message is not None:
        print(f'Message [Offset: {message.offset}, Value: {message.value}]')