
# - Import - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


import math # <3
import sys # Aus Stack Overflow kopiert
sys.stdout.flush() # https://stackoverflow.com/questions/493386/how-to-print-without-newline-or-space
import time # "The laws of time are mine and they will obey me!"





# - Textmethoden - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# sprint: Kurz fuer "slow print", kein tatsaechlicher Sprint
textSpeed = 0.1
def sprint(string):
    for i in string:
        sys.stdout.write(i)
        time.sleep(textSpeed)
    newline(1)


# Input: eine natuerliche Zahl n
# Output: N/A, Leasst n Zeilen aus
def newline(n):
    for i in range(n):
        print()

# Input: Ein String
# Ouptput: N/A, Gibt einen Texttrenner mit dem eingebenen String in der Mitte aus
def textDivider(string):
    # Die folgende Formel ergibt sich aus dieser Ueberlegung:
    # Nach Moeglichkeit soll der Texttrenner ~ 120 Zeichen lang sein.
    # Der String nimmt len(string) Zeichen ein.
    # Links und rechts des zentrierten Strings liegen eine gleiche gerade Anzahl an Zeichen.
    anz = math.floor( ( 90 - len(string) ) / 4 )
    # Zusammenbauen des Strings
    t = ""
    for _ in range(anz):
        t += "- "
    t += string
    for _ in range(anz):
        t += " -"
    print(t)

# Input: N/A
# Ouptput: N/A, Gibt einen Texttrenner aus
def neutralDivider():
    t = ""
    for _ in range(45):
        t += "- "
    print(t)


# Input: Eine Auswahl von Entschiedungsmöglichkeiten in Form von Strings in einer Liste
# Auch ist eine Auswahl aus eine Liste verborgener Entscheidungsmöglihckeit möglich
# Output: Das vom Nutzer ausgewählte String
def choice(*choices):
    # Gib alle (sichtbaren) Antwortmoeglichkeiten aus
    newline(1)
    # textDivider("Auswahlfenster")
    # newline(1)
    for i in range(len(choices)):
        s = "(" + str(i+1) + ") " + choices[i]
        sprint(s)
    # Erwarte Eingabe des Nutzers
    while True:
        newline(1)
        inp = input(">>> ")
        try:
            inp = int(inp)
            inp -= 1
            outp = choices[inp]
            break
        except ValueError:
            sprint("Ungültige Eingabe!")
        except IndexError:
            sprint("Ungültige Eingabe!")
    newline(1)
    # neutralDivider()
    # newline(2)
    return outp













# - Hauptmenü - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# Titelmenü
def titlescreen():
    newline(3435)
    neutralDivider()
    textDivider("Portable Dungeon")
    textDivider("by Alex Duca")
    neutralDivider()
    mainmenu()




# Hauptmenü
def mainmenu():
    newline(4)
    textDivider("Hauptmenü")
    c = choice("Spiel Starten","Einstellungen","Credits","Spiel Beenden")
    if c == "Spiel Starten":
        pass
    elif c == "Einstellungen":
        settings()
    elif c == "Credits":
        gameCredits()
    elif c == "Spiel Beenden":
        exit("Spiel wurde beendet.")




# Einstellungen
def settings():
    textDivider("Einstellungen")
    c = choice("Textgeschwindigkeit","Zurück zum Hauptmenü")

    # Einstellung der Textgeschwindigkeit
    if c == "Textgeschwindigkeit":
        textDivider("Textgeschwindigkeit")
        choices = ["Standard", "Sonic The Hedgehog", "An Actual Hedgehog"]
        Speeds = [0.1, 0.05, 0.205]
        newline(1)
        global textSpeed
        defaultTextSpeed = textSpeed
        for i in range(len(choices)):
            s = "(" + str(i + 1) + ") " + choices[i]
            textSpeed = Speeds[i]
            sprint(s)
        textSpeed = Speeds[0]
        while True:
            newline(1)
            inp = input(">>> ")
            try:
                inp = int(inp)
                inp -= 1
                outp = choices[inp]
                break
            except ValueError:
                sprint("Ungültige Eingabe!")
            except IndexError:
                sprint("Ungültige Eingabe!")
        textSpeed = Speeds[ choices.index(outp) ]
        settings()

    # Zurück zum Hauptmenü
    if c == "Zurück zum Hauptmenü":
        mainmenu()



