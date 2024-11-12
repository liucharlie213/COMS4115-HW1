from lexer import Lexer
import sys

class ASTNode:
    pass

class ObjectNode(ASTNode):
    def __init__(self, members=None):
        self.members = members or []

class ArrayNode(ASTNode):
    def __init__(self, elements=None):
        self.elements = elements or []

class PairNode(ASTNode):
    def __init__(self, key, value):
        self.key = key
        self.value = value

class ValueNode(ASTNode):
    def __init__(self, value):
        self.value = value  # Could be STRING, NUMBER, BOOLEAN, NULL, ObjectNode, or ArrayNode

def print_tree(node, indent=0):
    prefix = " " * (indent * 2)
    if isinstance(node, ObjectNode):
        print(f"{prefix}ObjectNode")
        for member in node.members:
            print_tree(member, indent + 1)
    elif isinstance(node, ArrayNode):
        print(f"{prefix}ArrayNode")
        for element in node.elements:
            print_tree(element, indent + 1)
    elif isinstance(node, PairNode):
        print(f"{prefix}PairNode: {node.key}")
        print_tree(node.value, indent + 1)
    elif isinstance(node, ValueNode):
        print(f"{prefix}ValueNode: {node.value}")

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0  # Tracks current token position

    def current_token(self):
        return self.tokens[self.position]

    def lookahead(self, offset=1):
        """Peek at the upcoming token without consuming it."""
        pos = self.position + offset
        if pos < len(self.tokens):
            return self.tokens[pos]
        return None  # End of tokens

    def consume(self, expected_type=None):
        token = self.current_token()
        print("token: ", token)
        if expected_type and token.type != expected_type:
            raise SyntaxError(f"A Expected {expected_type}, found {token.type}")
            
            
        # print("hello there")
        self.position += 1
        return token

    def parse(self):
        if self.current_token().type == "LBRACE":
            return self.parse_object()  # JSON always starts with an Object in our CFG
        else:
            raise SyntaxError("JSON must start with an object")
  
    def parse_object(self):
        self.consume("LBRACE")
        members = []
        if self.current_token().type != "RBRACE":
            members = self.parse_members()
        self.consume("RBRACE")
        return ObjectNode(members)

    def parse_members(self):
        members = [self.parse_pair()]
        while self.current_token().type == "COMMA" and self.lookahead().type != "STRING":
            self.consume(self.current_token().type)
        while self.current_token().type == "COMMA" and self.lookahead().type == "STRING":
            self.consume("COMMA")
            members.append(self.parse_pair())

        
        print("HI: ", self.current_token(), self.current_token().type)
        if self.current_token() and self.current_token().type not in ("COMMA", "RBRACE"):
            print("in error: ", self.current_token().type)
            raise SyntaxError(f"B Expected ',' or '}}' after key-value pair, found {self.current_token().type}")

        return members

    def parse_pair(self):
        key = self.consume("STRING").value
        # print("key: ", key)
        self.consume("COLON")
        while self.current_token().type == "COLON":
         self.consume("COLON")
        value = self.parse_value()
        return PairNode(key, value)

    def parse_array(self):
        self.consume("LBRACK")
        elements = []
        if self.current_token().type != "RBRACK":
            elements = self.parse_elements()
        self.consume("RBRACK")
        return ArrayNode(elements)

    def parse_elements(self):
        # deal w string followed by comma here
        elements = [self.parse_value()]

        while self.current_token().type != "COMMA" and self.current_token().type != "RBRACK":
            elements.append(self.parse_value())

        while self.current_token().type == "COMMA":
            self.consume("COMMA")
            elements.append(self.parse_value())
        

        # Lookahead to ensure no extra comma at the end of the object
        if self.current_token() and self.current_token().type not in ("COMMA", "RBRACK"):
            raise SyntaxError(f"Expected ',' or ']' after array element, found {self.lookahead().type}")

        return elements

    def parse_value(self):
        token = self.current_token()
        if token.type == "STRING":
            self.consume("STRING")
            return ValueNode(token.value)
        elif token.type == "NUMBER":
            self.consume("NUMBER")
            return ValueNode(token.value)
        elif token.type == "LBRACE":
            return self.parse_object()
        elif token.type == "LBRACK":
            return self.parse_array()
        elif token.type == "KEYWORD":
            self.consume(token.type)
            return ValueNode(token.value)
        else:
            raise SyntaxError(f"Unexpected token {token.type}")

