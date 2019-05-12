"""

"""


"""
Importware
"""
import math # <3
import random # Gott würfelt nicht
from copy import deepcopy # copy aber deep
import time


"""
Definiert die Farbwerte für die Ausgabe
"""
RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
LILA = '\033[95m'
END = '\033[0m'
POINT = "●"


# Defintion der Dimension des Spielbretts
feldBreite = None # > 0
feldHoehe = None # > 0
upPos = None
downPos = None
leftPos = None
rightPos = None
"""
Setzt die Dimension des Spielbretts fest.
Legt anschließend Start- und Endposition fest.
"""
def setzeFeldgroesse(nBreite, nHoehe):
    global feldBreite, feldHoehe, upPos, downPos, leftPos, rightPos

    # Defintion der Dimension des Spielbretts
    feldBreite = nBreite  # > 0
    feldHoehe = nHoehe  # > 0

    # Definition von upPos und downPos
    if feldBreite % 2 == 0:
        upPos = [math.floor(feldBreite / 2) - 1, feldHoehe - 1]
        downPos = [math.floor(feldBreite / 2), 0]
    else:
        upPos = [math.floor(feldBreite / 2), feldHoehe - 1]
        downPos = [math.floor(feldBreite / 2), 0]

    # Definition von upPos und downPos
    if feldHoehe % 2 == 0:
        leftPos = [ 0, math.floor(feldHoehe / 2) - 1 ]
        rightPos = [ feldBreite - 1, math.floor(feldHoehe / 2) ]
    else:
        leftPos = [0, math.floor(feldHoehe / 2)]
        rightPos = [feldBreite - 1, math.floor(feldHoehe / 2)]


"""
Gibt n Leerzeile in der Konsole aus.
"""
def newline(n):
    for i in range(n):
        print()


"""
Gibt eine Matrix "schön" in der Konsole aus.
"""
def printMatrix( matrix ):
    newline(1)
    for reihe in matrix:
        s = ""
        for i in range(len(reihe)):
            s += str(reihe[i]) + " "
        print(s)
    newline(1)


"""
Gibt mit einer Wahrscheinlichkeit von p1 den Wert 1 zurück, ansonsten 0.
"""
def randomBool( p1 ):
    if random.random() < p1:
        return 1
    else:
        return 0


"""
Gibt den Inhalt einer Zelle in einer Matrix zurück.
"""
def getZelle(matrix,pos):
    return matrix[pos[1]][pos[0]]


"""
Gibt eine Matrix zurück, die an der Position pos mit dem Wert content überschrieben wurde.
"""
def setZelle(matrix,pos,content):
    matrix[pos[1]][pos[0]] = content
    return matrix


"""
Generiert ein Feld mit einem "Stein zu Fläche"-Verhältnis von pSteine.
Dabei sind upPos, downPos, leftPos, rightPos freigehalten von Steinen.
"""
def generiereLevel( pSteine ):
    level = [[0 for _ in range(feldBreite)] for _ in range(feldHoehe)]
    for Zeile in level:
        for i in range(len(Zeile)):
            Zeile[i] = randomBool( pSteine )

    # Start und Endposition
    level = setZelle(level, upPos, 0)
    level = setZelle(level, downPos, 0)
    level = setZelle(level, leftPos, 0)
    level = setZelle(level, rightPos, 0)

    return level


"""
Bestimmt die naechste erreichbare Position von einem bestimmten Punkt in einem Level aus.
"""
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



"""
Ergebnislisten-Bearbeitung:
Entfernt das Element einer Listenliste, das pos als erstes Element hat.
"""
def posEntfernen(liste, pos):
    for Eintrag in liste:
        if Eintrag[0] == pos:
            liste.remove(Eintrag)
            return liste
    return liste

"""
Ergebnislisten-Bearbeitung:
Überprüft, ob ein Element in einer Listenliste pos als erstes Element hat.
"""
def posExistiert(liste, pos):
    for Eintrag in liste:
        if Eintrag[0] == pos:
            return True
    return False

"""
Ergebnislisten-Bearbeitung:
Gibt das zweite Element eines Elements einer Listenliste aus, das als erstes Element pos hat.
"""
def posPfad(liste, pos):
    for Eintrag in liste:
        if Eintrag[0] == pos:
            return Eintrag[1]
    return None



"""
Gibt die seit dem angegebenen Zeitpunkt vergangene Zeit zurück.
"""
def vergangeneZeit(zeitpunkt):
    return time.time() - zeitpunkt


Buchstabenliste = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
"""
Wandelt ein Koordinatentupel in die im Schach übliche Notation um.
"""
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

    # Färbt upPos, downPos, leftPos, rightPos in LILA
    content = getZelle(level, upPos)
    levelBunt = setZelle(levelBunt, upPos, LILA + str(content) + END)
    content = getZelle(level, downPos)
    levelBunt = setZelle(levelBunt, downPos, LILA + str(content) + END)
    content = getZelle(level, leftPos)
    levelBunt = setZelle(levelBunt, leftPos, LILA + str(content) + END)
    content = getZelle(level, rightPos)
    levelBunt = setZelle(levelBunt, rightPos, LILA + str(content) + END)

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

        # Färbt upPos, downPos, leftPos, rightPos in LILA
        content = getZelle(level, upPos)
        levelBunt = setZelle(levelBunt, upPos, LILA + str(content) + END)
        content = getZelle(level, downPos)
        levelBunt = setZelle(levelBunt, downPos, LILA + str(content) + END)
        content = getZelle(level, leftPos)
        levelBunt = setZelle(levelBunt, leftPos, LILA + str(content) + END)
        content = getZelle(level, rightPos)
        levelBunt = setZelle(levelBunt, rightPos, LILA + str(content) + END)

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
    ergebnisse.append([downPos, []])

    # Rufe das Ergebnis auf und formatiere es
    path = testLevel(level,upPos) # Aufruf

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


"""
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""


"""
Parameterauswahl
"""
# Das ist das Verhältnis zwischen Steine und Fläche aus dem Original-Pokemon-Spiel: 13/168 ~ 7,74%
pSteine = float(13/168) # Stein zu Fläche - Verhältnis
versuchsZeit = 1 #Sekunden # Anzahl der Sekunden, die das Programm höchstens rechnen soll
mindestlaengeLoesung = 11 # Mindestlänge des Lösungswegs
setzeFeldgroesse(8,8) # Größe des Felds


"""
Versuchsdurchführung
"""
startTime = time.time() # Setze den Timer auf
path = None
while path == None and vergangeneZeit(startTime) < versuchsZeit:
    level = generiereLevel(pSteine)
    path = startLevelTest(level)
    if path != None:
        if len(path) < mindestlaengeLoesung:
            path = None


"""
Ergebnisausgabe
"""
newline(1)
if path == None:
    print(None)
else:
    zeichneLevelMitLoesung(level, path)
    print("Länge des (kürzesten) Lösungspfads:", len(path))
    print("Zeit zur Generierung:", vergangeneZeit(startTime))
newline(1)