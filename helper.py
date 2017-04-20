import numpy as np
import matplotlib.pyplot as plot
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(gridSize):
    return np.random.choice(vals, gridSize*gridSize, p=[0.2, 0.8]).reshape(gridSize, gridSize)

def addGlider(row, col, grid):
    glider = np.array([[OFF, OFF, ON],
                       [ON,  OFF, ON],
                       [OFF, OFF, OFF]])
    grid[row:row+3, col:col+3] = glider

def addGosperGliderGun(row, col, grid):
    gun = np.zeros(11*38).reshape(11, 38)

    gun[5][1] = gun[5][2] = ON
    gun[6][1] = gun[6][2] = ON

    gun[3][13] = gun[3][14] = ON
    gun[4][12] = gun[4][16] = ON
    gun[5][11] = gun[5][17] = ON
    gun[6][11] = gun[6][15] = gun[6][17] = gun[6][18] = ON
    gun[7][11] = gun[7][17] = ON
    gun[8][12] = gun[8][16] = ON
    gun[9][13] = gun[9][14] = ON

    gun[1][25] = ON
    gun[2][23] = gun[2][25] = ON
    gun[3][21] = gun[3][22] = ON
    gun[4][21] = gun[4][22] = ON
    gun[5][21] = gun[5][22] = ON
    gun[6][23] = gun[6][25] = ON
    gun[7][25] = ON

    gun[3][35] = gun[3][36] = ON
    gun[4][35] = gun[4][36] = ON

    grid[row:row+11, col:col+38] = gun
