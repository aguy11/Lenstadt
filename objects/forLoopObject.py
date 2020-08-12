class ForLoopObject(object):
  def __init__(self): 
    self.exec_code = ""
  def transpile(self, temp, fro, to, indents):
    self.exec_code = self.exec_code + f"for {temp} in range({fro}, {to}):\n"
    for i in range(indents):
      self.exec_code = "\t" + self.exec_code
    return self.exec_code
