import numpy as np
from scipy.signal import convolve2d

def update_new(list_of_cells):
    grid = np.zeros((102, 102), dtype=int)
    for x, y in list_of_cells:
        grid[x, y] = 1

    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])

    neighbors = convolve2d(grid, kernel, mode='same')

    survive = (grid == 1) & ((neighbors == 2) | (neighbors == 3))
    born = (grid == 0) & (neighbors == 3)

    next_gen = survive | born
    new_list_of_cells = list(zip(*np.where(next_gen)))
    new_list_of_cells = [(x, y) for x, y in new_list_of_cells if 1 <= x <= 100 and 1 <= y <= 100]
    
    return new_list_of_cells

def number_of_alive_neighbours_new(coordinates, list_of_cells):
    grid = np.zeros((102, 102), dtype=int)
    for x, y in list_of_cells:
        grid[x, y] = 1

    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])
    
    neighbors = convolve2d(grid, kernel, mode='same')
    return neighbors[coordinates[0], coordinates[1]]

# Old code - naive approach using for loops

def update_old(list_of_cells):
    new_list_of_cells = []
    for i in range(1, 101):
        for j in range(1, 101):
            counter = number_of_alive_neighbours_old((i, j), list_of_cells)
            state = status_old((i, j), list_of_cells)
            if ((not(state) and (counter == 3)) or (state and (counter == 2 or counter == 3))):
                new_list_of_cells.append((i, j))
    return new_list_of_cells


def status_old(coordinates, list_of_cells):
    if coordinates in list_of_cells:
        return True
    else:
        return False


def number_of_alive_neighbours_old(coordinates, list_of_cells):
    counter = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (not(i == j == 0) and status_old((coordinates[0]+i, coordinates[1]+j), list_of_cells)):
                counter += 1
    return counter
