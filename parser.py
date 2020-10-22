import lexer, os, parseIndividual
from objects.varObject import VarObject
from objects.printObject import PrintObject
from objects.ifObject import IfObject
from objects.elseObject import ElseObject
from objects.elseIfObject import ElseIfObject
from objects.whileObject import WhileObject
from objects.forLoopObject import ForLoopObject
from objects.functionObject import FunctionObject
from objects.giveObject import GiveObject
from objects.functionSingleObject import FunctionSingleObject 
from objects.readFileObject import ReadFileObject
from objects.writeFileObject import WriteFileObject

class Parser(object):
  def __init__(self, tokens):
    self.tokens = tokens
    self.token_index = 0
    self.transpiled_code = ""
    self.indents = 0
    self.funcs = []
  def parse(self):
    
    while self.token_index < len(self.tokens):
      ###print(self.token_index)
      ##print(self.tokens[self.token_index][0])
      token_type = self.tokens[self.token_index][0]        
      token_value = self.tokens[self.token_index][1]
      #print(token_value + "Is it")

      if token_type == "IDENTIFIER" and self.tokens[self.token_index + 1][1] in ["+=", "=", "-="]:
        self.parse_variable_declaration(self.tokens[self.token_index : len(self.tokens)])
      elif token_type == "COMMENT":
        self.token_index += 1
      elif token_type == "IDENTIFIER" and token_value == "stampLn":
        self.parse_stamp_ln(self.tokens[self.token_index : len(self.tokens)])
      elif token_type == "IDENTIFIER" and token_value == "completeIf":
        self.parse_if_statement(self.tokens[self.token_index : len(self.tokens)])
      elif token_type == "IDENTIFIER" and token_value == "otherwise":
        self.parse_else_statement(self.tokens[self.token_index: len(self.tokens)])
      elif token_type == "IDENTIFIER" and token_value == "completeElseIf":
        self.parse_elif_statement(self.tokens[self.token_index: len(self.tokens)])
      elif token_type == "CASE" and token_value == "}":
        self.indents -= 1
        self.token_index += 1
      elif token_type == "CASE" and token_value == "{":
        self.token_index += 1
      elif token_type == "IDENTIFIER" and token_value == "completeWhile":
        self.parse_while_loop(self.tokens[self.token_index: len(self.tokens)])
      elif token_type == "IDENTIFIER" and token_value in self.funcs:
        self.parse_function(self.tokens[self.token_index: len(self.tokens)], token_value)
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
      elif token_type == "IDENTIFIER" and token_value == "loop":
        self.parse_for_loop(self.tokens[self.token_index: len(self.tokens)])
      elif token_type == "IDENTIFIER" and token_value == "give":
        self.parse_give(self.tokens[self.token_index: len(self.tokens)])
      elif token_type == "IDENTIFIER" and token_value == "defFunc":
        self.parse_function_declaration(self.tokens[self.token_index: len(self.tokens)])
      elif token_type == "IDENTIFIER" and token_value == "use":
        self.parse_import(self.tokens[self.token_index: len(self.tokens)])
      elif token_type == "IDENTIFIER" and token_value == "readFile":
        self.parseReadFile(self.tokens[self.token_index: -1])
      elif token_type == "IDENTIFIER" and token_value == "writeFile":
        self.parseWriteFile(self.tokens[self.token_index: -1])
      else:
        #print(self.token_index)
        raise SyntaxError("ERR: Undefined Item: " + token_value)
    self.transpiled_code = "import time, random, math\n" + self.transpiled_code
    #print("\n\n" + self.transpiled_code)
    with open("code.py", "w") as iju:
      iju.write(self.transpiled_code)
      iju.close()
    return self.transpiled_code
  def parse_extra(self):
    while self.token_index < len(self.tokens):
      ###print(self.token_index)
      ##print(self.tokens[self.token_index][0])
      token_type = self.tokens[self.token_index][0]        
      token_value = self.tokens[self.token_index][1]
      #print(token_value + "Is it")

      if token_type == "IDENTIFIER" and self.tokens[self.token_index + 1][1] in ["+=", "=", "-="]:
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
      elif token_type == "CASE" and token_value == "{":
        self.token_index += 1
      elif token_type == "IDENTIFIER" and token_value == "completeWhile":
        self.parse_while_loop(self.tokens[self.token_index: len(self.tokens)])
      elif token_type == "IDENTIFIER" and token_value in self.funcs:
        self.parse_function(self.tokens[self.token_index: len(self.tokens)], token_value)
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
      elif token_type == "IDENTIFIER" and token_value == "loop":
        self.parse_for_loop(self.tokens[self.token_index: len(self.tokens)])
      elif token_type == "IDENTIFIER" and token_value == "give":
        self.parse_give(self.tokens[self.token_index: len(self.tokens)])
      elif token_type == "IDENTIFIER" and token_value == "defFunc":
        self.parse_function_declaration(self.tokens[self.token_index: len(self.tokens)])
      elif token_type == "IDENTIFIER" and token_value == "use":
        self.parse_import(self.tokens[self.token_index: len(self.tokens)])
      else:
        #print(self.token_index)
        raise SyntaxError("ERR: Undefined Item: " + token_value)
    return self.transpiled_code
 
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
      elif token == 2 and token_type in ['IDENTIFIER', 'INTEGER', "BOOL", "STRING", "CASE"]:
        value = token_value
      elif token == 2 and token_type not in ['IDENTIFIER','INTEGER', "BOOL", "STRING", "CASE"]:
        raise ValueError("ERR: Inavlid Variable Value " + token_value + " in " + name)
      elif token >= 3 and token_type in ['IDENTIFIER', 'INTEGER', "BOOL", "STRING", "OPERATOR", "CASE"]:
        value = value + " " + token_value
      elif token >= 3 and token_type not in ['IDENTIFIER', 'INTEGER', "BOOL", "STRING", "OPERATOR", "CASe"]:
        raise ValueError("ERR: Inavlid Variable Value " + token_value + " in " + name)
      tokens_checked += 1
    ##print(name, operator, value)
    if name == "lenstadt":
      raise ValueError("Variable Cannot Be Named 'lenstadt'")
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
      elif token == 1 and token_type in ["IDENTIFIER", "STRING", "INTEGER", "BOOL", "OPERATOR"]:
        case = case + token_value
      elif token == 1 and token_value not in ["IDENTIFIER", "STRING", "INTEGER", "BOOL", "OPERATOR"]:
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

  def parse_for_loop(self, tkns):
    tokens_checked = 0
    temp_var = ""
    to = ''
    fro = ''
    place_holder = 0
    for token in range(len(tkns)):
      token_type = tkns[tokens_checked][0]
      token_value = tkns[tokens_checked][1]
      #print(token == place_holder and token_type in ['IDENTIFIER', 'INTEGER'])
      if token == 0:
        pass
      elif token_type == "CASE" and token_value == "{":
        break
      elif token == 1 and token_type == "IDENTIFIER":
        temp_var = token_value
      elif token == 1 and token_type != "IDENTIFIER":
        raise ValueError("Invalid Temporary Loop Variable: " + token_value)
      elif token == 2 and token_value == "from":
        pass
      elif token == 2 and token_value != "from":
        raise ValueError("'from' expected.")
      elif token == 3 and token_type in ['IDENTIFIER', 'INTEGER']:
        fro = fro + token_value
      elif token == 3 and token_type not in ['IDENTIFIER', 'INTEGER']:
        raise ValueError("Invalid to Value in Loop")
      elif token > 3 and token < place_holder and place_holder != 0 and token_type in ['IDENTIFIER', 'INTEGER', 'OPERATOR'] and token_value != "to":
        fro = fro + " " + token_value
      elif token > 3 and token_value == "to":
        place_holder = token + 1
        #print("Hahahaha " + str(place_holder))
      elif token > 3 and token_type not in ['INTEGER', 'IDENTIFIER', 'OPERATOR']:
        raise ValueError('Invalid From Value in Loop')
      elif token == place_holder and token_type in ['IDENTIFIER', 'INTEGER']:
        #print("Bob")
        to = to + token_value
      elif token == place_holder and token_type not in ['IDENTIFIER', 'INTEGER']:
        raise ValueError("Invalid to Value in Loop")
      elif token > place_holder and token_type in ['IDENTIFIER', 'INTEGER', 'OPERATOR']:
        to = to + " " + token_value
      elif token > place_holder and token_type not in ['INTEGER', 'IDENTIFIER', 'OPERATOR']:
        raise ValueError('Invalid To Value in Loop')
      tokens_checked += 1
    #print("Hey you ",  fro, to)
    ForLoopObj = ForLoopObject()
    self.transpiled_code = self.transpiled_code + ForLoopObj.transpile(temp_var, fro, to, self.indents)
    self.token_index += tokens_checked + 1
    self.indents += 1
  def parse_function_declaration(self, tkns):
    tokens_checked = 0
    name = ''
    params = []
    place = 0
    for token in range(len(tkns)):
      token_type = tkns[tokens_checked][0]
      token_value = tkns[tokens_checked][1]
      if token_type == "CASE" and token_value == "{":
        break
      elif token == 1 and token_type == "IDENTIFIER":
        name = token_value
      elif token == 1 and token_type != "IDENTIFIER":
        raise ValueError("Invalid Function Name")
      elif token == 2 and token_type == "CASE" and token_value == "(":
        pass
      elif token == 2 and token_value != "CASE":
        raise ValueError("'(' expected.")
      elif token == 2 and token_value != "(":
        raise ValueError("'(' expected.")
      elif token > 3 and token_value == ")":
        pass
      elif token == 3 and token_type == "IDENTIFIER":
        params.append(token_value)
        place = token + 1
      elif token == 3 and token_type == "CASE" and token_value == ")":
        pass
      elif token == 3 and token_type !=  "IDENTIFIER":
        raise ValueError("Invalid Parameter Name")
      elif token == place and place != 0 and token_type == "SEPERATOR":
        pass
      elif token == place and place != 0 and token_type != "SEPERATOR":
        raise ValueError("',' expected")
      elif token == place + 1 and token_type == "IDENTIFIER":
        params.append(token_value)
        place = token + 1
      elif token == place + 1 and token_type != "IDENTIFIER":
        raise ValueError("Invalid Parameter Name") 
      tokens_checked += 1
    FunctionObj = FunctionObject()
    self.transpiled_code = self.transpiled_code + FunctionObj.transpile(name, params, self.indents)
    self.token_index += tokens_checked + 1
    #print(name, tokens_checked, self.tokens[self.token_index])
    self.indents += 1
    self.funcs.append(name)
  def parse_give(self, tkns):
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
        raise ValueError("Invalid Give Value " + token_value)
      elif token >= 2 and token_type in ["IDENTIFIER", "STRING", "INTEGER", "BOOL", "OPERATOR"]:
        value = value + " " + token_value
      elif token >= 2 and token_type not in ["IDENTIFIER", "STRING", "INTEGER", "BOOL", "OPERATOR"]:
        raise ValueError("Invalid Give Value " + token_value)
      tokens_checked += 1
    GiveObj = GiveObject()
    self.transpiled_code = self.transpiled_code + GiveObj.transpile(value, self.indents)
    self.token_index = self.token_index + tokens_checked + 1
  def parse_function(self, tkns, nm):
    tokens_checked = 0
    name = nm
    pars = []
    current_par = ''
    place = 2
    for token in range(len(tkns)):
      token_type = tkns[tokens_checked][0]  
      token_value = tkns[tokens_checked][1]  
      #print(token)
      if token == 1 and token_type == "CASE" and token_value == "(":
        pass
      elif token == 1 and token_type != "CASE":
        #print("mhuah")
        raise ValueError("'(' expected")
      elif token == 1 and token_value != "(":
        #print("mhua")
        raise ValueError("'(' expected")
      elif token >= 2 and token_value == ")":
        if tkns[tokens_checked + 1][0] == "STATEMENT_END":
          pars.append(current_par)
          tokens_checked += 1
          break
        else:
          raise ValueError("';' expected")

      elif token == place and token_type in ['IDENTIFIER', 'STRING', 'BOOL', "INTEGER"]:
        current_par = token_value
      elif token == place and token_type not in ['IDENTIFIER', 'STRING', 'BOOL', "INTEGER"]:
        raise ValueError("Invalid Function Parameter Contents: " + token_value)
      elif token > place and token_type == "SEPERATOR":
        pars.append(current_par)
        current_par = ""
        place = token + 1

      elif token > place and token_type in ['IDENTIFIER', 'STRING', 'BOOL', "INTEGER", "OPERATOR"]:
        current_par = current_par + " " + token_value
      elif token > place and token_type not in ['IDENTIFIER', 'STRING', 'BOOL', "INTEGER", "OPERATOR"]:
        raise ValueError("Invalid Function Parameter Contents: " + token_value)
      tokens_checked += 1
    FunctionSingleObj = FunctionSingleObject()
    self.transpiled_code = self.transpiled_code + FunctionSingleObj.transpile(name, pars, self.indents)
    self.token_index = self.token_index + tokens_checked + 1
  def parse_import(self, tkns):
    tokens_checked = 0
    module = "modules/"
    mod2 = ""
    for token in range(len(tkns)):
      token_type = tkns[tokens_checked][0]  
      token_value = tkns[tokens_checked][1]  
      if token == 1 and token_type == "IDENTIFIER":
        module = module + token_value + ".stadt"
        mod2 = token_value
      elif token == 1 and token_type != "IDENTIFIER":
        raise ValueError("Invalid Module Name")
      elif token == 2 and token_type == "STATEMENT_END":
        #tokens_checked += 1
        break
      elif token == 2 and token_type != "STATEMENT_END":
        raise ValueError("Semicolon (;), expected")
      tokens_checked += 1

    if not os.path.exists(module):
      raise ImportError("Cannot Use " + mod2)
    else:
      IndividualPrsr = parseIndividual.IndividualParser(module)
      modulework = IndividualPrsr.add_code()
      self.transpiled_code = modulework[0] + self.transpiled_code
      self.funcs += modulework[1]
      self.token_index += tokens_checked + 1
  def parseReadFile(self, tkns):
    tokens_checked = 0
    filepath = ""  
    asread = False
    asread_token = 0
    varname = ""
    for token in range(len(tkns)):
      token_type = tkns[tokens_checked][0]  
      token_value = tkns[tokens_checked][1]
      if token == 1 and token_type in ["STRING", "IDENTIFIER"] and not asread:
        filepath = token_value
      elif token_type == "STATEMENT_END":
        break
      elif token == 1 and token_type not in ["STRING", "IDENTIFIER"] and not asread:
        raise ValueError("Invalid File Path to ReadFile")
      elif token >= 2 and token_value == "as":
        asread = True
        asread_token = token
      elif token >= 2 and token_type in ['IDENTIFIER', "STRING", "OPERATOR"] and not asread:
        filepath += " " + token_value
      elif token >= 2 and token_type not in ['IDENTIFIER', "STRING", "OPERATOR"] and not asread:
        raise ValueError("Invalid FilePath in ReadFile")
      elif token == asread_token + 1 and token_type in ['IDENTIFIER'] and asread:
        varname = token_value
      elif token == asread_token + 1 and token_type not in ['IDENTIFIER'] and asread:
        raise ValueError("Invalid Variable name in readFile")
        
      tokens_checked += 1

    ReadFileObj = ReadFileObject()
    self.transpiled_code += ReadFileObj.transpile(self.indents, varname, filepath)
    self.token_index += tokens_checked + 1
  def parseWriteFile(self, tkns):
    tokens_checked = 0
    filepath = ""  
    asread = False
    asread_token = 0
    text = ""
    for token in range(len(tkns)):
      token_type = tkns[tokens_checked][0]  
      token_value = tkns[tokens_checked][1]
      if token == 1 and token_type in ["STRING", "IDENTIFIER"] and not asread:
        filepath = token_value
      elif token_type == "STATEMENT_END":
        break
      elif token == 1 and token_type not in ["STRING", "IDENTIFIER"] and not asread:
        raise ValueError("Invalid File Path to WriteFile")
      elif token >= 2 and token_value == "as":
        asread = True
        asread_token = token
      elif token >= 2 and token_type in ['IDENTIFIER', "STRING", "OPERATOR"] and not asread:
        filepath += " " + token_value
      elif token >= 2 and token_type not in ['IDENTIFIER', "STRING", "OPERATOR"] and not asread:
        raise ValueError("Invalid FilePath in ReadFile")
      elif token == asread_token + 1 and token_type in ['IDENTIFIER', 'STRING'] and asread:
        text = token_value
      elif token == asread_token + 1 and token_type not in ['IDENTIFIER', 'STRING'] and asread:
        raise ValueError("Invalid Text value in writeFile")
      elif token >= asread_token + 1 and token_type in ['IDENTIFIER', 'STRING'] and asread:
        text += " " + token_value
      elif token >= asread_token + 1 and token_type not in ['IDENTIFIER', 'STRING'] and asread:
        raise ValueError("Invalid Text value in writeFile")
        
      tokens_checked += 1

    WriteFileObj = WriteFileObject()
    self.transpiled_code += WriteFileObj.transpile(self.indents, filepath, text)
    self.token_index += tokens_checked + 1
  
