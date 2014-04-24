"""
Project Euler Problem #017

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?
"""

import math,sys

def dig2string(n):
   if n == "0":
      return "zero"
   elif n == "1":
      return "one"
   elif n == "2":
      return "two"
   elif n == "3":
      return "three"
   elif n == "4":
      return "four"
   elif n == "5":
      return "five"
   elif n == "6":
      return "six"
   elif n == "7":
      return "seven"
   elif n == "8":
      return "eight"
   elif n == "9":
      return "nine"
   elif n == "10":
      return "ten"
   elif n == "11":
      return "eleven"
   elif n == "12":
      return "twelve"
   elif n == "13":
      return "thirteen"
   elif n == "14":
      return "fourteen"
   elif n == "15":
      return "fifteen"
   elif n == "16":
      return "sixteen"
   elif n == "17":
      return "seventeen"
   elif n == "18":
      return "eighteen"
   elif n == "19":
      return "nineteen"
   elif n == "20":
      return "twenty"
   elif n == "30":
      return "thirty"
   elif n == "40":
      return "forty"
   elif n == "50":
      return "fifty"
   elif n == "60":
      return "sixty"
   elif n == "70":
      return "seventy"
   elif n == "80":
      return "eighty"
   elif n == "90":
      return "ninety"
   elif n == "00":
      return ""
   else:
      return n

def num2string(n):
   strnum = str(n)[::-1]
   length = len(strnum)
   final = ""
   if length == 3:
      if (strnum[0] == "0" and strnum[1] == "0"):
        final = dig2string(strnum[2]) + " " + "hundred "
      else:
        final = dig2string(strnum[2]) + " " + "hundred and"
   if length >= 2:
      if (strnum[0] == "0" and strnum[1] == "0"):
         final += ""
      elif (strnum[0] == "0" or strnum[1] == "1"):
         final += dig2string(strnum[1] + strnum[0])
      else:
         final += dig2string(strnum[1]+"0") + " " + dig2string(strnum[0])
   else:
      final += dig2string(strnum)
   return final

sum = 11

for i in range (1,1000):
   print i
   print (num2string(i).replace(" ",""))
   sum += len(num2string(i).replace(" ",""))
print sum
