"""
Project Euler Problem #007

What is the 10 001st prime number?
"""

import math,sys

def primelist(n):
   a = []
   b = 1
   x = 2
   while b<=n :
      for i in range (2,x/2+1):
         if (x%i == 0):
            x+=1
            break
      else:
         a.append(x)
         b+=1
         x+=1
   return a


print primelist(10001)[10000]
