from Lexer import *

f = open('content.txt')

l = Lexer(f)

l.run()

token = l.next_token()

while token.sym != ERROR and token.sym != EOF:
    print(token)
    token = l.next_token()
