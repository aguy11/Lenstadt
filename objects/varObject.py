class VarObject(object):
  def __init__(self):
    self.exec_code = ""
  def transpile(self, name, operator, value, indents):
    self.exec_code = self.exec_code + f"{name} {operator} {value}\n"
    for i in range(indents):
      self.exec_code = "\t" + self.exec_code
    return self.exec_code
