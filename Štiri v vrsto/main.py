# -*- coding: UTF-8 -*-

''' Štiri v vrsto
    Avtor: Damir Tešnjak'''

from welcome_screen import welcome
from displayGrid import game_grid
from ifGridFull import ifGridFull
from insertToken import insert_token
from AiBrain import search_three_in_lines
from checkWinner import check_winner
from random import randint
import os

grid = [[" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "]]

def player(grid):
    playerChoice = int(raw_input("\n\n          Vstavite zeton (1-7): \n\n"))

    token = "X"
    target = playerChoice
    grid = insert_token(grid, target, token)
    print game_grid(grid)

    if check_winner(grid) == True:
        return True
    else:
        return None

def Ai(grid):
    os.system('cls')
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
                print "          Zmagali ste!"
                pressToContinue = raw_input("\n\n\n          'ENTER' za izhod: ").lower()
                if pressToContinue == "":
                    break
            if ifGridFull(grid) == True:
                print "          Neodloceno!"
                pressToContinue = raw_input("\n\n\n          'ENTER' za izhod: ").lower()
                if pressToContinue == "":
				    break
            choose = 1
        else:
            if Ai(grid) == False:
                print "          Racunalnik je zmagal!"
                pressToContinue = raw_input("\n\n\n          'ENTER' za izhod: ").lower()
                if pressToContinue == "":
                    break
            if ifGridFull(grid) == True:
                print "          Neodloceno!"
                pressToContinue = raw_input("\n\n\n          'ENTER' za izhod: ").lower()
                if pressToContinue == "":
                    break
            choose = 0

print "\n          ----STIRI V VRSTO----\n          by Damir Tesnjak"			
pressToContinue = raw_input("\n\n\n          'ENTER' za nadaljevanje: ").lower()

if pressToContinue == "":
    os.system('cls')

print "          Player: X\n          Ai: O\n"
pressToContinue = raw_input("\n\n\n          'ENTER' za nadaljevanje: ").lower()

if pressToContinue == "":
    os.system('cls')
start()