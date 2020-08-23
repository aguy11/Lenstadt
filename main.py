from lexer import Lexer
from parser import Parser

with open("test.stadt", "r") as wf:
  fr = wf.read()

lex = Lexer(fr)
tokens = lex.tokenize()
parse = Parser(tokens)
parse.parse()
with open("code.py", "r") as cd:
  code = cd.read()
exec(code)
