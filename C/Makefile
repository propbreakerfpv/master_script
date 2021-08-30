main: main.o parce.o
	gcc main.o parce.o -o main

main.o: src/main.c
	gcc -c src/main.c -o main.o

parce.o: src/parcer/parce.c line.o section.o token.o
	gcc -c src/parcer/parce.c line.o section.o token.o -o parce.o

line.o: src/structs/line.c
	gcc -c src/structs/line.c -o line.o

section.o: src/structs/section.c
	gcc -c src/structs/section.c -o section.o

token.o: src/structs/token.c
	gcc -c src/structs/token.c -o token.o

clean:
	rm *.o





#main:main.o parce.o
#	gcc main.o parce.o -o main
#
#main.o: src/main.c
#	gcc -c src/main.c -o main.o
#
#parce.o: src/parcer/parce.c token.o section.o line.o
#	gcc -c -l src/parcer/parce.c token.o section.o line.o -o parce.o
#
##parce.o: src/parcer/parce.c
##	gcc -c src/parcer/parce.c -o parce.o
#
#token.o: src/structs/token.c
#	gcc -c src/structs/token.c -o token.o
#
#section.o: src/structs/section.c
#	gcc -c src/structs/section.c -o section.o
#
#line.o: src/structs/line.c
#	gcc -c src/structs/line.c -o line.o
#
#clean:
#	rm *.o
