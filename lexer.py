from collections import deque
import sys
class Token:
  def __init__(self, type, value):
    self.type = type
    self.value = value
  
  def __repr__(self):
    return f'<{self.type}, {self.value}>'

class Lexer:
  def __init__(self, input_string):
    self.input = input_string
    self.pointer = 0
    self.tokens = []


  def scan(self):
    while self.pointer < len(self.input):
      char = self.input[self.pointer]

      if char in ['{', '}', '[', ']', ':', ',']:
        self.handle_single_character(char)
      
      elif char.isdigit() or (char == '.' and self.input[self.pointer + 1].isdigit()): 
        self.handle_number()
      
      elif char == '-':
        self.handle_number(is_neg=True)
      
      elif char == '"':
        self.handle_string()

      elif char.isalpha():
        self.handle_keyword()

      elif char.isspace():
        self.pointer += 1
      
      else: 
        self.handle_error()
        return

    return self.tokens
  
  def handle_single_character(self, char):
    token_type = {
      '{': 'LBRACE',
      '}': 'RBRACE',
      '[': 'LBRACK',
      ']': 'RBRACK',
      ':': 'COLON',
      ',': 'COMMA',
    }[char]

    self.tokens.append(Token(token_type, char))
    self.pointer += 1
  
  def handle_number(self, is_neg=False):
    num_str = deque()
    decimal = False

    if is_neg:
      num_str.append('-')
      self.pointer += 1
      if self.input[self.pointer] == '.' and self.input[self.pointer + 1].isdigit():
        num_str.append('0')
        num_str.append('.')
        self.pointer += 1
        decimal = True
    
    if self.input[self.pointer] == '.' and self.input[self.pointer + 1].isdigit():
      num_str.append('0')
      num_str.append('.')
      self.pointer += 1
      decimal = True
    
    while self.pointer < len(self.input) and self.input[self.pointer].isdigit() or self.input[self.pointer] == '.':
        if self.input[self.pointer] == '.' and decimal:
          self.pointer += 1
        if self.input[self.pointer] == '.' and not decimal:
          num_str.append(self.input[self.pointer])
          decimal = True
          self.pointer += 1
        
        else:
          num_str.append(self.input[self.pointer])
          self.pointer += 1
    
    if is_neg:
      num_str.popleft()
      while num_str[0] == '0' and len(num_str) > 1 and num_str[1] != '.':
        num_str.popleft()
      num_str.appendleft('-')
    else:
      while num_str[0] == '0' and len(num_str) > 1 and num_str[1] != '.':
        num_str.popleft()
        
    non_zero = False
    if is_neg:
      for i in range(1, len(num_str)):
        if num_str[i] != '0' or num_str[i] != '.':
          non_zero = True
    
    if is_neg and not non_zero:
      num_str.popleft()
  
    self.tokens.append(Token('NUMBER', ''.join(num_str)))
  
  def handle_string(self):
    # iterate past starting quote
    self.pointer += 1
    string_contents = []
    while self.pointer < len(self.input) and self.input[self.pointer] != '"':
      if self.input[self.pointer] == '\\' or self.input[self.pointer] == '\r' or self.input[self.pointer] == '\n':
        # upon invalid character, just ignore it
        self.pointer += 1

      else:
        # upon valid character, append
        string_contents.append(self.input[self.pointer])
        self.pointer += 1

    self.pointer += 1 # skip the closing pointer

    self.tokens.append(Token('STRING', ''.join(string_contents)))
  
  def handle_keyword(self):
    keyword_str = []

    # iterate through keyword
    while self.pointer < len(self.input) and self.input[self.pointer].isalpha() or self.input[self.pointer].isspace() or self.input[self.pointer].isdigit():
      # upon valid character, append
      if self.input[self.pointer].isalpha():
        keyword_str.append(self.input[self.pointer])
      self.pointer += 1

    keyword = ''.join(keyword_str)

    # check if valid keyword
    if keyword in ['true', 'false', 'null']:
      self.tokens.append(Token('KEYWORD', keyword))
    else:
      self.handle_error(type="KEYWORD")
      return
    
  def handle_error(self, type=None):
    print(self.tokens)
    if type:
      print(f'\nInvalid {type} at index {self.pointer}\n')
    else:
      print(f'\nInvalid character \'{self.input[self.pointer]}\' at index {self.pointer}\n')
    sys.exit(1)

def main():
  # read input string from command line
  lexer = Lexer(sys.argv[1])
  # tokens = lexer.scan()
  # print(tokens)      

main()
  