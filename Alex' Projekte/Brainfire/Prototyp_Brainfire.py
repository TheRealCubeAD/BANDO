# Gott würfelt nicht
import random

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

# Generiert ein Level
def generiereLevel( pSteine ):
    Level = [[0 for _ in range(8)] for _ in range(8)]
    for Zeile in Level:
        for i in range(len(Zeile)):
            Zeile[i] = randomBool( pSteine )
    return Level

while True:
    printMatrix(generiereLevel(0.2))
    input()