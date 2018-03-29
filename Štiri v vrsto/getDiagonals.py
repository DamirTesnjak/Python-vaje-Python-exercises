from getColumns import columns
from copy import copy

def diagonals_TRigth_BLeft(grid):

    new_grid = copy(grid)
    for i in range(0, len(new_grid)):
        new_grid[i] = new_grid[i] + ["n"] * (len(new_grid) - 1 - i)
        if i != 0:
            for j in range(0, i):
                new_grid[i].insert(0, "n")
    dTRigth_BLeft = columns(new_grid)
    return dTRigth_BLeft

def diagonals_TLeft_BRight(grid):
    new_grid = copy(grid)
    for i in range(0, len(new_grid)):
        new_grid[i] = new_grid[i] + ["n"] * i
        for j in range(0, len(new_grid) - 1 - i):
            new_grid[i].insert(0, "n")
    dTLeft_BRight = columns(new_grid)
    return dTLeft_BRight

def diagonals_length_four_or_over(diagonals):
    for x in range(len(diagonals)):
        diag_str = "".join(diagonals[x])
        diag_str = diag_str.replace("n", "")
        diag_list = list(diag_str)
        diagonals.append(diag_list)
    return diagonals[len(diagonals) / 2:]


def diagonals(grid):
    diag = diagonals_length_four_or_over(diagonals_TLeft_BRight(grid))[3:-3] + diagonals_length_four_or_over(diagonals_TRigth_BLeft(grid))[3:-3]
    return diag