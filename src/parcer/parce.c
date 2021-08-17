#include "parce.h"

Token** parce(char* code){
  int i = 0;
  while (code[i] != '\0') {
    printf("%c\n", code[i]);
    i++;
  }
}
