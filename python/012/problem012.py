"""
Project Euler Problem #012

What is the value of the first triangle number to have over five hundred divisors?
"""

import math,sys

def factor(n):
   a = 2
   #search up to square root, and the double the number of factors
   for x in range (2,int(math.sqrt(n))+1):
      if (n%x == 0):
         if (int(math.sqrt(n)) == x):
            a += 1
         else:
            a += 2
   return a

i=1
while (factor(i*(i+1)/2) < 501):
   factor(i)
   i += 1
print (i*(i+1))/2
