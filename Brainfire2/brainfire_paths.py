
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
print("Wie viele Felder ist der Raum hoch?")
hoehe = int(input(">>> "))
newline(1)
print("Wie viele Felder ist der Raum breit?")
breite = int(input(">>> "))
newline(1)


printMatrixRaum(Matrix)