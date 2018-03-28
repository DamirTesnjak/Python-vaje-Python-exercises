# -*- coding: UTF-8 -*-

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
                            break
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

    # Iskanje igralčevih 'X_XX' ali 'XX_X' v diagonali top-desno-spodaj-levo

    def search_opt_four(diagonals_grid, targets, opponentLines, correction):
        for diag in range(0, 3):
            diagonal = diagonals_grid[diag]
            line = "".join(diagonal)
            for pos in range(0, len(line) - len(opponentLines) + 1) or line == "X XX" or line == "XX X":
                if line[pos: pos + 4] == opponentLines:
                    col = pos + correction  # empty space in diagonal
                    if column_grid[-col - 2][col + 1] != " ":
                        targets.append(7 - col - 1)
                        break

    def search_opt_five(diagonals_grid, targets, opponentLines, correction):
        for diag in range(3, 6):
            diagonal = diagonals_grid[diag]
            line = "".join(diagonal)
            for pos in range(0, len(line) - len(opponentLines) + 1) or line == "X XX" or line == "XX X":
                if line[pos: pos + 4] == opponentLines:
                    col = pos + correction  # empty space in diagonal
                    if column_grid[-col - 1][col + 1 + diag - 3] != " ":
                        targets.append(7 - col)
                        break


    # Iskanje igralčevih 'X_XX' ali 'XX_X' v diagonali spodaj-desno-top-levo

    def search_opt_six(diagonals_grid, targets, opponentLines, correction):
        for diag in range(6, 9):
            diagonal = diagonals_grid[diag]
            line = "".join(diagonal)
            for pos in range(0, len(line) - len(opponentLines) + 1):
                if line[pos: pos + 4] == opponentLines or line == "X XX" or line == "XX X":
                    col = pos + correction  # empty space in diagonal
                    if correction == 1:
                        if column_grid[col][-diag + 5 - correction] != " ":
                            targets.append(col + 1)
                            break
                        else:
                            if column_grid[col][-diag + 5 - correction] != " ":
                                targets.append(col + 1)
                                break

    def search_opt_seven(diagonals_grid, targets, opponentLines, correction):
        for diag in range(9, 12):
            diagonal = diagonals_grid[diag]
            line = "".join(diagonal)
            for pos in range(0, len(line) - len(opponentLines) + 1):
                if line[pos: pos + 4] == opponentLines or line == "X XX" or line == "XX X":
                    col = pos + correction  # empty space in diagonal
                    if correction == 1:
                        if column_grid[col + 1][-diag + 5 - correction] != " ":
                            targets.append(col + 2)
                            break
                        else:
                            if column_grid[col + 1][-diag + 5 - correction] != " ":
                                targets.append(col + 2)
                                break

    # Iskanje igralčevih 'XXX' v diagonali top-desno-spodaj-levo

    def search_opt_eight(diagonals_grid, targets, opponentLines):

        # ----------------------------------------------------------------------------------
        "st. diag.                  0    1    2    3  "
        '''grid = [[" ", " ", " ", "X", "X", "X", "X"],
                   [" ", " ", "X", "X", "X", "X", "X"], 4
                   [" ", "X", "X", "X", "X", "X", "X"], 5
                   [" ", " ", " ", " ", "X", "X", " "], 
                   [" ", " ", " ", " ", "X", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " "]]'''

        for diag in range(0, 6):
            diagonal = diagonals_grid[diag]
            line = "".join(diagonal)
            for pos in range(0, len(line) - len(opponentLines) + 1):
                if line[pos: pos + 3] == opponentLines:
                    if pos == 0:
                        if diagonal[pos + 3] == " ":
                            if diag <= 0 and diag < 4:
                                if column_grid[diag][4] != " ":
                                    targets.append(diag + 1)
                                    break
                            if diag == 4:
                                if column_grid[3][-1] != " ":
                                    targets.append(4)
                                    break
                            if diag == 5:
                                targets.append(4)
                                break

                    # --------------------------------------------------
                    "st. diag.                  0    1    2    3  "
                    '''grid = [[" ", " ", " ", " ", " ", " ", " "],
                               [" ", " ", "X", " ", " ", " ", " "], 4
                               [" ", "X", "X", " ", " ", " ", " "], 5
                               ["X", "X", "X", "X", "X", "X", " "], 
                               ["X", "X", "X", "X", "X", " ", " "],
                               ["X", "X", "X", "X", " ", " ", " "]]'''

                    if pos == len(diagonal) - 3:
                        if diagonal[pos - 1] == " ":
                            if diag <= 0 and diag < 3:
                                if column_grid[3][diag + 1] != " ":
                                    targets.append(4)
                                    break

                            if diag <= 3 and diag < 6:
                                if column_grid[diag + 1][4] != " ":
                                    targets.append(4)
                                    break

        # ----------------------------------------------------------------------------------
            "st. diag.                  0    1    2    3  "
            '''grid = [[" ", " ", " ", " ", " ", " ", " "],
                       [" ", " ", " ", "X", "X", "X", " "], 4
                       [" ", " ", "X", "X", "X", "X", " "], 5
                       [" ", "X", "X", "X", "X", " ", " "], 
                       [" ", "X", "X", "X", " ", " ", " "],
                       [" ", " ", " ", " ", " ", " ", " "]]'''

            for diag in range(1, 3):
                diagonal = diagonals_grid[diag]
                line = "".join(diagonal)
                for pos in range(0, len(line) - len(opponentLines) + 1):
                    if line[pos: pos + 4] == opponentLines:
                        col = pos - 1  # empty space in diagonal
                        if column_grid[-col - 3][col + 1] != " ":
                            targets.append(-col - 3)

                        col = pos + 3  # empty space in diagonal
                        if column_grid[-col - 3][col + 1] != " ":
                            targets.append(-col - 3)
                            break

            for diag in range(3, 5):
                diagonal = diagonals_grid[diag]
                line = "".join(diagonal)
                for pos in range(0, len(line) - len(opponentLines) + 1):
                    if line[pos: pos + 4] == opponentLines:
                        if column_grid[6][-5] != " ":
                            targets.append(7)

                        if column_grid[3][5] == " ":
                            targets.append(4)
                            break


    # Iskanje igralčevih 'XXX' v diagonali spodaj-desno-top-levo

    def search_opt_nine(diagonals_grid, targets, opponentLines):

        # ----------------------------------------------------------------------------------
        "st. diag.                  0    1    2    3  "
        '''grid= 8[["X", "X", "X", "X", " ", " ", " "],
                 7 ["X", "X", "X", "X", "X", " ", " "], 4
                 6 ["X", "X", "X", "X", "X", "X", " "], 5
                   [" ", "X", "X", " ", " ", " ", " "], 
                   [" ", " ", "X", " ", " ", " ", " "],
                   [" ", " ", " ", " ", " ", " ", " "]]'''

        for diag in range(6, 12):
            diagonal = diagonals_grid[diag]
            line = "".join(diagonal)
            for pos in range(0, len(line) - len(opponentLines) + 1):
                if line[pos: pos + 3] == opponentLines:
                    if pos == 0:
                        if diagonal[pos + 3] == " ":
                            if diag in range(7,9):
                                if column_grid[3][5 - diag + 1] != " ":
                                    targets.append(4)
                                    break
                            if diag == 6:
                                if column_grid[3][-1] == " ":
                                    targets.append(4)
                                    break
                            if diag in range(9, 12):
                                if column_grid[diag - 12][-2] != " ":
                                    targets.append(diag - 4)
                                    break

                    # --------------------------------------------------
                    "st. diag.                  0    1    2    3  "
                    '''grid = [[" ", " ", " ", " ", " ", " ", " "],
                               [" ", " ", " ", " ", "X", " ", " "], 4
                               [" ", " ", " ", " ", "X", "X", " "], 5
                               [" ", "X", "X", "X", "X", "X", "X"], 
                               [" ", " ", "X", "X", "X", "X", "X"],
                               [" ", " ", " ", "X", "X", "X", "X"]]'''

                    if pos == len(diagonal) - 3:
                        if diagonal[pos - 1] == " ":
                            if diag in range(9, 12):
                                if column_grid[4][12 - diag] != " ":
                                    targets.append(4)
                                    break

                            if diag in range(6, 9):
                                if column_grid[diag - 4 - 1][3] != " ":
                                    targets.append(diag - 4)
                                    break

            # KONČATI ŠE TO!---------------------------------------------------
            "st. diag.                  0    1    2    3  "
            '''grid = [[" ", " ", " ", " ", " ", " ", " "],
                       [" ", "X", "X", "X", " ", " ", " "], 4
                       [" ", "X", "X", "X", "X", " ", " "], 5
                       [" ", " ", "X", "X", "X", "X", " "], 
                       [" ", " ", " ", "X", "X", "X", " "],
                       [" ", " ", " ", " ", " ", " ", " "]]'''

            for diag in range(1, 3):
                diagonal = diagonals_grid[diag]
                line = "".join(diagonal)
                for pos in range(0, len(line) - len(opponentLines) + 1):
                    if line[pos: pos + 4] == opponentLines:
                        col = pos + 3  # empty space in diagonal
                        if column_grid[-col - 2][col + 1] != " ":
                            targets.append(7 - col - 1)
                            break

            for diag in range(3, 5):
                diagonal = diagonals_grid[diag]
                line = "".join(diagonal)
                for pos in range(0, len(line) - len(opponentLines) + 1):
                    if line[pos: pos + 4] == opponentLines:
                        col = pos  # empty space in diagonal
                        if column_grid[col + 1][-col - 1] != " ":
                            targets.append(col + 2)
                            break



    """Od tu naprej koda poskrbi da..."""

    """Če računalnik najde vrstico ali diagonalo s katero bi igralec v naslednji potezi zmagal,
    izbere tisti stolpec da igralcu prepreči zmago. Če ne najde omenjenih vrstic, potem računalnik 
    išče tisto svojo vrstico ali diagonalo, s katero bi v svoji potezi zmagal in temu primerno izbere 
    ustrezen stolpec (variable 'target'). Drugače izbere naključen stolpec."""

    search_opt_one(grid, targets, player_opt1)
    search_opt_two(grid, targets, player_opt2, fix_pos1)
    search_opt_two(grid, targets, player_opt3, fix_pos2)
    search_opt_three(column_grid, targets, player_opt1)
    search_opt_four(diagonals_grid, targets, player_opt2, fix_pos1)
    search_opt_four(diagonals_grid, targets, player_opt3, fix_pos2)
    search_opt_five(diagonals_grid, targets, player_opt2, fix_pos1)
    search_opt_five(diagonals_grid, targets, player_opt3, fix_pos2)
    search_opt_six(diagonals_grid, targets, player_opt2, fix_pos1)
    search_opt_six(diagonals_grid, targets, player_opt3, fix_pos2)
    search_opt_seven(diagonals_grid, targets, player_opt2, fix_pos1)
    search_opt_eight(diagonals_grid, targets, player_opt1)
    #search_opt_nine(diagonals_grid, targets, player_opt1)


    if targets != []:
        randomIndexs_of_target = randint(0, len(targets)-1)
        target = targets[randomIndexs_of_target]
        return target
    else:
        search_opt_one(grid, targets, Ai_opt1)
        search_opt_two(grid, targets, Ai_opt2, fix_pos1)
        search_opt_two(grid, targets, Ai_opt3, fix_pos2)
        search_opt_three(column_grid, targets, Ai_opt1)
        search_opt_four(diagonals_grid, targets, Ai_opt2, fix_pos1)
        search_opt_four(diagonals_grid, targets, Ai_opt3, fix_pos2)
        search_opt_five(diagonals_grid, targets, Ai_opt2, fix_pos1)
        search_opt_five(diagonals_grid, targets, Ai_opt3, fix_pos2)
        search_opt_six(diagonals_grid, targets, Ai_opt2, fix_pos1)
        search_opt_six(diagonals_grid, targets, Ai_opt3, fix_pos2)
        search_opt_seven(diagonals_grid, targets, Ai_opt2, fix_pos1)
        search_opt_seven(diagonals_grid, targets, Ai_opt3, fix_pos2)
        search_opt_eight(diagonals_grid, targets, Ai_opt1)
        #search_opt_nine(diagonals_grid, targets, Ai_opt1)

        if targets == []:
            target = randint(1, 7)
            return target
        else:
            randomIndexs_of_target = randint(0, len(targets) - 1)
            target = targets[randomIndexs_of_target]
            return target