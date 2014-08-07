#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int sum, i;

int N=100;

size_t len(const char *a) {
  return strlen(a);
}

int main () {

  const char *p = NULL;

  for(i=1; i< N; i++) {
    sum = sum + i ;
  }
  printf ("size of a = %d\n", len(p));

  std::cout<<sum;
  std::cout<<sum/NULL;
}
