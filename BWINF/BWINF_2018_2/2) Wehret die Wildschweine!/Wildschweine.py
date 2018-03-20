import time
from PIL import Image, ImageDraw
from copy import deepcopy

# Um Pillow in PyCharm zu nuttzen:
# Strg + Alt + S -> Project Interpretor -> Pluszeichen -> "Pillow"

# Methode zur Ausgabe einer Matrix
def printMatrix(matrix):
    for i in range(len(matrix)):
        reihe = matrix[i]
        print(reihe)

def betrag(n):
    if n < 0:
        return -1 * n
    else:
        return n

def nichtNegativ(n):
    if n < 0:
        return 0
    else:
        return n

def aufrunden(n):
    n = str(n)
    if len(n) < 5:
        while len(n) < 5:
            n += "0"
        n2 = n
    elif len(n) >= 5:
        n2 = int(float(n)*1000)
        n2 += 1
        n2 = n2 / 1000
        n2 = str(n2)
    return n2


def ZeichneFeld(F):

    # Visualisierung:

    global h_max
    global feldbreite
    global feldlaenge

    s = 50
    x_max = feldbreite * s
    y_max = feldlaenge * s

    # Initialisierung des Bildes
    pic = Image.new("RGB", ((x_max+1, y_max+1)), (255, 255, 255))
    draw = ImageDraw.Draw(pic)

    for Reihe in range(feldbreite):
        for Spalte in range(feldlaenge):
            farbe = int( 255 * float(F[Spalte][Reihe]) / h_max )
            draw.rectangle([(Reihe*s, Spalte*s),((Reihe+1)*s,(Spalte+1)*s)], (farbe, farbe, farbe), (255, 255, 255))

    # Einzeichnen des Rasters
    for i in range(0, feldbreite+1):
        draw.line([(0,i*s),(x_max,i*s)], (0, 0, 255))
        draw.line([(i*s,0),(i*s,y_max)], (0, 0, 255))

    pic.show()


def ZeichneFeldMitPfad(F, P):

    # Visualisierung:

    global h_max
    global feldbreite
    global feldlaenge

    s = 50
    x_max = feldbreite * s
    y_max = feldlaenge * s

    # Initialisierung des Bildes
    pic = Image.new("RGB", ((x_max+1, y_max+1)), (255, 255, 255))
    draw = ImageDraw.Draw(pic)

    for Reihe in range(feldbreite):
        for Spalte in range(feldlaenge):
            farbe = int( 255 * float(F[Spalte][Reihe]) / h_max )
            draw.rectangle([(Reihe*s, Spalte*s),((Reihe+1)*s,(Spalte+1)*s)], (farbe, farbe, farbe), (255, 255, 255))

    # Einzeichnen des Rasters
    for i in range(0, feldbreite+1):
        draw.line([(0,i*s),(x_max,i*s)], (0, 0, 255))
        draw.line([(i*s,0),(i*s,y_max)], (0, 0, 255))

    del P[0]
    del P[len(P)-1]

    while len(P) >= 2:
        xy1 = P[0].split()
        xy2 = P[1].split()
        x1 = int(xy1[0])
        y1 = int(xy1[1]) + 1
        x2 = int(xy2[0])
        y2 = int(xy2[1]) + 1
        draw.line([(x1 * s, y1 * s), (x2 * s, y2 * s)], (255, 0, 0))
        del P[0]

    pic.show()

# Beginn des Programms
print()
print("- - - - - Programmstart - - - - -")
print()
print()


# - - - - -
# Schritt 1:
# Einlesen der Textdatei
# - - - - -

print("Dateiname der Textdatei.")
dateiname = input(">>> ")
textdatei = open(dateiname, "r")

# Matrix des Feldes
Feld = []
for line in textdatei:
    Reihe = line.rstrip()
    Reihe = Reihe.split()
    for i in Reihe:
        i = float(i)
    if len(Reihe) != 1:
        Feld.append(Reihe)
textdatei.close()

# Masse des Feldes
feldlaenge = len(Feld)
feldbreite = len(Feld[0])


h_max = 0
for Reihe in Feld:
    for Zelle in Reihe:
        if float(Zelle) > h_max:
            h_max = float(Zelle)

altesFeld = deepcopy(Feld)

# - - - - -
# Schritt 2:
# Aufsetzen der Matrizen
# - - - - -

Knoten = []
Knoten.append("S")
Knoten.append("E")
for y in range(feldlaenge - 1):
    for x in range(feldbreite + 1):
        Knoten.append( str(x) + " " + str(y) )


# Setze die Adjazenzmatrix auf
Adjazenzmatrix = [[-1 for x in range(len(Knoten))] for y in range(len(Knoten))]

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
            dif = aufrunden( nichtNegativ( 1 - betrag(float(Feld[y][x]) - float(Feld[y][x-1])) ) / 2 )
            if dif == 0:
                dif = 0
            Adjazenzmatrix[Knoten.index(i)][Knoten.index(i2)] = dif
            Adjazenzmatrix[Knoten.index(i2)][Knoten.index(i)] = dif
        if y < feldlaenge - 1 and x < feldbreite:
            i2 = str(x + 1) + " " + str(y)
            dif = nichtNegativ( 1 - betrag(float(Feld[y][x]) - float(Feld[y+1][x])) ) / 2
            if dif == 0:
                dif = 0
            Adjazenzmatrix[Knoten.index(i)][Knoten.index(i2)] = dif
            Adjazenzmatrix[Knoten.index(i2)][Knoten.index(i)] = dif

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

