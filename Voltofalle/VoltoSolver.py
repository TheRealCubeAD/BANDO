
# - Import - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


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
def titlescreen():
    newline(3435)
    neutralDivider()
    textDivider("Volto-Solver")
    textDivider("by Alex Duca")
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

titlescreen()


"""
Input: String string, int length
Output: string, der Eingabe String, nur am Anfang verlaengert
"""
def f(string, length):
    string = str(string)
    while len(string) < length:
        string = " " + string
    return string


# Methode zur Ausgabe einer Matrix
def printMatrix(matrix):
    newline(1)
    for i in range(len(matrix)):
        reihe = matrix[i]
        print(reihe)
    newline(1)

# - Spielmethoden - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Legende:
"""
╔════╦════╦════╦════╦════╗────┐
║  1 ║  2 ║  3 ║  4 ║  5 ║    │
╠════╬════╬════╬════╬════╣────┤
║  6 ║  7 ║  8 ║  9 ║ 10 ║    │
╠════╬════╬════╬════╬════╣────┤
║ 11 ║ 12 ║ 13 ║ 14 ║ 15 ║    │
╠════╬════╬════╬════╬════╣────┤
║ 16 ║ 17 ║ 18 ║ 19 ║ 20 ║    │
╠════╬════╬════╬════╬════╣────┤
║ 21 ║ 22 ║ 23 ║ 24 ║ 25 ║    │
╚════╩════╩════╩════╩════╝────┘
│    │    │    │    │    │
└────┴────┴────┴────┴────┘
"""

def printLegendeFelder():
    newline(1)
    print("╔════╦════╦════╦════╦════╗────┐")
    print("║  1 ║  2 ║  3 ║  4 ║  5 ║    │")
    print("╠════╬════╬════╬════╬════╣────┤")
    print("║  6 ║  7 ║  8 ║  9 ║ 10 ║    │")
    print("╠════╬════╬════╬════╬════╣────┤")
    print("║ 11 ║ 12 ║ 13 ║ 14 ║ 15 ║    │")
    print("╠════╬════╬════╬════╬════╣────┤")
    print("║ 16 ║ 17 ║ 18 ║ 19 ║ 20 ║    │")
    print("╠════╬════╬════╬════╬════╣────┤")
    print("║ 21 ║ 22 ║ 23 ║ 24 ║ 25 ║    │")
    print("╚════╩════╩════╩════╩════╝────┘")
    print("│    │    │    │    │    │     ")
    print("└────┴────┴────┴────┴────┘     ")
    newline(1)



# Legende:
"""
╔════╦════╦════╦════╦════╗────┐
║    ║    ║    ║    ║    ║  1 │
╠════╬════╬════╬════╬════╣────┤
║    ║    ║    ║    ║    ║  2 │
╠════╬════╬════╬════╬════╣────┤
║    ║    ║    ║    ║    ║  3 │
╠════╬════╬════╬════╬════╣────┤
║    ║    ║    ║    ║    ║  4 │
╠════╬════╬════╬════╬════╣────┤
║    ║    ║    ║    ║    ║  5 │
╚════╩════╩════╩════╩════╝────┘
│ 10 │  9 │  8 │  7 │  6 │
└────┴────┴────┴────┴────┘
"""


def printLegendeIndikatoren():
    newline(1)
    print("╔════╦════╦════╦════╦════╗────┐")
    print("║    ║    ║    ║    ║    ║  1 │")
    print("╠════╬════╬════╬════╬════╣────┤")
    print("║    ║    ║    ║    ║    ║  2 │")
    print("╠════╬════╬════╬════╬════╣────┤")
    print("║    ║    ║    ║    ║    ║  3 │")
    print("╠════╬════╬════╬════╬════╣────┤")
    print("║    ║    ║    ║    ║    ║  4 │")
    print("╠════╬════╬════╬════╬════╣────┤")
    print("║    ║    ║    ║    ║    ║  5 │")
    print("╚════╩════╩════╩════╩════╝────┘")
    print("│ 10 │  9 │  8 │  7 │  6 │     ")
    print("└────┴────┴────┴────┴────┘     ")
    newline(1)


