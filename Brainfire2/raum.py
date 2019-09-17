import time
import random


#VORSICHT: Im gesamten Programm wird immer ERST Y DANN X angegeben, da damit leichter zu rechnen ist.

class POS:  #Speicher y,x ein einem Objekt. Kann leicht für mehrere Dimensionen ausgebaut werden.
    y = None
    x = None

    def __init__(self,ny,nx):
        self.y = ny
        self.x = nx

    def __eq__(self, other):  #Nimmt eine andere POS und vergleicht die Koordinaten mit den eigenen
        return self.y == other.y and self.x == other.x

    def __add__(self, other):  #Nimmt eine andere POS und addiert die Koordinaten. Gibt eine neue POS zurück
        return POS(self.y + other.y, self.x + other.x)

    def inText(self):  #Gibt einen String der Form (y/x) zurück (für Ausgabemethoden)
        return "("+str(self.y)+"/"+str(self.x)+")"


class ZUSTAND:  #Hilfsstruktur für die Breitensuche. Könnte für die Benutzung von Items erweitert werden
    pos = None  #Position POS des Zustands

    depht = None  #Tiefe des Zustands in der Breitensuche
    mother = None  #Vorgänger-Zustand

    goToos = None  #Richtungen, die von diesem Zustand aus probiert werden sollen

    def __init__(self,npos,nmother,ngoToos):
        self.pos = npos
        self.mother = nmother
        if self.mother:
            self.depht = self.mother.depht + 1
        else:
            self.depht = 0
        self.goToos = ngoToos

    def __eq__(self, other):  #Vergleicht diesen Zustand mit einem anderen
        return self.pos == other.pos

    def getPath(self):  #Gibt rekursiv den gegangenen Pfad als Liste von Positionen zurück
        if self.mother:
            path = self.mother.getPath()
            path.append(self.pos)
            return path
        else:
            return [self.pos]





class ROOM:  #Raum beinhaltet die Matrix, alle Eingänge, und ob diese miteinander verbunden sind
    matrix = None  #2-Dimensionale Map  0 -> Eis   1 -> Fels
    IO = None  #Liste aller Ein/Ausgänge. Diese werden als POS gespeichert
    connections = None  #Boolean-Matrix die angibt, welche Eingänge verbunden sind.
                    #Der Index eines Eingangs in dieser Matrix in y und x Richtung ist gleich dem Index in der IO-Liste
                    #Diese Matrix ist nicht vorgegeben sondern wird später generiert

    paths = None

    sy = None  #Grösse der Map in y
    sx = None  #Grösse der Map in x

    random_tresh = None  #Wahrscheinlichkeit für einen Felsen bei der Generierung der Map

    def __init__(self):
        self.sx = 16
        self.sy = 16
        self.random_tresh = 0.2
        self.IO = all_doors
        self.connections = [[False for _ in range(len(self.IO))] for __ in range(len(self.IO))]
                                                                      #Setzt alle Werte dieser Matrix auf Falsch
        self.paths = [[None for _ in range(len(self.IO))] for __ in range(len(self.IO))]
        # Setzt alle Werte dieser Matrix auf Falsch

    def createMatrix(self):  #Generiert eine zufällige Map (den Schmarn kennst du ja)
        self.matrix = []
        for y in range(self.sy):
            cur = []
            for x in range(self.sx):
                if self.random_tresh > random.random():
                    cur.append(1)
                else:
                    cur.append(0)
            self.matrix.append(cur)

        for pos in self.IO:  #Stellt sicher dass die Eingänge frei sind
            self.matrix[pos.y][pos.x] = 0


    def addConn(self,start,end): #Fügt eine Verbindung hinzu. Wird von der Breitensuche aufgerufen
        startIndex = self.IOindex(start.pos)
        endIndex = self.IOindex(end.pos)

        if not self.connections[startIndex][endIndex]:  #Prüfen ob bereits eine Verbindung existiert
            self.connections[startIndex][endIndex] = True  #Verbindung hinzufügen
            self.paths[startIndex][endIndex] = end.getPath()  #Pfad auslesen und speichern
            return all(self.connections[startIndex])  #Zurückgeben ob alle Ausgänge von diesem Eingang erreicht werden

        return False


    def IOindex(self,pos):  #Sucht den Index eines Eingangs aus der IO-Liste raus
        for i in range(len(self.IO)):
            if pos == self.IO[i]:
                return i
        return None

    def get(self,pos):  #Gibt den Wert der übergebenen POS in der Matrix zurück
        if pos.y in range(self.sy) and pos.x in range(self.sx):
            return self.matrix[pos.y][pos.x]
        else:
            return None  #Gibt es diese Position nicht (Wand) wird None zurückgegeben

    def printMatrix(self):  #Gibt die Matrix in der Konsole aus
        for ry in self.matrix:
            row = ""
            for rx in ry:
                row += str(rx)
                row += "  "
            print(row)


    def printConnections(self):  #Gibt die Verbindungs-Matrix in der Konsole aus
        row = "      "
        for i in self.IO:
            row += i.inText()
            row += " "
        print(row)

        for i in range(len(self.IO)):
            row = self.IO[i].inText() + " "
            for o in self.connections[i]:
                row += str(o)
                row += "  "
            print(row)


    def printPaths(self):  #Gibt alle kürzesten Pfade von einem Eingang zu einem Ausgang aus
        for startIndex in range(len(self.IO)):
            for endIndex in range(len(self.IO)):
                if self.connections[startIndex][endIndex] and startIndex != endIndex:
                    row = self.IO[startIndex].inText()
                    row += " -> "
                    row += self.IO[endIndex].inText()
                    row += " ::"
                    for pos in self.paths[startIndex][endIndex]:
                        row += " " + pos.inText() + " -"
                    print(row)


