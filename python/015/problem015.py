"""
Project Euler Problem #015

Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

"""
Sketched what a 3x3 would be on back of envelope, got 20 paths.
This gives :
   n=1 : 2
   n=2 : 6
   n=3 : 20
   ...
This is a pattern inside pascals triangle for the center number in every other
row. Realized this by looking at the number of paths passing through a given edge
node, which gives a pascal triangle formation.

The equation for a location in pascals triangle is:
   n! / (k! * (n-k)!)
   where n = row (starting from 0) and k = index from left of row (starting at 0)

Since we are locating the middle numeral in every other row the equation used is
  (2g)! / (g!)^2
"""

import math,sys

g = 20 #20x20 grid

print math.factorial(2*g)/(math.factorial(g)*math.factorial(g))
