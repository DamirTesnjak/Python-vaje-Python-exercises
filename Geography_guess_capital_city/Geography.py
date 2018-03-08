# -*- coding: UTF-8 -*-

'''Avtor: Damir Tešnjak'''

print "\n----GUESS CAPITAL CITY----"
print "\n Guess the capital city of a country. You'll have 30 turns.\n" \
      "\n Good luck!" \
      "\n\n 30 pts EXPERT" \
      "\n up to 29 pts Excellent" \
      "\n up to 20 pts Good" \
      "\n up to 15 pts It could be better" \
      "\n up to 10 pts GO BACK TO SCHOOL!!!"

import random

points = 0

for x in range(30):

    dictLines = {}          # Prazen dictionary keys=COUNTRIES, value=CAPITAL CITY

    for y in range(3):
        with open("national_capital_cities.txt", 'r') as file:
            lines =file.readlines()                     # Branje vseh vrstic v datoteki
            selectedLine = random.choice(lines)         #Izbira naključne vrstice
            lineAsList = selectedLine.split(",")        #String pretvorimo v 'list', deliminator ','

        dictLines[lineAsList[1][1:]] = lineAsList[2]    #Vnos keys=COUNTRIES, value=CAPITAL CITY v dictionary

    ordDictKeys = dictLines.keys()          #Dobiti ključe
    randomIndex = random.randint(0,2)       #Naključen indeks
    country = ordDictKeys[randomIndex]      #Dobimo izbrano državo za katero iščemo glavno mesto

    #Izpis vpračanja
    print "\n What is the capital city of " + country + "?" \
        "\n\n A: " + dictLines[ordDictKeys[0]] + \
        "\n B: " + dictLines[ordDictKeys[1]] + \
        "\n C: " + dictLines[ordDictKeys[2]]

    answerIndex = {"A": 0, "B": 1, "C": 2}          # Dictionary keys=odgovor, value=indeks
    answer = raw_input("\nYour answer: ")           #Vnos odgovora

    #Preverimo, če je odgovor pravilen
    if answerIndex[answer.upper()] == ordDictKeys.index(country):
        print "Correct"
        points += 1
    else:
        print "Incorrect! It is " + dictLines[ordDictKeys[randomIndex]] + "!"

if points == 30:
    print "\nEXPERT!"
elif points > 20 and points <= 29:
    print "\nExcellent!"
elif points > 15 and points <= 20:
    print "\nGood!"
elif points > 10 and points <= 15:
    print "\nIt could be better!"
else:
    print "\nGO BACK TO SCHOOL!!!"