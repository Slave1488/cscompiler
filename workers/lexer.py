from collections import namedtuple
from enum import Enum
from .worker import Worker

ERROR_LEXER = 20
ERROR_READER = 21

Token = namedtuple("Token", [
    "sym",
    "value"
])

Sym = Enum("Sym", [
    "EOF",
    "SPACE",
    "SPECIAL",
    "ESCAPE",
    "WORD",
    "ERROR"
])

SPECIAL_CHARACTERS = ['{', '}', '(', ')', '<', '>',
                      ';', '+', '-', '*', '/', '=',
                      '!', '|', '&', '?', ':', '.']


class Lexer(Worker):
    def __init__(self):
        super().__init__([])

    @property
    def token(self):
        return self._product

    def error(self, msg):
        self._error(msg, ERROR_LEXER)

    def _make(self):
        pass

    def next(self):
        return self._make()

__all__ = [
    "Lexer",
    "Token"
]
