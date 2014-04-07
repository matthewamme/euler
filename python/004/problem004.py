"""
Project Euler Problem #004

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import math,sys

def ispalin(n):
    r = str(n)
    for i in range (0,len(r)):
       if (r[i] != r[len(r)-1-i]):
         return 0;
    else:
      return 1;

a=0
for x in range(1,999):
   for y in range (1,999):
      if (ispalin(x*y) and x*y>a):
         a = x*y

print a
