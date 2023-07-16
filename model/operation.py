from enum import Enum
from typing import List


class OperationCode(Enum):
    ADD = "add"
    SUB = "sub"
    MUL = "mul"
    DIV = "div"

    @classmethod
    def values(cls) -> List[str]:
        """ Returns the possible values as a list of strings. """
        return [e.value for e in cls]
