import re
import random

DL_OP = {'+': 'ADD', '-': 'SUBTRACT', '(': 'PL', ')': 'PI', '*': 'MUL', '^': 'EXPONENT', '&': 'AND', '|': 'OR',
         '/': 'DIVIDE', '//': 'MODULE', ':=': 'ASSIGNMENT', '=': 'EQUAL', '<': 'LESS THAN', '>': 'GREATER THAN',
         '<=': 'LESS THAN OR EAQUL', '>=': 'LESS THAN OR EAQUL', '!=': 'NOT EQUAL', '%': 'END OF LINE', ',': 'vir', }
RS = {'DEFAULT': 'INTEGER TYPE', 'AND': 'REAL TYPE', 'SWITCH': 'WORD TYPE', 'NAMESPACE': 'CHARACTER TYPE',
      'THROW': 'ARRAY TYPE', 'CATCH': 'CONDITIONAL STATEMENTS', 'NEW': 'STATES A LOOP'}
letters = ['~', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sym = []
file = open("E://Assignment-03.txt", "r")
read_file = file.read()
f = read_file.split("\n")
A = ""
B = ""
C = ""
D = ""
pattern = ""
lexeme = ""
token = ("", "")
# col = 0
line = 0
lineLen = 0
next_line = False
state = True
blank = ""
tokens = []
print("--------------------------------------")
print("|            LEXICAL PHASE           |")
print("|            TOKENIZATION            |")
print("--------------------------------------\n")


# we seperate - numbers in negative numbers
def seperator(ch):
    for char in ch:
        if char == "-":
            tokens.append("ABC")
        else:
            tokens.append(char)


# lexical analyzer
# splitting with space and tab and add to a list
while line < len(f):
    my_list = f[line].split()

    lineLen = 0
    while lineLen < len(my_list):
        for ch in my_list:

            i = 0
            if state:
                # check if it is a digit
                if ch in digits:
                    pattern = "DEFAULT"
                    lexeme = int(ch)
                    token = (pattern, lexeme)
                    lineLen += 1

                try:
                    float(ch)
                    # check if it is a decimal number
                    if "." in ch:
                        pattern = "AND"
                        lexeme = float(ch)
                        token = (pattern, lexeme)
                        print(token)
                        seperator(ch)
                        lineLen += 1
                    else:
                        pattern = "DEFAULT"
                        lexeme = int(ch)
                        token = (pattern, lexeme)
                        print(token)
                        seperator(ch)
                        lineLen += 1
                except ValueError:
                    if ch[0] in letters and ch[0:1] != "|.":
                        C = ""
                        if len(ch) > 1 and ch not in RS and (my_list[my_list.index(ch) - 1] != "'" or my_list[
                            my_list.index(ch) + 1] != "'") and ch not in sym:
                            C = C + ch
                            pattern = "ID"  # identifier
                            lexeme = C
                            token = (pattern, lexeme)
                            tokens.append(str(lexeme))
                            print(token)
                            sym.append(ch)
                            lineLen += 1
                        elif my_list[my_list.index(ch) - 1] == "'" and my_list[my_list.index(ch) + 1] == "'" and len(
                                ch) == 1:
                            pattern = "NAMESPACE"  # character
                            lexeme = ch
                            token = (pattern, lexeme)
                            tokens.append(lexeme)
                            print(token)
                            lineLen += 1
                        elif len(ch) == 1 and ch not in sym:
                            pattern = "ID"
                            lexeme = ch
                            token = (pattern, lexeme)
                            tokens.append(lexeme)
                            print(token)
                            sym.append(ch)  # add to symbol table
                            lineLen += 1
                        elif ch in RS:
                            pattern = "RS"  # reserved word
                            lexeme = ch.upper()
                            constant = RS[ch]
                            token = (pattern, lexeme, constant)
                            tokens.append(lexeme)
                            print(token)
                            lineLen += 1
                        elif ch in sym:
                            pattern = "ID"
                            lexeme = ch
                            token = (pattern, lexeme)
                            tokens.append(lexeme)
                            print(token)
                            lineLen += 1
                        else:
                            pattern = "SWITCH"  # word
                            lexeme = ch
                            token = (pattern, lexeme)
                            print(token)
                            lineLen += 1



                    elif ch == "'":
                        pattern = "Quetation"
                        lexeme = ch
                        token = (pattern, lexeme)
                        tokens.append(lexeme)
                        print(token)
                        lineLen += 1
                    elif ch == "|.":
                        state = False
                        A = A + ch
                        pattern = "Comment AND"
                        lexeme = "|."
                        token = (pattern, lexeme)
                        tokens.append(lexeme)
                        print(token)
                        lineLen += 1
                        if ch != ".|":
                            A = A + ch
                            lineLen += 1
                        break

                    elif ch in DL_OP:
                        pattern = "DL_OP"
                        lexeme = ch
                        constant = DL_OP[ch]
                        token = (pattern, lexeme, constant)
                        tokens.append(lexeme)
                        print(token)
                        lineLen += 1
                    elif ch == "||":
                        pattern = "Comment"
                        lexeme = "||"
                        token = (pattern, lexeme)
                        tokens.append(lexeme)
                        print(token)
                        break
                    elif ch.ANDtswith("@") or ch.ANDtswith("!"):
                        pattern = "Error"
                        token = (pattern, ch)
                        tokens.append(lexeme)
                        print(token)
                        lineLen += 1
            elif ch == ".|":
                state = True
                A = A + ch
                pattern = "Comment End"
                lexeme = ".|"
                token = (pattern, lexeme)
                tokens.append(lexeme)
                print(token)

        break
    line += 1

sharp = ("#")
tokens.append(sharp)

# parsing table
table = {}
table[("S'", "|.")] = ['#', 'S']
table[("S'", "||")] = ['#', 'S']
table[("S'", "NAMESPACE")] = ['#', 'S']
table[("S'", "SWITCH")] = ['#', 'S']
table[("S'", "AND")] = ['#', 'S']
table[("S'", "DEFAULT")] = ['#', 'S']
table[("S'", "THROW")] = ['#', 'S']
table[("S'", "NEW")] = ['#', 'S']
table[("S'", "CATCH")] = ['#', 'S']
table[("S'", "#")] = ['#', 'S']

table[("S", "|.")] = ['S', 'T8']
table[("S", "||")] = ['S', 'T8']
table[("S", "NAMESPACE")] = ['S', '%', 'T7']
table[("S", "SWITCH")] = ["S", "%", "T5"]
table[("S", "AND")] = ['S', '%', 'T2']
table[("S", "DEFAULT")] = ['S', '%', 'T2']
table[("S", "THROW")] = ['S', '%', 'T6']
table[("S", "NEW")] = ['S', 'T4']
table[("S", "CATCH")] = ['S', 'T3']
table[("S", "#")] = ["EPSILON"]

table[("T2", "AND")] = ['Expression', ':=', 'ID', 'AND']
table[("T2", "DEFAULT")] = ['Expression', ':=', 'ID', 'DEFAULT']

table[("T3", "CATCH")] = [')', 'CONDITION', '(', 'CATCH']
table[("T4", "NEW")] = [')', 'CONDITION', '(', 'NEW']

table[("Tab", "|.")] = ["EPSILON"]
table[("Tab", "||")] = ["EPSILON"]
table[("Tab", "NAMESPACE")] = ["EPSILON"]
table[("Tab", "SWITCH")] = ["EPSILON"]
table[("Tab", "AND")] = ["EPSILON"]
table[("Tab", "DEFAULT")] = ["EPSILON"]
table[("Tab", "THROW")] = ["EPSILON"]
table[("Tab", "NEW")] = ["EPSILON"]
table[("Tab", "CATCH")] = ["EPSILON"]
table[("Tab", "#")] = ["EPSILON"]

table[("Expression", "0")] = ['E', 'A']
table[("Expression", "1")] = ['E', 'A']
table[("Expression", "2")] = ['E', 'A']
table[("Expression", "3")] = ['E', 'A']
table[("Expression", "4")] = ['E', 'A']
table[("Expression", "5")] = ['E', 'A']
table[("Expression", "6")] = ['E', 'A']
table[("Expression", "7")] = ['E', 'A']
table[("Expression", "8")] = ['E', 'A']
table[("Expression", "9")] = ['E', 'A']
# table[("Expression", "id")] = ['E', 'A']
table[("Expression", "(")] = ['E', 'A']
table[("Expression", "ABC")] = ['E', 'A']

table[("E", "|")] = ["EPSILON"]
table[("E", "&")] = ["EPSILON"]
table[("E", ">")] = ["EPSILON"]
table[("E", "<")] = ["EPSILON"]
table[("E", "=")] = ["EPSILON"]
table[("E", "(")] = ["EPSILON"]
table[("E", ")")] = ["EPSILON"]
table[("E", "+")] = ['E', 'A', '+']
table[("E", "-")] = ['E', 'A', '-']
table[("E", ".")] = ['E', 'A', '.']
table[("E", "%")] = ["EPSILON"]

table[("A", "0")] = ['A1', 'U']
table[("A", "1")] = ['A1', 'U']
table[("A", "2")] = ['A1', 'U']
table[("A", "3")] = ['A1', 'U']
table[("A", "4")] = ['A1', 'U']
table[("A", "5")] = ['A1', 'U']
table[("A", "6")] = ['A1', 'U']
table[("A", "7")] = ['A1', 'U']
table[("A", "8")] = ['A1', 'U']
table[("A", "9")] = ['A1', 'U']
table[("A", "(")] = ['A1', 'U']
table[("A", "ABC")] = ['A1', 'U', 'ABC']

table[("U", "0")] = ['NUMBER', 'D']
table[("U", "1")] = ['NUMBER', 'D']
table[("U", "2")] = ['NUMBER', 'D']
table[("U", "3")] = ['NUMBER', 'D']
table[("U", "4")] = ['NUMBER', 'D']
table[("U", "5")] = ['NUMBER', 'D']
table[("U", "6")] = ['NUMBER', 'D']
table[("U", "7")] = ['NUMBER', 'D']
table[("U", "8")] = ['NUMBER', 'D']
table[("U", "9")] = ['NUMBER', 'D']
table[("U", "(")] = ['NUMBER', 'D']

table[("A1", "|")] = ["EPSILON"]
table[("A1", "&")] = ["EPSILON"]
table[("A1", ">")] = ["EPSILON"]
table[("A1", "<")] = ["EPSILON"]
table[("A1", "=")] = ["EPSILON"]
table[("A1", ")")] = ["EPSILON"]
table[("A1", "(")] = ["EPSILON"]
table[("A1", "*")] = ['A1', 'D', '*']
table[("A1", "^")] = ['A1', 'D', '^']
table[("A1", "//")] = ['A1', 'D', '//']
table[("A1", "/")] = ['A1', 'D', '/']
table[("A1", "+")] = ["EPSILON"]
table[("A1", "-")] = ["EPSILON"]
table[("A1", ".")] = ["EPSILON"]
table[("A1", "%")] = ["EPSILON"]
table[("A1", "-")] = ["EPSILON"]
table[("A1", "ABC")] = ["EPSILON"]

table[("D", "0")] = ["0"]
table[("D", "1")] = ["1"]
table[("D", "2")] = ["2"]
table[("D", "3")] = ["3"]
table[("D", "4")] = ["4"]
table[("D", "5")] = ["5"]
table[("D", "6")] = ["6"]
table[("D", "7")] = ["7"]
table[("D", "8")] = ["8"]
table[("D", "9")] = ["9"]
table[("D", "(")] = [')', 'Expression', '(']

table[("CONDITION", "0")] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", "1")] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", "2")] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", "3")] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", "4")] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", "5")] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", "6")] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", "7")] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", "8")] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", "9")] = ['C', 'Expression', 'OPERATOR', 'Expression']
# table[("CONDITION",  "id")] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", '(')] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", "ABC")] = ['C', 'Expression', 'OPERATOR', 'Expression']

