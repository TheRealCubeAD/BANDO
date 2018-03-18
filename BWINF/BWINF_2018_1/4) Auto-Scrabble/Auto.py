# Die txt-Datei "kuerzelliste", welche sich im selben Ordner befinden muss wie das Skript, wird geoeffnet
doc = open("kuerzelliste.txt")

def fit(a, b):         # Die Methode prueft, ob das Kuerzel a den ersten Buchstaben des Wortes b entspricht
    b = b[0:(len(a))]  # Das Wort b wird von vorne auf die Laenge von a gekuerzt
    if a == b:         # Wenn das Kuerzel a dem gekuerzten Wort b entspricht,
        return True    # Dann Wird der Boolean True zurueckgegeben
    else:              # Wenn nicht,
        return False   # Dann wird der Boolean False zurueckgegeben


def word(wort):  # Die rekursive Methode prueft, ob ein Wort als meherere Nummerschilder geschrieben werden kann
    global L  # Die Liste L wird globalisiert, damit alle Rekursionsstufen darauf zugreifen koennen
    for i in k:  # Die Liste aller Ortskuerzel wird als i durchiteriert
        if fit(i, wort):  # Es wird geprueft, ob das aktuelle Ortskuerzel zu dem aktuellen Wort passt
            try:
                part = [i, wort[len(i)]]  # Eine Liste part mit dem Kuerzel und dem naechsten Buchstaben wird erstellt
                if umlaute.count(part[1]) == 1:  # Wenn dieser Buchstabe ein Umlaut ist,
                    return False  # Dann wird der Boolean False zurueckgegeben
                if part[0] + part[1] == wort:  # Wenn das Nummernschild dem uebergebenem Wort entspricht,
                    L.append([part[0], part[1]])  # Dann wird das Nummernschild der Liste L hinzugefuegt
                    return True  # Und der Boolean True zurueckgegeben
                # Sonst wird das Wort ohne dem Kuerzel und dem naechsten Buchstaben weitergegeben
                elif word(wort[(len(part[0]) + 1):]): # Wenn True zurueckgegeben wird,
                    L.append([part[0], part[1]])  # Dann wird das Nummernschild der Liste L hinzugefuegt
                    return True  # Und der Boolean True zurueckgegeben
            except IndexError:  # Wenn das Nummernschild mehr Buchstaben besitzt als das Wort
                return False  # Dann wird False zurueckgegeben
            try:
                part = [i, wort[len(i)] + wort[len(i) + 1]]
                # Eine Liste part mit dem Kuerzel und den naechsten 2 Buchstaben wird erstellt
                for j in range(2):  # Durchlaufe 0 bis 1 als j
                    if umlaute.count(part[1][j]) == 1:  # Sollte einer der beiden Buchstaben ein Umlaut sein
                        return False  # Dann wird False zurueckgegeben
                if part[0] + part[1] == wort:  # Wenn das Nummernschild dem uebergebenen Wort entspricht
                    L.append([part[0], part[1]])  # Dann wird das Nummernschild der Liste L uebergeben
                    return True  # Und True zurueckgegeben
                elif word(wort[(len(part[0]) + 2):]):
                	# Sonst wird das restliche Wort weitergegeben
                	# Wenn True zurueckgegeben wird
                    L.append([part[0], part[1]])  # Dann wird das Nummernschild der Liste L hinzugefuegt
                    return True  # und True zurueckgegeben
            except IndexError:  # Wenn das Nummernschild laenger als das uebergebene Wort ist
                return False  # Dann wird False zurueckgegeben
    return False  # Wenn keines der Kuerzel passt, dann wird False zurueckgegeben


umlaute = ["Ä", "Ü", "Ö"]  # Eine Liste mit allen Umlauten
k = []  # Eine Liste in der alle Kuerzel stehen sollen
for line in doc:  # Durchlaufe jede Zeile in doc als line
    k.append(line[:-1])  # Fuege k line ohne dem letzen Zeichen zu

while True:
    wor = input(">>>")  # Frage nach einem zu untersuchenden Wort
    L = []  # Erstelle die Nummernschildliste L
    if word(wor):  # Uebergebe das Wort word.
    # Wenn True zurueckgegeben wird
        print(L[::-1])  # Dann wird die Liste umgedreht und ausgegeben
    else:  # Sonst
        print("Dieses Wort laesst sich nicht zerlegen.")  # Laesst sich das Wort nicht zerlegen
