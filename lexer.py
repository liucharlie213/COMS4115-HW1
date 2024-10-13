from collections import deque
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
    # print("IM SCANNING")
    print('input string: ', self.input)
    while self.pointer < len(self.input):
      char = self.input[self.pointer]
      print("scanning char: ", char)

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
        # explore this more
        self.handle_error()

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
    print("hello")
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
          print("hi")
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
    
    print('num str: ', num_str)
    
    all_zeros = True
    if is_neg:
      for i in range(1, len(num_str)):
        if num_str[i] != '0' or num_str[i] != '.':
          all_zeros = False
          break
    
    if is_neg and all_zeros:
      num_str.popleft()
      
    # if len(num_str) == 2 and num_str[0] == '-' and num_str[1] == '0':
    #   num_str.popleft()
  
    self.tokens.append(Token('NUMBER', ''.join(num_str)))
  
  def handle_string(self):
    # starts at '"'
    # print("handling string")
    start = self.pointer
    self.pointer += 1
    string_contents = []
    while self.pointer < len(self.input) and self.input[self.pointer] != '"':
      # print("char: ", self.input[self.pointer])
      if self.input[self.pointer] == '\\' or self.input[self.pointer] == '\r' or self.input[self.pointer] == '\n':
        # upon invalid character, just ignore it
        self.pointer += 1

      else:
        # upon valid character, append
        string_contents.append(self.input[self.pointer])
        self.pointer += 1

    # print("string: ", ''.join(string_contents))
    self.pointer += 1 # skip the closing pointer

    self.tokens.append(Token('STRING', ''.join(string_contents)))
  
  def handle_keyword(self):
    keyword_str = []
    while self.pointer < len(self.input) and self.input[self.pointer].isalpha() or self.input[self.pointer].isspace() or self.input[self.pointer].isdigit():
      if self.input[self.pointer].isalpha():
        keyword_str.append(self.input[self.pointer])
      self.pointer += 1
    print(keyword_str)
    keyword = ''.join(keyword_str)
    if keyword in ['true', 'false', 'null']:
      self.tokens.append(Token('KEYWORD', keyword))
    else:
      self.handle_error(type="KEYWORD", value=keyword)
    
  def handle_error(self, type=None, value=None):
    print(self.tokens)
    if type and value:
      raise Exception(f'Invalid {type}: {value}')
    raise Exception(f'Invalid character \'{self.input[self.pointer]}\' at index {self.pointer}')

def main():
  print("Hello, World!")
  lexer = Lexer('{"name": "John", "bool": true, "age": -000.0.4, "city": "Montana" "Montana" }')
  tokens = lexer.scan()
  print(tokens)      

main()
  