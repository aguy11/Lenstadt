class WriteFileObject(object):
  def __init__(self):
    self.exec_code = ""
  def transpile(self, indents, filepath, text):
    self.exec_code += f"with open({filepath}, 'w') as lenstadt:\n\tlenstadt.write({text})\n"
    for i in range(indents):
      self.exec_code = "\t" + self.exec_code
    return self.exec_code
