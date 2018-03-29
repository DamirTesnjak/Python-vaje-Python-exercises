# -*- coding: UTF-8 -*-

from random import randint
from getDiagonals import *
from getColumns import columns


def search_three_in_lines(grid):
    targets = []
    column_grid = columns(grid)
    rotated_dTLeft_BRight = list(zip(*reversed(diagonals_TLeft_BRight(grid))))
    rotated_dTRigth_BLeft = list(zip(*reversed(diagonals_TRigth_BLeft(grid))))

    Ai_opt1 = "OOO"
    Ai_opt2 = "OO"
    Ai_opt3 = "O OO"
    Ai_opt4 = "OO O"

    player_opt1 = "XXX"
    player_opt2 = "XX"
    player_opt3 = "X XX"
    player_opt4 = "XX X"

    fix_pos1 = 1  # za Ai_opt2 in player_opt2
    fix_pos2 = 2  # za Ai_opt3 in player_opt3

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
                        if grid[row][pos + 3] == " ":
                            targets.append(pos + 3 + 1)
                            break

    # Iskanje igralčevih 'X_XX' ali 'XX_X' v vrstici

    def search_opt_two(grid, targets, opponentLines, correction):
            for row in range(len(grid) - 1, -1, -1):
                line = "".join(grid[row])
                for pos in range(0, len(line) - len(opponentLines) + 1):
                    if line[pos: pos + 4] == opponentLines:
                        targets.append(pos + correction + 1)
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



    # Iskanje igralčevih 'XXX' v diagonali spodaj-desno-top-levo

    def search_opt_four(rotated_dTRigth_BLeft, targets, opponentLines):
        for row in range(len(rotated_dTRigth_BLeft)-1, -1, -1):
            line = "".join(rotated_dTRigth_BLeft[row])
            for pos in range(0, len(line) - len(opponentLines) + 1):
                if line[pos: pos + 3] == opponentLines:
                    if pos == 0:
                        try:
                            if rotated_dTRigth_BLeft[row][pos + 3] == " ":
                                if rotated_dTRigth_BLeft[row + 1][pos + 2] != " ":
                                    targets.append(row - 1)
                                    break
                        except IndexError:
                            continue

                    elif pos == len(rotated_dTRigth_BLeft[row]) - 3:
                        try:
                            if rotated_dTRigth_BLeft[row][pos - 1] == " ":
                                if rotated_dTRigth_BLeft[row + 1][pos - 2] != " ":
                                    targets.append(row - 1)
                                    break
                        except IndexError:
                            continue
                    else:
                        try:
                            if rotated_dTRigth_BLeft[row][pos - 1] == " ":
                                if rotated_dTRigth_BLeft[row + 1][pos - 2] != " ":
                                    targets.append(row - 1)
                                    break
                        except IndexError:
                            continue
                        try:
                            if rotated_dTRigth_BLeft[row][pos + 3] == " ":
                                if rotated_dTRigth_BLeft[row + 1][pos + 2] != " ":
                                    targets.append(row - 1)
                                    break
                        except IndexError:
                            continue

    def search_opt_five(rotated_dTLeft_BRight, targets, opponentLines):
        for row in range(len(rotated_dTLeft_BRight)-1, -1, -1):
            line = "".join(rotated_dTLeft_BRight[row])
            for pos in range(0, len(line) - len(opponentLines) + 1):
                if line[pos: pos + 3] == opponentLines:
                    if pos == 0:
                        try:
                            if rotated_dTLeft_BRight[row][pos + 3] == " ":
                                if rotated_dTLeft_BRight[row - 1][pos + 2] != " ":
                                    targets.append(row - 2)
                                    break
                        except IndexError:
                            continue
                    elif pos == len(rotated_dTLeft_BRight[row]) - 3:
                        try:
                            if rotated_dTLeft_BRight[row][pos - 1] == " ":
                                if rotated_dTLeft_BRight[row + 1][pos - 2] != " ":
                                    targets.append(row + 1)
                                    break
                        except IndexError:
                            continue
                    else:
                        try:
                            if rotated_dTLeft_BRight[row][pos - 1] == " ":
                                if rotated_dTLeft_BRight[row + 1][pos - 2] != " ":
                                    targets.append(row + 1)
                                    break
                        except IndexError:
                            continue
                        try:
                            if rotated_dTLeft_BRight[row][pos + 3] == " ":
                                if rotated_dTLeft_BRight[row - 1][pos + 2] != " ":
                                    targets.append(row - 2)
                                    break
                        except IndexError:
                            continue

    def search_opt_six(rotated_dTRigth_BLeft, targets, opponentLines):

        for row in range(len(rotated_dTRigth_BLeft)-1, -1, -1):
            line = "".join(rotated_dTRigth_BLeft[row])
            for pos in range(0, len(line) - len(opponentLines) + 1):
                if line[pos: pos + 2] == opponentLines:
                    if pos == 0:
                        if rotated_dTRigth_BLeft[row][pos + 2] == " ":
                            try:
                                if rotated_dTRigth_BLeft[row + 1][pos + 1] != " ":
                                    targets.append(row - 1)
                                    break
                            except IndexError:
                                continue
                    elif pos == len(rotated_dTRigth_BLeft[row]) - 2:
                        try:
                            if rotated_dTRigth_BLeft[row][pos - 1] == " ":
                                if rotated_dTRigth_BLeft[row + 1][pos - 1] != " ":
                                    targets.append(row - 1)
                                    break
                        except IndexError:
                            continue
                    else:
                        try:
                            if rotated_dTRigth_BLeft[row][pos - 1] == " ":
                                if rotated_dTRigth_BLeft[row + 1][pos - 1] != " ":
                                    targets.append(row - 1)
                                    break
                        except IndexError:
                            continue
                        if rotated_dTRigth_BLeft[row][pos + 2] == " ":
                            try:
                                if rotated_dTRigth_BLeft[row + 1][pos + 1] != " ":
                                    targets.append(row - 1)
                                    break
                            except IndexError:
                                continue

    def search_opt_seven(rotated_dTLeft_BRight, targets, opponentLines):
        for row in range(len(rotated_dTLeft_BRight)-1, -1, -1):
            line = "".join(rotated_dTLeft_BRight[row])
            for pos in range(0, len(line) - len(opponentLines) + 1):
                if line[pos: pos + 2] == opponentLines:
                    if pos == 0:
                        try:
                            if rotated_dTLeft_BRight[row][pos + 2] == " ":
                                if rotated_dTLeft_BRight[row - 1][pos + 1] != " ":
                                    targets.append(row - 1)
                                    break
                        except IndexError:
                            continue
                    elif pos == len(rotated_dTLeft_BRight[row]) - 2:
                        try:
                            if rotated_dTLeft_BRight[row][pos - 1] == " ":
                                if rotated_dTLeft_BRight[row + 1][pos - 1] != " ":
                                    targets.append(row + 1)
                                    break
                        except IndexError:
                            continue
                    else:
                        try:
                            if rotated_dTLeft_BRight[row][pos - 1] == " ":
                                if rotated_dTLeft_BRight[row + 1][pos - 1] != " ":
                                    targets.append(row + 1)
                                    break
                        except IndexError:
                            continue
                        try:
                            if rotated_dTLeft_BRight[row][pos + 2] == " ":
                                if rotated_dTLeft_BRight[row - 1][pos + 2] != " ":
                                    targets.append(row - 1)
                                    break
                        except IndexError:
                            continue

    """Od tu naprej koda poskrbi da..."""

    """Če računalnik najde vrstico ali diagonalo s katero bi igralec v naslednji potezi zmagal,
    izbere tisti stolpec da igralcu prepreči zmago. Če ne najde omenjenih vrstic, potem računalnik 
    išče tisto svojo vrstico ali diagonalo, s katero bi v svoji potezi zmagal in temu primerno izbere 
    ustrezen stolpec (variable 'target'). Drugače izbere naključen stolpec."""

    search_opt_one(grid, targets, player_opt1)
    search_opt_two(grid, targets, player_opt3, fix_pos1)
    search_opt_two(grid, targets, player_opt4, fix_pos2)
    search_opt_three(column_grid, targets, player_opt1)
    search_opt_four(rotated_dTRigth_BLeft, targets, player_opt1)
    search_opt_five(rotated_dTLeft_BRight, targets, player_opt1)
    search_opt_six(rotated_dTRigth_BLeft, targets, player_opt2)
    search_opt_seven(rotated_dTLeft_BRight, targets, player_opt2)


    if targets != []:
        randomIndexs_of_target = randint(0, len(targets)-1)
        target = targets[randomIndexs_of_target]
        return target
    else:
        search_opt_one(grid, targets, Ai_opt1)
        search_opt_two(grid, targets, Ai_opt3, fix_pos1)
        search_opt_two(grid, targets, Ai_opt4, fix_pos2)
        search_opt_three(column_grid, targets, Ai_opt1)
        search_opt_four(rotated_dTRigth_BLeft, targets, Ai_opt1)
        search_opt_five(rotated_dTLeft_BRight, targets, Ai_opt1)
        search_opt_six(rotated_dTRigth_BLeft, targets, Ai_opt2)
        search_opt_seven(rotated_dTLeft_BRight, targets, Ai_opt2)

        if targets == []:
            target = randint(1, 7)
            return target
        else:
            randomIndexs_of_target = randint(0, len(targets) - 1)
            target = targets[randomIndexs_of_target]
            return target