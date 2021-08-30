#ifndef SECTION_H
#define SECTION_H

#include <stdio.h>

typedef struct {
  char* type; // expretion, definition, other
  int line;
  int row;
  char* file;

  Token tok[32];
}Section;

#endif
