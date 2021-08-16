#ifndef ADD_H
#define ADD_H

#include <stdio.h>

struct Token siplify(struct Token* expretion);


struct Token{
  char* value;
  char* type;
  char* file;
  int line;
  int row;
};




#endif
