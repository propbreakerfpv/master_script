def genarate_asm(tokens):
    i = 0
    out = ""
    out += "section .data\n"
    for t in tokens:
        if t.type == "vardef" and tokens[i+1].type == "var":
            if tokens[i+3].value[0] == '"' or tokens[i+3].value[0] == "'":
                out += "  " + tokens[i+1].value + " db " + tokens[i+3].value + ", 10\n"
            else:
                out += "  " + tokens[i+1].value + " db " + tokens[i+3].value + "\n"
        i = i + 1
    out += "section .text\n"
    out += "  global _start\n"
    out += "_start:\n"
    out += "  mov rax, 1\n"
    out += "  mov rdi, 1\n"
    out += "  mov rsi, variablestring\n"
    out += "  mov rdx, 13\n"
    out += "  syscall\n"
    out += "  mov rax, 60\n"
    out += "  mov rdi, 0\n"
    out += "  syscall\n"
    return out
