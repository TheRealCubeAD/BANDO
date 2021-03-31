x = []
with open("test1.TXT", "r") as file:
    for line in file:
        x.append(line.split(" "))

# lt ist eine Liste, in der jede Lücke als einzelnes steht
lt = x[0]
# w ist eine Liste aller einzusetztenden Wörter
woerter = x[1]

""" dw (dictionarywörter) ist ein Dictionary, dass alle Wörter als key hat und zunächst als value für jeden key 
eine list hat """
dw = {}
for word in woerter:
    dw[word] = []

# wir speichern in dsonderzeichen die Indexe der Sondezeichen, um sie am Ende wieder einzusetzen
# (siehe setze_sonderzeichen_ein())
dsonderzeichen = {"!": [], "?": [], ".": [], ",": []}
for index, luecke in enumerate(lt):
    if "!" in luecke:
        dsonderzeichen["!"].append(index)
    if "?" in luecke:
        dsonderzeichen["?"].append(index)
    if "." in luecke:
        dsonderzeichen["."].append(index)
    if "," in luecke:
        dsonderzeichen[","].append(index)


# Funktion, die alle Sonderzeichen aus dem Lückentext entfernt
def delete_sonderzeichen():
    for luecke in range(len(lt)):
        lt[luecke] = lt[luecke].replace(",", "").replace("!", "").replace("?", "").replace(".", "").replace("\n", "")


# check_unterstriche() checkt ob die Luecke, die als Parameter genommen wird, nur aus "_" besteht, falls ja -->
# return True
def check_unterstriche(lue):
    for i in lue:
        if i != lue[0]:
            return False
    return True


# checkt ob der Lückentext fertig ist, falls ja return True
# der lückentext ist fertig sobald es in keinem wort mehr "_" gibt
def done():
    for i in lt:
        if "_" in i:
            return False
    return True


# checkt, ob alle übrigen keys (Wörter) doppelt eingesetzt werden müssen
def checkvorkommnis():
    for key, val in dmm.items():
        # wenn der value des keys <= 1 ist also eine leere liste ist --> continue
        if len(val) < 1:
            continue
        # checkt, ob Zahlen innerhalb eines values doppelt vorkommen, es dieses Wort also zweimal gibt
        # Parameter ist hierbei der value eines keys in dem dictionary "dw"
        elif len(set(val)) != len(val):
            continue
        # falls keine der beiden oberen Bedingungen zutrifft, steht fest, dass es einen key gibt der nicht
        # doppelt vorhanden ist und noch regulär eingesetzt werden muss
        else:
            return False
    # wenn alle Bedinungrn stimmen und die restlichen Wörter alle doppelt einzusetzten sind, return True
    return True


# hängt jedem Wort (key) in dw eine Liste an, in der alle passenden Postionen für das Wort stehen
# w ist eine Liste mit allen Wörtern
# lt ist eine Liste mit dem Lückentext
def create_dw():
    for wort in woerter:
        for indexlt in range(len(lt)):
            # wenn die Länge der Lücke ungleich der Länge des Wortes ist, wird direkt die nächste Lücke gecheckt
            if len(wort) != len(lt[indexlt]):
                continue
            # wenn das Wort nur aus "_" besteht, wird dem dictionary "dw" als value direkt der Index der Lücke
            # hinzugefügt
            elif check_unterstriche(lt[indexlt]):
                dw[wort].append(indexlt)
            # falls die Länge des Wortes gleich der Länge der Lücke ist und die Lücke einen Buchstaben enthält
            else:
                # loop durch die Länge der Lücke
                for k in range(len(lt[indexlt])):
                    # checkt ob ein Charackter in dem Lückenfeld gleich ist wie ein Charackter am selben Index des
                    # möglichen Lösungswortes
                    if lt[indexlt][k] == wort[k]:
                        # wenn das Wort passen könnte, wird der Index der entsprechenden Lücke als Value bei dem Wort
                        # im dictionary "dw" hinzugefügt
                        dw[wort].append(indexlt)
    """ Am Ende erhalten wir einen dictionary, in dem für jedes Wort (key), jede Stelle, an der es im Lückentext passen
     könnte, in Form eines Indexes, in einer Liste (value), festgehalten ist """


