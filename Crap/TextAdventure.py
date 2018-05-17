import time # importiert das ZeitModul

# choice(Liste)
# Gibt dem Spieler eine Liste aus Strings aus
# Dieser sucht sich ein Element dieser Liste aus
# Eingabe erfolgt über zwei Möglichkeiten:
# a) Die Nummer aus der Liste
# b) Der genau so abgetippter String
# Rückgabewert ist der gewählte String
def choice(Liste):
    while 1:
        print(Liste) # Gibt die Liste aus
        a = input(">>> ") # Eingabemöglichkeit
        for i in range(len(Liste)):
            if a == Liste[i]: # Vergleicht String mit allen Strings
                return(a) # Auswurf des Strings bei Gleichheit
        try: # Verusucht String zu formatieren
            return(Liste[int(a)-1])
        except ValueError:
            pass # Mache weiter, wenn String nicht formatiert werden kann
        except IndexError:
            pass # Mache weiter, wenn Int nicht im Bereich der Liste ist
        print("Ungültige Eingabe")
        print()

# Lässt einen Char. reden.
# Braucht einen Char. und den gesprochenen Text
# Gibt diesen aus und wartet entsprechend wie lange der text war
def redet(Char, Text):
    print(Char+":","'"+Text+"'")
    time.sleep((len(Char)+len(Text))*0.08)

# Wie reden, nur für den Erzähler
def erzählen(Text):
    print(Text)
    time.sleep(len(Text)*0.075)

# Überspringt einige Zeilen
def skip(AnzahlZeilen):
    for i in range(0,AnzahlZeilen):
        print()
        time.sleep(0.5)

global Inventar
Inventar = []

# Übergibt dem Spieler ein Item
def erhalten(Item):
    print()
    print("#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#")
    print("Du erhällst das Item:   "+Item)
    erzählen("#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#+#")
    print()
    Inventar.append(Item)

Hand = 0

def tragen(Item):
    global Hand
    Hand = Item
    erzählen("Du trägst nun das Item:   "+Item)
    print()

def inv():
    if Inventar == []:
        erzählen("Es befindet sich kein Item in deinem Inventar.")
    else:
        print()
        print("Wähle ein Objekt.")
        a = choice(Inventar)
        tragen(a)

def it():
    if Hand == 0:
        erzählen("Du trägst im Moment kein Item.")
    else:
        erzählen("Du trägst das Item:   "+Hand)
        
### Beginn der handlung ###


skip(5)


# Frägt den Spieler nach dem Namen
print("Wie nennen sie dich?")
name = input(">>> ")
skip(1)
print("Ist "+name+" dein Name?")
c = choice(["Ja","Nein"])
if c == "Nein":
    while 1:
        skip(1)
        print("Jetzt sag schon, wie nennen sie dich?")
        name = input(">>> ")
        skip(1)
        print("Ist "+name+" also dein Name?")
        c = choice(["Ja","Nein"])
        if c == "Ja":
            break
        skip(1)

 # Als Witz sollen die Namen einiger Personen abgeändert weden
if name == "Benno" or name == "Benjamin" or name == "Benno" or name == "benjamin":
    name = "Jonas"
elif name == "Andreas" or name == "andreas":
    name = "Gott"
elif name == "Noah" or name == "noah":
    name = "Laurenzius"
elif name == "Simon" or name == "simon":
    name = "Günther"
elif name == "Johanna" or name == "johanna":
    name = "Jojo"
elif name == "Mihnea" or name == "mihnea":
    name = "Metalhead43"
elif name == "Emery" or name == "Embo":
    name = "Von Grafenstein"
elif name == "Igor" or name == "Papa" or name == "igor" or name == "papa":
    name = "Oberhaupt der Familie Duca"
elif name == "Natasa" or name == "natasa" or name == "Mama" or name == "mama":
    name = "Weibliches Oberhaupt der Familie Duca"

skip(3)
# Tutorial
erzählen("Willkommen, "+name+"!")
erzählen("Dies ist ein kleines Mini-Textadventure, das ich geschrieben habe.")
skip(1)
print("Während des Textadventures wirst du auf folgende Auswahlboxen treffen")
choice(["ok","verstanden","interessant"])
erzählen("Du kannst die Antwort, die du eingeben willst, einfach nachtippen.")
erzählen("Es ist jedoch auch möglich die entsprechende Nummer zu wählen.")
erzählen("Dabei ist '1' die erste Antwortmöglichkeit, '2' die zweite, und so weiter.")
skip(1)
print("Probiere es doch einmal aus!")
choice(["In Ordnung","Alles klar","Schau her"])
erzählen("Sehr gut!")
erzählen("Auch hast du in diesem Spiel ein Inventar.")
erzählen("Alle Gegenstände, die du im Spiel erhällst, landen darin.")
erzählen("Wenn sich die Möglichkeit bietet, kannst du dein Inventar untersuchen.")
skip(1)
print("Untersuche dein Inventar!")
choice(["Inventar"])
inv()
erzählen("Okay, nimm diesen Kanister Benzin und fackel mir ja nicht meine Bude ab.")
erhalten("Benzin")
print("Probier es noch einmal!")
choice(["Inventar"])
inv()
erzählen("Items, die du in der Hand hälst, kannst du mit 'Item' einsetzen.")
erzählen("Du hast nun alles nötige Wissen, um dieses Spiel zu spielen!")
erzählen("Ich wünsche dir viel Spaß und Glück!")
skip(2)
erzählen("Und gib mir das Benzin zurück.")
time.sleep(1)
erzählen("Du kleiner Pisser.")
Inventar = []
Hand = 0

