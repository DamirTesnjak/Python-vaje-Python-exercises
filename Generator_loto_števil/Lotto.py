# -*- coding: UTF-8 -*-

'''Author: Damir Tešnjak'''

import random

print "\n----Lottery numbers generator----"

def inputNum():

    try:
        global x
        x = int(raw_input('\nPlease enter how many random numbers would\n'
                          'you like to have (1-39): '))
    except ValueError:
        print("Input is not a number! Try again! ")
        inputNum()

    return generator(x)

def generator(num):

    numList = []
    count = 0

    while count < num:                      # Število ižrebanih številk zagotovimo s štetjem vnesenih številk v seznam.
        randNum = random.randint(1, 39)     # Naključno ižrebana številka (1-39)
        if randNum not in numList:
            numList.append(randNum)
            count += 1

    numList.sort()                          # Številke razvrstimo od najmanjše do največje
    return numList

print "\n", inputNum(), "\nEND"             #Izpis
