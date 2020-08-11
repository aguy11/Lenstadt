class PrintObject(object):
  def __init__(self):
    self.exec_code = ""
  def transpile(self, value, indents):
    self.exec_code = self.exec_code + f"print({value})\n"
    for i in range(indents):
      self.exec_code = "\t" + self.exec_code
    return self.exec_code
