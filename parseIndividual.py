import parser, lexer

class IndividualParser(object):
  def __init__(self, path):
    self.path = path
  def add_code(self):
    with open(self.path, "r") as ooo:
      oo = ooo.read()
    lexe = lexer.Lexer(oo)
    toki = lexe.tokenize()
    par = parser.Parser(toki)
    cod = par.parse()
    return cod

