"""
DEVELOPER-NOTICE:
Prytotyp_Brainfire.py, Verison: 1.1

Diese Version kann:
- Das Projekt durch Einsatz von Klassen ernstnehmen

"""


"""
Importware
"""
import math # <3
import random # Gott würfelt nicht
from copy import deepcopy # copy aber deep
import time
import string


"""
Definiert die Farbwerte für die Ausgabe
"""
RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
LILA = '\033[95m'
END = '\033[0m'
POINT = "●"

"""
Definiert ein paar nützliche Stringlisten.
"""
Buchstabenliste = [x for x in string.ascii_lowercase]
directions = ["up","down","left","right"]
Inputs = directions + random.shuffle([3])
items = {0:"Elektromagnet",1:"Sprungstiefel",2:"Kraftband",3:"Hammer",4:"Schwimmreifen",5:"Bumerang"}


"""
Gibt n Leerzeile in der Konsole aus.
"""
def newline(n):
    for i in range(n):
        print()


"""
Gibt mit einer Wahrscheinlichkeit von p1 den Wert 1 zurück, ansonsten 0.
"""
def randomBool( p1 ):
    if random.random() < p1:
        return 1
    else:
        return 0


"""
Gibt die seit dem angegebenen Zeitpunkt vergangene Zeit zurück.
"""
def vergangeneZeit(zeitpunkt):
    return time.time() - zeitpunkt




class POS:

    x = 0
    y = 0

    def __init__(self,nX,nY):
        self.x = nX
        self.y = nY

    def __add__(self, other):
        return POS(x+other.x,y+other.y)

class MATRIX:

    matrix = [[]]
    breite = 0
    hoehe = 0

    def __init__(self, nBreite = 1, nHoehe = 1, standardwert = -1):
        self.matrix = [[standardwert for _ in range(nBreite)] for _ in range(nHoehe)]
        self.breite = nBreite
        self.hoehe = nHoehe

    def getBreite(self):
        return self.breite

    def getHoehe(self):
        return self.hoehe

    def getZelle(self,pos):
        return self.matrix[pos.y][pos.x]

    def setZelle(self,pos,content):
        self.matrix[pos.y][pos.x] = content

    def getMatrix(self):
        return self.matrix

    def copyMatrix(self, nMatrix):
        self.matrix = deepcopy(nMatrix.getMatrix())
        self.breite = nMatrix.getBreite()
        self.hoehe = nMatrix.getHoehe()

    """
    Gibt eine Matrix "schön" in der Konsole aus.
    """
    def printMatrix(self):
        newline(1)
        for reihe in self.matrix:
            s = ""
            for i in range(len(reihe)):
                s += str(reihe[i]) + " "
            print(s)
        newline(1)

