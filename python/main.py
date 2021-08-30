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
class String(Token):
    pass
class Char(Token):
    pass
class Int(Token):
    pass
class Float(Token):
    pass


class Equals(Token):
    pass

class Newline(Token):
    def print(self):
        print("\\n")

#####################
#### Expretion ######
#####################
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
    return code


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
    for i in code:
        if white_space(i) != "null" or i == ";": # end the token and remove white space
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
    print(tokes)
    tokens = []
    skip = -1
    expretion = False
    i = 0
    for t in tokes:
        if skip < i:
            if t == "int":
                var = Var("int", "int", 0, 0)
                tokens.append(var)
                skip = i + 1
                int = Int("intv", tokes[i+1], 0, 0)
                tokens.append(int)
                expretion = True
            elif t == "float":
                var = Var("float", "float", 0, 0)
                tokens.append(var)
                skip = i + 1
                float = Float("floatv", tokes[i+1], 0, 0)
                tokens.append(float)
                expretion = True
            elif t == "char":
                var = Var("char", "char", 0, 0)
                tokens.append(var)
                skip = i + 1
                char = Char("charv", tokes[i+1], 0, 0)
                tokens.append(char)
                expretion = True
            elif t == "string":
                var = Var("string", "string", 0, 0)
                tokens.append(var)
                skip = i + 1
                string = String("stringv", tokes[i+1], 0, 0)
                tokens.append(string)
                expretion = True
            elif (t[0] == "0" or t[0] == "1" or t[0] == "2" or t[0] == "3" or t[0] == "4" or t[0] == "5" or t[0] == "6" or t[0] == "7" or t[0] == "8" or t[0] == "9") and expretion == True and "." not in t:
                expint = ExpInt("expint", t, 0, 0)
                tokens.append(expint)
            elif (t[0] == "0" or t[0] == "1" or t[0] == "2" or t[0] == "3" or t[0] == "4" or t[0] == "5" or t[0] == "6" or t[0] == "7" or t[0] == "8" or t[0] == "9") and expretion == True and "." in t:
                expfloat = ExpFloat("expfloat", t, 0, 0)
                tokens.append(expfloat)
            elif t[0] == "'" and expretion == True:
                expchar = ExpChar("expchar", t, 0, 0)
                tokens.append(expchar)
            elif t[0] == '"' and expretion == True:
                expstring = ExpString("expstring", t, 0, 0)
                tokens.append(expstring)
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

def vars(tokens):
    varlist = {}
    i = 0
    for t in tokens:
        if t.type == "expint":
            varlist[tokens[i-2].value] = t.value
        elif t.type == "expfloat":
            varlist[tokens[i-2].value] = t.value
        i = i + 1
    print(varlist)

def main(): # main function
    code = get_file("test.ms")

    tokens = get_tokens(code)
    for i in tokens:
        i.print()

    print("\n")
    vars(tokens)
main()
