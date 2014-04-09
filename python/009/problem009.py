"""
Project Euler Problem #009

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math,sys

i = 400 
while (1):
   for x in range (1,i):
      for y in range (1,x):
         if (i*i == x*x + y*y and i + x + y == 1000):
            print i*x*y
            sys.exit()
   i+=1
