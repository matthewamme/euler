/*
 * Project Euler
 * Matt Amme
 * Problem 001
 * Find the sum of all the multiples of 3 or 5 below 1000.
 */

#include <stdio.h>
#include <stdlib.h>

int main (void){
   int i,t = 0;

   for( i=1 ; i < 1000 ; i++ ){
      if (i % 3 == 0 | i % 5 == 0)
         t += i;
   }
   printf("%d\n",t);
  return 0;
}
