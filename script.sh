printf "\nSample 1 Input: Completely Valid Input\n"
printf "{\"name\": \"John Doe\", \"age\": 30,\"isStudent\": false, \"grades\": [85, 90, 78], \"address\": { \"street\": \"123 Main St\",  \"city\": \"Anytown\"}}\n\n"
printf "Sample 1 Expected Output:\n" 
printf "[<LBRACE, {>, <STRING, name>, <COLON, :>, <STRING, John Doe>, <COMMA, ,>, <STRING, age>, <COLON, :>, <NUMBER, 30>, <COMMA, ,>, <STRING, isStudent>, <COLON, :>, <KEYWORD, false>, <COMMA, ,>, <STRING, grades>, <COLON, :>, <LBRACK, [>, <NUMBER, 85>, <COMMA, ,>, <NUMBER, 90>, <COMMA, ,>, <NUMBER, 78>, <RBRACK, ]>, <COMMA, ,>, <STRING, address>, <COLON, :>, <LBRACE, {>, <STRING, street>, <COLON, :>, <STRING, 123 Main St>, <COMMA, ,>, <STRING, city>, <COLON, :>, <STRING, Anytown>, <RBRACE, }>, <RBRACE, }>]\n\n"
printf "Sample 1 Actual Output:\n"
python lexer.py '{"name": "John Doe", "age": 30,"isStudent": false, "grades": [85, 90, 78],  "address": { "street": "123 Main St",   "city": "Anytown"}}'

printf '......................................................................................\n\n'

printf "Sample 2 Input: Handling Keywords with Non-alphabetical Errors\n"
printf '{"name": "John Doe", "age": 30, "isStudent": fal se,"isGraduating": tru3e,"graduationDate": nu4ll}\n\n'
printf 'Sample 2 Expected Output:\n'
printf '[<LBRACE, {>, <STRING, name>, <COLON, :>, <STRING, John Doe>, <COMMA, ,>, <STRING, age>, <COLON, :>, <NUMBER, 30>, <COMMA, ,>, <STRING, isStudent>, <COLON, :>, <KEYWORD, false>, <COMMA, ,>, <STRING, isGraduating>, <COLON, :>, <KEYWORD, true>, <COMMA, ,>, <STRING, graduationDate>, <COLON, :>, <KEYWORD, null>, <RBRACE, }>]\n\n'
printf "Sample 2 Actual Output:\n"
python lexer.py '{"name": "John Doe", "age": 30, "isStudent": fal se,"isGraduating": tru3e,"graduationDate": nu4ll}'

printf '......................................................................................\n\n'

printf "Sample 3 Input: Handling Leading Decimals in Number Tokens\n"
printf '{ "name": "John Doe", "age": 30, "grades": [.85, .9], "balances due": [-.80, -10.50]}\n\n'
printf "Sample 3 Expected Output:\n"
printf "[<LBRACE, {>, <STRING, name>, <COLON, :>, <STRING, John Doe>, <COMMA, ,>, <STRING, age>, <COLON, :>, <NUMBER, 30>, <COMMA, ,>, <STRING, grades>, <COLON, :>, <LBRACK, [>, <NUMBER, 0.85>, <COMMA, ,>, <NUMBER, 0.9>, <RBRACK, ]>, <COMMA, ,>, <STRING, balances due>, <COLON, :>, <LBRACK, [>, <NUMBER, -0.80>, <COMMA, ,>, <NUMBER, -10.50>, <RBRACK, ]>, <RBRACE, }>] \n\n"
printf "Sample 3 Output:\n"
python lexer.py '{ "name": "John Doe", "age": 30, "grades": [.85, .9], "balances due": [-.80, -10.50]}'

printf '......................................................................................\n\n'

printf "Sample 4 Input: Handling Leading 0s in Number Tokens\n"
printf '{ "name": "John Doe", "age": 000030, "grades": [85.7, 002.9, 000.0], "balances due": [-078, -005.90]}\n\n'
printf "Sample 4 Expected Output:\n"
printf 'Sample 4 Actual Output:\n'
printf '[<LBRACE, {>, <STRING, name>, <COLON, :>, <STRING, John Doe>, <COMMA, ,>, <STRING, age>, <COLON, :>, <NUMBER, 30>, <COMMA, ,>, <STRING, grades>, <COLON, :>, <LBRACK, [>, <NUMBER, 85.7>, <COMMA, ,>, <NUMBER, 2.9>, <COMMA, ,>, <NUMBER, 0.0>, <RBRACK, ]>, <COMMA, ,>, <STRING, balances due>, <COLON, :>, <LBRACK, [>, <NUMBER, -78>, <COMMA, ,>, <NUMBER, -5.90>, <RBRACK, ]>, <RBRACE, }>\n\n'
python lexer.py '{ "name": "John Doe", "age": 000030, "grades": [85.7, 002.9, 000.0], "balances due": [-078, -005.90]}'

printf '......................................................................................\n\n'

printf "Sample 5 Input: Handling Miscallaneous Alphanumerical Characters Placed in Invalid Position:\n"
printf '{ "name": "John Doe",  "age": 30a0,  "isStudent": false,  "grades": [85, 90, 78]}\n\n'
printf "Sample 5 Expected Output:\n"
printf '[<LBRACE, {>, <STRING, name>, <COLON, :>, <STRING, John Doe>, <COMMA, ,>, <STRING, age>, <COLON, :>, <NUMBER, 30>]\n\n'
printf "Sample 5 Actual Output:\n"
python lexer.py '{ "name": "John Doe",  "age": 30a0,  "isStudent": false,  "grades": [85, 90, 78]}'
