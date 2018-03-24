from random import randint

def insert_token(grid, target, token):

    numLine = 5

    try:
        while grid[numLine][target - 1] != " ":
            numLine -= 1
            if numLine == -1:
                numLine = 5
                target = randint(1,7)

        rowTarget = grid[numLine]
        rowTarget.insert(target - 1, token)
        del rowTarget[target]
        grid.insert(numLine, rowTarget)
        del grid[numLine + 1]
        return grid

    except IndexError:
        return grid
