# -*- coding: UTF-8 -*-
"""
@author: Abdallah Emad
"""
import random as rd
count = 0
flag = True
rd_num = rd.randint(0, 9)
while flag:
    user = input('Guess a number between 0 and 9 or type exit to exit: ')
    count += 1
    if user.lower() == 'exit':
        flag = False
        print('you guessed %i times' % rd_num)
        break
    else:
        try:
            if int(user) == rd_num:
                print('Yes, the number was %i, you guessed %i times' % (rd_num, count))
                flag = False
                break
            elif int(user) < rd_num:
                print('Sorry!, your number is smaller')
            elif int(user) > rd_num:
                print('Sorry!, your number is larger')
        except ValueError:
            print('Sorry!, please enter a number between 0 and 9')
