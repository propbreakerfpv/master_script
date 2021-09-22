test.asm: test.asm
	nasm -O0 -f elf64 test.asm -o test.o
	ld test.o -o test

make-test:
	python3.10 main.py
	nasm -f elf64 t.asm -o t.o
	ld t.o -o t

run:
	./test

run-test:
	./t
