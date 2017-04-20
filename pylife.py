import sys, argparse
import numpy as np
import matplotlib.pyplot as plot
import matplotlib.animation as animation
from helper import *

def update(frameNumber, image, grid, gridSize):
    newGrid = grid.copy()
    for index in range(gridSize):
        for subIndex in range(gridSize):
            total = int((grid[index, (subIndex-1)%gridSize] + grid[index, (subIndex+1)%gridSize] +
                         grid[(index-1)%gridSize, subIndex] + grid[(index+1)%gridSize, subIndex] +
                         grid[(index-1)%gridSize, (subIndex-1)%gridSize] + grid[(index-1)%gridSize, (subIndex+1)%gridSize] +
                         grid[(index+1)%gridSize, (subIndex-1)%gridSize] + grid[(index+1)%gridSize, (subIndex+1)%gridSize])/ON)

            if grid[index, subIndex]  == ON:
                if (total < 2) or (total > 3):
                    newGrid[index, subIndex] = OFF
            else:
                if total == 3:
                    newGrid[index, subIndex] = ON

    image.set_data(newGrid)
    grid[:] = newGrid[:]
    return image

def main():
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
    parser.add_argument('--grid-size', dest='gridSize', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    args = parser.parse_args()

    gridSize = 100
    if args.gridSize and int(args.gridSize) > 8:
        gridSize = int(args.gridSize)

    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)

    grid = np.array([])

    if args.glider:
        grid = np.zeros(gridSize*gridSize).reshape(gridSize, gridSize)
        addGlider(1, 1, grid)
    elif args.gosper:
        grid = np.zeros(gridSize*gridSize).reshape(gridSize, gridSize)
        addGosperGliderGun(10, 10, grid)
    else:
        grid = randomGrid(gridSize)

    fig, ax = plot.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, gridSize),
                                  frames = 10,
                                  interval=updateInterval,
                                  save_count=50)

    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])

    plot.show()

if __name__ == '__main__':
    main()
