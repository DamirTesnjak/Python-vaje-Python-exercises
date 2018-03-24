from getDiagonals import diagonals
from getColumns import columns

def check_winner(grid):
    numOf_X = 4
    for row in diagonals(grid) + columns(grid) + grid:
        rowAsString = "".join(row)
        if "X"*numOf_X in rowAsString:
            return True

        elif "O"*numOf_X in rowAsString:
            return False

    return None