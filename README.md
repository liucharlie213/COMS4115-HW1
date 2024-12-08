# COMS4115-HW1

## Lexical Grammar

LBRACE = {\
RBRACE = }\
LBRACK = [\
RBRACK = ]\
COLON = :\
COMMA = ,\

STRING = “[^”\\\r\n]*” = double quotes, anything BUT what follows ^, double quotes

NUMBER = -?(0 | [1-9][0-9]*)(\.[0-9]+)? = integers, decimals, negatives and no leading 0s 

KEYWORD = true | false | null

Whitespaces = don’t even tokenize, are ignored

## Script Instructions

chmod 755 script.sh if necessary

Run ./script.sh      

### Samples Part 1:

Sample 1: Completely valid input to show the different token types

Sample 2: KEYWORDS contain a few non-alphabetical errors to show that the lexer just skips past the non-alphabetical error and repairs the keyword

Sample 3: Leading decimals are not allowed in NUMBER tokens so the lexer will add a 0 in front of the leading decimal

Sample 4: Leading 0s are also not allowed in NUMBER tokens so the lexer will truncate the excess leading zeros

Sample 5: If the input string has a random alphanumerical character placed in an invalid position the lexer will report the valid tokens tokenized up to that error index and then report the error neatly


# COMS4115-HW2

Walkthrough video: https://youtu.be/AoaUlBJCehU

### Samples Part 2:

Sample 1: Completely valid input to show a AST populated with a variety of data types

Sample 2: JSON objects are populated using key-value pair elements, which are separated by commas. When duplicate commas are found between key-value pairs, the parser eats them up and builds an error-handled AST

Sample 3: Trailing commas that appear behind the final key-value pair element in a JSON object is also processed by the parser and the an error-handled AST is built.

Sample 4: Key-value pairs are separated by colons. When duplicate colons are found within key-value pairs, the parse processees then and builds an error-handled AST

Sample 5: Array value elements are separated by commas. When these commas are missing, the parser deliminates by space and builds an error-handled AST

## CFG
Nontermals:\
JSON\
Object\
Members\
Pair\
Value

Terminals:
LBRACE = {\
RBRACE = }\
LBRACK = [\
RBRACK = ]\
COLON = :\
COMMA = ,\
STRING = as defined in lexical grammar\
NUMBER = as defined in lexical grammar\
KEYWORDS = true, false, null\

JSON → Object

Object → LBRACE RBRACE\
Object → LBRACE Members RBRACE

Members → Pair\
Members → Pair COMMA Members

Pair → STRING COLON Value

Value → STRING\
Value → NUMBER\
Value → Object\
Value → Array\
Value → true\
Value → false\
Value → null

Array → LBRACK RBRACK\
Array → LBRACK Elements RBRACK

Elements → Value\
Elements → Value COMMA Elements

# COMS4115 - HW3
Sample 1: Completely Valid Input to show how an AST with various data types and nesting is generated as a dictionary

Sample 2: Duplicate commas are deleted and then the dictionary is generated as intended

Sample 3: Tokens are formed up to the alphanumerical positional error, the error is reported, then the dictionary is still generated with the error corrected

Sample 4: If a JSON object key-value pair is missing a comma, the parsing error is reported and no dictionary is generated

Sample 5: If an array value in a JSON objects' key-value pair is missing its deliminating commas, the commas are added and the dictionary is generated with the error handled

Sample 6: If a JSON object has duplicate key-value pairs, the duplicate pair is eliminated and the dictionary is generated with unique key-value pairs

## Teammates:

Charles Liu CRL2157\
Markus Tran HT2573