table[("OPERATOR", ">")] = [">"]
table[("OPERATOR", "<")] = ["<"]
table[("OPERATOR", "=")] = ["="]

table[("C", "|")] = ['CONDITION', '|']
table[("C", "&")] = ['CONDITION', '&']
table[("C", ")")] = ["EPSILON"]
table[("C", "(")] = [')', 'CONDITION', '(']

table[("T5", "SWITCH")] = ["WORD", "SWITCH"]

table[("R", ":=")] = ["'", "'", ":="]

table[("T6", "THROW")] = ['K', 'THROW']

table[("K", "SWITCH")] = ['L', 'SWITCH']
table[("K", "AND")] = ['L', 'AND']
table[("K", "DEFAULT")] = ['L', 'DEFAULT']

table[("SIZE", ",")] = ['COMMA', ',']

table[("COMMA", "0")] = ['NUMBER1', 'NUMBER']
table[("COMMA", "1")] = ['NUMBER1', 'NUMBER']
table[("COMMA", "2")] = ['NUMBER1', 'NUMBER']
table[("COMMA", "3")] = ['NUMBER1', 'NUMBER']
table[("COMMA", "4")] = ['NUMBER1', 'NUMBER']
table[("COMMA", "5")] = ['NUMBER1', 'NUMBER']
table[("COMMA", "6")] = ['NUMBER1', 'NUMBER']
table[("COMMA", "7")] = ['NUMBER1', 'NUMBER']
table[("COMMA", "8")] = ['NUMBER1', 'NUMBER']
table[("COMMA", "9")] = ['NUMBER1', 'NUMBER']
table[("COMMA", ",")] = ['NUMBER', 'DIGIT']
table[("COMMA", ",")] = ['NUMBER', 'DIGIT']

