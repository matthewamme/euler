"""
Project Euler Problem #005

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

import math,sys

def isdivis(n):
    for i in range (11,20):
       if (n%i != 0):
         return 0
    else:
      return 1

#Start a number divisble by all primes (and largest divisor), reduces runtime
i=20*19*17*13*11*7*5*3*2

while(1):
   if (isdivis(i)):
      print i
      sys.exit()
   i+=20
