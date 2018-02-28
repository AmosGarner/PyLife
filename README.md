# PyLife
Conway's game of life written in Python as a birthday present for a colleague. Capable of rendering random populations or populations made from text passed in as a parameter.

## Project Info:
* Name: PyLife
* Version: 1.0
* Author: Amos Garner

## Install Commands:
Clone project repository into project directory:
```git clone git@github.com:AmosGarner/PyLife.git```

## How to run:
``` python pylife.py [--param] [paramValue]```

EX: ```python pylife.py --display alphanumspec --grid-size 135 --interval 100```

When you run the program the program window will pop up with the starting data projected on the screen followed by a request for a key press in your console to run the simulation.

To exit the program either press your OS's close program button or kill the process using the CLI.

## Parameters:
* ```--grid-size```: Changes the area of the simulation (default: 100)
* ```--display```: Displays a string of text passed in as a parameter value
    * ```--display alphanumspec```: will generate a plot of all the character currently mapped in the system
* ```--interval```: The speed at which the animation updates (default: 50 Milliseconds)
* all parameters are optional and the program can be run just by using: ```python pylife.py```

### Outside Resources:
* Wiki page for Conway's Game: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
