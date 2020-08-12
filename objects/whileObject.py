class WhileObject(object):
  def __init__(self):
    self.exec_code = ""
  def transpile(self, case, indents):
    self.exec_code = self.exec_code + f"while {case}:\n"
    for i in range(indents):
      self.exec_code = "\t" + self.exec_code
    return self.exec_code
