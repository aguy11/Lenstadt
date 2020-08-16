class FunctionObject(object):
  def __init__(self):
    self.exec_code = ""
  def transpile(self, name, parameters, indents):
    self.exec_code = self.exec_code + f"def {name}("
    
    for i in parameters:
      if i != parameters[-1]:
        self.exec_code = self.exec_code + f"{i},"
      else:
        self.exec_code = self.exec_code + parameters[-1]
    self.exec_code = self.exec_code + "):\n"
    for i in range(indents):
      self.exec_code = "\t" + self.exec_code
    return self.exec_code
