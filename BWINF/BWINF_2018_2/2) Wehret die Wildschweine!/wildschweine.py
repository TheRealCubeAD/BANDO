import time
from PIL import Image, ImageDraw
from copy import deepcopy
from math import ceil
# Um Pillow in PyCharm zu nutzen:
# Strg + Alt + S -> Project Interpretor -> Pluszeichen -> "Pillow"

# input: eine Matrix
# Korrekt formatierte Ausgabe der Matrix im Textfeld
def printMatrix(matrix):
    for i in matrix:
        s = ""
        for j in i:
            s += j + "  "
        print(s)

def printMatrixMitPfad(matrix):
    roteQuadrate = []
    RED = '\033[91m'
    END = '\033[0m'
    for i in range(len(P)-1):
        e1, e2, a = kante(P[i], P[i+1])
        roteQuadrate.append(e1)
        roteQuadrate.append(e2)
    for y in range(len(matrix)):
        Reihe = matrix[y]
        s = ""
        for x in range(len(Reihe)):
            if [x, y] in roteQuadrate:
                s += RED + Reihe[x] + END + " "
            else:
                s += Reihe[x] + " "
        print(s)


# input: ein Float
# output: Eine Aufrundung des Floats auf 0, wenn dieser negativ ist
def nichtNegativ(n):
    if n < 0:
        return 0
    else:
        return n

# input: eine Float
# output: ein String mit der aufgerundeten Zahl im Format "(-)X.XXX"
# Dabei ist X eine Ziffer, das Vorzeichen - ist optional
def aufrunden(n):
    n = float(n)
    n = round(n,8)
    n2 = str(float(ceil(n*1000)/1000))
    a = 6
    if n2[0] != "-":
        n2 = " " + n2
    while len(n2) < a:
        n2 += "0"
    return n2


# input: eine Feldmatrix mit einem String fuer den Dateinamen
# Visualisierung der Feldmatrix in einer exportierten Bilddatei
def ZeichneFeld(F, name):
    s = 50
    x_max = feldbreite * s
    y_max = feldlaenge * s

    # Initialisierung des Bildes
    pic = Image.new("RGB", ((x_max+1, y_max+1)), (255, 255, 255))
    draw = ImageDraw.Draw(pic)

    for Reihe in range(feldbreite):
        for Spalte in range(feldlaenge):
            farbe = int( 255 * ( float(F[Spalte][Reihe]) - h_min ) / ( h_max - h_min) )
            draw.rectangle([(Reihe*s, Spalte*s),((Reihe+1)*s,(Spalte+1)*s)], (farbe, farbe, farbe), (255, 255, 255))

    # Einzeichnen des Rasters
    for i in range(0, feldbreite+1):
        draw.line([(0,i*s),(x_max,i*s)], (0, 0, 255), 1)
        draw.line([(i*s,0),(i*s,y_max)], (0, 0, 255), 1)

    pic.save(name)
    pic.show()


# input: eine Feldmatrix mit Pfad einer roten Linie und Dateinamen
# Genau wie ZeichneFeld(F, name) nur mit einem zusaetzlich eingezeichnetem Pfad
def ZeichneFeldMitPfad(F, PP, name):

    # Visualisierung:
    s = 50
    x_max = feldbreite * s
    y_max = feldlaenge * s

    # Initialisierung des Bildes
    pic = Image.new("RGB", ((x_max+1, y_max+1)), (255, 255, 255))
    draw = ImageDraw.Draw(pic)

    for Reihe in range(feldbreite):
        for Spalte in range(feldlaenge):
            farbe = int(255 * (float(F[Spalte][Reihe]) - h_min) / (h_max - h_min))
            draw.rectangle([(Reihe*s, Spalte*s),((Reihe+1)*s,(Spalte+1)*s)], (farbe, farbe, farbe), (255, 255, 255))

    # Einzeichnen des Rasters
    for i in range(0, feldbreite+1):
        draw.line([(0,i*s),(x_max,i*s)], (0, 0, 255), 1)
        draw.line([(i*s,0),(i*s,y_max)], (0, 0, 255), 1)

    while len(PP) >= 2:
        x1,y1 = PP[0].split()
        x2,y2 = PP[1].split()
        x1 = int(x1)
        y1 = int(y1) + 1
        x2 = int(x2)
        y2 = int(y2) + 1
        draw.line([(x1 * s, y1 * s), (x2 * s, y2 * s)], (255, 0, 0), 5)
        del PP[0]

    pic.save(name)
    pic.show()


# input: Zwei Koordinatenpunkte e1 und e2 im Format "x y"
# output: Ausgabe der Achsenbezeichnung, zu der die Kante e1,e2 parallel verlaeuft
def getdir(e1,e2):
    e1x,e1y = e1.split()
    e2x,e2y = e2.split()
    if e1x != e2x:
        return "x"
    elif e1y != e2y:
        return "y"

