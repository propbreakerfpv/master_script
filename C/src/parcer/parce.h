#ifndef PARCE_H
#define PARCE_H

#include <stdio.h>

#include "../structs/token.h"
#include "../structs/section.h"
#include "../structs/line.h"

Token** parce(char* code);

#endif
