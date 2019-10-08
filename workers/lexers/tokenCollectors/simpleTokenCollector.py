from abc import ABC, abstractmethod, abs
from enum import Enum

__all__ = [
    "SimpleTokenCollector"
]

SPECIAL_CHARACTERS = ['{', '}', '(', ')', '<', '>',
                      ';', '+', '-', '*', '/', '=',
                      '!', '|', '&', '?', ':', '.']

State = Enum("State", [
    "Waiting",
    "Ready",
    "Complete",
    "Miss"
])


class SimpleTokenCollector(ABC):
    _SYM = None

    def __init__(self):
        self.state = State.Waiting
        self._value = ''
