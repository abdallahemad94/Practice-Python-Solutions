# -*- coding: utf-8 -*-
"""
Asks the user for a string and print out whether this string is a
palindrome or not.

Created on Thu Mar  1 22:49:48 2018

@author: Abdallah Emad
"""

word = input('Please enter a word: ')
print('Great!, the word {0} is palindrome'.format(word)
      if word == word[::-1]
      else 'Sorry!, the word {0} is not palindrome'.format(word))
