import sys
from abc import ABC, abstractmethod
from collections import namedtuple

__all__ = [
    "Worker"
]

ERROR_WORKER = 100


def dict_to_namedtuple(dict_, name="namedtuple"):
    return namedtuple(name, dict_.keys())(*dict_.values())


class Worker(ABC):
    def __init__(self, **workplace):
        self._workplace = dict_to_namedtuple(workplace, "Workplace")
        self._product = None

    def _error(self, msg, ERROR=ERROR_WORKER):
        print("{} error: {}".format(type(self).__name__, msg))
        sys.exit(ERROR)

    @abstractmethod
    def _make(self, **kwargs):
        pass
