
import time



# - - - - - Programminterne Moduswahl - - - - -
#modus = "quadrat"
modus = "quadrat_schnell"
#modus = "rechteck"
#modus = "rechteck_schnell"


#
# Beginn des Programms
print()
print("- - - - - Programmstart - - - - -")
print()
print()

if modus == "quadrat":

    # e = Groese der Ebene
    print()
    print("Wie gross soll das Quadrat sein?")
    b = int(input(">>> "))
    h = b

    print()
    print("Sollen die Denkschritte ausgegeben werden?", "( Ja: (1), Nein: (0) )")
    lautDenken = bool(int(input(">>> ")))


elif modus == "quadrat_schnell":

    # e = Groese der Ebene
    print()
    print("Wie gross soll das Quadrat sein?")
    b = int(input(">>> "))
    h = b
    lautDenken = False


elif modus == "rechteck":

    # e = Groese der Ebene
    print()
    print("Wie breit soll die Ebene sein?")
    b = int(input(">>> "))

    print()
    print("Wie hoch soll die Ebene sein?")
    h = int(input(">>> "))

    print()
    print("Sollen die Denkschritte ausgegeben werden?", "( Ja: (1), Nein: (0) )")
    lautDenken = bool(int(input(">>> ")))


elif modus == "rechteck_schnell":

    # e = Groese der Ebene
    print()
    print("Wie breit soll die Ebene sein?")
    b = int(input(">>> "))

    print()
    print("Wie hoch soll die Ebene sein?")
    h = int(input(">>> "))

    lautDenken = False

print()
print()
e = min(b, h)

# n = Anzahl der Farben
n = 1


# Methode zur Ausgabe einer Matrix
def printMatrix(matrix):
    for i in range(len(matrix)):
        reihe = matrix[i]
        print(reihe)



# Methode zur Bestimmung eines richtig gestzten Quadrats
def farbeGueltig(Ebene, x, y):

    # Probiere alle Groessen aus
    for i in range(1, e):
        # Probiere alle Richtungen aus
        for j in range(4):

            Quadrat = [] # Alle Farben eines Quadrats
            Quadrat.append( Ebene[y][x] ) # Fokus Punkt

            # rechts oben
            if j == 0 and x + i <= b - 1 and y + i <= h - 1:
                Quadrat.append( Ebene[y][x + i] ) # rechts
                Quadrat.append( Ebene[y + i][x] ) # oben
                Quadrat.append( Ebene[y + i][x + i] ) # rechts oben

            # rechts unten
            if j == 1 and x + i <= b - 1 and y - i >= 0:
                Quadrat.append( Ebene[y][x + i] ) # rechts
                Quadrat.append( Ebene[y - i][x] ) # unten
                Quadrat.append( Ebene[y - i][x + i] ) # rechts unten

            # links oben
            if j == 2 and x - i >= 0 and y + i <= h - 1:
                Quadrat.append( Ebene[y][x - i] ) # links
                Quadrat.append( Ebene[y + i][x] ) # oben
                Quadrat.append( Ebene[y + i][x - i] ) # links oben

            # links unten
            if j == 3 and x - i >= 0 and y - i >= 0:
                Quadrat.append(Ebene[y][x - i]) # links
                Quadrat.append(Ebene[y - i][x]) # unten
                Quadrat.append( Ebene[y - i][x - i] ) # links unten

            if len(Quadrat) == 4:
                for k in Quadrat:
                    if Quadrat.count(k) >= 3 and k != -1:
                        return False

    return True


def findeFaerbung(Ebene):

    # Gehe die Ebene durch
    for y in range(h):
        for x in range(b):

            # Suche nach dem ersten unbesetzten Feld
            if Ebene[y][x] == -1:

                # Probiere alle Farben durch
                for f in Farben:
                    Ebene[y][x] = f

                    if lautDenken:
                        print()
                        printMatrix(Ebene)

                    # Ueberpruefe die eingesetzte Farbe
                    if farbeGueltig(Ebene, x, y):

                        # Ueberpruefe die Ebene vollstaendig ist
                        if x == b - 1 and y == h - 1:
                            if not lautDenken:
                                print()
                                printMatrix(Ebene)
                            return True

                        # Suche weiter
                        if findeFaerbung(Ebene):
                            return True

                Ebene[y][x] = -1

                if lautDenken:
                    print()
                    printMatrix(Ebene)

                return False


while n <= e:

    # Alle erlaubten Farben
    Farben = [f for f in range(n)]

    # Ebene
    Ebene1 = [[-1 for x in range(b)] for y in range(h)]

    if lautDenken:
        print()
        print()
        print()
        print("n =",n)

    if findeFaerbung(Ebene1):
        break

    # Erhoehe die Anzahl der Farben um 1
    n += 1


print()
print("Ein", str(b)+"x"+str(h)+"-Feld", "braucht mindestens", n, "Farben.")


print()
print()
print("Laufzeit:", str(time.process_time()), "s")

# Programmende
print()
print()
print(" - - - - - Programmende - - - - -")
print()