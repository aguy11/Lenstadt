import re

class Lexer(object):
  def __init__(self, code):
    self.source_code = code
    self.tokens = []
  def tokenize(self):
    source = self.source_code.split()
    tokens = []
    source_index = 0
    while source_index < len(source):
      word = source[source_index]
      ##print(word)
      if word[0] == "&":
        begin = "'''"
        alls = ""
        while True:
          source_index += 1
          vql = source[source_index]
          if vql[-1] == "&":
            alls =  "\n" + begin + alls + " " + vql[ : -1] + begin
            break
          else:
            alls = alls + " " + vql
        tokens.append(['COMMENT', alls])
      elif word in ['{', '}']:
        tokens.append(["CASE", word])
      elif word == "<(":
        tokens.append(["CASE", '('])
      elif word == ",":
        tokens.append(['SEPERATOR', ","])
      elif word == ")>":
        tokens.append(["CASE", ")"])
      elif word == ")>;":
        tokens.append(["CASE", ")"])
        tokens.append(["STATEMENT_END", ";"])
      elif word == "<()>":
        tokens.append(["CASE", "("])
        tokens.append(["CASE", ")"])
      elif word == "/":
        tokens.append(["PASSON", "/"])
      elif word == "#":
        tokens.append(['USE_DELCARATION', "#"])
      elif word == ";":
        tokens.append(["STATEMENT_END", ";"])
      elif word == "(":
        items = []
        activ = False
        cases = {"(": ")"}
        tosee = [")"]
        cntr = 0
        hoe = False
        tobrk = False
        for i in source[source_index + 1:]:
          cntr += 1
          #print(tosee)
          #print(i)
          #print(i == tosee[0] or i == tosee[0] + ";")
          isit = i in cases
          #print(isit)
          if isit:
            #print("Whee")
            items.append(i)
            hoe = True
            tosee.insert(0, cases[i])
          elif i != ")" and i != ");" and i != tosee[0] + ";":
            if not hoe:
              if i[-1] == ",":
                
                items.append(i[:-1])
              else:
                items.append(i)
            else:
              #print("whoopee")
              old_item = items[-1]
              del items[-1]
              items.append(old_item + i)
          elif i == tosee[0] or i == tosee[0] + ";":
            if i == tosee[0]:
              items[-1] = items[-1] + i
            else:
              activ = True
              tobrk = True
            del tosee[0]
            if tobrk:
              break


        trtuple = "("
        for x in items:
          trtuple += f"{x},"
        trtuple = trtuple[:-1]
        trtuple += ")"
        tokens.append(["IDENTIFIER", trtuple])
        if activ:
          tokens.append(['STATEMENT_END', ";"])
        source_index += cntr

      elif word in ["captureStr", "captureInt", "captureBool", "captureFloat"]:
        if word == "captureStr":
          strt = "input("
          paras = 1
        elif word == "captureInt":
          strt = "int(input("
          paras = 2
        elif word == "captureFloat":
          strt = "float(input("
          paras = 2
        elif word == "captureBool":
          strt = "bool(input("
          paras = 2
        whole_vals = ""
        nums = 0

        while True:
          nums += 1
          if source[source_index + nums][-1] == ";":
            whole_vals = whole_vals + " " + source[source_index + nums][ : -1]
            nums += 1
            break
          else:
            whole_vals = whole_vals +  " " + source[source_index + nums]
        whole = strt + whole_vals[1 : ]
        for o in range(paras):
          whole = whole + ")"
        tokens.append(["IDENTIFIER", whole])
        tokens.append(["STATEMENT_END", ";"])
        source_index += (nums - 1)
      
      elif word in ['==', "/", "+=", "-=", "-", "+", "*", "<", ">", "<=", ">=", "!=", "or", "and", "in", "not", "=", "**"]:
        tokens.append(["OPERATOR", word])
      elif word in ['True', 'False'] or word[ : -1] in ['True', 'False']:
        if word[-1] == ";":
          tokens.append(['BOOL', word[ : -1]])
          tokens.append(["STATEMENT_END", ";"])
        else:
          tokens.append(['BOOL', word])
      
      elif re.match("[a-z]", word.lower()):
        ###print("Hey: " + i)
        if word[-1] == ";" and word[0] != '"':
          if len(word) != 2:
            tokens.append(["IDENTIFIER", word[ : -1]])
          else:
            tokens.append(["IDENTIFIER", word[0]])
          tokens.append(["STATEMENT_END", ";"])
        else:
          tokens.append(["IDENTIFIER", word])
      elif re.match('[0-9]', word) or re.match('[0-9]', word):
        if word[-1] == ";":
          if len(word) != 2:
            tokens.append(["INTEGER", word[ : -1]])
          else:
            tokens.append(["INTEGER", word[0]])
          tokens.append(["STATEMENT_END", ";"])
        else:
          tokens.append(["INTEGER", word])
      elif word[0] in ['"', "'"] and word[-1] == word[0] or word[-2] == word[0]:
        if word[-1] == ";":
          tokens.append(["STRING", word[ :-1]])
          tokens.append(["STATEMENT_END", ";"])
        else:
          tokens.append(["STRING", "f" + word])

      elif word[0] in ['"', "'", "'''"]:
          tr = word[0]
          while True:
            source_index += 1
            ####printsource_index)
            word = word + f" {source[source_index]}"
            if word[-1] == tr or word[-2] == tr:
              ###print"DOING IT: " + i)
              if word[-1] == ";":
                tokens.append(["STRING", "f" + word[ : -1]])
                tokens.append(["STATEMENT_END", ";"])
              else:
                tokens.append(["STRING", "f" + word])
              break
            else:
              continue
    
      source_index += 1
    ##print(tokens)
    return tokens

