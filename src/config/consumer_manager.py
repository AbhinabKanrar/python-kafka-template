from confluent_kafka import Consumer

from src.config.config_manager import ConfigManager


class ConsumerManager:
    def __init__(self) -> None:
        self.config_manager = ConfigManager()
        self.consumer = self.__init_consumer__()

    def __init_consumer__(self):
        c = Consumer(
            {
                "bootstrap.servers": self.config_manager.bootstrap_servers,
                "group.id": self.config_manager.group_id,
                "auto.offset.reset": "latest",
            }
        )

        c.subscribe(self.config_manager.topics)

        return c
