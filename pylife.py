import sys, argparse
import numpy as np
import matplotlib.pyplot as plot
import matplotlib.animation as animation

from helper import *
from displayTextSpawner import displayText
from inputValidator import validateInput

paused = True
iteration = 0

def update(frameNumber, image, grid, gridSize):
    newGrid = grid.copy()
    global paused
    global iteration

    if paused is True and iteration > 0:
        value = raw_input('Press any [Key] to start simulation:')
        image.set_data(newGrid)
        grid[:] = newGrid[:]
        paused = False
    else:
        for index in range(gridSize):
            for subIndex in range(gridSize):
                total = int((grid[index, (subIndex-1)%gridSize] + grid[index, (subIndex+1)%gridSize] +
                             grid[(index-1)%gridSize, subIndex] + grid[(index+1)%gridSize, subIndex] +
                             grid[(index-1)%gridSize, (subIndex-1)%gridSize] + grid[(index-1)%gridSize, (subIndex+1)%gridSize] +
                             grid[(index+1)%gridSize, (subIndex-1)%gridSize] + grid[(index+1)%gridSize, (subIndex+1)%gridSize])/ON)
                if iteration > 0:
                    if grid[index, subIndex]  == ON:
                        if (total < 2) or (total > 3):
                            newGrid[index, subIndex] = OFF
                    else:
                        if total == 3:
                            newGrid[index, subIndex] = ON
        image.set_data(newGrid)
        grid[:] = newGrid[:]
        iteration += 1

    return image

def main():
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
    parser.add_argument('--grid-size', dest='gridSize', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', dest='glider', required=False)
    parser.add_argument('--gosper', dest='gosper', required=False)
    parser.add_argument('--display', dest='displayText', required=False)
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
    elif args.displayText and validateInput(args.displayText):
        if args.displayText == 'alphanumspec':
            grid = displayText('abcdefghijklmnopqrstuvwxyz_0123456789_', gridSize)
        elif args.displayText == 'david':
            grid = displayText('happy_birthday___david!!!!', gridSize)
        else:
            grid = displayText(args.displayText, gridSize)
    else:
        grid = randomGrid(gridSize)

    fig, ax = plot.subplots()
    img = ax.imshow(grid, interpolation='nearest')

    plot.title("PyLife V1.0")

    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, gridSize),
                                  frames = 10,
                                  interval=updateInterval,
                                  save_count=50)

    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])

    plot.show()

if __name__ == '__main__':
    main()
