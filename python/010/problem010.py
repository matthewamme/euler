"""
Project Euler Problem #010

Find the sum of all the primes below two million.
"""

import math,sys

#extemely ineffecient atm
def primesum(n):
   a = 2 
   b = [2]
   x = 3
   while 1:
      for i in b:
         if (x%i == 0):
            x+=1
            break
      else:
         if (x>n):
            break
         else:
            a += x
            b.append(x)
            x += 2
   return a



#print primesum(200)
#print primesum(200000)
print primesum(2000000)
