"""
Todo:
    error handling
    and basicly evrything

mabe to many classes?


"""

from to_asm import *
from error import *

class Token():

    def __init__(self, type, value, line, row):
        self.type = type
        self.value = value
        self.line = line
        self.row = row

    def print(self):
        print(self.value)

class Var(Token): # any refrence to a variable
    pass

class VarDef(Token): # key word 'var' for defining variables
    pass

class Equals(Token): # simble '=' for assining values and compareing if dubled
    pass

class Newline(Token): # new line char '\n'
    pass

class Exp(Token): # expretion any section of code that returns a value
                  # exaple: '5 + 3' or 'variable + function() / 2'
                  # here function wold have to return a value otherwise this expretion
                  # wold return null
    pass


def get_file(file_path): # reads from a file
    file = open(file_path, "r")
    code = file.read()
    file.close()
    return code

def file_out(cont, file_path): # writes to a file
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
    error = Error()
    toke = ""
    tokes = []
    last_toke = ""
    data = False
    for i in code: # loop though all the chars in are code
        if( i == '"' or i == "'") and not data:
            data = True
        elif i == '"' or i == "'":
            data = False
        if (white_space(i) != "null" or i == ";") and (not data): # end the token and remove white space
            if toke != "": tokes.append(toke)
            if i == ";":  tokes.append("\n;") # append new line chars
            if i == "\n" and last_toke != ";": tokes.append("\n")# cheack for ";"
            toke = ""
            last_toke = i
            continue

        # update last_toke and toke
        last_toke = i
        toke += i

    # make tokens into objects
    tokens = []
    line = 1
    skip = -1
    expretion = False
    i = 0
    for t in tokes: # loop though all the token and make token objects
        if skip < i: # skip is used if a case handals more than one token

            if t == "var": # handles two tokens
                vardef = VarDef("vardef", "var", 0, 0)
                tokens.append(vardef)
                skip = i + 1
                var = Var("var", tokes[i+1], 0, 0)
                tokens.append(var)
                expretion = True
            elif tokes[i-3] == "var" and expretion == True: # variable asinment
                #(t[0] == "0" or t[0] == "1" or t[0] == "2" or t[0] == "3" or t[0] == "4" or t[0] == "5" or t[0] == "6" or t[0] == "7" or t[0] == "8" or t[0] == "9") and expretion == True:
                exp = Exp("exp", t, 0, 0)
                tokens.append(exp)
            elif t == "=":
                equals = Equals("equals", "=", 0, 0)
                tokens.append(equals)
            elif t == "\n" or t == "\n;":
                if t == "\n":
                    error.error("missing ';'",str(line))
                new = Newline("newline", "\n", 0, 0)
                tokens.append(new)
                expretion = False
                line = line + 1
            else:
                error.error("unknown token", line)
        i = i + 1
    return tokens



def main(): # main function
    error = Error()
    code = get_file("test.ms") # read code from file

    tokens = get_tokens(code) # genarate tokens

    asm = genarate_asm(tokens) # genarate assembly

    file_out(asm, "t.asm") # write asm to file

if __name__ == "__main__":
    main()