def gameCredits():
    textDivider("Credits")
    newline(1)
    sprint("Leitung:                    Alex Duca")
    sprint("Programmierung:             Alex Duca")
    sprint("Spieldesign:                Alex Duca")
    sprint("Technische Unterstützung:   Alex Duca")
    newline(1)
    sprint("Besonderen Dank an Alex Duca.")
    mainmenu()




# Öffne Titelbildschirm
titlescreen()









# - Spielklassen - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# Hilfsliste fuer die Angabe der Koordinaten
Alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]


class Monster:

    # Konstruktor
    def __init__(self, name, room, coordinates, movement, range, armor, hits, damage, healthpoints):
        self.name = str(name)
        self.room = room
        self.coordinates = str(coordinates)
        self.movement = int(movement)
        self.range = int(range)
        self.armor = int(armor)
        self.hits = int(hits)
        self.damage = int(damage)
        self.healthpoints = int(healthpoints)






class Player:

    # Konstruktor
    def __init__(self, name, room, coordinates, profession, strength, dexterity, wisdom):
        self.name = str(name)
        self.floor = floor
        self.coordinates = str(coordinates)
        self.strength = int(strength)
        self.dexterity = int(dexterity)
        self.movement = math.floor( int(dexterity) / 2 )
        self.wisdom = int(wisdom)
        self.actionpoints = 2 * int(wisdom)
        self.profession = "None"



class Weapon:

    # Konstruktor
    def __init__(self, name, range, damage, hits, hands):
        self.name = str(name)
        self.range = int(range)
        self.hits = int(hits)
        self.hands = int(hands)

handAxe = Weapon("Axt",1,2,0,1)
sword = Weapon("Schwert",1,2,0,1)
dagger = Weapon("Dolch",1,1,1,1)
battleAxe = Weapon("Kampf-Axt",1,3,0,2)
ironKnuckles = Weapon("Schlagringe",1,1,1,2)
bow = Weapon("Bogen",3,2,0,2)
wand = Weapon("Zauberstab",3,1,1,1)


class Floor:

    # Konstruktor
    def __init__(self, game, width, height):

        # Referenz zur Game-Klasse
        self.game = game

        # Korrektur der Breite
        width = int(width)
        if width > 26:
            width = 26
        if width < 2:
            width = 2
        self.width = width

        # Korrektur der Hoehe
        height = int(height)
        if height < 2:
            height = 2
        self.height = height

        # Raeume
        self.rooms = [ [ Room(self) for x in range(width) ] for y in range(height) ]
        self.generateRoomplan()
        self.fillWithMonsters()



    # Generiere die Raeume
    def generateRoomplan(self):

        # Beschreibung
        for i in range(self.width * self.height):
            pass



    # Fuelle die Ebene mit Monster
    def fillWithMonsters(self):
        pass



    # Koordinatenformatierung: Tupel -> String
    def tupelToString(self, tupel):
        pass



    # Koordinatenformatierung: String -> Tupel
    def stringToTupel(self, string):
        pass






class Room:

    # Konstruktor
    def __init__(self, floor):
        self.floor = floor
        self.coordinates = (0,0)
        self.walls = [0,0,0,0]
        self.state = 0

    # Setze Koordinaten
    def setCoordinates(self, coordinates):
        self.coordinates = coordinates





class Game:

    def __init__(self, dungeon, players):
        self.dungeon = dungeon
        self.players = players
        self.monsters = monsters










# - Spiel - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def characterCustomization():

    newline(4)
    textDivider("Charakter-Erstellung")

    newline(2)
    sprint("Wähle eine Klasse!")
    kriegerKlasse   = "Krieger   - Kennt keine Zaubersprüche und kann keine Schriftrollen verwenden"
    diebKlasse      = "Dieb      - Kennt keine Zaubersprüche und kann Schriftrollen verwenden"
    elfKlasse       = "Elf       - Kennt einen Zauberspruch und kann Schriftrollen verwenden"
    magierKlasse    = "Magier    - Kennt zwei Zaubersprüche und kann Schriftrollen verwenden"
    klasse = choice(kriegerKlasse,diebKlasse,elfKlasse,magierKlasse)











