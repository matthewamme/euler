"""
Project Euler Problem #002

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

a = 1
b = 0
c = 0
t = 0

while a < 4000000:
   c = a
   a = a+b
   b = c
   if (a%2 == 0):
      t += a
print t
