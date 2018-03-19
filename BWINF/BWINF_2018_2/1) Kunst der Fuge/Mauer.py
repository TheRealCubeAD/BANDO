# Import des Zufallsmoduls
import random

# Um Pillow in PyCharm zu nuttzen:
# Strg + Alt + S -> Project Interpretor -> grünes Plus -> "Pillow"

# Import der Image Library
from PIL import Image, ImageDraw


# Beginn des Programms
print()
print("- - - - - Programmstart - - - - -")
print()
print()

# Eingabe von n
print("Gib n an.")
n = int(input(">>> "))

print()
print()

# Berechnungen der relevanten Angaben
fugenProReihe = n - 1
fugenInMauer = int(n * (n + 1) / 2 - 1)
anzahlReihen = int(fugenInMauer / fugenProReihe)

# Matrizen und Listen fuer das Backtracking
Fugen = [[0 for x in range(fugenProReihe)] for y in range(anzahlReihen)]
freieFugen = [i + 1 for i in range(fugenInMauer)]
Mauer = [[0 for x in range(n)] for y in range(anzahlReihen)]

# Methode zur Ausgabe einer Matrix
def printMatrix(matrix):
    for i in range(len(matrix)):
        reihe = matrix[i]
        print(reihe)


# Funktion: FindeLoesung(Matrizen und Listen)
def findeMauer(Fugen, freieFugen, Mauer):

    # Kopiere die Liste der freien Fugen
    durchzuprobierendeFreieFugen = freieFugen[:]
    # Suche nach der ersten freien Fuge in der Fugenmatrix
    for y in range(anzahlReihen):
        for x in range(fugenProReihe):
            if Fugen[y][x] == 0:
                if x > 0:
                    # Betrachte die Fuge vor der ersten leeren
                    groesteFuge = Fugen[y][x-1]
                    try:
                        # Alle Fugen kleiner als die vorhergehende muessen nicht ausporbiert werden
                        while durchzuprobierendeFreieFugen[0] <= groesteFuge:
                            del durchzuprobierendeFreieFugen[0]
                    except IndexError:
                        pass
                break
        if Fugen[y][x] == 0:
            break

    # Solange es noch Moeglichkeiten zum Durchprobieren gibt:
    while durchzuprobierendeFreieFugen != []:
        # a) waehle einen neuen Teil-Loesungsschritt:
        # Suche eine zufaellige Moeglichkeit aus
        fuge = random.choice(durchzuprobierendeFreieFugen)
        # Suche die erste leere Fuge
        for y in range(anzahlReihen):
            for x in range(fugenProReihe):
                if Fugen[y][x] == 0:
                    # I) erweitere Matrizen um Wahl:
                    # Setze die auszuprobierende Fuge ein
                    Fugen[y][x] = fuge
                    # Erweitere die Mauermatrix in Abhaengigkeit von der Fugenmatrix
                    if x == 0:
                        Mauer[y][x] = fuge
                    else:
                        mauerSumme = 0
                        for i in range(x):
                            mauerSumme += Mauer[y][i]
                        Mauer[y][x] = fuge - mauerSumme
                    if x == fugenProReihe - 1:
                        Mauer[y][x+1] = int(n * (n + 1) / 2) - fuge
                    # Setze die eingesetzte Fuge auf nicht-frei
                    freieFugen.remove(fuge)
                    # b) falls Wahl gueltig ist:
                    # Ueberpruefe, ob in der Mauer keine zwei Kloetzchen der gleichen Laenge sind
                    if gueltigeMauer(Mauer):
                        # II) falls Matrix vollständig ist, return true; // Loesung gefunden!
                        # Ueberpuefe, ob die Mauer vollstaendig ist
                        if mauerVollstaendig(Mauer):
                            # Wenn Ja, Dann gib die Mauer aus
                            print("Mauer:")
                            printMatrix(Mauer)
                            print()
                            print("Fugen:")
                            printMatrix(Fugen)
                            print()
                            print("freie Fugen:")
                            print(freieFugen)
                            print()
                            # Loesung gefunden:
                            return True
                        else:
                            # falls findeMauer(Fugen, freieFugen, Mauer)) return true; // Loesung!
                            # Suche auf Basis der eingesetzten Werte weiter nach der Mauer:
                            if findeMauer(Fugen, freieFugen, Mauer):
                                return True
                    # mache Wahl rueckgaengig, da es fuer diese Werte keine Loesung gibt
                    Fugen[y][x] = 0
                    Mauer[y][x] = 0
                    if x == fugenProReihe - 1:
                        Mauer[y][x + 1] = 0
                    freieFugen.append(fuge)
                    freieFugen.sort()
                    break
            if Fugen[y][x] == 0:
                break
        # Entferne die durchzuprobierende Option, da diese durchprobiert wurde
        durchzuprobierendeFreieFugen.remove(fuge)
    # 2. Da es keinen neuen Teil-Loesungsschritt gibt: return false // Keine Loesung!
    return False



# Ueberprueft, ob in einer Reihe keine zwei Kloetchen gleich lang sind bzw. zu lang bzw. zu kurz sind
def gueltigeMauer(Mauer):
    for r in Mauer:
        K = []
        for k in r:
            K.append(k)
            if (K.count(k) > 1 and k != 0) or k > n or k < 0:
                return False
    return True

# Ueberprueft, ob in jeder Reihe alle Laengen von 1 bis n vorkommen
def mauerVollstaendig(Mauer):
    for r in Mauer:
        for k in r:
            if k == 0:
                return False
    return True


# Setze die Hoehe der Mauermatrix auf die Obergrenze und probiere von da runter
while True:

    # Vorbereitung fuer das Backtracking
    Fugen = [[0 for x in range(fugenProReihe)] for y in range(anzahlReihen)]
    freieFugen = [i + 1 for i in range(fugenInMauer)]
    Mauer = [[0 for x in range(n)] for y in range(anzahlReihen)]

    if findeMauer(Fugen, freieFugen, Mauer):
        break

    # Falls es fuer diese Hoehe keine Mauer gab, versuch es mit der naechst kleineren
    anzahlReihen -= 1

# Visuelle Ausgabe
s = 40  # Streckfaktor s
x_max = int( s * ( n * (n + 1) / 2 ) )  # Breite
y_max = int( s * anzahlReihen )  # Hoehe

# Initialisierung des Bildes
pic = Image.new("1", ((x_max+1, y_max+1)), 1)
draw = ImageDraw.Draw(pic)

# Einzeichnen der Grundlinien
for i in range(0, anzahlReihen+1):
    draw.line([(0,i*s),(x_max,i*s)])
draw.line([(0,0),(0,y_max)])
draw.line([(x_max,0),(x_max,y_max)])

# Einzeichenen der Fugen
for R in range(0,len(Mauer)):
    r = 0
    Reihe = Mauer[R]
    for f in range(0,len(Reihe)):
        r += Reihe[f]
        draw.line([(r*s, R*s), (r*s, (R+1)*s)])

pic.save( str(n)+"-Mauer.png")
pic.show()



# Programmende
print()
print(" - - - - - Programmende - - - - -")
print()