dateipfad = "wichteln" + input("Dateipfad: ") + ".txt"
datei = open(dateipfad, 'r')
anzahl_kinder = int(datei.readline())
wunschliste = []
for _ in range(anzahl_kinder):
    wunsch_str = datei.readline().split()
    wunsch_int = [int(geschenk_nummer)-1 for geschenk_nummer in wunsch_str]
    wunschliste.append(wunsch_int)
datei.close()
geschenkverteilung = [-1 for _ in range(anzahl_kinder)]
kinder_ohne_geschenke = [kind_nummer for kind_nummer in range(anzahl_kinder)]
geschenke_ohne_kind = [geschenk_nummer for geschenk_nummer in range(anzahl_kinder)]


def verteile_ein_geschenk(wunschart, freie_geschenke):

    if wunschart == 3:
        kind_nummer = kinder_ohne_geschenke[0]
        geschenk_nummer = freie_geschenke[0]
        geschenkverteilung[kind_nummer] = geschenk_nummer
        kinder_ohne_geschenke.remove(kind_nummer)
        geschenke_ohne_kind.remove(geschenk_nummer)
        return None

    reservierungen = [[] for _ in range(anzahl_kinder)]
    for kind_nummer in kinder_ohne_geschenke:
        wunschgeschenk_nummer = wunschliste[kind_nummer][wunschart]
        if wunschgeschenk_nummer in freie_geschenke:
            reservierungen[wunschgeschenk_nummer].append(kind_nummer)

    for geschenk_nummer, reservierung in enumerate(reservierungen):
        if len(reservierung) == 1:
            einziges_kind_nummer = reservierungen[geschenk_nummer][0]
            geschenkverteilung[einziges_kind_nummer] = geschenk_nummer
            kinder_ohne_geschenke.remove(einziges_kind_nummer)
            geschenke_ohne_kind.remove(geschenk_nummer)
            return None
        if len(reservierung) >= 2:
            freie_geschenke.remove(geschenk_nummer)

    return verteile_ein_geschenk(wunschart + 1, freie_geschenke)


while kinder_ohne_geschenke:
    verteile_ein_geschenk(0, geschenke_ohne_kind[:])

anzahl_wunscharten = [0 for _ in range(3)]
for kind_nummer, geschenk_nummer in enumerate(geschenkverteilung):
    if geschenk_nummer in wunschliste[kind_nummer]:
        wunschart = wunschliste[kind_nummer].index(geschenk_nummer)
        anzahl_wunscharten[wunschart] += 1
        wunsch = "(" + str(wunschart + 1) + ". Wunsch)"
    else:
        wunsch = ""
    print("Kind", kind_nummer+1, "erhaelt Geschenk", geschenk_nummer+1, wunsch)
for wunschart, anzahL_wunschart in enumerate(anzahl_wunscharten):
    print("Anzahl", str(wunschart + 1) + ".", "Wunsch:", anzahL_wunschart)