def main():
    # Read input string from command line
    lexer = Lexer(sys.argv[1])
    tokens = lexer.scan()
    parser = Parser(tokens)
    try:
        ast = parser.parse()
        print_tree(ast)
    except SyntaxError as e:
        print(f"Syntax Error: {e}")

main()

# from lexer import Lexer
# import sys
# class ASTNode:
#   pass

# class ObjectNode(ASTNode):
#   def __init__(self, members=None):
#       self.members = members or []

# class ArrayNode(ASTNode):
#   def __init__(self, elements=None):
#       self.elements = elements or []

# class PairNode(ASTNode):
#   def __init__(self, key, value):
#       self.key = key
#       self.value = value

# class ValueNode(ASTNode):
#   def __init__(self, value):
#       self.value = value  # Could be STRING, NUMBER, BOOLEAN, NULL, ObjectNode, or ArrayNode

# def print_tree(node, indent=0):
#     prefix = " " * (indent * 2)
#     if isinstance(node, ObjectNode):
#         print(f"{prefix}ObjectNode")
#         for member in node.members:
#             print_tree(member, indent + 1)
#     elif isinstance(node, ArrayNode):
#         print(f"{prefix}ArrayNode")
#         for element in node.elements:
#             print_tree(element, indent + 1)
#     elif isinstance(node, PairNode):
#         print(f"{prefix}PairNode: {node.key}")
#         print_tree(node.value, indent + 1)
#     elif isinstance(node, ValueNode):
#         print(f"{prefix}ValueNode: {node.value}")

# class Parser:
#   def __init__(self, tokens):
#       self.tokens = tokens
#       self.position = 0  # Tracks current token position

#   def current_token(self):
#       return self.tokens[self.position]

#   def consume(self, expected_type=None):
#       token = self.current_token()
#       if expected_type and token.type != expected_type:
#           # handle error using lookahead

#           raise SyntaxError(f"Expected {expected_type}, found {token.type}")
#       self.position += 1
#       return token

#   def parse(self):
#     if self.current_token().type == "LBRACE":
#       return self.parse_object()  # JSON always starts with an Object in our CFG
#     else:
#         raise SyntaxError("JSON must start with an object")
  

#   def parse_object(self):
#       self.consume("LBRACE")
#       members = []
#       if self.current_token().type != "RBRACE":
#           members = self.parse_members()
#       self.consume("RBRACE")
#       return ObjectNode(members)

#   def parse_members(self):
#       members = [self.parse_pair()]
#       while self.current_token().type == "COMMA":
#           self.consume("COMMA")
#           members.append(self.parse_pair())
#       return members

#   def parse_pair(self):
#       key = self.consume("STRING").value
#       self.consume("COLON")
#       value = self.parse_value()
#       return PairNode(key, value)

#   def parse_array(self):
#       self.consume("LBRACK")
#       elements = []
#       if self.current_token().type != "RBRACK":
#           elements = self.parse_elements()
#       self.consume("RBRACK")
#       return ArrayNode(elements)

#   def parse_elements(self):
#       elements = [self.parse_value()]
#       while self.current_token().type == "COMMA":
#           self.consume("COMMA")
#           elements.append(self.parse_value())
#       return elements

#   def parse_value(self):
#       token = self.current_token()
#       print("token: ", token)
#       if token.type == "STRING":
#           self.consume("STRING")
#           return ValueNode(token.value)
#       elif token.type == "NUMBER":
#           self.consume("NUMBER")
#           return ValueNode(token.value)
#       elif token.type == "LBRACE":
#           return self.parse_object()
#       elif token.type == "LBRACK":
#           return self.parse_array()
#       elif token.type == "KEYWORD":
#           self.consume(token.type)
#           return ValueNode(token.value)
#       else:
#           raise SyntaxError(f"Unexpected token {token.type}")

# def main():
#     # read input string from command line
#     lexer = Lexer(sys.argv[1])
#     tokens = lexer.scan()
#     print("token: ", tokens)
#     parser = Parser(tokens)
#     ast = parser.parse()
#     print_tree(ast)

# main()