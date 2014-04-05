"""
Project Euler Problem #003

What is the largest prime factor of the number 600851475143 ?
"""

import math

def factor(n):
   a = []
   for x in range (2,int(math.sqrt(n))+1):
      if (n%x == 0):
         a.append(x)
   return a

#Was originally passing a list of primes here, not needed now
def primelist(n):
   a = []
   for x in range (2,n):
      for i in range (2,x/2+1):
         if (x%i == 0):
            break
      else:
         a.append(x)
   return a

def isprime(n):
    r = 0
    for x in range (2,n/2+1):
       if (n%x == 0):
          break
    else:
       r = 1
    return r

b = []
b = factor (600851475143)
print  b
a = 0
for x in b:
   if (isprime(x) == 1):
      a=x
print a
