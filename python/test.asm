
section .data:
  text db "as", 10

section .text
  global_start

_start:
  mov rax, 1
  mov rdi, 1
  mov rsi, text
  mov rdx, 14
  syscall

  mov rax, 60
  mov rdi, 0
  syscall