PunkteSummen = [-1 for x in range(10)] # die Liste, die die Summe der Punkte in der obigen Reihenfolge hat
VoltoSummen = [-1 for x in range(10)]  # die Liste, die die Summe der Voltobaelle in der obigen Reihenfolge hat


def erfrageSummen():
    printLegendeIndikatoren()
    print("Punkte Summen:")
    for i in range(10):
        PunkteSummen[i] = intIntervallChoice(0,15)
    newline(1)
    print("Volto Summen:")
    for i in range(10):
        VoltoSummen[i] = intIntervallChoice(0,5)
    newline(3)

# erfrageSummen()
erfrageSummen()


"""
Brute-Force wie folgt:

Definiere eine Liste mit fünf leeren Listen
[ [], [], [], [], [] ]

die i-te Unterliste enthält alle möglichen Belegung der i-ten Reihe.

Anschließend Brute-Force alle Matrizen.

"""

BF = [ [], [], [], [], [] ]

def bestimmeZeile(zeile):
    backtrackingZeile(zeile, [])

def backtrackingZeile(zeile, Liste):
    if len(Liste) < 5:
        pointsSum = 0
        voltoSum = 0
        for i in Liste:
            pointsSum += i
            if i == 0:
                voltoSum += 1
            if pointsSum > PunkteSummen[zeile] or voltoSum > VoltoSummen[zeile]:
                return False
            elif pointsSum == PunkteSummen[zeile] and voltoSum == VoltoSummen[zeile]:
                return False
        for i in range(4):
            backtrackingZeile(zeile, Liste + [i])
    else:
        pointsSum = 0
        voltoSum = 0
        for i in Liste:
            pointsSum += i
            if i == 0:
                voltoSum += 1
        if pointsSum == PunkteSummen[zeile] and voltoSum == VoltoSummen[zeile]:
            gefundeneListe = BF[zeile]
            gefundeneListe.append(Liste)

for i in range(5):
    bestimmeZeile(i)



Matrizen = []

def bestimmeMatrizen():
    backtrackingMatrix([])

def backtrackingMatrix(Matrix):
    if len(Matrix) < 5:
        for spalte in range(5):
            pointsSum, voltoSum = berechneSpaltensumme(spalte, Matrix)
            if pointsSum > PunkteSummen[9 - spalte] or voltoSum > VoltoSummen[9 - spalte]:
                return False
            elif pointsSum == PunkteSummen[9 - spalte] and voltoSum == VoltoSummen[9 - spalte]:
                return False
        for i in BF[len(Matrix)]:
            backtrackingMatrix(Matrix + [i])
    elif len(Matrix) == 5:
        if Matrix[0] == [1,1,1,0,0]:
            pass
        for spalte in range(5):
            pointsSum, voltoSum = berechneSpaltensumme(spalte,Matrix)
            if pointsSum == PunkteSummen[9 - spalte] and voltoSum == VoltoSummen[9 - spalte]:
                pass
            else:
                return False
        Matrizen.append(Matrix)


"""
Output: (PunkteSumme,VoltoSumme) der Spalte
"""
def berechneSpaltensumme(spalte,Matrix):
    pointsSum = 0
    voltoSum = 0
    for zeile in Matrix:
        pointsSum += zeile[spalte]
        if zeile[spalte] == 0:
            voltoSum += 1
    return pointsSum, voltoSum


bestimmeMatrizen()








