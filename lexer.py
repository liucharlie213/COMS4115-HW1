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
      elif char.isdigit() or char == '-':
        self.handle_number()
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
  
  def handle_number(self):
    start = self.pointer
    while self.pointer < len(self.input) and self.input[self.pointer].isdigit() or self.input[self.pointer] == '-':
      print("scanning digit: ", self.input[self.pointer])
      self.pointer += 1
      # pointer is pointer one index beyond the last digit
      number = self.input[start:self.pointer]
    self.tokens.append(Token('NUMBER', number))
  
  def handle_string(self):
    # starts at '"'
    print("handling string")
    start = self.pointer
    self.pointer += 1
    string_contents = []
    while self.pointer < len(self.input) and self.input[self.pointer] != '"':
      print("char: ", self.input[self.pointer])
      if self.input[self.pointer] == '\\' or self.input[self.pointer] == '\r' or self.input[self.pointer] == '\n':
        # upon invalid character, just ignore it
        self.pointer += 1

      else:
        # upon valid character, append
        string_contents.append(self.input[self.pointer])
        self.pointer += 1

    print("string: ", ''.join(string_contents))
    self.pointer += 1 # skip the closing pointer

    self.tokens.append(Token('STRING', ''.join(string_contents)))
  
  def handle_keyword(self):
    print("skipping keyword for now")
    pass

def main():
  print("Hello, World!")
  lexer = Lexer('{"name": "John", "age": 30, "city": "Montana"}')
  tokens = lexer.scan()
  print(tokens)      

main()
  