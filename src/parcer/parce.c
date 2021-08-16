#include "parce.h"

struct Token** parce(char* code){
  int i = 0;
  while (code[i] != "\0") {
    printf("%s\n", code[i]);

    i++;
  }
}
