import numpy as np

ON = 255
OFF = 0
vals = [ON, OFF]

def displayText(input, gridSize):
    grid = generateBlankGroup(gridSize)
    index = 1
    x = gridSize / 2
    for value in list(input):
        print(5 * index)
        print(gridSize)
        if 5*index >= gridSize:
            index = 1
            x = gridSize/2 + 6

        grid = spawnValue(value, x, 5 * index, grid)
        index += 1
    return grid

def spawnValue(char, row, col, grid):
    if(char == 'a'):
        value = np.array([[OFF, ON, ON, OFF],
                           [ON, OFF, OFF, ON],
                           [ON, ON, ON, ON],
                           [ON, OFF, OFF, ON],
                           [ON, OFF, OFF, ON],])
    if(char == 'b'):
        value = np.array([[ON, ON, ON, OFF],
                           [ON, OFF, OFF, ON],
                           [ON, ON, ON, ON],
                           [ON, OFF, OFF, ON],
                           [ON, ON, ON, OFF],])
    if(char == 'c'):
        value = np.array([[ON, ON, ON, ON],
                           [ON, OFF, OFF, OFF],
                           [ON, OFF, OFF, OFF],
                           [ON, OFF, OFF, OFF],
                           [ON, ON, ON, ON],])
    if(char == 'd'):
        value = np.array([[ON, ON, ON, OFF],
                           [ON, OFF, OFF, ON],
                           [ON, OFF, OFF, ON],
                           [ON, OFF, OFF, ON],
                           [ON, ON, ON, OFF],])
    if(char == 'e'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == 'f'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == 'g'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == 'h'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == 'i'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == 'j'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == 'k'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == 'l'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == 'm'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == 'n'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == 'o'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == 'p'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == 'q'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == 'r'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == 's'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == 't'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == 'u'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == 'v'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == 'w'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == 'x'):
       value = np.array([[ON, OFF, OFF, ON],
                          [ON, OFF, OFF, ON],
                          [OFF, ON, ON, OFF],
                          [ON, OFF, OFF, ON],
                          [ON, OFF, OFF, ON],])
    if(char == 'y'):
       value = np.array([[ON, OFF, OFF, ON],
                          [ON, OFF, OFF, ON],
                          [OFF, ON, ON, OFF],
                          [OFF, ON, OFF, OFF],
                          [OFF, ON, OFF, OFF],])
    if(char == 'z'):
       value = np.array([[ON, ON, ON, ON],
                          [OFF, OFF, ON, OFF],
                          [OFF, ON, OFF, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == '0'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, ON],
                          [ON, OFF, OFF, ON],
                          [ON, OFF, OFF, ON],
                          [ON, ON, ON, ON],])
    if(char == '1'):
       value = np.array([[OFF, ON, ON, OFF],
                          [ON, ON, ON, OFF],
                          [OFF, ON, ON, OFF],
                          [OFF, ON, ON, OFF],
                          [OFF, ON, ON, OFF],])
    if(char == '2'):
       value = np.array([[ON, ON, ON, ON],
                          [OFF, OFF, OFF, ON],
                          [ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, ON],])
    if(char == '3'):
       value = np.array([[ON, ON, ON, ON],
                          [OFF, OFF, OFF, ON],
                          [OFF, ON, ON, ON],
                          [OFF, OFF, OFF, ON],
                          [ON, ON, ON, ON],])
    if(char == '4'):
       value = np.array([[ON, OFF, OFF, ON],
                          [ON, OFF, OFF, ON],
                          [ON, ON, ON, ON],
                          [OFF, OFF, OFF, ON],
                          [OFF, OFF, OFF, ON],])
    if(char == '5'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [OFF, OFF, OFF, ON],
                          [ON, ON, ON, OFF],])
    if(char == '6'):
       value = np.array([[ON, ON, OFF, OFF],
                          [ON, OFF, OFF, OFF],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, ON],
                          [ON, ON, ON, OFF],])
    if(char == '7'):
       value = np.array([[ON, ON, ON, ON],
                          [OFF, OFF, OFF, ON],
                          [OFF, ON, ON, OFF],
                          [OFF, ON, OFF, OFF],
                          [OFF, ON, OFF, OFF],])
    if(char == '8'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, ON],
                          [ON, ON, ON, OFF],
                          [ON, OFF, OFF, ON],
                          [ON, ON, ON, ON],])
    if(char == '9'):
       value = np.array([[ON, ON, ON, ON],
                          [ON, OFF, OFF, ON],
                          [ON, ON, ON, ON],
                          [ON, OFF, OFF, OFF],
                          [ON, OFF, OFF, OFF],])
    if(char == '_'):
       value = np.array([[OFF, OFF, OFF, OFF],
                          [OFF, OFF, OFF, OFF],
                          [OFF, OFF, OFF, OFF],
                          [OFF, OFF, OFF, OFF],
                          [OFF, OFF, OFF, OFF],])
    if(char == '!'):
       value = np.array([[OFF, ON, ON, OFF],
                          [OFF, ON, ON, OFF],
                          [OFF, ON, ON, OFF],
                          [OFF, OFF, OFF, OFF],
                          [OFF, ON, ON, OFF],])
    if(char == '?'):
       value = np.array([[OFF, ON, ON, OFF],
                          [ON, OFF, OFF, ON],
                          [OFF, OFF, ON, OFF],
                          [OFF, OFF, OFF, OFF],
                          [OFF, OFF, ON, OFF],])
    if(char == '.'):
       value = np.array([[OFF, OFF, OFF, OFF],
                          [OFF, OFF, OFF, OFF],
                          [OFF, OFF, OFF, OFF],
                          [OFF, ON, ON, OFF],
                          [OFF, ON, ON, OFF],])

    grid[row-2:row+3, col-2:col+2] = value
    return grid

def generateBlankGroup(gridSize):
    return np.zeros(gridSize*gridSize).reshape(gridSize, gridSize)
