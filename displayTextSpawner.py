import numpy as np

def displayText(input):
    print(generateBlankGroup())

def spawnValue(value, position):
    return False

def generateBlankGroup():
    return np.zeros(4*4).reshape(4*4)
