class ReadFileObject(object):
  def __init__(self):
    self.exec_code = ""
  def transpile(self, indents, varname, filepath):
    self.exec_code += f"with open({filepath}, 'r') as lenstadt:\n\t{varname} = lenstadt.read()\n"
    for i in range(indents):
      self.exec_code = "\t" + self.exec_code
    return self.exec_code
