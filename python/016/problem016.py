"""
Project Euler Problem #016

What is the sum of the digits of the number 2^1000?
"""

import math,sys

g = 20 #20x20 grid

sum = 0
for a in str(int(math.pow(2,1000))):
   sum += int(a)
print sum