class ROOM:

    feldBreite = None
    feldHoehe = None
    Matrix = None
    upPos = None
    downPos = None
    leftPos = None
    rightPos = None
    ebene = None

    def __init__(self, feldBreite = 8, feldHoehe = 8, pSteine = float(13/168), ebene = 0):
        self.setzeFeldgroesse(feldBreite, feldHoehe)
        self.Matrix = MATRIX(nBreite = self.feldBreite, nHoehe = self.feldHoehe, standardwert = 0)
        self.ebene = 0

    """
    Setzt die Dimension des Spielbretts fest.
    Legt anschließend Start- und Endposition fest.
    """
    def setzeFeldgroesse(self, nBreite, nHoehe):

        # Defintion der Dimension des Spielbretts
        self.feldBreite = nBreite  # > 0
        self.feldHoehe = nHoehe  # > 0

        # Definition von upPos und downPos
        if self.feldBreite % 2 == 0:
            self.upPos = POS(math.floor(self.feldBreite / 2) - 1, self.feldHoehe - 1)
            self.downPos = POS(math.floor(self.feldBreite / 2), 0)
        else:
            self.upPos = POS(math.floor(self.feldBreite / 2), self.feldHoehe - 1)
            self.downPos = POS(math.floor(self.feldBreite / 2), 0)

        # Definition von upPos und downPos
        if self.feldHoehe % 2 == 0:
            self.leftPos = POS(0, math.floor(self.feldHoehe / 2) - 1)
            self.rightPos = POS(self.feldBreite - 1, math.floor(self.feldHoehe / 2))
        else:
            self.leftPos = POS(0, math.floor(self.feldHoehe / 2))
            self.rightPos = POS(self.feldBreite - 1, math.floor(self.feldHoehe / 2))


    """
    Generiert ein Feld mit einem "Stein zu Fläche"-Verhältnis von pSteine.
    Dabei sind upPos, downPos, leftPos, rightPos freigehalten von Steinen.
    """
    def generiereLevel(self, pSteine):

        for x in range(self.Matrix.getBreite()):
            for y in range(self.Matrix.getHoehe()):
                self.Matrix.setZelle( POS(x,y), randomBool(pSteine) )

        # Start und Endposition
        self.Matrix.setZelle(upPos, 0)
        self.Matrix.setZelle(downPos, 0)
        self.Matrix.setZelle(leftPos, 0)
        self.Matrix.setZelle(rightPos, 0)


    """
    Bestimmt die naechste erreichbare Position von einem bestimmten Punkt in einem Level aus.
    """
    def laufen(self, pos, richtung):
        iRichtung = {"up": POS(0, -1), "down": POS(0, 1), "left": POS(-1, 0), "right": POS(1, 0)}
        vektor = iRichtung[richtung]
        npos = pos + vektor
        if npos.x not in range(self.feldBreite) or npos.y not in range(self.feldHoehe):
            return pos
        elif self.getZelle(npos) == 1:
            return pos
        else:
            return self.laufen(npos, richtung)


    """
    Zeichnet ein Level in die Konsole.
    Die Methode ist dazu da, um die lösbaren Rätsel selbst auszuprobieren.
    Folgende Visualierungsprozesse werden durchgeführt:
    - Färbung aller Steine in ROT
    - Färbung der Anfangs- und Endposition in LILA
    """
    def zeichneRaum(self):

        # Legt eine Kopie des Levels zur Bearbeitung an
        levelBunt = MATRIX()
        levelBunt.copyMatrix(self.Matrix)

        # Färbt die Steine ROT
        for x in range(levelBunt.getBreite()):
            for y in range(levelBunt.getHoehe()):
                pos = POS(x,y)
                if levelBunt.getZelle(pos) == 1:
                    levelBunt.setZelle( pos, RED + "1" + END )

        # Färbt upPos, downPos, leftPos, rightPos in LILA
        for pos in [self.upPos,self.downPos,self.leftPos,self.rightPos]:
            content = self.getZelle(pos)
            levelBunt.setZelle(pos, LILA + str(content) + END )

        # Ausgabe der Matrix
        levelBunt.printMatrix()


    """
    Zeichnet ein Level inklusive Lösung in die Konsole.
    Die Methode ist dazu da, um die Lösung eines Rätsels zu visualisieren.
    Folgende Visualierungsprozesse werden durchgeführt:
    - Färbung aller Steine in ROT
    - Färbung des Lösungswegs in GRÜN
    - Färbung der Anfangs- und Endposition in LILA
    - Ausgabe der Lösung in Schachnotation
    """
    def zeichneRaumMitLoesung(self, path):

        # Legt eine Kopie des Levels zur Bearbeitung an
        levelBunt = MATRIX()
        levelBunt.copyMatrix(self.Matrix)

        # Färbt die im Lösungspfad besuchten Felder GRÜN
        for pos in path:
            content = levelBunt.getZelle(pos)
            levelBunt.setZelle(pos, GREEN + str(content) + END)

        # Färbt die Steine ROT
        for x in range(levelBunt.getBreite()):
            for y in range(levelBunt.getHoehe()):
                pos = POS(x, y)
                if levelBunt.getZelle(pos) == 1:
                    levelBunt.setZelle(pos, RED + "1" + END)

        # Färbt upPos, downPos, leftPos, rightPos in LILA
        for pos in [self.upPos,self.downPos,self.leftPos,self.rightPos]:
            content = self.getZelle(pos)
            levelBunt.setZelle(pos, LILA + str(content) + END )

        # Ausgabe
        newline(1)  # Leerzeile
        levelBunt.printMatrix()  # Level
        # Generierung der Lösungsangabe
        if self.feldBreite <= 26:
            s = ""
            for i in path:
                s += self.schachnotation(i) + " "
        else:
            s = ""
            for i in path:
                s += str(i) + " "
        print(s)  # Ausgabe der Lösung
        newline(1)  # Leerzeile


    """
    Wandelt ein POS-Objekt in die im Schach übliche Notation um.
    """
    def schachnotation(self, pos):
        x = Buchstabenliste[pos.x]
        y = str(self.feldHoehe - pos.y)
        return x + y







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