table[("NUMBER1", ",")] = ['NUMBER', ',']
table[("NUMBER1", "%")] = ["EPSILON"]

table[("DIGIT", "0")] = ["0"]
table[("DIGIT", "1")] = ["1"]
table[("DIGIT", "2")] = ["2"]
table[("DIGIT", "3")] = ["3"]
table[("DIGIT", "4")] = ["4"]
table[("DIGIT", "5")] = ["5"]
table[("DIGIT", "6")] = ["6"]
table[("DIGIT", "7")] = ["7"]
table[("DIGIT", "8")] = ["8"]
table[("DIGIT", "9")] = ["9"]

table[("NUMBER", "0")] = ['NUMBER', 'DIGIT']
table[("NUMBER", "1")] = ['NUMBER', 'DIGIT']
table[("NUMBER", "2")] = ['NUMBER', 'DIGIT']
table[("NUMBER", "3")] = ['NUMBER', 'DIGIT']
table[("NUMBER", "4")] = ['NUMBER', 'DIGIT']
table[("NUMBER", "5")] = ['NUMBER', 'DIGIT']
table[("NUMBER", "6")] = ['NUMBER', 'DIGIT']
table[("NUMBER", "7")] = ['NUMBER', 'DIGIT']
table[("NUMBER", "8")] = ['NUMBER', 'DIGIT']
table[("NUMBER", "9")] = ['NUMBER', 'DIGIT']