"""
Ausgabe:
╔═════════════╦═════════════╦═════════════╦═════════════╦═════════════╗─────────────┐
║   0: xxx%   ║   0: xxx%   ║   0: xxx%   ║   0: xxx%   ║   0: xxx%   ║             │
║   1: xxx%   ║   1: xxx%   ║   1: xxx%   ║   1: xxx%   ║   1: xxx%   ║   Σ: xx     │
║   2: xxx%   ║   2: xxx%   ║   2: xxx%   ║   2: xxx%   ║   2: xxx%   ║   Φ: xx     │
║   3: xxx%   ║   3: xxx%   ║   3: xxx%   ║   3: xxx%   ║   3: xxx%   ║             │
╠═════════════╬═════════════╬═════════════╬═════════════╬═════════════╣─────────────┤
║   0: xxx%   ║   0: xxx%   ║   0: xxx%   ║   0: xxx%   ║   0: xxx%   ║             │
║   1: xxx%   ║   1: xxx%   ║   1: xxx%   ║   1: xxx%   ║   1: xxx%   ║   Σ: xx     │
║   2: xxx%   ║   2: xxx%   ║   2: xxx%   ║   2: xxx%   ║   2: xxx%   ║   Φ: xx     │
║   3: xxx%   ║   3: xxx%   ║   3: xxx%   ║   3: xxx%   ║   3: xxx%   ║             │
╠═════════════╬═════════════╬═════════════╬═════════════╬═════════════╣─────────────┤
║   0: xxx%   ║   0: xxx%   ║   0: xxx%   ║   0: xxx%   ║   0: xxx%   ║             │
║   1: xxx%   ║   1: xxx%   ║   1: xxx%   ║   1: xxx%   ║   1: xxx%   ║   Σ: xx     │
║   2: xxx%   ║   2: xxx%   ║   2: xxx%   ║   2: xxx%   ║   2: xxx%   ║   Φ: xx     │
║   3: xxx%   ║   3: xxx%   ║   3: xxx%   ║   3: xxx%   ║   3: xxx%   ║             │
╠═════════════╬═════════════╬═════════════╬═════════════╬═════════════╣─────────────┤
║   0: xxx%   ║   0: xxx%   ║   0: xxx%   ║   0: xxx%   ║   0: xxx%   ║             │
║   1: xxx%   ║   1: xxx%   ║   1: xxx%   ║   1: xxx%   ║   1: xxx%   ║   Σ: xx     │
║   2: xxx%   ║   2: xxx%   ║   2: xxx%   ║   2: xxx%   ║   2: xxx%   ║   Φ: xx     │
║   3: xxx%   ║   3: xxx%   ║   3: xxx%   ║   3: xxx%   ║   3: xxx%   ║             │
╠═════════════╬═════════════╬═════════════╬═════════════╬═════════════╣─────────────┤
║   0: xxx%   ║   0: xxx%   ║   0: xxx%   ║   0: xxx%   ║   0: xxx%   ║             │
║   1: xxx%   ║   1: xxx%   ║   1: xxx%   ║   1: xxx%   ║   1: xxx%   ║   Σ: xx     │
║   2: xxx%   ║   2: xxx%   ║   2: xxx%   ║   2: xxx%   ║   2: xxx%   ║   Φ: xx     │
║   3: xxx%   ║   3: xxx%   ║   3: xxx%   ║   3: xxx%   ║   3: xxx%   ║             │
╚═════════════╩═════════════╩═════════════╩═════════════╩═════════════╝─────────────┘
│             │             │             │             │             │
│   Σ: xx     │   Σ: xx     │   Σ: xx     │   Σ: xx     │   Σ: xx     │
│   Φ: xx     │   Φ: xx     │   Φ: xx     │   Φ: xx     │   Φ: xx     │
│             │             │             │             │             │
└─────────────┴─────────────┴─────────────┴─────────────┴─────────────┘
"""

