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
tab = "    "

"""
Definiert ein paar nützliche Stringlisten.
"""
Buchstabenliste = [x for x in string.ascii_lowercase]
directions = ["up","down","left","right"]
itemList = [4]
random.shuffle(itemList)
Inputs = [0] + itemList
items = {1:"Elektromagnet",2:"Sprungstiefel",3:"Kraftband",4:"Hammer",5:"Schwimmreifen",6:"Bumerang"}


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


def gehen(pos,dir,matrix):
    npos = pos + dir
    if not matrix.inMatrix(npos):
        return pos, matrix
    elif matrix.getZelle(npos) > 0:
        return pos, matrix
    else:
        return gehen(npos,dir,matrix)

def hammer(pos,dir,matrix):
    attacPos = pos + dir
    if matrix.inMatrix(attacPos):
        matrix.setZelle(attacPos,0)
    return pos,matrix


itemMethods = [gehen,None,None,None,hammer]


class POS:

    x = 0
    y = 0

    def __init__(self,nX,nY):
        self.x = nX
        self.y = nY

    def __add__(self, other):
        return POS(self.x+other.x,self.y+other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class MATRIX:

    matrix = [[]]
    breite = 0
    hoehe = 0

    def __init__(self, nBreite = 1, nHoehe = 1, standardwert = -1):
        self.matrix = [[standardwert for _ in range(nBreite)] for _ in range(nHoehe)]
        self.breite = nBreite
        self.hoehe = nHoehe

    def __eq__(self, other):
        return self.matrix == other.getMatrix()

    def getBreite(self):
        return self.breite

    def getHoehe(self):
        return self.hoehe

    def getZelle(self,pos):
        return self.matrix[pos.y][pos.x]

    def setZelle(self,pos,content):
        self.matrix[pos.y][pos.x] = content

    def inMatrix(self,pos):
        return pos.x in range(self.getBreite()) and pos.y in range(self.getHoehe())

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


class PFAD:

    posListe = None
    matrixListe = None
    laenge = 0
    itemsUsed = False

    def __init__(self):
        self.posListe = []
        self.matrixListe = []
        self.laenge = 0

    def append(self, pos, matrix):
        self.posListe.append(pos)
        self.matrixListe.append(matrix)
        self.laenge += 1

    def exists(self, pos, matrix):
        for i in range(self.laenge):
            if self.posListe[i] == pos and self.matrixListe[i] == matrix:
                return True
        return False



class ROOM:

    feldBreite = None
    feldHoehe = None
    Matrix = None
    upPos = None
    downPos = None
    leftPos = None
    rightPos = None
    ebene = None
    inputs = None

    loesungsMatrix = None
    backtrackingPfade = None

    def __init__(self, feldBreite = 8, feldHoehe = 8, nEbene = 0):
        self.setzeFeldgroesse(feldBreite, feldHoehe)
        self.Matrix = MATRIX(nBreite = self.feldBreite, nHoehe = self.feldHoehe, standardwert = 0)
        self.ebene = nEbene
        self.inputs = Inputs[:(2+nEbene)]

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
        self.Matrix.setZelle(self.upPos, 0)
        self.Matrix.setZelle(self.downPos, 0)
        self.Matrix.setZelle(self.leftPos, 0)
        self.Matrix.setZelle(self.rightPos, 0)



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


    """
    Berechnet die schnellsten Pfade von jedem Eingan zu jeden Ausgang
    """
    def starteBacktracking(self):
        self.backtrackingPfade = [[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]]]  #Ebene 1: 4 Listen für jeden Startpunkt
                                                                                #Ebene 2: 3 Listen für jeden Endpunkt
                                                                                #Ebene 3: Alle Pfade (PATH)
        startPositions = [self.upPos,self.downPos,self.leftPos,self.rightPos]
        for Ipos in range(len(startPositions)):                                 #Starte backtracking für jeden Start
            print(Ipos)
            pos = startPositions[Ipos]
            endingPositions = deepcopy(startPositions)
            del(endingPositions[endingPositions.index(pos)])
            self.backtracking(pos,deepcopy(self.Matrix),PFAD(),endingPositions,Ipos)


    """"
    Rekursiver Backtrackinalgorithmus 
        - Betrachtet alle möglichen Eingabekombinationen
        - Speichert einen Pfad der zu einem Ausgang führt in backtrackingPfade
    """
    def backtracking(self,pos,matrix,pfad,endingPositions,Ispos):
        if pfad.exists(pos,matrix):  #Abbruch wenn der Zustand bereits behandelt wurde
            return
        else:
            pfad.append(deepcopy(pos),deepcopy(matrix))  #Zustand dem Pfad hinzufügen

        for Iepos in range(len(endingPositions)):  #Prüft ob einer der Ausgänge erreicht wurde
            if pos == endingPositions[Iepos]:
                print("Ende gefunden")
                self.backtrackingPfade[Ispos][Iepos].append(deepcopy(pfad))  #Fügt den aktuellen Pfad
                                                                                # den Ergebnissen hinzu
        for input in self.inputs:  #Probiert alle Aktionen ausgehend von dem aktuellem Zustand
            for dir in [POS(0,1),POS(0,-1),POS(1,0),POS(-1,0)]:  #Wendet gewählte Aktion auf alle Richtungen an
                nPos, nMatrix = itemMethods[input](deepcopy(pos),deepcopy(dir),deepcopy(matrix))
                nPfad = deepcopy(pfad)
                if input > 0:
                    nPfad.itemsUsed = True  #Markiert im Pfad, dass ein Item verwendet wurde
                self.backtracking(nPos,nMatrix,nPfad,endingPositions,Ispos)  #Rekursiver Aufruf




    def alleLoesungenAusgabe(self):

        startPositions = [self.upPos, self.downPos, self.leftPos, self.rightPos]

        for i in range(4): # Ausgabe der Ergebnisse
            print("START:", self.schachnotation(startPositions[i]) )
            newline(1)
            ePosi = deepcopy(startPositions)
            del(ePosi[i])
            for e in range(3):
                newline(1)
                tab = "    "
                print(2*tab, "ENDE:", self.schachnotation(ePosi[e]) )
                for p in self.backtrackingPfade[i][e]:
                    zeichneRaumMitLoesung(self, posListe)
                    print(2*tab, "Items used:", p.itemsUsed)







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


r1 = ROOM()
r1.generiereLevel(float(13/168))
r1.starteBacktracking()
r1.alleLoesungenAusgabe()