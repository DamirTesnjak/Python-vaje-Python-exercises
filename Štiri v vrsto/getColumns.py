def columns(grid):
    individual_column = []
    columns_grid = []

    for x in range(0, len(grid[0])):
        for row in range(0, len(grid)):
            individual_column.append(grid[row][x])
        columns_grid.append(individual_column)
        individual_column = []

    return columns_grid