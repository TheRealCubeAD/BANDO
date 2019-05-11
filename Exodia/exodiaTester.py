import random

def mischen():
    random.shuffle(Deck)

def ziehen():
    Hand.append(Deck[0])
    del Deck[0]

def zauberkarteAktiviert(zauberkarte):
    for i in Bibliotheken:
        i += 1
    Hand.remove(zauberkarte)
    Friedhof.append(zauberkarte)
    aktivierteKarten.append(zauberkarte)

uebrigeNoramalbeschwoerungen = 1
aktivierteKarten = []
Friedhof = []
Deck = []
Hand = []

Bibliotheken = []

for _ in range(1): # Exodia
    Deck.append("Linker Arm der Verbotenen")
for _ in range(1): # Exodia
    Deck.append("Rechtes Bein der Verbotenen")
for _ in range(1): # Exodia
    Deck.append("Linkes Bein der Verbotenen")
for _ in range(1): # Exodia
    Deck.append("Rechter Arm der Verbotenen")
for _ in range(3): # Engine
    Deck.append("Magische Bibliothek des Königs")
for _ in range(1): # Exodia
    Deck.append("Exodia, die Verbotene")
for _ in range(2):
    Deck.append("Sammle deinen Geist")
for _ in range(1):
    Deck.append("Ein Tag voller Frieden")
for _ in range(1):
    Deck.append("Törichte Begräbnisbeigaben")
for _ in range(3):
    Deck.append("Pokal des Asses")
for _ in range(1):
    Deck.append("Doppelbeschwörung")
for _ in range(1):
    Deck.append("Emporkömmling Goblin")
for _ in range(3):
    Deck.append("Goldenes Bambusschwert")
for _ in range(3):
    Deck.append("Geschäfte mit der finsteren Welt")
for _ in range(2):
    Deck.append("Gespür für Zauberkraft")
for _ in range(1):
    Deck.append("Törichtes Begräbnis")
for _ in range(3):
    Deck.append("Magischer Hammer")
for _ in range(3):
    Deck.append("Toon-Inhaltsverzeichnis")
for _ in range(3):
    Deck.append("In die Leere")
for _ in range(1):
    Deck.append("Topf der Gegengesetzlichkeit")
for _ in range(1):
    Deck.append("Zerbrochenes Bambusschwert")
for _ in range(3):
    Deck.append("Verfluchtes Bambusschwert")

mischen()

for _ in range(5):
    ziehen()
print(Hand)

while True:

    # WIN CONDITION
    # 1.) Wenn alle Teile von Exodia auf der Hand liegen, gewinnst du.
    if Hand.count("Linker Arm der Verbotenen") == Hand.count("Rechtes Bein der Verbotenen") == Hand.count("Linkes Bein der Verbotenen") == Hand.count("Rechter Arm der Verbotenen") == Hand.count("Exodia, die Verbotene") == 1:
        print("EXODIA, OBLITERATE!")
        input("")
        sys.exit()

    # ENGINE
    # 2.) Wenn eine Bibliothek beschwörbar ist, dann beschwöre sie.
    elif Hand.count("Magische Bibliothek des Königs") >= 1 and uebrigeNoramalbeschwoerungen > 0:
        Bibliotheken.append(0)
        Hand.remove("Magische Bibliothek des Königs")
        uebrigeNoramalbeschwoerungen -= 1
    # 3.) Wenn eine Bibliothek drei Zählmarken hat, so ziehe eine Karte
    elif Bibliotheken.count(3) >= 1:
        Bibliotheken.remove(3)
        Bibliotheken.append(0)
        ziehen()
    # 4.) Wenn bereits eine Bibliothek auf dem Feld liegt, so aktiviere Doppelbeschwörung, wenn möglich.
    elif len(Bibliotheken) > 1 and Hand.count("Doppelbeschwörung") > 0:
        if not aktivierteKarten.count("Doppelbeschwörung"):
            uebrigeNoramalbeschwoerungen += 1
        zauberkarteAktiviert("Doppelbeschwörung")

    