skip(15)
# Zeit- und Ortsangabe
erzählen("17:34 Uhr, Sonntag")
erzählen("Treppenhaus, Palast")

skip(3)
# Schwesterszene
redet("Halbschwester","Na los, wach auf!")
redet("Halbschwester",name+"!")
redet("Halbschwester","Wach doch bitte auf!")
redet("Halbschwester","Verdammt. Sie kommen!")
skip(1)
erzählen("Du hörst wie deine Halbschwester wegläuft.")
erzählen("Deine Familie lässt dich im Stich.")
erzählen("Dieses Teufelspack!")

skip(3)
# Wache bringt dich ins Gefängnis
redet("Wache","Hey du! Steh auf!")
skip(1)
erzählen("Du spürst einen kräftigen Arm, der nach dir packt.")
erzählen("Du wirst in einen Raum verfrachtet.")
skip(1)
redet("Wache","Wie konntest du überhaupt die Tür aufsperren?")
redet("Wache","Du hast Komplizen, nicht wahr?")
redet("Wache","Sucht den Rest der Streuselbande, die können nicht weit weg sein.")
skip(1)
erzählen("Der Wache schließt die Gittertür ab und geht.")

# Kerker
# Kerker
skip(6)
erzählen("Du befindest dich in einem Kerker.")
Kerker = ["Umschauen","Schreien","Inventar","Item"]
Kerker.sort()
while 1:
    skip(1)
    c = choice(Kerker)
    if c == "Inventar":
        inv()
    elif c == "Item":
        it()
    elif c == "Schreien":
        erzählen("Du schreist laut, aber es passiert nichts.")
        Kerker.remove("Schreien")
    elif c == "Umschauen":
        erzählen("Vor dir befindet sich die Gittertür.")
        Kerker.append("Gittertür")
        erzählen("In einer Ecke liegt ein umgefallener Holzstuhl.")
        Kerker.append("Holzstuhl")
        Kerker.remove("Umschauen")
        Kerker.sort()
    elif c == "Holzstuhl":
        erhalten("Holzstuhl")
        Kerker.remove("Holzstuhl")
    elif c == "Gittertür":
        if Hand == "Holzstuhl":
            erzählen("Du versuchst mit dem Holzstuhl die Gittertür zu biegen.")
            erzählen("Dein Holzstuhl geht kaputt. Dabei bricht ein Bein des Stuhls ab.")
            Hand = 0
            erhalten("Holzstab")
            Inventar.remove("Holzstuhl")
            Kerker.append("Meditieren")
        else:
            erzählen("Du rüttelst an der Gittertür, aber es passiert nichts.")
    elif c == "Meditieren":
        erzählen("Du entscheidest dich nach deinem verzweifelten Ausbruchversuch")
        erzählen("einfach zu meditieren.")
        break

skip(5)
erzählen("Checkpoint geladen.")

while 1:
    skip(15)
    erzählen("30 Jahre später.")
    skip(1)
    erzählen("16:20 Uhr, Dienstag")
    erzählen("Kerker, Palast")
    skip(5)

    erzählen("Eines Tages rüttelt jemand fest an der Kerkertür.")
    erzählen("Er flüstert einen Namen und sagt er will dich befreien,")
    erzählen("jedoch braucht er für eine legale Herangehensweise deine Willenserklärung,")
    erzählen("da er sich sonst strafbar machen würde.")
    c = choice(["Bitte, rette mich!","Rette mich!","Bonjour!","Lass mich in Ruhe."])
    if c == "Rette mich!":
        erzählen("Selbst nach 30 Jahren Haft hast du nicht das Recht unhöflich zu werden.")
        erzählen("Moses, ein Freund des Erzählers, spaltet deinen Körper in zwei.")
        skip(3)
    elif c == "Bitte, rette mich!":
        erzählen("Dein rätselhafter Retter kommt näher und schaut dich mit einem liebvollen Blick an.")
        choice(["Wer bist du?","Kennen wir uns?","Schwester?"])
        redet("Rätselhafte Person","Es tut mir Leid! Ich dachte du wärst jemand anderes.")
        erzählen("Er verlässt dich.")
        erzählen("Du bekommst einen Herzinfarkt.")
    elif c == "Bonjour!":
        erzählen("Die rätselhafte Person vergewaltigt dich.")
    elif c == "Lass mich in Ruhe.":
        redet("Rätselhafte Person","Nur einer im ganzen Königreich könnte unter diesen Umständen so frech sein.")
        redet("Rätselhafte Person","Mein Freund "+name+", du bist es!")
        redet("Mohammed","Ich habe dich nach 30 Jahren endlich gefunden!")
        erzählen("Dein alter Freund Mohammed ist gerade dabei die Kerkertür zu öffnen.")
        erzählen("Er bekommt einen Herzinfarkt.")
        erzählen("Du bekommst einen Herzinfarkt.")
        erzählen("Sämtliche Kinder auf der Krankenstation bekommen einen Herzinfarkt.")

    skip(5)
    erzählen("Game Over")
    skip(2)
    erzählen("Möchtest du den letzten Checkpoint laden?")
    c = choice(["Ja","Nein"])
    if c == "Nein":
        break

erzählen("Vielen Dank für's Spielen!")
erzählen("Ich hoffe es hat Spaß gemacht!")
skip(5)
