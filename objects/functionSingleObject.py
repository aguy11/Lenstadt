class FunctionSingleObject(object):
  def __init__(self):
    self.exec_code = ""
  def transpile(self, name, params, indents):
    self.exec_code = self.exec_code + f"{name}("
    
    for i in params:
      if i != params[-1]:
        self.exec_code = self.exec_code + f"{i},"
      else:
        self.exec_code = self.exec_code + params[-1]
    self.exec_code = self.exec_code + ")\n"
    for i in range(indents):
      self.exec_code = "\t" + self.exec_code
    return self.exec_code
