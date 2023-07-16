from enum import Enum
from typing import List


class OperationCode(Enum):
    ADD = "add"
    SUB = "sub"
    MUL = "mul"
    DIV = "div"

    @classmethod
    def values(cls) -> List[str]:
        return [e.value for e in cls]
