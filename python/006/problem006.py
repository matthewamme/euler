"""
Project Euler Problem #006

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

import math,sys

def sumsquares(n):
    t= 0
    for i in range (1,n+1):
      t += i*i
    return t

def squaresums(n):
   t = 0
   for i in range(1,n+1):
      t += i
   return t*t

print  squaresums(100) - sumsquares(100)
