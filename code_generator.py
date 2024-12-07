from parser import ObjectNode, ArrayNode, PairNode, ValueNode, ASTNode, Parser
from lexer import Lexer
import sys
class CodeGenerator:
    def convert(self, node):
        if isinstance(node, ObjectNode):
            return self.convert_object(node)
        elif isinstance(node, ArrayNode):
            return self.convert_array(node)
        elif isinstance(node, PairNode):
            return self.convert_pair(node)
        elif isinstance(node, ValueNode):
            return self.convert_value(node)
        else:
            raise ValueError(f"Unsupported node type: {type(node)} in code generation phase")

    def convert_object(self, node):
        # convert object members (key-value pairs) into a dictionary
        return {key: value for key, value in (self.convert(member) for member in node.members)}

    def convert_array(self, node):
        # convert array elements into a list
        return [self.convert(element) for element in node.elements]

    def convert_pair(self, node):
        # PairNode has a key and a value, return as a tuple for use in a dictionary
        key = node.key
        value = self.convert(node.value)
        return key, value

    def convert_value(self, node):
        # directly return the value for ValueNode, recursively convert if it's another AST node
        # print("node value: ", node.value, type(node.value))
        if isinstance(node.value, ASTNode):
            return self.convert(node.value)
        elif isinstance(node.value, str):
            if node.value == "true":
                return True
            elif node.value == "false":
                return False
            elif node.value == "null":
                return None
            else:
                # retain as string for regular strings
                return node.value  
        elif isinstance(node.value, (int, float)):
            # print("HELLO")
            # retain numeric values
            return node.value  
        else:
            # retain other values
            return node.value  


# def main():
#     lexer = Lexer(sys.argv[1])
#     try:
#         tokens = lexer.scan()
#         # print("tokens", tokens)
#         parser = Parser(tokens)
#         ast = parser.parse()

#         code_generator = CodeGenerator()
#         result = code_generator.convert(ast)
#         print(result)  
#     catch:
#         print(f"Syntax Error: {e}")

def main():
    lexer = Lexer(sys.argv[1])
    try:
        tokens = lexer.scan()
        parser = Parser(tokens)
        ast = parser.parse()

        code_generator = CodeGenerator()
        result = code_generator.convert(ast)
        print(result)
    except SyntaxError as e:
        print(f"Syntax Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


main()
