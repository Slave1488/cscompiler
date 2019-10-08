from collections import namedtuple
from enum import Enum
from ..worker import *
from .tokenCollectors.simpleTokenCollector import SimpleTokenCollector

__all__ = [
    "SimpleLexer"
]

ERROR_LEXER = 20
DEFINE = None


class SimpleLexer(Worker):
    _OK = True
    _MISS = False

    def __init__(self):
        super().__init__(token_collectors=["msg"])

    @property
    def _collectors(self):
        return self._workplace.token_collectors

    @property
    def token(self):
        return self._product

    @token.setter
    def token(self, value):
        self._product = value

    def _error(self, msg):
        super()._error(msg, ERROR_LEXER)

    def _make(self):
        ch = DEFINE
        ready = False
        while not ready:
            for collector in self._collectors:
                pass
            ready = True
        return self._OK if ready else self._MISS

    def next(self):
        return self._make()
