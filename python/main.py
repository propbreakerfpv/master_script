"""
Todo:
    error handling
    and basicly evrything

mabe to many classes?


"""

from to_asm import *

class Token():

    def __init__(self, type, value, line, row):
        self.type = type
        self.value = value
        self.line = line
        self.row = row

    def print(self):
        print(self.value)

class Var(Token):
    pass

class VarDef(Token):
    pass
'''class String(Token):
    pass
class Char(Token):
    pass
class Int(Token):
    pass
class Float(Token):
    pass
'''

class Equals(Token):
    pass

class Newline(Token):
    def print(self):
        print("\\n")

#####################
#### Expretion ######
#####################
class Ex(Token):
    pass
class Expretion(Token):
    pass
class ExpInt(Expretion):
    pass
class ExpString(Expretion):
    pass
class ExpFloat(Expretion):
    pass
class ExpChar(Expretion):
    pass

def get_file(file_path): # reads for a file
    file = open(file_path, "r")
    code = file.read()
    file.close()
    return code

def file_out(cont, file_path):
    file = open(file_path, "w")
    file.write(cont)
    file.close()


def white_space(char): # retirns the type of white space
    match char:
        case "\n":
            return "nl"
        case "\t":
            return "t"
        case " ":
            return "s"
        case unknown_command:
            return "null"

def get_tokens(code): # divids the code into tokens
    toke = ""
    tokes = []
    last_toke = ""
    # loop though all the chars in are code
    data = False
    for i in code:
        if( i == '"' or i == "'") and not data:
            data = True
        elif i == '"' or i == "'":
            data = False
        if (white_space(i) != "null" or i == ";") and (not data): # end the token and remove white space
            if toke != "": tokes.append(toke)
            if i == ";":  tokes.append("\n") # append new line chars
            if i == "\n" and last_toke != ";": # cheack for ";"
                print("[ERROR] needed ';'") # error handling needed
            toke = ""
            last_toke = i
            #print("white_space")
            continue

        # update last_toke and toke
        last_toke = i
        toke += i

    # make tokens into objects
    tokens = []
    skip = -1
    expretion = False
    '''for s in tokes
        print(s.value)'''
    i = 0
    for t in tokes: # loop though all the token and make token objects
        if skip < i: # skip is used if a case handals more than one token

            if t == "var":
                vardef = VarDef("vardef", "var", 0, 0)
                tokens.append(vardef)
                skip = i + 1
                var = Var("var", tokes[i+1], 0, 0)
                tokens.append(var)
                expretion = True
            elif tokes[i-3] == "var" and expretion == True:
                #(t[0] == "0" or t[0] == "1" or t[0] == "2" or t[0] == "3" or t[0] == "4" or t[0] == "5" or t[0] == "6" or t[0] == "7" or t[0] == "8" or t[0] == "9") and expretion == True:
                ex = Ex("ex", t, 0, 0)
                tokens.append(ex)
                print()
            elif t == "=":
                equals = Equals("equals", "=", 0, 0)
                tokens.append(equals)
            elif t == "\n":
                new = Newline("newline", "\n", 0, 0)
                tokens.append(new)
                expretion = False
            else:
                print("unknown token")
        i = i + 1
    return tokens



def main(): # main function
    code = get_file("test.ms")

    tokens = get_tokens(code)
    '''for i in tokens:
        i.print()'''

    asm = genarate_asm(tokens)
    file_out(asm, "t.asm")
main()
