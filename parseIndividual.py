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
    nm = self.path[8: -6]
    line1 = f"class {nm.upper()}:\n"
    lastln = f"{nm} = {nm.upper()}\n"
    lns = cod.split("\n")
    loins = []
    for i in lns:
      loins.append("\t" + i)
    loins = loins[:-1]
    loins.append("\n")
    sep = "\n"
    lins = sep.join(loins)
    lins = line1 + lins + lastln
    funcs = []
    for x in par.funcs:
      funcs.append(f"{nm}.{x}")
    return lins, funcs

