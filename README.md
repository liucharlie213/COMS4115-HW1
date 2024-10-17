# COMS4115-HW1

## Lexical Grammar

LBRACE = {
RBRACE = }

LBRACK = [
RBRACK = ]

COLON = :
COMMA = ,

STRING = “[^”\\\r\n]*” = double quotes, anything BUT what follows ^, double quotes

NUMBER = -?(0 | [1-9][0-9]*)(\.[0-9]+)? = integers, decimals, negatives and no leading 0s 

KEYWORDS = true | false | null

Whitespaces = don’t even tokenize, are ignored

## Script Instructions

chmod 755 script.sh if necessary

Run ./script.sh      

Sample 1: Completely valid input to show the different token types

Sample 2: KEYWORDS contain a few non-alphabetical errors to show that the lexer just skips past the non-alphabetical error and repairs the keyword

Sample 3: Leading decimals are not allowed in NUMBER tokens so the lexer will add a 0 in front of the leading decimal

Sample 4: Leading 0s are also not allowed in NUMBER tokens so the lexer will truncate the excess leading zeros

Sample 5: If the input string has a random alphanumerical character placed in an invalid position the lexer will report the valid tokens tokenized up to that error index and then report the error neatly

## Teammates:

Charles Liu CRL2157
Markus Tran HT2573

