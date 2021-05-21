import os
import sys

from dotenv import load_dotenv


class ConfigManager:
    def __init__(self) -> None:
        env = sys.argv[1] if len(sys.argv) >= 2 else None

        if env:
            load_dotenv(f".env.{sys.argv[1]}")
        else:
            load_dotenv()

        self.__init_kafka_prop__()

    def __init_kafka_prop__(self):
        self.bootstrap_servers = os.environ.get("bootstrap.servers")
        self.group_id = os.environ.get("group.id")
        self.topics = os.environ.get("topics").split(",")
