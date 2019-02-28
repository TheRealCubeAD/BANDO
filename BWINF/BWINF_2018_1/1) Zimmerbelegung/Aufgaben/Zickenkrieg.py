doc = open("zimmerbelegung" + input("Datei >>>") + ".txt")  # Die Datei wird geöffnet


def posk_p(z):  # Suche eine Übereinstimmung der positiven Wünsche des Zimmers z mit den Namen in personen
    for person1 in z:  # Durchlaufe jede Person im Zimmer z als person1
        for pos in person1[1]:  # Durchlaufe jeden positiven Wunsch der person1 als pos
            index = 0  # index ist die Position der aktuellen person2 in personen
            for person2 in personen:  # Durchlaufe jede person in personen als person2
                if pos == person2[0]:  # Prüfe auf Übereinstimmung zwischen pos und dem Namen von person2
                    return index  # Gebe die Position von person2 in personen zurück
                index += 1  # Erhöhe index um 1
    return -1  # Gebe -1 zurück (keine Übereinstimmungen)


def posp_k(z):  # Suche eine Übereinstimmung der positiven Wünsche in personen und der Namen im Zimmer z
    index = 0  # index ist die Position der aktuellen person2 in personen
    for person2 in personen:  # Durchlaufe personen als person2
        for pos in person2[1]:  # Durchlaufe die positiven Wünsche der person2 als pos
            for person1 in z:  # Durchlaufe z als person1
                if pos == person1[0]:  # Prüfe auf Übereinstimmung zwischen pos und den Namen von person1
                    return index  # Gebe die Position von person2 in personen zurück
        index += 1  # Erhöhe index um 1
    return -1  # Gebe -1 zurück (keine Übereinstimmungen)


def negk_p(index, z):  # Suche eine Übereinstimmung der negativen Wünsche im Zimmer z mit der Person an der Stelle index
    name = personen[index][0]  # Der Name der person an der Stelle index in personen wird als name gespeichert
    for person1 in z:  # Durchlaufe die Personen des Zimmers z als person1
        for neg in person1[2]:  # Durchlaufe die negativen Wünsche von person1 als neg
            if neg == name:  # Prüfe auf Übereinstimmung zwischen neg und name
                return True  # Gebe Wahr zurück (negative Übereinstimmung)
    return False  # Gebe Falsch zurück (keine negative Übereinstimmung)

# Suche eine Übereinstimmung der negativen Wünsche der Person and der Stelle index in personen und den Namen in z
def negp_k(index, z):
    for neg in personen[index][2]:  # Durchlaufe alle negativen Wünsche der Person an der Stelle index in personen
        for person1 in z:  # Durchlaufe z als person1
            if neg == person1[0]:  # Prüfe auf Übereinstimmung zwischen neg und dem Namen von person1
                return True  # Gebe Wahr zurück (negative Übereinstimmung)
    return False  # Gebe Falsch zurück (keine negative Übereinstimmung)


count = 1  # count wird genutzt um zu prüfen in was für einer Zeile sich das Programm befindet (name,+,-,leer)
zimmer = []  # Liste aller erstellten Zimmer
personen = []  # Liste mit allen noch nicht zugewiesenen Personen
for line in doc:  # Durchlaufe jede Zeile des Dokuments als line
    if count == 1:  # wenn in der aktuellen Zeile ein name ist
        p = [line.rstrip()]  # erstelle die Liste p (neue person) mit dem Namen an erster Stelle
    elif count == 2:  # wenn in der aktuellen Zeile die Wünsche sind
        l = line[2:]  # speichere die Zeile ohne das + am anfang als l
        p.append(l.split())  # teile l bei Leerzeichen und setze die Liste mit allen Wünschen an die zweite Stelle von p
    elif count == 3:  # wenn in der aktuellen Zeile die negativen Wünsche sind
        l = line[2:]  # speichere die Zeile ohne das - am anfang als l
        p.append(l.split())  # teile l bei Leerzeichen und setze die Liste aller neg. Wünsche an die zweite Stelle von p
        personen.append(p)  # füge die erstellte Person p der Liste personen hinzu
    elif count == 4:  # wenn in der aktuellen Zeile nichts steht
        count = 0  # setze count wieder auf 0
    count += 1  # erhöhe count um 1

try:
    while len(personen) > 0:  # wiederhole, solange personen nicht lehr ist
        nzimmer = [personen[0]]  # erstelle ein neues Zimmer und füge die erste Person in personen hinzu
        reszimmer = []  # erstelle das gleich Zimmer in dem am Ende nur die Namen stehen
        del (personen[0])  # löscche die hinzugefügte Person aus personen
        found = True  # found gibt an, ob in einem Durchlauf ein Treffer gefunden wurde
        while found:  # wiederhole solange im vorherigen Durchgang ein Treffer gefunden wurde
            found = False  # setze found standartgemäß auf Falsch
            ind = posk_p(nzimmer)  # prüfe auf Übereinstimmung und speichere den zurückgegebenen Index als ind
            if ind != -1:  # wenn eine Übereinstimmung gefunden wurde
            	# prüfe auf (nicht) negative Übereinstimmung bei der gefundenen Person
                if not negk_p(ind, nzimmer) and not negp_k(ind, nzimmer):
                    nzimmer.append(personen[ind])  # füge die gefundene Person dem aktuellen Zimmer hinzu
                    del (personen[ind])  # lösche die hinzugefügte Person aus personen
                    found = True  # steze found auf Wahr
                else:  # wenn negative Übereinstimmung gefunden wurde
                    abbruch = 1 / 0  # springe zu Zeile 91 durch einen provozierten Fehler
            else:
                ind = posp_k(nzimmer)  # prüfe auf Übereinstimmung und speichere den zurückgegebenen Index als ind
                if ind != -1:  # wenn eine Übereinstimmung gefunden wurde
                	# prüfe auf (nicht) negative Übereinstimmung bei der gefundenen Person
                    if not negk_p(ind, nzimmer) and not negp_k(ind, nzimmer):
                        nzimmer.append(personen[ind])  # füge die gefundene Person dem aktuellen Zimmer hinzu
                        del (personen[ind])  # lösche die gefundene Person aus personen
                        found = True  # setze found auf Wahr
                    else:  # wenn negative Übereinstimmung gefunden wurde
                        fail = 1 / 0  # springe zu Zeile 91 durch einen provozierten Fehler
        for person in nzimmer:  # Durchaufe nzimmer als person
            reszimmer.append(person[0])  # füge reszimmer den Namen von person hinzu
        zimmer.append(reszimmer)  # füge das erstellte Zimmer der Liste aller Zimmer hinzu
except ZeroDivisionError:  # fange jeden "durch Null geteilt" Error auf
    print("Keine Zimmerbelegung möglich!")  # Gebe den text "Keine Zimmerbelegung möglich!" aus
print(zimmer)  # Gebe die Liste mit allen Zimmern aus