table[("NUMBER", ",")] = ["EPSILON"]
table[("NUMBER", "|")] = ["EPSILON"]
table[("NUMBER", "&")] = ["EPSILON"]
table[("NUMBER", ">")] = ["EPSILON"]
table[("NUMBER", "<")] = ["EPSILON"]
table[("NUMBER", "=")] = ["EPSILON"]
table[("NUMBER", ")")] = ["EPSILON"]
table[("NUMBER", "(")] = ["EPSILON"]
table[("NUMBER", ".")] = ["EPSILON"]
table[("NUMBER", "*")] = ["EPSILON"]
table[("NUMBER", "^")] = ["EPSILON"]
table[("NUMBER", "//")] = ["EPSILON"]
table[("NUMBER", "/")] = ["EPSILON"]
table[("NUMBER", "+")] = ["EPSILON"]
table[("NUMBER", "-")] = ["EPSILON"]
table[("NUMBER", "%")] = ["EPSILON"]

table[("T7", "NAMESPACE")] = ['CHAR', 'NAMESPACE']

table[("T8", "|.")] = [".|", "|."]
table[("T8", "||")] = ["||"]

index = 0
while index < len(sym):
    for i in sym:
        table[("Expression", i)] = ['E', 'A']
        table[("A", i)] = ['A1', 'U']
        table[("U", i)] = ['NUMBER', 'D']
        table[("D", i)] = ["ID"]
        table[("ID", i)] = [i]
        table[("CONDITION", i)] = ['C', 'Expression', 'OPERATOR', 'Expression']
        table[("WORD", i)] = ["R", "ID"]
        table[("L", i)] = ['SIZE', 'ID']
        table[("CHAR", i)] = ['R', 'ID']
        index += 1
    break

print("\n")
print(tokens)
print("\n")


# parser
def parser(tokens, table):
    acceptable = True
    temp = 0
    j = 0
    stack = []
    stack.append("S'")
    while len(stack) > 0:
        top = stack[len(stack) - 1]
        token = tokens[temp]
        if top == token and token != "#":
            stack.pop()
            top = stack[len(stack) - 1]
            temp += 1

        elif top == token and top == "#":
            print("---------------------------------------")
            print("|           PARSING PHASE             |")
            print("|       SYNTAX ANALYSIS PHASE         |")
            print("---------------------------------------")
            print("OUTPUT : INPUT PARSED")
            print(stack)
            print(token)
            print(top)
            break

        else:
            if (top, token) not in table.keys():
                acceptable = False
                break
            elif (top, token) in table:
                states = table[(top, token)]
                stack.pop()
                for char in states:
                    if char != "EPSILON":
                        stack.append(char)
                        top = stack[len(stack) - 1]
                    elif char == "EPSILON":
                        j += 1

    if not acceptable:
        print("---------------------------------------")
        print("|           PARSING PHASE             |")
        print("|       SYNTAX ANALYSIS PHASE         |")
        print("---------------------------------------")
        print("OUTPUT : INPUT NOT PARSED")
        print(stack)
        print(token)
        print(top)


