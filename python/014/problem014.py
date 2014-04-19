"""
Project Euler Problem #014

The following iterative sequence is defined for the set of positive integers:
n = n/2 (n is even)
n = 3n + 1 (n is odd)

Which starting number, under one million, produces the longest chain?
"""

import math,sys

def prob14(n):
   c = 1
   while (n!= 1):
      if (n%2 == 0):
         n = n/2
      else:
         n = 3*n + 1
      c += 1
   return c

long = 0
longn = 0
i= 3
while i != 1000001:
   t = prob14(i)
   if (t > long):
      long = t
      longn = i
   i += 2
print longn