# noch zu besuchende Knoten
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

    indexKnoten = Knoten.index(naechsterKnoten)
    Reihe = Adjazenzmatrix[indexKnoten]
    for i in range(len(Reihe)):
        if Reihe[i] != -1:
            distanz = float(Dijkstra[1][indexKnoten]) + float(Reihe[i])
            if Dijkstra[1][i] > distanz:
                Dijkstra[1][i] = distanz
                Dijkstra[2][i] = naechsterKnoten

Pfad = []
letzterKnoten = "E"
while letzterKnoten != "S":
    Pfad.append(letzterKnoten)
    indexKnoten = Knoten.index(letzterKnoten)
    letzterKnoten = Dijkstra[2][indexKnoten]
Pfad.append(letzterKnoten)
Pfad.reverse()


# - - - - -
# Schritt 4:
# Umbauarbeiten angeben
# - - - - -

S = 0

for i in range(1, len(Pfad)-2):
    xy1 = Pfad[i]
    xy2 = Pfad[i+1]
    dif = float(Adjazenzmatrix[Knoten.index(xy1)][Knoten.index(xy2)])
    if dif > 0:
        xy1_ = xy1.split()
        xy2_ = xy2.split()
        x1 = int(xy1_[0])
        y1 = int(xy1_[1])
        x2 = int(xy2_[0])
        y2 = int(xy2_[1])
        if x1 > x2 and y1 == y2:
            feld1 = float(Feld[y1][x2])
            feld2 = float(Feld[y1+1][x2])
            if feld1 < feld2:
                Kox1 = x2
                Koy1 = y1
                Kox2 = x2
                Koy2 = y1+1
                Feld[y1][x2] = aufrunden( float(Feld[y1][x2]) - dif )
                Feld[y1+1][x2] = aufrunden( float(Feld[y1+1][x2]) + dif )
            else:
                Kox1 = x2
                Koy1 = y1+1
                Kox2 = x2
                Koy2 = y1
                Feld[y1][x2] = aufrunden( float(Feld[y1][x2]) + dif )
                Feld[y1+1][x2] = aufrunden( float(Feld[y1+1][x2]) - dif )
        elif x1 < x2 and y1 == y2:
            feld1 = float(Feld[y1][x1])
            feld2 = float(Feld[y1+1][x1])
            if feld1 < feld2:
                Kox1 = x1
                Koy1 = y1
                Kox2 = x1
                Koy2 = y1+1
                Feld[y1][x1] = aufrunden( float(Feld[y1][x1]) - dif )
                Feld[y1+1][x1] = aufrunden( float(Feld[y1+1][x1]) + dif )
            else:
                Kox1 = x1
                Koy1 = y1+1
                Kox2 = x1
                Koy2 = y1
                Feld[y1][x1] = aufrunden( float(Feld[y1][x1]) + dif )
                Feld[y1 + 1][x1] = aufrunden( float(Feld[y1 + 1][x1]) - dif )
        elif x1 == x2 and y1 > y2:
            feld1 = float(Feld[y1][x1])
            feld2 = float(Feld[y1][x1-1])
            if feld1 < feld2:
                Kox1 = x1
                Koy1 = y1
                Kox2 = x1-1
                Koy2 = y1
                Feld[y1][x1] = aufrunden( float(Feld[y1][x1]) - dif )
                Feld[y1][x1-1] = aufrunden( float(Feld[y1][x1-1]) + dif )
            else:
                Kox1 = x1
                Koy1 = y1
                Kox2 = x1 - 1
                Koy2 = y1
                Feld[y1][x1] = aufrunden( float(Feld[y1][x1]) + dif )
                Feld[y1][x1-1] = aufrunden( float(Feld[y1][x1-1]) - dif )
        elif x1 == x2 and y1 < y2:
            feld1 = float(Feld[y2][x1])
            feld2 = float(Feld[y2][x1-1])
            if feld1 < feld2:
                Kox1 = x1
                Koy1 = y2
                Kox2 = x1-1
                Koy2 = y2
                Feld[y2][x1] = aufrunden( float(Feld[y2][x1]) - dif )
                Feld[y2][x1-1] = aufrunden( float(Feld[y2][x1-1]) + dif )
            else:
                Kox1 = x1-1
                Koy1 = y2
                Kox2 = x1
                Koy2 = y2
                Feld[y2][x1] = aufrunden( float(Feld[y2][x1]) + dif )
                Feld[y2][x1-1] = aufrunden( float(Feld[y2][x1-1]) - dif )

        dif = aufrunden(dif)
        print("Kippe von", "(" + str(Kox1) + "," + str(Koy1) + ")", "nach", "(" + str(Kox2) + "," + str(Koy2) + ")",
              str(dif), "m")
        dif = float(dif)
        S += dif
        feld1 += dif
        feld2 -= dif
        Adjazenzmatrix[Knoten.index(xy1)][Knoten.index(xy2)] = 0
        Adjazenzmatrix[Knoten.index(xy2)][Knoten.index(xy1)] = 0

print()
print("Es wurden insgesmt", str(S), "m", "Erde verschoben.")

for Reihe in Feld:
    for Zelle in Reihe:
        if float(Zelle) > h_max:
            h_max = float(Zelle)

print(Pfad)

printMatrix(altesFeld)
printMatrix(Feld)

ZeichneFeld(altesFeld)
ZeichneFeldMitPfad(Feld, Pfad)


print()
print()
print("Laufzeit:", str(time.process_time()), "s")

# Programmende
print()
print()
print(" - - - - - Programmende - - - - -")
print()