parser(tokens, table)

# Semantic Analysis Phase
print("---------------------------------------------")
print("|          SEMANTIC ANALYSIS PHASE          |")
print("---------------------------------------------")
print("Decleration Statements For This Language")
print("---------------------------------------")
dataTypes = ['DEFAULT', 'NAMESPACE', 'SWITCH', 'AND']
file = open("E://Decleration.txt", "r")
integerr = file.readline()
print(integerr)
characterr = file.readline()
print(characterr)
floatt = file.readline()
print(floatt)
stNEWg = file.readline()
print(stNEWg)
data = [integerr, characterr, floatt, stNEWg]
print("-----------------------------")
print("Current Decleration Statement")
print("-----------------------------")
tok = []
f = random.choice(data)
f = f.replace('\n', '')
tok = f.split(' ')
print(tok, "\n")


def checkk(typee, value):
    if typee == 'DEFAULT' and re.match('^[0-9]+$', value):
        return True
    elif typee == 'SWITCH' and re.match('^"[\w]+"$', value):
        return True
    elif typee == 'NAMESPACE' and re.match('^"[A-Z|a-z]"$', value):
        return True
    elif typee == 'AND' and re.match('[+-]?\d+\.\d+', value):
        return True
    else:
        return False


def main():
    error = False
    flag = True
    i = 0
    namee = ""
    tipe = ""
    while i < len(tok):
        if tok[i] in dataTypes:
            flag = True
            while i < len(tok) and flag == True:
                if tok[i] in dataTypes:
                    tipe = tok[i]
                    i += 1
                else:
                    print("Data Type is not expected but got something else. ")
                    error = True
                    i += 1
                if re.match('^~[a-zA-Z]+$', tok[i]):
                    namee = tok[i]
                    i += 1
                else:
                    print("ERROR: Invalid Variable Name")
                    error = True
                    i += 1
                if tok[i] == ':=':
                    i += 1
                else:
                    print("ERROR: ':=' expected but got something else")
                    error = True
                    i += 1
                if checkk(tipe, tok[i]):
                    tipe = ""
                    i += 1
                else:
                    print("ERROR:", namee, "'s Datatype Mismatch")
                    error = True
                    i += 1
                if tok[i] == '%' or tok[i] == ' ':
                    C=i + 1
                    flag = False
                else:
                    print("ERROR:", namee, "'s Terminator missing")
                    error = True
                    i += 1
        else:
            i += 1
    if (not error):
        print("Declaration statement is correct. No errors found. ")


main()
print()
# Intermediate Code Generator
print("---------------------------------------")
print("|     INTERMEDIATE CODE GENERATOR     |")
print("---------------------------------------")
OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRI = {'+': 1, '-': 1, '*': 2, '/': 2}


### INFIX ===> POSTFIX ###
def infix_to_postfix(formula):
    stack = []  # only pop when the coming op has priority
    output = ''
    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()  # pop '('
        else:
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    # leftover
    while stack:
        output += stack.pop()
    print(f'POSTFIX: {output}')
    return output


### INFIX ===> PREFIX ###
def infix_to_prefix(formula):
    op_stack = []
    exp_stack = []
    for ch in formula:
        if not ch in OPERATORS:
            exp_stack.append(ch)
        elif ch == '(':
            op_stack.append(ch)
        elif ch == ')':
            while op_stack[-1] != '(':
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append(op + b + a)
            op_stack.pop()  # pop '('
        else:
            while op_stack and op_stack[-1] != '(' and PRI[ch] <= PRI[op_stack[-1]]:
                op = op_stack.pop()
                a = exp_stack.pop()
                b = exp_stack.pop()
                exp_stack.append(op + b + a)
            op_stack.append(ch)

    # leftover
    while op_stack:
        op = op_stack.pop()
        a = exp_stack.pop()
        b = exp_stack.pop()
        exp_stack.append(op + b + a)
    print(f'PREFIX: {exp_stack[-1]}')
    return exp_stack[-1]


### THREE ADDRESS CODE GENERATION ###
def generate3AC(pos):
    print("### THREE ADDRESS CODE GENERATION ###")
    exp_stack = []
    t = 1

    for i in pos:
        if i not in OPERATORS:
            exp_stack.append(i)
        else:
            print(f't{t} := {exp_stack[-2]} {i} {exp_stack[-1]}')
            exp_stack = exp_stack[:-2]
            exp_stack.append(f't{t}')
            t += 1


expres = input("INPUT THE EXPRESSION: ")
pre = infix_to_prefix(expres)
pos = infix_to_postfix(expres)
generate3AC(pos)
