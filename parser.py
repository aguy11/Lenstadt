from objects.varObject import VarObject
from objects.printObject import PrintObject
from objects.ifObject import IfObject
from objects.elseObject import ElseObject
from objects.elseIfObject import ElseIfObject
from objects.whileObject import WhileObject

class Parser(object):
  def __init__(self, tokens):
    self.tokens = tokens
    self.token_index = 0
    self.transpiled_code = ""
    self.indents = 0
  def parse(self):
    while self.token_index < len(self.tokens):
      ##print(self.token_index)
      ##print(self.tokens[self.token_index])
      token_type = self.tokens[self.token_index][0]        
      token_value = self.tokens[self.token_index][1]
      print(token_value + "Is it")
      if token_type == "IDENTIFIER" and self.tokens[self.token_index + 1][0] == "OPERATOR":
        self.parse_variable_declaration(self.tokens[self.token_index : len(self.tokens)])
      elif token_type == "COMMENT":
        self.token_index += 1
      elif token_type == "IDENTIFIER" and token_value == "stampLn":
        self.parse_stamp_ln(self.tokens[self.token_index : len(self.tokens)])
      elif token_type == "IDENTIFIER" and token_value == "completeIf":
        self.parse_if_statement(self.tokens[self.token_index : len(self.tokens)])
      elif token_type == "IDENTIFIER" and token_value == "completeElse":
        self.parse_else_statement(self.tokens[self.token_index: len(self.tokens)])
      elif token_type == "IDENTIFIER" and token_value == "completeElseIf":
        self.parse_elif_statement(self.tokens[self.token_index: len(self.tokens)])
      elif token_type == "CASE" and token_value == "}":
        self.indents -= 1
        self.token_index += 1
      elif token_type == "IDENTIFIER" and token_value == "completeWhile":
        self.parse_while_loop(self.tokens[self.token_index: len(self.tokens)])
      elif token_type == "IDENTIFIER" and token_value == "quitLoop":
        if self.tokens[self.token_index + 1][1] == ";":
          exec_code = "break"
          for i in range(self.indents):
            exec_code = "\t" + exec_code
          self.transpiled_code = self.transpiled_code + f"{exec_code}\n"
          self.token_index += 2
        else:
          raise ValueError("';' expected after quitLoop statement")
      elif token_type == "IDENTIFIER" and token_value == "advance":
        if self.tokens[self.token_index + 1][1] == ";":
          exec_code = "pass"
          for i in range(self.indents):
            exec_code = "\t" + exec_code
          self.transpiled_code = self.transpiled_code + f"{exec_code}\n"
          self.token_index += 2
        else:
          raise ValueError("';' expected after advance statement")
      else:
        raise SyntaxError("ERR: Undefined Item: " + token_value)


    print(self.transpiled_code)
    #try:    #This stuff is for later, I feel
    exec(self.transpiled_code)
    #except: #For errors that Python will call, not exactly sure about these yet
      #raise 


  def parse_variable_declaration(self, tkns):
    tokens_checked = 0
    name = ''
    operator = ''
    value = ''
    for token in range(len(tkns)):
      token_type = tkns[tokens_checked][0]
      token_value = tkns[tokens_checked][1]
      if token_type == "STATEMENT_END":
        break
      elif token == 0 and token_type == "IDENTIFIER":
        name = token_value
      elif token == 0 and token_value != "IDENTIFIER":
        raise ValueError("ERR: Invalid Variable Name " + token_value)
      elif token == 1 and token_type == "OPERATOR":
        operator = token_value
      elif token == 1 and token_type != "OPERATOR":
        raise ValueError("ERR: Invalid Variable Operator " + token_value)
      elif token == 2 and token_type in ['IDENTIFIER', 'INTEGER', "BOOL", "STRING"]:
        value = token_value
      elif token == 2 and token_type not in ['IDENTIFIER','INTEGER', "BOOL", "STRING"]:
        raise ValueError("ERR: Inavlid Variable Value " + token_value)
      elif token >= 3 and token_type in ['IDENTIFIER', 'INTEGER', "BOOL", "STRING", "OPERATOR"]:
        value = value + " " + token_value
      elif token >= 3 and token_type not in ['IDENTIFIER', 'INTEGER', "BOOL", "STRING", "OPERATOR"]:
        raise ValueError("ERR: Inavlid Variable Value " + token_value)
      tokens_checked += 1
    #print(name, operator, value)
    VarObj = VarObject()
    self.transpiled_code = self.transpiled_code + VarObj.transpile(name, operator, value, self.indents)
    self.token_index += tokens_checked + 1


  def parse_stamp_ln(self, tkns):
    tokens_checked = 0
    value = ''
    for token in range(len(tkns)):
      token_type = tkns[tokens_checked][0]
      token_value = tkns[tokens_checked][1]
      if token_type == "STATEMENT_END":
        break
      elif token == 1 and token_type in ["IDENTIFIER", "STRING", "INTEGER", "BOOL"]:
        value = token_value
      elif token == 1 and token_type not in ["IDENTIFIER", "STRING", "INTEGER", "BOOL"]:
        raise ValueError("Invalid StampLn Value " + token_value)
      elif token >= 2 and token_type in ["IDENTIFIER", "STRING", "INTEGER", "BOOL", "OPERATOR"]:
        value = value + " " + token_value
      elif token >= 2 and token_type not in ["IDENTIFIER", "STRING", "INTEGER", "BOOL", "OPERATOR"]:
        raise ValueError("Invalid StampLn Value " + token_value)
      tokens_checked += 1
    printObj = PrintObject()
    self.transpiled_code = self.transpiled_code + printObj.transpile(value, self.indents)
    self.token_index += tokens_checked + 1
  def parse_if_statement(self, tkns):
    tokens_checked = 0
    case = ''
    for token in range(len(tkns)):
      token_type = tkns[tokens_checked][0]
      token_value = tkns[tokens_checked][1]
      if token_type == "CASE" and token_value == "{":
        break
      elif token == 1 and token_type in ["IDENTIFIER", "STRING", "INTEGER", "BOOL"]:
        case = case + token_value
      elif token == 1 and token_value not in ["IDENTIFIER", "STRING", "INTEGER", "BOOL"]:
        raise ValueError("Invalid CompleteIf Statement Particle: " + token_value)
      elif token >= 1 and token_type in ["IDENTIFIER", "STRING", "INTEGER", "BOOL", "OPERATOR"]:
        case = case + " " + token_value
      elif token >= 1 and token_type in ["IDENTIFIER", "STRING", "INTEGER", "BOOL", "OPERATOR"]:
        raise ValueError("Invalid CompleteIf Statement Particle: " + token_value)
      tokens_checked += 1
    IfObj = IfObject()
    self.transpiled_code = self.transpiled_code + IfObj.transpile(case, self.indents)
    self.token_index = self.token_index + tokens_checked + 1
    self.indents += 1
  def parse_else_statement(self, tkns):
    tokens_checked = 0
    for token in range(len(tkns)):
      token_type = tkns[tokens_checked][0]
      token_value = tkns[tokens_checked][1]
      if token == 1 and token_type == "CASE" and token_value == "{":
        break
      elif token == 1 and not token_type == "CASE" and token_value == "{":
        raise ValueError("Invalid CompleteElse Particle: " + token_value)
      tokens_checked += 1
    ElseObj = ElseObject()
    self.transpiled_code = self.transpiled_code + ElseObj.transpile(self.indents)
    self.token_index = self.token_index + tokens_checked + 1
    self.indents += 1
  def parse_elif_statement(self, tkns):
    tokens_checked = 0
    case = ''
    for token in range(len(tkns)):
      token_type = tkns[tokens_checked][0]
      token_value = tkns[tokens_checked][1]
      if token_type == "CASE" and token_value == "{":
        break
      elif token == 1 and token_type in ["IDENTIFIER", "STRING", "INTEGER", "BOOL"]:
        case = case + token_value
      elif token == 1 and token_value not in ["IDENTIFIER", "STRING", "INTEGER", "BOOL"]:
        raise ValueError("Invalid CompleteElseIf Statement Particle: " + token_value)
      elif token >= 1 and token_type in ["IDENTIFIER", "STRING", "INTEGER", "BOOL", "OPERATOR"]:
        case = case + " " + token_value
      elif token >= 1 and token_type in ["IDENTIFIER", "STRING", "INTEGER", "BOOL", "OPERATOR"]:
        raise ValueError("Invalid CompleteElseIf Statement Particle: " + token_value)
      tokens_checked += 1
    ElseIfObj = ElseIfObject()
    self.transpiled_code = self.transpiled_code + ElseIfObj.transpile(case, self.indents)
    self.token_index += tokens_checked + 1
    self.indents += 1
  def parse_while_loop(self, tkns):
    tokens_checked = 0
    case = ''
    for token in range(len(tkns)):
      token_type = tkns[tokens_checked][0]
      token_value = tkns[tokens_checked][1]
      if token_type == "CASE" and token_value == "{":
        break
      elif token == 1 and token_type in ["IDENTIFIER", "STRING", "INTEGER", "BOOL"]:
        case = case + token_value
      elif token == 1 and token_value not in ["IDENTIFIER", "STRING", "INTEGER", "BOOL"]:
        raise ValueError("Invalid CompleteWhile Particle: " + token_value)
      elif token >= 1 and token_type in ["IDENTIFIER", "STRING", "INTEGER", "BOOL", "OPERATOR"]:
        case = case + " " + token_value
      elif token >= 1 and token_type in ["IDENTIFIER", "STRING", "INTEGER", "BOOL", "OPERATOR"]:
        raise ValueError("Invalid CompleteWhile  Particle: " + token_value)
      tokens_checked += 1
    WhileObj = WhileObject()
    self.transpiled_code = self.transpiled_code + WhileObj.transpile(case, self.indents)
    self.token_index += tokens_checked + 1
    self.indents += 1