# erstellt einen dictionary (dictionaryMehrereMöglichkeiten = dmm), in dem alle Wörter stehen, deren value mehr als
# einen Index hat
# Alle Wörter, die an einer Stelle passen, also nur einen Wert im value haben, werden direkt eingesetzt
dmm = {}
# in used werden alle Wörter abgelegt, die schon richtig eingesetzt wurden
used = []


def dic_mehrere_moegl():
    for key in dw:
        # wenn die Länge des values größer als eins ist:
        if len(dw[key]) > 1:
            # fügt dem dictionary dmm den key und den value hinzu
            dmm[key] = dw[key]
        else:
            # im Lückentext das entsprechende Wort an der richtigen Stelle ersetzen
            lt[dw[key][0]] = key


# Liste, in der alle Werte aus den values in dmm stehen
list_vals = []


def liste_aller_index():
    for key, value in dmm.items():
        for val in value:
            list_vals.append(val)


# Hauptfunktion
def setze_passende_worte_ein():
    for key, val in dmm.items():
        # wenn der key noch nicht eingesetzt wurde
        if key not in used:
            # loopt für jeden key durch den value
            for v in val:
                # wenn an dem Index im Lückentext schon ein Wort eingefügt ist, es also an dem Index keine "_" mehr gibt
                if "_" not in lt[v]:
                    # entfernt aus dem value des keys den Index
                    dmm[key].remove(v)
                    # wenn in list_vals der Index vorhanden ist, wird er dort auch entfernt
                    if v in list_vals:
                        list_vals.remove(v)
                        # wenn die Länge des values nach dem Entfernen des nicht passenden Indexes eins ist
                        if len(dmm[key]) == 1:
                            # dann kann direkt im Lückentext die Lücke durch das Wort ersetzt werden
                            lt[dmm[key][0]] = key
                            # danach wird der value aus der liste_vals und dem dictionary gelöscht
                            list_vals.remove(dmm[key][0])
                            dmm[key].remove(dmm[key][0])
                # checkt, ob der Index in der Liste (list_vals) nur einmal enthalten ist
                if list_vals.count(v) == 1:
                    # checkt nochmal zur Sicherheit, ob noch kein Wort in der Lücke ist und ersetzt dann die Lücke
                    # mit dem passendem Wort
                    if "_" in lt[v]:
                        lt[v] = key
                        used.append(key)
                        # löscht danach alle Werte die im Value stehen aus "list_vals"
                        for num in val:
                            if num in list_vals:
                                list_vals.remove(num)
                        dmm[key] = []
                        break


# wenn checkvorkommnis() True returned, setzt es alle übrigen Wörter ein
def doppelte_worte_einsetzte():
    if checkvorkommnis():
        for key, val in dmm.items():
            if key not in used:
                for v in set(val):
                    if "_" in lt[v]:
                        lt[v] = key


# Setzt ganz am Ende die vorher entfernten Sonderzeichen wieder ein
def setze_sonderzeichen_ein():
    for key, val in dsonderzeichen.items():
        for ind in val:
            lt[ind] = lt[ind] + key


def loese_lueckentext():
    # alle Funktionen die zum erstellen des Inputs und der Varibalen benötigt werden
    delete_sonderzeichen()
    create_dw()
    dic_mehrere_moegl()
    liste_aller_index()

    # ruft so lange alle Funktionen auf, bis der Lückentext fertig gelöst ist
    while not done():
        setze_passende_worte_ein()
        doppelte_worte_einsetzte()
    setze_sonderzeichen_ein()
    # returned am Ende den fertigen Lückentext
    return " ".join(lt)


print(loese_lueckentext())
