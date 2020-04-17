grid = ['WBWBWBWBWBWBWBW', 'WWWWWWWBWWWWWWW', 'WBWBWBWBWBWBWBW', 'WWBWWWWWWWWWWWW', 'WBWBWBWBWBWBWBW', 'WWWWWWWBBWWWWWW', 'WBWBBBWBWBWBWBW',
        'BWWWWWWWWWWWWWB', 'WBWBWBWBWBBBWBW', 'WWWWWWBBWWWWWWW', 'WBWBWBWBWBWBBBW', 'WWWWWWWWWWWWWWW', 'WBWBWBWBWBWBWBW', 'WWWWWWWBWWWWWWW', 'WBWBWBWBWBWBWBW']
BLACK = 'B'
WHITE = 'W'
SEQUENCE = BLACK+WHITE+WHITE


def addBlacksAround(grid):
    width = len(grid[0])
    newGrid = [BLACK+row+BLACK for row in grid]
    newGrid.append((width+2)*BLACK)
    newGrid.insert(0, (width+2)*BLACK)
    return newGrid


def numberGrid(grid):
    positionsOfNumbers = []
    number = 1
    width = len(grid[0])

    def sequenceFound(row, col):
        return grid[row][col-1]+grid[row][col]+grid[row][col+1] == SEQUENCE or grid[row-1][col]+grid[row][col]+grid[row+1][col] == SEQUENCE

    for row in range(1, width-1):
        for col in range(1, width-1):
            if sequenceFound(row, col):
                positionsOfNumbers.append((row-1, col-1, number))
                number += 1
    return positionsOfNumbers


print(numberGrid(addBlacksAround(grid)))
