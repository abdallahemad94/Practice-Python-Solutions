# -*- coding: utf-8 -*-
"""
Rock-Paper-Scissors game.

Created on Thu Mar  1 23:21:18 2018

@author: Abdallah Emad
"""
import random as rd


def player1():
    flag = True
    while flag:
        try:
            print('Player 1 please choose:')
            p1 = input('p for Paper, r for Rock, or s for scissors: ')
            if not len(p1) == 1:
                raise IndexError
            if not (p1 == 'r' or p1 == 's' or p1 == 'p'):
                raise ValueError
        except IndexError:
            print('Sorry!, must enter only one letter\n')
        except ValueError:
            print('Sorry!, must enter p for Paper, r for Rock', end='')
            print(', or s for scissors\n')
        else:
            flag = False
            p1.lower()
            p1 = 'Paper' if p1 == 'p' else\
                'Scissors' if p1 == 's' else\
                'Rock' if p1 == 'r' else p1
    return p1


def player2():
    flag = True
    while flag:
        try:
            print('Player 2 please choose:')
            p2 = input('p for Paper, r for Rock, or s for scissors: ')
            if not len(p2) == 1:
                raise IndexError
            if not (p2 == 'r' or p2 == 's' or p2 == 'p'):
                raise ValueError
        except IndexError:
            print('Sorry!, must enter only one letter\n')
        except ValueError:
            print('Sorry!, must enter p for Paper, r for Rock', end='')
            print(', or s for scissors\n')
        else:
            flag = False
            p2.lower()
            p2 = 'Paper' if p2 == 'p' else\
                'Scissors' if p2 == 's' else\
                'Rock' if p2 == 'r' else p2
    return p2


def check(p1, p2, mode):
    referee = {'Paper': 'Rock', 'Rock': 'Scissors', 'Scissors': 'Paper'}
    if p1 == p2:
        return 'Draw, player 1 played %s, player 2 played %s\n' % (p1, p2)
    else:
        if referee[p1] == p2:
            return 'Congrats, player 1 won\n'
        elif referee[p2] == p1:
            if mode == 1:
                return 'Congrats, player 2 won\n'
            elif mode == 2:
                return 'Sorry Player 1, Computer won\n'


def get_mode():
    flag = True
    while flag:
        try:
            print('Please choose a mode:')
            mode = int(input('enter 1 for PvP game, or 2 for PvC game: '))
            if not (mode == 1 or mode == 2):
                raise ValueError
        except TypeError:
            print('Sorry!, must enter a number')
        except ValueError:
            print('Sorry!, must enter 1 for PvP game,', end=' ')
            print('or 2 for PvC game\n')
        else:
            flag = False
    return mode


def game():
    play = True
    print('Welcome to Rock Paper Scissors game')
    while play:
        mode = get_mode()
        if mode == 1:
            print(check(player1(), player2(), mode))
        elif mode == 2:
            computer = rd.choice(['Paper', 'Rock', 'Scissors'])
            print(check(player1(), computer, mode))
        print('Do you want to play Again?')
        while True:
            ask = input('press y to play again, or n to exit: ')
            if ask.lower() == 'n':
                play = False
                print('Ok, bye-bye\n')
                break
            elif ask.lower() == 'y':
                print('Ok, lets play again\n')
                break
            else:
                print('Sorry!, I did not understand that\n')


if __name__ == '__main__':
    game()