# Input: Zwei Knoten e1 und e2, die eine Kante bilden
# Output: Koordinaten, der beiden anliegenden Planquadrate und deren Hoehedifferenz
def kante(e1,e2):
    richtung = getdir(e1, e2)
    x1, y1 = e1.split()
    x2, y2 = e2.split()
    p1 = [None, None]
    p2 = [None, None]
    if richtung == "x":
        xm = min(int(x1), int(x2))
        p1 = [xm, int(y1)]
        p2 = [xm, int(y1) + 1]
    elif richtung == "y":
        ym = min(int(y1), int(y2))
        p1 = [int(x1) - 1, int(ym) + 1]
        p2 = [int(x1), int(ym) + 1]
    p1h = float(Feld[p1[1]][p1[0]])
    p2h = float(Feld[p2[1]][p2[0]])
    diff = round((p2h - p1h), 3)
    return p1,p2,diff


# Beginn des Programms
print()
print("- - - - - Programmstart - - - - -")
print()
print()



# - - - - -
# Schritt 1:
# Einlesen der Textdatei
# - - - - -

# Oeffnen der Datei mit der Feldmatrix
print("Dateiname der Textdatei.")
dateiname = input(">>> ")
textdatei = open(dateiname, "r")
print()

# Initialisierung der Matrix des Feldes
Feld = []
for line in textdatei:
    Reihe = line.split()
    if len(Reihe) != 1:
        Reihe2 = []
        for i in Reihe:
            x = aufrunden(i)
            Reihe2.append(x)
        Feld.append(Reihe2)
textdatei.close()

# Dimensionen des Feldes
feldlaenge = len(Feld)  # Breite
feldbreite = len(Feld[0])  # Laenge
h_max = 0 - float("inf")  # Hoehe
h_min = float("inf")  # Tiefe
for Reihe in Feld:
    for Zelle in Reihe:
        if float(Zelle) > h_max:
            h_max = float(Zelle)
        if float(Zelle) < h_min:
            h_min = float(Zelle)

# Prüfe auf rechteckigkeit des Feldes
for fx in Feld:
    if len(fx) != feldbreite:
        print("Eingabe nicht rechteckig")
        print()
        print()
        print(" - - - - - Programmende - - - - -")
        print()
        input()
        exit()

# Zwischenspeichern des Feldes
altesFeld = deepcopy(Feld)



# - - - - -
# Schritt 2:
# Initialisierung des Graphens
# - - - - -

# Aufsetzen der Knotenliste
Knoten = ["S","E"]
for y in range(feldlaenge - 1):
    for x in range(feldbreite + 1):
        Knoten.append( str(x) + " " + str(y) )


# Aufsetzen der Adjazenzmatrix
Adjazenzmatrix = [[-1 for x in range(len(Knoten))] for y in range(len(Knoten))]

# Gewichtung der Kanten
for i in Knoten:
    if i == "S":
        for j in Knoten:
            if j[0] == "0":
                Adjazenzmatrix[Knoten.index(i)][Knoten.index(j)] = 0
                Adjazenzmatrix[Knoten.index(j)][Knoten.index(i)] = 0
    elif i == "E":
        for j in Knoten:
            if j != "S" and j != "E":
                k = j.split()
                if k[0] == str(feldbreite):
                    Adjazenzmatrix[Knoten.index(i)][Knoten.index(j)] = 0
                    Adjazenzmatrix[Knoten.index(j)][Knoten.index(i)] = 0
    else:
        k = i.split()
        x = int(k[0])
        y = int(k[1])
        if x > 0 and y > 0 and x < feldbreite:
            i2 = str(x) + " " + str(y - 1)
            diff = aufrunden(nichtNegativ(1 - abs(float(Feld[y][x]) - float(Feld[y][x - 1]))) / 2)
            if diff == 0:
                diff = 0
            Adjazenzmatrix[Knoten.index(i)][Knoten.index(i2)] = diff
            Adjazenzmatrix[Knoten.index(i2)][Knoten.index(i)] = diff
        if y < feldlaenge - 1 and x < feldbreite:
            i2 = str(x + 1) + " " + str(y)
            diff = nichtNegativ(1 - abs(float(Feld[y][x]) - float(Feld[y + 1][x]))) / 2
            if diff == 0:
                diff = 0
            Adjazenzmatrix[Knoten.index(i)][Knoten.index(i2)] = diff
            Adjazenzmatrix[Knoten.index(i2)][Knoten.index(i)] = diff

print()




# - - - - -
# Schritt 3:
# Guenstigsten Blockadepfad finden
# - - - - -


