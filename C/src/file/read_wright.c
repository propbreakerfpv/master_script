#include "readwright.h"

FILE fsetup(char* filename, char* r_w){
  File *file;
  file = fopen(filename, r_w)
  if(file == NULL){
  printf("ERROR while opening%s\n", filename);
  }
  return file;
}


char* read_char_file(FILE file){
  
  fgets()
}
