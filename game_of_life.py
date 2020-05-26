#!python3
import random
import itertools
import copy


def create_grid(rows, columns):
    return [[random.randint(0, 1) for row in range(rows)] for column in range(columns)]


def update_grid(grid, rows, columns):
    def count_living_neighbours(row, column):
        living_neighbours = 0
        if grid[(row - 1 + rows) % rows][(column - 1 + columns) % columns]:
            living_neighbours += 1
        if grid[(row - 1 + rows) % rows][(column + 0) % columns]:
            living_neighbours += 1
        if grid[(row - 1 + rows) % rows][(column + 1) % columns]:
            living_neighbours += 1
        if grid[(row + 0) % rows][(column - 1 + columns) % columns]:
            living_neighbours += 1
        if grid[(row + 0) % rows][(column + 1) % columns]:
            living_neighbours += 1
        if grid[(row + 1) % rows][(column - 1 + columns) % columns]:
            living_neighbours += 1
        if grid[(row + 1) % rows][(column + 0) % columns]:
            living_neighbours += 1
        if grid[(row + 1) % rows][(column + 1) % columns]:
            living_neighbours += 1
        return living_neighbours

    new_grid = copy.deepcopy(grid)

    for row in range(rows):
        for column in range(columns):
            living_neighbours = count_living_neighbours(row, column)
            if living_neighbours in (2, 3):
                if living_neighbours == 3 and grid[row][column] == 0:
                    new_grid[row][column] = 1
            else:
                new_grid[row][column] = 0
    return new_grid


def game(rows, columns, CYCLES=1):
    all_generations = []
    grid = create_grid(rows, columns)
    all_generations.append(grid)
    for cycle in range(CYCLES):
        grid = update_grid(grid, rows, columns)
        all_generations.append(grid)
    return all_generations


if __name__ == "__main__":
    for generation in game(4, 4):
        for row in generation:
            for column in row:
                print(column, end=' ')
            print()
        print()
