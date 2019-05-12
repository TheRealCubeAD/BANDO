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
feldBreite = 8 # > 0
feldHoehe = 8 # > 0


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

    # keine Randstine an der Endposition
    #if feldBreite >= 3:
        #level = setZelle(level, [endingPos[0]-1, 0], 0)
        #level = setZelle(level, [endingPos[0]+1, 0], 0)

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

# Entfernt das Element einer Listenliste, das pos als erstes Element hat.
def posEntfernen(liste, pos):
    for Eintrag in liste:
        if Eintrag[0] == pos:
            liste.remove(Eintrag)
            return liste
    return liste

# Überprüft, ob ein Element in einer Listenliste pos als erstes Element hat.
def posExistiert(liste, pos):
    for Eintrag in liste:
        if Eintrag[0] == pos:
            return True
    return False

# Gibt das zweite Element eines Elements einer Listenliste aus, das als erstes Element pos hat.
def posPfad(liste, pos):
    for Eintrag in liste:
        if Eintrag[0] == pos:
            return Eintrag[1]
    return None

"""
Wandelt ein Koordinatentupel in die im Schach übliche Notation um.
"""
Buchstabenliste = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def schachnotation( tupel ):
    x = Buchstabenliste[ tupel[0] ]
    y = str( feldHoehe - tupel[1] )
    return x + y


"""
Zeichnet ein Level in die Konsole.
Die Methode ist dazu da, um die lösbaren Rätsel selbst auszuprobieren.
Folgende Visualierungsprozesse werden durchgeführt:
- Färbung aller Steine in ROT
- Färbung der Anfangs- und Endposition in LILA
"""
def zeichneLevel(level):

    # Legt eine Kopie des Levels zur Bearbeitung an
    levelBunt = deepcopy(level)

    # Färbt die Steine ROT
    for zeile in levelBunt:
        for i in range(len(zeile)):
            if zeile[i] == 1:
                zeile[i] = RED + "1" + END

    # Färbt die Anfangsposition LILA
    content = getZelle(level, startingPos)
    levelBunt = setZelle(levelBunt, startingPos, LILA + str(content) + END)
    # Färbt die Endposition LILA
    content = getZelle(level, endingPos)
    levelBunt = setZelle(levelBunt, endingPos, LILA + str(content) + END)

    # Ausgabe der Matrix
    printMatrix(levelBunt)


"""
Zeichnet ein Level inklusive Lösung in die Konsole.
Die Methode ist dazu da, um die Lösung eines Rätsels zu visualisieren.
Folgende Visualierungsprozesse werden durchgeführt:
- Färbung aller Steine in ROT
- Färbung des Lösungswegs in GRÜN
- Färbung der Anfangs- und Endposition in LILA
- Ausgabe der Lösung in Schachnotation
"""
def zeichneLevelMitLoesung(level, path):

    # Legt eine Kopie des Levels zur Bearbeitung an
    levelBunt = deepcopy(level)

    # Färbt die im Lösungspfad besuchten Felder GRÜN
    for pos in path:
        content = getZelle(level, pos)
        levelBunt = setZelle(levelBunt,pos, GREEN + str(content) + END)

    # Färbt die Steine ROT
    for zeile in levelBunt:
        for i in range(len(zeile)):
            if zeile[i] == 1:
                zeile[i] = RED + "1" + END

    # Färbt die Anfangsposition LILA
    content = getZelle(level, startingPos)
    levelBunt = setZelle(levelBunt, startingPos, LILA + str(content) + END)
    # Färbt die Endposition LILA
    content = getZelle(level, endingPos)
    levelBunt = setZelle(levelBunt, endingPos, LILA + str(content) + END)

    # Ausgabe
    newline(1) # Leerzeile
    printMatrix(levelBunt) # Level
    # Generierung der Lösungsangabe
    if feldBreite <= 26:
        s = ""
        for i in path:
            s += schachnotation(i) + " "
    else:
        s = ""
        for i in path:
            s += str(i) + " "
    print(s) # Ausgabe der Lösung
    newline(1) # Leerzeile




directions = ["up","down","left","right"]
ergebnisse = []
def startLevelTest(level):
    # Setze die Startwerte auf Anfang
    global ergebnisse
    ergebnisse = []
    ergebnisse.append([endingPos, []])

    # Rufe das Ergebnis auf und formatiere es
    path = testLevel(level,startingPos) # Aufruf

    if None in path:
        path = None

    return path


def testLevel(level,pos):
    global ergebnisse

    # Wenn das Ergebniss schon mal ausgerechnet wurde, dann gib es wieder aus:
    if posExistiert(ergebnisse, pos):
        pfad = posPfad(ergebnisse, pos)
        if None in pfad:
            return pfad
        else:
            return [pos] + posPfad(ergebnisse, pos)

    # Ansonsten rechne es aus und speichere es:
    moeglichePfade = []
    ergebnisse.append( [ pos, [None for _ in range(feldBreite*feldHoehe)] ] ) # Eintrag in Arbeit

    for direction in directions:
        mPfad = testLevel( level, laufen(level, pos, direction) )
        moeglichePfade.append( mPfad )
    besterPfad = [None for _ in range(feldBreite*feldHoehe)]
    for pfad in moeglichePfade:
        if len(pfad) <= len(besterPfad) and None not in pfad:
            besterPfad = pfad

    posEntfernen( ergebnisse, pos ) # Arbeit abgeschlossen
    ergebnisse.append( [pos, besterPfad] ) # Arbeit speichern
    if None in besterPfad:
        return [None for _ in range(feldBreite*feldHoehe)]
    else:
        return [pos] + besterPfad


# Das ist das Verhältnis zwischen Steine und Fläche aus dem Original-Pokemon-Spiel: 13/168
pSteine = float(13/168)

path = None
while path == None:
    level = generiereLevel(pSteine)
    path = startLevelTest(level)
    if path != None:
        if len(path) < (feldBreite + feldHoehe):
            path = None
zeichneLevelMitLoesung(level, path)
print("Länge des (kürzesten) Lösungspfads:",len(path))
newline(1)