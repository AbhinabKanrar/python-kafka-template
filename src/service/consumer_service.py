from src.config.consumer_manager import ConsumerManager


class ConsumerService:
    def __init__(self) -> None:
        self.consumer = ConsumerManager().consumer

    def load_consumer(self):
        while True:
            msg = self.consumer.poll(1.0)

            if msg and not msg.error():
                print(
                    "Received message: {}".format(
                        msg.value().decode("utf-8")))

        self.consumer.close()
