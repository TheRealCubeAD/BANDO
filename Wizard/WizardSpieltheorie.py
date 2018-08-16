
# printListe(Liste)
# Gibt dem Nutzer eine Liste schoen formatiert aus
def printListe(Liste):
    string = "[ "
    for i in Liste:
        string += str(i) + ", "
    string = string[:-2]
    string += " ]"
    print(string)


# choice(Liste)
# Gibt dem Nutzer eine Liste aus Strings aus
# Dieser sucht sich ein Element dieser Liste aus
# Eingabe erfolgt über zwei Möglichkeiten:
# a) Die Nummer aus der Liste
# b) Der genau so abgetippter String
# Rückgabewert ist der gewählte String
def strChoice(Liste):
    while 1:
        printListe(Liste) # Gibt die Liste aus
        a = input(">>> ") # Eingabemöglichkeit
        for i in range(len(Liste)):
            if a == Liste[i]: # Vergleicht String mit allen Strings
                return(a) # Auswurf des Strings bei Gleichheit
        try: # Verusucht String zu formatieren
            a = int(a)
            if len(Liste) >= a > 0:
                return(Liste[int(a)-1])
        except ValueError:
            pass # Mache weiter, wenn String nicht formatiert werden kann
        except IndexError:
            pass # Mache weiter, wenn Int nicht im Bereich der Liste ist
        print("Ungueltige Eingabe.")
        print()


# choice(Liste)
# Gibt dem Spieler eine Liste aus Integer aus
# Dieser sucht sich ein Element dieser Liste aus
# Eingabe erfolgt über das genaue Abtippen des Integers
# Rückgabewert ist der gewählte Integer
def intChoice(Liste):
    while 1:
        printListe(Liste) # Gibt die Liste aus
        a = input(">>> ") # Eingabemöglichkeit
        try:
            a = int(a)
            error = False
        except ValueError:
            error = True
        if not error:
            for i in Liste:
                if a == i: # Vergleicht String mit allen Strings
                    return(a) # Auswurf des Strings bei Gleichheit
        print("Ungueltige Eingabe")
        print()



def erfrageKarte():
    print("Ist die Karte eine Farb- oder Sonderkarte?")
    artKarte = strChoice(["Farbkarte", "Sonderkarte"])
    print()
    if artKarte == "Farbkarte":
        print("Welche Farbe hat die Farbkarte?")
        farbeKarte = strChoice(["rot","gruen","blau","gelb"])
        print()
        print("Welche Zahl hat die Farbkarte?")
        zahlKarte = intChoice([1,2,3,4,5,6,7,8,9,10,11,12,13])
    if artKarte == "Sonderkarte":
        print("Welche Sonderkarte ist es?")
        if edition == "Standardedition":
            Karte = strChoice(["Narr", "Zauberer"])
        if edition == "Jubiliaeumsedition":
            Karte = strChoice(["Narr", "Zauberer", "Wolke", "Jongleur", "Werwolf", "Bombe", "Fee", "Drache"])


# Beginn des Programms
print()
print("- - - - - Programmstart - - - - -")
print()
print()
print("Wird die die Standard- oder Jubilaeumsedition gespielt?")
edition = strChoice(["Standardedition","Jubiliaeumsedition"])
print()
print()
print("Wie viele Spieler gibt es?")
anzahlSpieler = intChoice([3,4,5,6])
print()
print()
print("Position 1 ist links vom Kartengeber.")
print("An welcher Position sitzen Sie?")
position = intChoice([ i for i in range(1, anzahlSpieler+1) ])
print()
print()
print("Gefragt wird nach der Karte, die oben auf dem Stapel liegt.")
stapelKarte = erfrageKarte()
print()
print()
print("Gefragt wird nach der Karte, die auf der eigenen Hand liegt.")
eigeneKarte = erfrageKarte()
print()
print()