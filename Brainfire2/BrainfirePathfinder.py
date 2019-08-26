
# - Importware - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



import math # <3
import sys # Aus Stack Overflow kopiert
sys.stdout.flush() # https://stackoverflow.com/questions/493386/how-to-print-without-newline-or-space
import time # "The laws of time are mine and they will obey me!"
from copy import deepcopy # fuer das Zwischenspeichern von Bearbeitungsversuchen des Feldes





# - Textmethoden - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



"""
Input: Ein String
Output: N/A, Gibt einen Texttrenner mit dem eingebenen String in der Mitte aus
"""
def textDivider(string):
    # Die folgende Formel ergibt sich aus dieser Ueberlegung:
    # Nach Moeglichkeit soll der Texttrenner ~ 120 Zeichen lang sein.
    # Der String nimmt len(string) Zeichen ein.
    # Links und rechts des zentrierten Strings liegen eine gleiche gerade Anzahl an Zeichen.
    anz = math.floor( ( 90 - len(string) ) / 4 )
    # Zusammenbauen des Strings
    print("- "*anz + string + " -"*anz)



"""
Input: N/A
Output: N/A, Gibt einen Texttrenner aus
"""
def neutralDivider():
    print("- "*45)



"""
Input: eine natuerliche Zahl n
Output: N/A, Leasst n Zeilen aus
"""
def newline(n):
    for i in range(n):
        print()



"""
Input: N/A
Output: N/A, Gibt ein Titelmenue aus
"""
def titlescreen(title, author):
    newline(10)
    neutralDivider()
    textDivider(title)
    textDivider(author)
    neutralDivider()



"""
Input: N/A
Output: int, eine ganze Zahl, die vom Nutzer eingegeben wird
"""
def intChoice():
    inp = input(">>> ")
    try:
        if float(inp) != int(inp):
            Fehler = int("Erzeuge ValueError")
        inp = int(inp)
    except ValueError:
        print("Die Eingabe ist keine ganze Zahl.")
        return intChoice()
    return inp



"""
Input: int min, int max
Output: int, eine natuerliche Zahl zwischen min und max, die vom Nutzer eingegeben wird
"""
def intIntervallChoice(min, max):
    inp = intChoice()
    if min <= inp <= max:
        return inp
    else:
        print("Die Eingabe liegt nicht im gültige Intervall.")
        return(intIntervallChoice(min,max))



"""
Input: String string, int length
Output: string, der Eingabe String, nur am Anfang verlaengert
"""
def f(string, length):
    string = str(string)
    while len(string) < length:
        string = " " + string
    return string


"""
Input: Matrix
Output: N/A, gibt die Matrix aus
"""
def printMatrix(matrix):
    newline(1)
    for i in range(len(matrix)):
        reihe = matrix[i]
        print(reihe)
    newline(1)



titlescreen("Pathfinder for Brainfire","by Alex Duca")





# - Ausgabemethoden - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



def printLeererRaum(breite, hoehe):

    Matrix = [[" " for y in range(hoehe)] for x in range(breite)]
    printMatrixRaum(Matrix)



def printMatrixRaum(Matrix):

    hoehe = len(Matrix)
    breite = len(Matrix[0])

    ersteZeile = "╔═══" + "╦═══" * (breite - 1) + "╗"
    mittlereZeile = "╠═══" + "╬═══" * (breite - 1) + "╣"
    letzteZeile = "╚═══" + "╩═══" * (breite - 1) + "╝"

    newline(1)
    print(ersteZeile)
    print(stringArray(Matrix[0]))
    for i in range(hoehe-1):
        print(mittlereZeile)
        print(stringArray(Matrix[i+1]))
    print(letzteZeile)
    newline(1)



def stringArray(Array):
    string = "║"
    for i in Array:
        string += " "
        string += i
        string += " ║"
    return string



newline(3)
print("Wie viele Felder ist der Raum breit?")
hoehe = intIntervallChoice(2, float("inf"))
newline(1)
print("Wie viele Felder ist der Raum hoch?")
breite = intIntervallChoice(2, float("inf"))
newline(1)


Matrix = [[" " for y in range(breite)] for x in range(hoehe)]

startPos = (1,0)
endPos = ( hoehe - 1 - 1, breite - 1 )

# printMatrixRaum(Matrix)





# - Pathfinding - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def pfeil(richtung):
    if richtung == (1,0):
        return "↓"
    elif richtung == (0,1):
        return "→"
    elif richtung == (-1,0):
        return "↑"
    elif richtung == (0,-1):
        return "←"

def inRange(pos):
    global hoehe, breite
    if 0 <= pos[0] <= (hoehe-1) and 0 <= pos[1] <= (breite-1):
        return True
    else:
        return False




alleRaeume = []
Richtungen = [ (1,0), (0,1), (-1,0), (0,-1) ]

def startBacktracking(Matrix):

    # Globale Informationen
    global alleRaeume, Richtungen, hoehe, breite, startPos, endPos
    alleRaeume = []
    backupKopieMatrix = deepcopy(Matrix)

    # Probiere in alle Richtungen
    for richtung in Richtungen:

        neuePos = startPos
        Matrix = deepcopy(backupKopieMatrix)



        while True:

            altePos = neuePos

            # Probiere einen Schritt nach vorne
            neuePos = ( altePos[0] + richtung[0], altePos[1] + richtung[1] )

            # Wenn du gegen eine Wand stoesst
            if not inRange(neuePos):
                MatrixKopie = deepcopy(Matrix)
                backtracking(MatrixKopie, neuePos, richtung)
                # Wir sind dann auch fertig fuer die Richtung
                break

            # Lege einen Pfeil auf dem Boden in aktuelle Laufrichtung
            Matrix[neuePos[0]][neuePos[1]] = pfeil(richtung)


            # Versuche einen Stein vor die neue Position zu legen und starte Backtracking
            stein = ( neuePos[0] + richtung[0], neuePos[1] + richtung[1] )
            if inRange(stein):

                Matrix[ stein[0] ][ stein[1] ] = "●"
                MatrixKopie = deepcopy(Matrix)
                backtracking(MatrixKopie, neuePos, richtung)

                # Nach erfolgreihem Steinelegen, nimm ihn wieder weg und lauf weiter in die Richtung
                Matrix[ stein[0] ][ stein[1] ] = " "




    for Raum in alleRaeume:
        printMatrixRaum(Raum)

    print(len(alleRaeume))

def backtracking(Matrix, eigenePos, letzteRichtung):

    # Globale Informationen
    global alleRaeume, Richtungen, hoehe, breite, startPos, endPos

    Matrix[startPos[0]][startPos[1]] = "S"
    Matrix[endPos[0]][endPos[1]] = "Z"

    MatrixKopie = deepcopy(Matrix)

    alleRaeume.append(MatrixKopie)


startBacktracking(Matrix)
