def checking_columns(columns_grid):
    for column in columns_grid:
        columnAsString = "".join(column)
        if "X"*4 in columnAsString:
            return True

        elif "O"*4 in columnAsString:
            return False

    return "draw"