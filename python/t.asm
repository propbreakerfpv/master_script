section .text
  variable_int db 45
  variable_float db 3.52
  variable_char db 'A', 10
  variablestring db "hello, world", 10
  string db "ok?", 10
  global _start
_start:
  mov rax, 1
  mov rdi, 1
  mov rsi, variablestring
  mov rdx, 13
  syscall
  mov rax, 60
  mov rdi, 0
  syscall
