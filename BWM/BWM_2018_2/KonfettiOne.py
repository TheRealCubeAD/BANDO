
import time
import math
from copy import deepcopy


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

# Beginn des Programms
print()
print("- - - - - Programmstart - - - - -")
print()
print()


print()
print("Wie gross soll das Quadrat sein?")
b = int(input(">>> "))
print()


