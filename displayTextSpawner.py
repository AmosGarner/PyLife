import numpy as np

ON = 255
OFF = 0
vals = [ON, OFF]

def displayText(input, gridSize):
    grid = generateBlankGroup(gridSize)
    grid = spawnValue('A', gridSize/2, gridSize/2, grid)
    return grid

def spawnValue(value, row, col, grid):
    value = np.array([[OFF, ON, ON, OFF],
                       [ON, OFF, OFF, ON],
                       [ON, ON, ON, ON],
                       [ON, OFF, OFF, ON],])
    grid[row:row+4, col:col+4] = value
    return grid

def generateBlankGroup(gridSize):
    return np.zeros(gridSize*gridSize).reshape(gridSize, gridSize)
