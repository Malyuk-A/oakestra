import enum
from typing import Any


class CustomEnum(enum.Enum):
    def __str__(self) -> str:
        return self.value


JSON_SLA = Any
