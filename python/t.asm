section .text
  variable_int db 45
  variable_float db 3.52
  variable_char dq 0
  variablestring db "hello, world", 10
  string db "ok?", 10
  global _start
_start:
  push rax
  mov rax, qword[variable_int]
  mov [variable_char], rax
  pop rax
  mov rax, 1
  mov rdi, 1
  mov rsi, variablestring
  mov rdx, 13
  syscall
  mov rax, 60
  mov rdi, 0
  syscall
