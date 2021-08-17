#include "readwright.h"

char* read_file(char* filename){
  FILE *file;
  file = fopen(filename, "r");
  if(file == NULL){
    printf("ERROR while opening%s\n", filename);
  }
  while((ch = fgetc(fp)) != EOF)
      printf("%c", ch);

  }
