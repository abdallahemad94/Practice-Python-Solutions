# -*- coding: UTF-8 -*-
"""
Asks the user for a number.
Depending on whether the number is even or odd,
prints out an appropriate message.

@author Abdallah Emad
"""

num = int(input("Enter a number: "))
check = int(input("Enter a number to divide by: "))

typ = "even" if num % 2 == 0 else "odd"
print('%i is %s' % (num, typ))
# Extras:
print('%i is a multiple of 4' % num) if num % 4 == 0 else None

print('%i divides evenly into %i' % (num, check) if num % check == 0
      else '%i does not divides evenly into %i' % (num, check))
