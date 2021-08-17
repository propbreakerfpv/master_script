#ifndef TOKEN_H
#define TOKEN_H


#include <stdio.h>

typedef struct {
  char* value;
  char* type;
  char* file;
  int line;
  int row;
}Token;

#endif
