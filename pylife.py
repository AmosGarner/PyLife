import sys, argparse
import numpy as np
import matplotlib.pyplot as plot
import matplotlib.animation as animation
from helper import *

ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(scale):
    return np.random.choice(vals, scale*scale, p=[0.2, 0.8]).reshape(scale, scale)

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

def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for index in range(N):
        for subIndex in range(N):
            total = int((grid[index, (subIndex-1)%N] + grid[index, (subIndex+1)%N] +
                         grid[(index-1)%N, subIndex] + grid[(index+1)%N, subIndex] +
                         grid[(index-1)%N, (subIndex-1)%N] + grid[(index-1)%N, (subIndex+1)%N] +
                         grid[(index+1)%N, (subIndex-1)%N] + grid[(index+1)%N, (subIndex+1)%N])/255)
            # apply Conway's rules
            if grid[index, subIndex]  == ON:
                if (total < 2) or (total > 3):
                    newGrid[index, subIndex] = OFF
            else:
                if total == 3:
                    newGrid[index, subIndex] = ON

    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img

def main():
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    args = parser.parse_args()

    N = 100
    if args.N and int(args.N) > 8:
        N = int(args.N)

    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)

    grid = np.array([])

    if args.glider:
        grid = np.zeros(N*N).reshape(N, N)
        addGlider(1, 1, grid)
    elif args.gosper:
        grid = np.zeros(N*N).reshape(N, N)
        addGosperGliderGun(10, 10, grid)
    else:
        grid = randomGrid(N)

    fig, ax = plot.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                  frames = 10,
                                  interval=updateInterval,
                                  save_count=50)

    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])

    plot.show()

if __name__ == '__main__':
    main()
