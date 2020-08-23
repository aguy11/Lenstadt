import parser, lexer

class IndividualParser(object):
  def __init__(self, path):
    self.path = path
    self.extras = ['time', 'random', 're', 'math']
  def add_code(self):
    with open(self.path, "r") as ooo:
      oo = ooo.read()
    lexe = lexer.Lexer(oo)
    toki = lexe.tokenize()
    par = parser.Parser(toki)
    cod = par.parse_extra()
    
    return cod, par.funcs

