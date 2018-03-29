def ifGridFull(grid):
    flat_list = [item for row in grid for item in row]

    ''' Enako kot
        for row in grid:
            for item in row:
                flat_list.append(item)
    '''

    if " " not in flat_list:
        return True
    else:
        return None