# Dijkstra-Algorithmus
Dijkstra = []
Dijkstra.append(Knoten)  # Alle Knoten
Distanzen = [float("inf") for i in range(len(Knoten))]  # Distanzen sind alle unendlich
Distanzen[0] = 0  # Distanz des Startknotens ist 0
Dijkstra.append(Distanzen)  # Distanz
Dijkstra.append(["-1" for i in range(len(Knoten))])  # Vorgaenger

# Liste der noch zu besuchenden Knoten
unbesuchteKnoten = Knoten[:]

# Solange noch nicht alle Knoten besucht wurden:
while unbesuchteKnoten != []:

    # Finde den Knoten mit der kuerzesten Distanz
    kuerzesteDistanz = float("inf")
    naechsterKnoten = "-1"
    for i in unbesuchteKnoten:
        indexKnoten = Knoten.index(i)
        if Dijkstra[1][indexKnoten] < kuerzesteDistanz:
            kuerzesteDistanz = Dijkstra[1][indexKnoten]
            naechsterKnoten = Knoten[indexKnoten]

    # Speichere, dass dieser Knoten besucht wurde
    unbesuchteKnoten.remove(naechsterKnoten)

    # Besuche alle seine Nachbarknoten und ueberschreibe wenn noetig deren Distanz / Vorgaenger
    indexKnoten = Knoten.index(naechsterKnoten)
    Reihe = Adjazenzmatrix[indexKnoten]
    for i in range(len(Reihe)):
        if Reihe[i] != -1:
            distanz = round((float(Dijkstra[1][indexKnoten]) + float(Reihe[i])),4)
            if Dijkstra[1][i] > distanz:
                Dijkstra[1][i] = distanz
                Dijkstra[2][i] = naechsterKnoten

# Bestimmte den kuerzesten Pfad von S zu E
P = []
letzterKnoten = "E"
while letzterKnoten != "S":
    P.append(letzterKnoten)
    indexKnoten = Knoten.index(letzterKnoten)
    letzterKnoten = Dijkstra[2][indexKnoten]
P.append(letzterKnoten)
P.reverse()


# - - - - -
# Schritt 4:
# Umbauarbeiten angeben
# - - - - -

# Zwischenspeichern des Feldes
altesFeld = deepcopy(Feld)

P.remove("S")
P.remove("E")

Merkliste = [0 for i in range(len(P) - 1)]


aenderung1 = True
while aenderung1:
    aenderung1 = False
    Locks = [False for i in range(len(P) - 1)]
    for i in range(len(P) - 1):
        p1,p2,diff = kante(P[i], P[i + 1])
        if abs(diff) >= 1:
            Locks[i] = True
        else:
            aenderung1 = True
    aenderung2 = True
    while aenderung2:
        aenderung2 = False
        for ii in range(len(P) - 1):
            if not Locks[ii]:
                p1, p2, diff = kante(P[ii], P[ii + 1])
                if abs(diff) not in [1, 1.001]:
                    um = float(aufrunden((1 - abs(diff)) / 2))
                    if diff < 0:
                        um *= -1
                    Feld[p1[1]][p1[0]] = aufrunden(float(Feld[p1[1]][p1[0]]) - um)
                    Feld[p2[1]][p2[0]] = aufrunden(float(Feld[p2[1]][p2[0]]) + um)
                    Merkliste[ii] += um
                    aenderung2 = True


printMatrixMitPfad(altesFeld)
print()
print()
print()
printMatrixMitPfad(Feld)
print()
print()
print()
S = 0
for i in range(len(P)-1):
    p1, p2, diff = kante( P[i], P[i+1] )
    verschoben = aufrunden(round(abs(Merkliste[i]),3))
    S += float(verschoben)
    if round(Merkliste[i],3) < 0:
        print("Kippe von", p2, "nach", p1, "insgesamt", verschoben.replace(" ", "") , "Meter Erde.")
    elif round(Merkliste[i],3) > 0:
        print("Kippe von", p1, "nach", p2, "insgesamt", verschoben.replace(" ", "")  , "Meter Erde.")
    else:
        pass
print()
print("In der Summe werden", aufrunden(S).replace(" ", "") ,"Meter Erde verschoben.")



# Ausgabe der Laufzeit
print()
print()
print("Laufzeit:", str(time.process_time()), "s")


for Reihe in Feld:
    for Zelle in Reihe:
        if float(Zelle) > h_max:
            h_max = float(Zelle)
        if float(Zelle) < h_min:
            h_min = float(Zelle)


# Ausgabe der Bilddateien
bilddateiname = ""
for i in range(len(dateiname)-4):
    bilddateiname += dateiname[i]

ZeichneFeld(altesFeld, str( "input-"+bilddateiname+".png") )
ZeichneFeldMitPfad(Feld, P, str("output-" + bilddateiname + ".png"))


# Programmende
print()
print()
print(" - - - - - Programmende - - - - -")
print()