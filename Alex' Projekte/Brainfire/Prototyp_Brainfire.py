import random # Gott würfelt nicht
from copy import deepcopy # copy aber deep

RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
LILA = '\033[95m'
END = '\033[0m'
POINT = "●"


# Gibt n Leerzeilen aus
def newline(n):
    for i in range(n):
        print()

# Gibt Matrix in Konsole aus
def printMatrix( matrix ):
    newline(1)
    for i in range(len(matrix)):
        reihe = matrix[i]
        print(reihe)
    newline(1)

# Lost mit einer Wahrscheinlichkeit von p1 die Zahl 1 aus.
def randomBool( p1 ):
    if random.random() < p1:
        return 1
    else:
        return 0

def getZelle(matrix,pos):
    return matrix[pos[1]][pos[0]]

# Generiert ein Level
def generiereLevel( pSteine ):
    Level = [[0 for _ in range(8)] for _ in range(8)]
    for Zeile in Level:
        for i in range(len(Zeile)):
            Zeile[i] = randomBool( pSteine )
    return Level

endingPos = None
visitedNodes = None
directions = ["up","down","left","right"]

def startLevelTest(level):
    global endingPos,visitedNodes
    startingPos = [3,7]
    endingPos = [4,0]
    visitedNodes = []
    return testLevel(level,startingPos,[])

def laufen(level,pos,richtung):
    iRichtung = {"up":(0,-1),"down":(0,1),"left":(-1,0),"right":(1,0)}
    ix,iy = iRichtung[richtung]
    npos = [pos[0] + ix, pos[1] + iy]
    if npos[0] not in range(8) or npos[1] not in range(8):
        return pos
    elif getZelle(level,npos) == 1:
        return pos
    else:
        return laufen(level,npos,richtung)


def testLevel(level,pos,path):
    global visitedNodes
    path.append(pos)
    if pos == endingPos:
        return path

    if pos in visitedNodes:
        return None
    visitedNodes.append(pos)

    for direction in directions:
        statement = testLevel(level,laufen(level,pos,direction),path+[])
        if statement != None:
            return statement

    return None







while True:
    level = generiereLevel(0.2)
    printMatrix(level)
    print(startLevelTest(level))
    input()