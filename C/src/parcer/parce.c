#include "parce.h"

Token** parce(char* code){
  int i = 0;
  Line line;
  line.file = "main.ms";
  Section sec;
  sec.line = 0;
  sec.row = 0;
  sec.file = "main.ms";
  Token token;
  token.file = "main,ms";
  token.line = 0;
  token.row = 0;
  while (code[i] != '\0') {
    printf("%c\n", code[i]);
    if(code[i] == ' '){
    }
    i++;
  }
}
