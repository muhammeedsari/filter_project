from core.kafka import Kafka
from core.error_success_result import ErrorResult


class AdminController:

    def create_topic(self, topic='credit_card', num_partitions=2):
        try:
            kafka = Kafka()
            kafka.create_topics(topic=topic, num_partitions=num_partitions)
        except Exception as err:
            print(ErrorResult(message=err.__doc__))
