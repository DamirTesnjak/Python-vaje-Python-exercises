# -*- coding: UTF-8 -*-

''' Štiri v vrsto
    Avtor: Damir Tešnjak'''

from displayGrid import game_grid
from ifGridFull import ifGridFull
from insertToken import insert_token
from AiBrain import search_three_in_lines
from checkWinner import check_winner
from random import randint

print "\n----ŠTIRI V VRSTO----\n"

print "Player: X\nAi: O\n"

grid = [[" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "]]

print game_grid(grid)

def player(grid):
    playerChoice = int(raw_input("Vstavite žeton (1-7): "))

    token = "X"
    target = playerChoice
    grid = insert_token(grid, target, token)
    print game_grid(grid)

    if check_winner(grid) == True:
        return True
    else:
        return None

def Ai(grid):
    token = "O"
    target = search_three_in_lines(grid)
    grid = insert_token(grid, target, token)
    print game_grid(grid)

    if check_winner(grid) == False:
        return False
    else:
        return None

# KDO ZAČNE IGRO, IN NADALJNI POTEK IGRE

def start():
    choose = randint(0, 1)

    while True:
        if choose == 0:
            if player(grid) == True:
                print "Zmagali ste!"
                break
            if ifGridFull(grid) == True:
                print "Neodločeno!"
                break

            choose = 1
        else:
            if Ai(grid) == False:
                print "Računalnik je zmagal!"
                break
            if ifGridFull(grid) == True:
                print "Neodločeno!"
                break
            choose = 0

start()