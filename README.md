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

## Teammates:

Charles Liu CRL2157
Markus Tran HT2573

