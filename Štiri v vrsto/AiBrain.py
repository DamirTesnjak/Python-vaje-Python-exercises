# -*- coding: UTF-8 -*-

# Spodnja koda so 'možgani' igrice

from random import randint
from getColumns import columns
from getDiagonals import diagonals


def search_three_in_lines(grid):

    targets = []
    column_grid = columns(grid)
    diagonals_grid = diagonals(grid)

    Ai_opt1 = "OOO"
    Ai_opt2 = "O OO"
    Ai_opt3 = "OO O"

    player_opt1 = "XXX"
    player_opt2 = "X XX"
    player_opt3 = "XX X"


    # Iskanje igralčevih 'XXX' v vrstici/diagonali

    def search_opt_one(grid, targets, opponentLines):
        for row in range(len(grid)-1, -1, -1):
            line = "".join(grid[row])
            for pos in range(0, len(line) - len(opponentLines) + 1):
                if line[pos: pos + 3] == opponentLines:
                    if pos == 0:
                        if grid[row][pos + 3] == " ":
                            targets.append(pos + 3 + 1)
                            break
                    elif pos == 4:
                        if grid[row][pos - 1] == " ":
                            targets.append(pos)
                            break
                    else:
                        if grid[row][pos - 1] == " ":
                            targets.append(pos)
                            break
                        if grid[row][pos + 3] == " ":
                            targets.append(pos + 3 + 1)
                            break


    # Iskanje igralčevih 'X_XX' ali 'XX_X' v vrstici/diagonali

    def search_opt_two(grid, targets, opponentLines):

        if opponentLines == "X XX" or opponentLines == "O OO":
            for row in range(len(grid) - 1, -1, -1):
                line = "".join(grid[row])
                for pos in range(0, len(line) - len(opponentLines) + 1):
                    if line[pos: pos + 4] == opponentLines:
                        targets.append(pos + 1 + 1)
                        break

        else:
            for row in range(len(grid) - 1, -1, -1):
                line = "".join(grid[row])
                for pos in range(0, len(line) - len(opponentLines) + 1):
                    if line[pos: pos + 4] == opponentLines:
                        targets.append(pos + 2 + 1)
                        break


    # Iskanje igralčevih 'XXX' v stolpcu

    def search_opt_three(column_grid, targets, opponentLines):
        for col in range(0, len(column_grid)-1):
            column = "".join(column_grid[col])
            for pos in range(0, 4):
                if column[pos: pos + 3] == opponentLines and pos >= 1:
                    if column[pos-1] != " ":
                        continue
                    else:
                        targets.append(col + 1)
                        break


    # Napisat ŠE funkcijo za diagonale ...
	
	'''def search_opt_four():'''
		
	

    """Od tu naprej koda poskrbi da..."""

    """Če računalnik najde vrstico s katero bi igralec v naslednji potezi zmagal,
    izbere tisti stolpec da igralcu prepreči zmago. Če ne najde omenjenih vrstic,
    potem računalnik išče tisto svojo vrstico, s katero bi v tej potezi zmagal in
    temu primerno izbere ustrezen stolpec (variable 'target'). Drugače izbere
    naključen stolpec."""

    search_opt_one(grid, targets, player_opt1)
    search_opt_two(grid, targets, player_opt2)
    search_opt_two(grid, targets, player_opt3)
    search_opt_three(column_grid, targets, player_opt1)


    if targets != []:
        randomIndexs_of_target = randint(0, len(targets)-1)
        target = targets[randomIndexs_of_target]
        return target
    else:
        search_opt_one(grid, targets, Ai_opt1)
        search_opt_two(grid, targets, Ai_opt2)
        search_opt_two(grid, targets, Ai_opt3)
        search_opt_three(column_grid, targets, Ai_opt1)
        if targets == []:
            target = randint(1, 7)
            return target
        else:
            randomIndexs_of_target = randint(0, len(targets) - 1)
            target = targets[randomIndexs_of_target]
            return target