import os
from enum import Enum


class Env(Enum):
    RPI_LOG_FILE = "RPI_LOG_FILE"
    GRAPHITE_HOST = "GRAPHITE_HOST"
    GRAPHITE_PORT = "GRAPHITE_PORT"
    RPI_NETWORK_MASK = "RPI_NETWORK_MASK"

    def resolve(self) -> str:
        value = os.getenv(self.value)
        if not value:
            raise RuntimeError(f"Environment value for {self.name} is not set")
        return value
