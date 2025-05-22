def update(list_of_cells):
    new_list_of_cells = []
    for i in range(1, 101):
        for j in range(1, 101):
            counter = number_of_alive_neighbours((i, j), list_of_cells)
            state = status((i, j), list_of_cells)
            if ((not(state) and (counter == 3)) or (state and (counter == 2 or counter == 3))):
                new_list_of_cells.append((i, j))
    return new_list_of_cells


def status(coordinates, list_of_cells):
    if coordinates in list_of_cells:
        return True
    else:
        return False


def number_of_alive_neighbours(coordinates, list_of_cells):
    counter = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (not(i == j == 0) and status((coordinates[0]+i, coordinates[1]+j), list_of_cells)):
                counter += 1
    return counter
