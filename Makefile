main: main.o add.o token.o parce.o
	gcc main.o add.o token.o parce.o -o main

main.o: src/main.c
	gcc -c src/main.c -o main.o

add.o: src/testing/add.c
	gcc -c src/testing/add.c -o add.o

token.o: src/token/token.c
	gcc -c src/token/token.c -o token.o

parce.o: src/parcer/parce.c
	gcc -c src/parcer/parce.c -o parce.o

clean:
	rm *.o
