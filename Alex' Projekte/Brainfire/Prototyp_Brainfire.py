# Importware
import math # <3
import random # Gott würfelt nicht
from copy import deepcopy # copy aber deep

# Definitionen der farbigen Outputs
RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
LILA = '\033[95m'
END = '\033[0m'
POINT = "●"

# Defintion der Dimension des Spielbretts
feldBreite = 4 # > 0
feldHoehe = 4 # > 0

# Start- und Zielpunkt
if feldBreite % 2 == 0:
    startingPos = [ math.floor(feldBreite/2)-1 , feldHoehe-1 ]
    endingPos = [ math.floor(feldBreite/2) , 0 ]
else:
    startingPos = [math.floor(feldBreite / 2), feldHoehe - 1]
    endingPos = [math.floor(feldBreite / 2), 0]


# Gibt n Leerzeilen aus
def newline(n):
    for i in range(n):
        print()

# Gibt Matrix in Konsole aus
def printMatrix( matrix ):
    newline(1)
    for reihe in matrix:
        s = ""
        for i in range(len(reihe)):
            s += str(reihe[i]) + " "
        print(s)
    newline(1)

# Lost mit einer Wahrscheinlichkeit von p1 die Zahl 1 aus.
def randomBool( p1 ):
    if random.random() < p1:
        return 1
    else:
        return 0

# Bestimmt Inhalt einer Zelle
def getZelle(matrix,pos):
    return matrix[pos[1]][pos[0]]

# Setzt den Inhalt einer Zelle fest
def setZelle(matrix,pos,content):
    matrix[pos[1]][pos[0]] = content
    return matrix

# Generiert ein Level
def generiereLevel( pSteine ):
    level = [[0 for _ in range(feldBreite)] for _ in range(feldHoehe)]
    for Zeile in level:
        for i in range(len(Zeile)):
            Zeile[i] = randomBool( pSteine )

    # Start und Endposition
    level = setZelle(level, startingPos, 0)
    level = setZelle(level, endingPos, 0)

    # Randstine an der Endposition
    #level = setZelle(level, [4+1, 0], 0)
    #level = setZelle(level, [4-1, 0], 0)

    return level


# Bestimmt die naechste erreichbare Position von einem bestimmten Punkt aus
def laufen(level,pos,richtung):
    iRichtung = {"up":(0,-1),"down":(0,1),"left":(-1,0),"right":(1,0)}
    ix,iy = iRichtung[richtung]
    npos = [pos[0] + ix, pos[1] + iy]
    if npos[0] not in range(feldBreite) or npos[1] not in range(feldHoehe):
        return pos
    elif getZelle(level,npos) == 1:
        return pos
    else:
        return laufen(level,npos,richtung)



visitedNodes = None
directions = ["up","down","left","right"]

def startLevelTest(level):
    global visitedNodes
    visitedNodes = []

    levelBunt = deepcopy(level)
    path = testLevel(level,startingPos,[])
    if path != None:
        for pos in path:
            content = getZelle(level, pos)
            levelBunt = setZelle(levelBunt,pos, GREEN + str(content) + END)
        for zeile in levelBunt:
            for i in range(len(zeile)):
                if zeile[i] == 1:
                    zeile[i] = RED + "1" + END
        newline(2)
        printMatrix(levelBunt)
        newline(1)
        print(path)
        newline(2)
    return path


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




pSteine = float(8.4)
pSteine /= 100
path = None
while path == None:
    path = startLevelTest(generiereLevel(pSteine))