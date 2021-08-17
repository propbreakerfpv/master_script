#include "parcer/parce.h"

#define SIZEOF_CODE sizeof(code)/sizeof(code[0])

int main(int argc, char const *argv[]) {
  parce("if i == 5");
  return 0;
}
