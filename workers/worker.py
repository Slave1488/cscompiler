from abc import ABC, abstractmethod

ERROR_WORKER = 100


class Worker(ABC):
    def __init__(self, workplace):
        self._workplace = workplace
        self._product = None

    def _error(self, msg, ERROR=ERROR_WORKER):
        print("{} error: {msg}".format(type(self).__name__))
        self.product = msg
        sys.exit(ERROR)

    @abstractmethod
    def _make(self, **kwargs):
        pass
