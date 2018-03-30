import time
from PIL import Image, ImageDraw
from copy import deepcopy
from math import ceil
# Um Pillow in PyCharm zu nuttzen:
# Strg + Alt + S -> Project Interpretor -> Pluszeichen -> "Pillow"

# input: eine Matrix
# Korrekt formatierte Ausgabe der Matrix im Textfeld
def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


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
    n2 = str(float(ceil(n*1000)/1000))
    a = 5
    if n2[0] == "-":
        a += 1
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


# input: eine Feldmatrix mit Pfad einer roten Linie une Dateinamen
# Genau wie ZeichneFeld(F, name) nur mit einem zusaetzlich eingezeichnetem Pfad
def ZeichneFeldMitPfad(F, P, name):

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

    while len(P) >= 2:
        x1,y1 = P[0].split()
        x2,y2 = P[1].split()
        x1 = int(x1)
        y1 = int(y1) + 1
        x2 = int(x2)
        y2 = int(y2) + 1
        draw.line([(x1 * s, y1 * s), (x2 * s, y2 * s)], (255, 0, 0), 5)
        del P[0]

    pic.save(name)
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
        for i in Reihe:
            i = float(i)
        Feld.append(Reihe)
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
    if len(fx) != feldlaenge:
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
            dif = aufrunden( nichtNegativ( 1 - abs(float(Feld[y][x]) - float(Feld[y][x-1])) ) / 2 )
            if dif == 0:
                dif = 0
            Adjazenzmatrix[Knoten.index(i)][Knoten.index(i2)] = dif
            Adjazenzmatrix[Knoten.index(i2)][Knoten.index(i)] = dif
        if y < feldlaenge - 1 and x < feldbreite:
            i2 = str(x + 1) + " " + str(y)
            dif = nichtNegativ( 1 - abs(float(Feld[y][x]) - float(Feld[y+1][x])) ) / 2
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
            distanz = float(Dijkstra[1][indexKnoten]) + float(Reihe[i])
            if Dijkstra[1][i] > distanz:
                Dijkstra[1][i] = distanz
                Dijkstra[2][i] = naechsterKnoten

# Bestimmte den kuerzesten Pfad von S zu E
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

# A) Teile den roten Pfad in moeglichst lange geradlinigie bzw. auschliessliche eckige Pfade auf
# B) Bearbeite die geradlinigen Teilpfade mit dem gewoehnlich Algorithmus
# C) Bearbeite die eckigen Pfade wie folgt:
#    Wiederhole solange, bis es nach einem Durchlauf keine Aenderung mehr gibt:
#  I) "Locke" alle Kanten, wo die Hoehendifferenz 1 oder groesser ist.
#  II) Wiederhole solange, bis es nach einem Durchlauf keine Aenderung mehr gibt:
#     a) Gehe alle Kanten der Reihe nach durch und kippe ueber die Kante die Menge an Erde,
#        damit die Hoehendifferenz nach der Umbauarbeit genau 1 oder genau 1.001 ist.
# => Wichtig ist alle Aenderungen zu speichern und am Ende die Gesamtaenderung auszugeben.

Pfad.remove("S")
Pfad.remove("E")

def getdir(e1,e2):
    e1x,e1y = e1.split()
    e2x,e2y = e2.split()
    if e1x != e2x:
        return "x"
    elif e1y != e2y:
        return "y"

gerade_pfade = []
ecken = []
eck_pfade = []
for ei in range(len(Pfad)):
    try:
        if getdir(Pfad[ei],Pfad[ei+1]) != getdir(Pfad[ei+1],Pfad[ei+2]):
            ecken.append(ei+1)
    except IndexError:
        pass

last_ecke = -1
for ei in ecken+[len(Pfad)]:
    cur_gerade = []
    for kn in range(last_ecke+1,ei):
        cur_gerade.append(Pfad[kn])
    gerade_pfade.append(cur_gerade)
    last_ecke = ei


print(ecken)
print(gerade_pfade)
print(Pfad)

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

# ZeichneFeld(altesFeld, str( "input-"+bilddateiname+".png") )
ZeichneFeldMitPfad(Feld, Pfad, str( "output-"+bilddateiname+".png"))


# Programmende
print()
print()
print(" - - - - - Programmende - - - - -")
print()
input("töte mich")