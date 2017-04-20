from alphaNumLib import *

alphaNumArray = alphaArray + numArray + specialArray

def validateInput(input):
    if(checkInAlphaNumSpec(input)):
        return True
    else:
        return False

def checkInAlphaNumSpec(input):
    inputCharArray = list(input.lower())
    for value in inputCharArray:
        if value not in alphaNumArray:
            return False
    return True
