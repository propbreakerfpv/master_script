section .text
  variable_int db 45
  variable_float db 3.52
  variable_char db variable_int
  variablestring db "hello, world", 10
  string db "ok?", 10
  global _start
_start:
  mov 0x0, 0x450
  mov rax, 1
  mov rdi, 1
  mov rsi, 0x0
  mov rdx, 1
  syscall
  mov rax, 60
  mov rdi, 0
  syscall