class TRACKER:  #Diese Klasse übernimmt die Breitensuche. (Letzendlich füllt sie nur die Verbindungs-Matrix in ROOM aus)
    room = None  #Der zu behandelnde Raum
    matrix = None  #Kopie der Matrix des Raums, damit schneller darauf zugegriffen werden kann


    def __init__(self,nroom):  #Der zu behandelnde Raum wird übergeben
        self.room = nroom
        self.matrix = self.room.matrix


    def startTracking(self):  #Ruft den tracker für jede Starposition in IO auf
        for i in self.room.IO:
            z = ZUSTAND(i,None,[up,down,left,right])
            self.track(z)


    def track(self,start):  #Breitensuche !nicht rekursiv!
        visited = []  #Besuchte Positionen
        snake = [start]  #Warteschlange (snake lol) der zu bearbeitenden Zustände
        while snake:  #Solange die Warteschlange nicht leer ist
            curZst = snake[0]  #Nimmt den ersten Zustand der Schlange
            del (snake[0])     #und löscht ihn aus der Schlange
            if not curZst in visited:  #wenn der Zustand noch nicht besucht wurde
                visited.append(curZst)  #als besucht makieren
                if curZst.pos in self.room.IO:  #wenn die Position ein Ausgang ist
                    finish = self.room.addConn(start,curZst)  #wird die entsprechende Verbindung hinzugefügt
                    if finish:  #Abbruch wenn bereits alle Ausgänge gefunden wurden
                        return
                #Füge alle von dieser Position zu erreichenden Positionen der Schlange hinzu
                for dir in curZst.goToos:  #Für alle Richtungen die im Zustand angegeben sind
                    newPos = self.run(curZst.pos,dir)  #Neue Position berechnen
                    if dir == up or dir == down:  #Wenn in Y-Richtung gegangen wurde
                        newGoToos = [left, right]  #als nächstes in X-Richtungen gehen
                    else:
                        newGoToos = [up, down]  #sonst als nächstes in Y-Richtungen gehen
                    snake.append(ZUSTAND(newPos,curZst,newGoToos))  #neuen Zustand erstellen und der Schlange anfügen


    def run(self,pos,direction): #Berechnet rekursiv welche Position
        # (abhänig von Startposition und Richtung) erreicht wird
        nextPos = pos + direction  #direction ist auch eine POS (hier als Vektor zu sehen)
        value = self.room.get(nextPos)  #Findet raus welchen Wert die nächste Position hätte
        if value == 1 or value == None:  #Wenn Stein oder Wand
            return pos  #Position davor rekursiv zurückgeben
        else:
            return self.run(nextPos,direction)  #weiterlaufen

up = POS(-1, 0)
down = POS(1, 0)
left = POS(0, -1)
right = POS(0, 1)

door_left = POS(8,0)
door_up = POS(0,7)
door_down = POS(15,8)
door_right = POS(7,15)
door_middle = POS(6,9)

all_doors = [door_left,door_right,door_up,door_down,door_middle]


def test():                  #Testablauf:
    l = ROOM()               #Raum initialisieren
    l.createMatrix()         #Raum generieren
    l.printMatrix()          #Raum ausgeben
    t = TRACKER(l)           #Breitensuche initialisieren
    time.clock()             #Uhr starten
    t.startTracking()        #Breitensuche starten
    print()
    print(time.clock())      #Uhr ausgeben
    print()
    l.printConnections()     #Verbindungen ausgeben
    print()
    l.printPaths()           #Pfade ausgeben