def printWahrscheinlichkeitstabelle():
    W = bestimmeWahrscheinlichkeiten()
    print("╔═════════════╦═════════════╦═════════════╦═════════════╦═════════════╗─────────────┐")
    print("║   0: "+f(W[0][0],3)+"%   ║   0: "+f(W[1][0],3)+"%   ║   0: "+f(W[2][0],3)+"%   ║   0: "+f(W[3][0],3)+"%   ║   0: "+f(W[4][0],3)+"%   ║             │")
    print("║   1: "+f(W[0][1],3)+"%   ║   1: "+f(W[1][1],3)+"%   ║   1: "+f(W[2][1],3)+"%   ║   1: "+f(W[3][1],3)+"%   ║   1: "+f(W[4][1],3)+"%   ║   Σ: "+f(PunkteSummen[0],2)+"     │")
    print("║   2: "+f(W[0][2],3)+"%   ║   2: "+f(W[1][2],3)+"%   ║   2: "+f(W[2][2],3)+"%   ║   2: "+f(W[3][2],3)+"%   ║   2: "+f(W[4][2],3)+"%   ║   Φ: "+f(VoltoSummen[0],2)+"     │")
    print("║   3: "+f(W[0][3],3)+"%   ║   3: "+f(W[1][3],3)+"%   ║   3: "+f(W[2][3],3)+"%   ║   3: "+f(W[3][3],3)+"%   ║   3: "+f(W[4][3],3)+"%   ║             │")
    print("╠═════════════╬═════════════╬═════════════╬═════════════╬═════════════╣─────────────┤")
    print("║   0: "+f(W[5][0],3)+"%   ║   0: "+f(W[6][0],3)+"%   ║   0: "+f(W[7][0],3)+"%   ║   0: "+f(W[8][0],3)+"%   ║   0: "+f(W[9][0],3)+"%   ║             │")
    print("║   1: "+f(W[5][1],3)+"%   ║   1: "+f(W[6][1],3)+"%   ║   1: "+f(W[7][1],3)+"%   ║   1: "+f(W[8][1],3)+"%   ║   1: "+f(W[9][1],3)+"%   ║   Σ: "+f(PunkteSummen[1],2)+"     │")
    print("║   2: "+f(W[5][2],3)+"%   ║   2: "+f(W[6][2],3)+"%   ║   2: "+f(W[7][2],3)+"%   ║   2: "+f(W[8][2],3)+"%   ║   2: "+f(W[9][2],3)+"%   ║   Φ: "+f(VoltoSummen[1],2)+"     │")
    print("║   3: "+f(W[5][3],3)+"%   ║   3: "+f(W[6][3],3)+"%   ║   3: "+f(W[7][3],3)+"%   ║   3: "+f(W[8][3],3)+"%   ║   3: "+f(W[9][3],3)+"%   ║             │")
    print("╠═════════════╬═════════════╬═════════════╬═════════════╬═════════════╣─────────────┤")
    print("║   0: "+f(W[10][0],3)+"%   ║   0: "+f(W[11][0],3)+"%   ║   0: "+f(W[12][0],3)+"%   ║   0: "+f(W[13][0],3)+"%   ║   0: "+f(W[14][0],3)+"%   ║             │")
    print("║   1: "+f(W[10][1],3)+"%   ║   1: "+f(W[11][1],3)+"%   ║   1: "+f(W[12][1],3)+"%   ║   1: "+f(W[13][1],3)+"%   ║   1: "+f(W[14][1],3)+"%   ║   Σ: "+f(PunkteSummen[2],2)+"     │")
    print("║   2: "+f(W[10][2],3)+"%   ║   2: "+f(W[11][2],3)+"%   ║   2: "+f(W[12][2],3)+"%   ║   2: "+f(W[13][2],3)+"%   ║   2: "+f(W[14][2],3)+"%   ║   Φ: "+f(VoltoSummen[2],2)+"     │")
    print("║   3: "+f(W[10][3],3)+"%   ║   3: "+f(W[11][3],3)+"%   ║   3: "+f(W[12][3],3)+"%   ║   3: "+f(W[13][3],3)+"%   ║   3: "+f(W[14][3],3)+"%   ║             │")
    print("╠═════════════╬═════════════╬═════════════╬═════════════╬═════════════╣─────────────┤")
    print("║   0: "+f(W[15][0],3)+"%   ║   0: "+f(W[16][0],3)+"%   ║   0: "+f(W[17][0],3)+"%   ║   0: "+f(W[18][0],3)+"%   ║   0: "+f(W[19][0],3)+"%   ║             │")
    print("║   1: "+f(W[15][1],3)+"%   ║   1: "+f(W[16][1],3)+"%   ║   1: "+f(W[17][1],3)+"%   ║   1: "+f(W[18][1],3)+"%   ║   1: "+f(W[19][1],3)+"%   ║   Σ: "+f(PunkteSummen[3],2)+"     │")
    print("║   2: "+f(W[15][2],3)+"%   ║   2: "+f(W[16][2],3)+"%   ║   2: "+f(W[17][2],3)+"%   ║   2: "+f(W[18][2],3)+"%   ║   2: "+f(W[19][2],3)+"%   ║   Φ: "+f(VoltoSummen[3],2)+"     │")
    print("║   3: "+f(W[15][3],3)+"%   ║   3: "+f(W[16][3],3)+"%   ║   3: "+f(W[17][3],3)+"%   ║   3: "+f(W[18][3],3)+"%   ║   3: "+f(W[19][3],3)+"%   ║             │")
    print("╠═════════════╬═════════════╬═════════════╬═════════════╬═════════════╣─────────────┤")
    print("║   0: "+f(W[20][0],3)+"%   ║   0: "+f(W[21][0],3)+"%   ║   0: "+f(W[22][0],3)+"%   ║   0: "+f(W[23][0],3)+"%   ║   0: "+f(W[24][0],3)+"%   ║             │")
    print("║   1: "+f(W[20][1],3)+"%   ║   1: "+f(W[21][1],3)+"%   ║   1: "+f(W[22][1],3)+"%   ║   1: "+f(W[23][1],3)+"%   ║   1: "+f(W[24][1],3)+"%   ║   Σ: "+f(PunkteSummen[4],2)+"     │")
    print("║   2: "+f(W[20][2],3)+"%   ║   2: "+f(W[21][2],3)+"%   ║   2: "+f(W[22][2],3)+"%   ║   2: "+f(W[23][2],3)+"%   ║   2: "+f(W[24][2],3)+"%   ║   Φ: "+f(VoltoSummen[4],2)+"     │")
    print("║   3: "+f(W[20][3],3)+"%   ║   3: "+f(W[21][3],3)+"%   ║   3: "+f(W[22][3],3)+"%   ║   3: "+f(W[23][3],3)+"%   ║   3: "+f(W[24][3],3)+"%   ║             │")
    print("╚═════════════╩═════════════╩═════════════╩═════════════╩═════════════╝─────────────┘")
    print("│             │             │             │             │             │              ")
    print("│   Σ: "+f(PunkteSummen[9],2)+"     │   Σ: "+f(PunkteSummen[8],2)+"     │   Σ: "+f(PunkteSummen[7],2)+"     │   Σ: "+f(PunkteSummen[6],2)+"     │   Σ: "+f(PunkteSummen[5],2)+"     │              ")
    print("│   Φ: "+f(VoltoSummen[9],2)+"     │   Φ: "+f(VoltoSummen[8],2)+"     │   Φ: "+f(VoltoSummen[7],2)+"     │   Φ: "+f(VoltoSummen[6],2)+"     │   Φ: "+f(VoltoSummen[5],2)+"     │              ")
    print("│             │             │             │             │             │              ")
    print("└─────────────┴─────────────┴─────────────┴─────────────┴─────────────┘              ")


def bestimmeWahrscheinlichkeiten():
    W = [[0 for x in range(4)] for y in range(25)]
    for Matrix in Matrizen:
        for y in range(5):
            for x in range(5):
                W[x+5*y][Matrix[y][x]] += 1
    V = [[0 for x in range(4)] for y in range(25)]
    for i in range(25):
        for j in range(4):
            V[i][j] = int( W[i][j] * 100 / len(Matrizen) )
    return V

printWahrscheinlichkeitstabelle()

while len(Matrizen) > 1:

    printLegendeFelder()
    newline(1)
    print("Feldnummer")
    feldnummer = intIntervallChoice(1,25)
    newline(1)
    print("aufgedeckte Zahl")
    zahl = intIntervallChoice(0,3)
    newline(1)

    x = feldnummer - 1
    y = 0

    while x > 4:
        x -= 5
        y += 1

    M = deepcopy(Matrizen)

    for Matrix in Matrizen:
        if Matrix[y][x] != zahl:
            M.remove(Matrix)

    Matrizen = M + []

    newline(5)

    printWahrscheinlichkeitstabelle()

input("")