

def scale(pos, formSize, toSize):
    return [int(pos[i] * toSize[i] / formSize[i]) for i in range(2)]

def toGrid(pos, gridSize, offset = (0,0)):
    return [int( (pos[i] - offset[i]) // gridSize[i] * gridSize[i] + offset[i] ) for i in range(2)]