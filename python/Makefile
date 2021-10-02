test.asm: main.py t.asm
	python3.10 main.py
	nasm -f elf64 t.asm -o t.o
	ld t.o -o t

p:
	nasm -f elf64 t.asm -o t.o
	ld t.o -o t


run:
	./t

clean:
	rm t
	rm t.o
