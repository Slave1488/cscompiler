import sys
from collections import namedtuple

ERROR_LEXER = 20

EOF, SPACE, SPECIAL, ESCAPE, WORD, ERROR = range(6)

SPECIAL_CHARACTERS = ['{', '}', '(', ')', '<', '>',
                      ';', '+', '-', '*', '/', '=',
                      '!', '|', '&', '?', ':', '.']


Token = namedtuple("Token", [
    "sym",
    "value"
])


def get_token(get_char, move_char, verify_char):
    token = ''
    while verify_char(get_char()):
        token += get_char()
        move_char()
    return token


class Lexer:
    def __init__(self, input):
        self.is_running = False
        self._char = ''
        self._token = Token(EOF, '')
        self.set_input(input)

    def error(self, msg):
        print("Lexer error: {}".format(msg))
        self.stop
        self._token = Token(ERROR, msg)
        sys.exit(ERROR_LEXER)

    def set_input(self, input):
        self._input = input
        if self.is_running:
            self.move_char()

    def run(self):
        self.is_running = True
        self.move_char()

    def stop(self):
        self.is_running = False

    def move_char(self):
        if not self.is_running:
            return
        try:
            self._char = self._input.read(1)
        except Exception as e:
            self._input.close()
            self.error(e)

    def next_token(self):
        if not self.is_running:
            return

        def get_char():
            return self._char

        def verify_char_is_eof(char):
            return len(char) == 0

        def verify_char_is_space(char):
            return char.isspace()

        def verify_char_is_special(char):
            return char in SPECIAL_CHARACTERS

        def verify_char_is_escape(char):
            return char == '\\'

        def verify_char_is_word(char):
            return not verify_char_is_eof(char) and \
                   not verify_char_is_space(char) and \
                   not verify_char_is_special(char) and \
                   not verify_char_is_escape(char)

        if verify_char_is_eof(self._char):
            self._token = Token(EOF, self._char)
            self.move_char()
        elif verify_char_is_space(self._char):
            self._token = Token(SPACE, get_token(get_char,
                                                 self.move_char,
                                                 verify_char_is_space))
        elif verify_char_is_special(self._char):
            self._token = Token(SPECIAL, self._char)
            self.move_char()
        elif verify_char_is_escape(self._char):
            value = self._char
            self.move_char()
            value += self._char
            self.move_char()
            self._token = Token(ESCAPE, value)
        else:
            self._token = Token(WORD, get_token(get_char,
                                                self.move_char,
                                                verify_char_is_word))
        return self._token
