#ifndef LINE_H
#define LINE_H

#include <stdio.h>

typedef struct {
  char* file;
  int line;

  Section sec[32];
}Line;


#endif
