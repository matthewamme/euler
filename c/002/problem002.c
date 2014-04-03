/*
 * Project Euler
 * Matt Amme
 * Problem 002
 * By considering the terms in the Fibonacci sequence whose values do not exceed
 * four million, find the sum of the even-valued terms.
 * Find the sum of all the multiples of 3 or 5 below 1000.
 */

#include <stdio.h>
#include <stdlib.h>

int main (void){
   int i = 1;
   int j = 0;
   int k = 0;
   int t = 0;
   while( i < 4000000 ){
      k = i;
      i += j;
      j = k;
      if ((i%2) == 0){
         t += i;
      }
   }
  printf("%d\n",t);
  return 0;
}
