import time

# dateiname = input("Dateipfad: ")
dateiname = "raetsel4.txt"
datei = open(dateiname, 'r', encoding='utf-8')
lueckenwoerter = datei.readline().split()
woerter = datei.readline().split()
datei.close()
kandidaten_fuer_lueckenworter = [[] for _ in lueckenwoerter]
loesungen_fuer_lueckenwoerter = [-1 for _ in lueckenwoerter]
ergebnis = []


def satzzeichen_am_ende(lueckenwort):
    if lueckenwort[-1] in [',', '.', '!', '?']:
        return lueckenwort[-1]
    else:
        return ""


def passt_rein(wort, lueckenwort):
    if len(wort) != len(lueckenwort) - len(satzzeichen_am_ende(lueckenwort)):
        return False
    for position_buchstabe, buchstabe in enumerate(wort):
        if lueckenwort[position_buchstabe] == '_':
            pass
        elif lueckenwort[position_buchstabe] == buchstabe:
            pass
        else:
            return False
    return True


for position_lueckenwort, lueckenwort in enumerate(lueckenwoerter):
    for position_wort, wort in enumerate(woerter):
        if passt_rein(wort, lueckenwort):
            kandidaten_fuer_lueckenworter[position_lueckenwort].append(position_wort)


while -1 in loesungen_fuer_lueckenwoerter:

    for position_lueckenwort, kandidaten in enumerate(kandidaten_fuer_lueckenworter):
        if loesungen_fuer_lueckenwoerter[position_lueckenwort] == -1:
            if len(kandidaten) == 1:
                loesungen_fuer_lueckenwoerter[position_lueckenwort] = kandidaten[0]
            elif [woerter[position_wort] for position_wort in kandidaten] == [woerter[kandidaten[0]]] * len(kandidaten):
                loesungen_fuer_lueckenwoerter[position_lueckenwort] = kandidaten[0]
                break

    for position_lueckenwort, kandidaten in enumerate(kandidaten_fuer_lueckenworter):
        if loesungen_fuer_lueckenwoerter[position_lueckenwort] == -1:
            for kandidat in kandidaten:
                for vergebene_loesung in loesungen_fuer_lueckenwoerter:
                    if kandidat == vergebene_loesung:
                        kandidaten.remove(kandidat)


for position_lueckenwort, position_wort in enumerate(loesungen_fuer_lueckenwoerter):
    wort = woerter[position_wort]
    lueckenwort = lueckenwoerter[position_lueckenwort]
    wort += satzzeichen_am_ende(lueckenwort)
    ergebnis.append(wort)

print(" ".join(ergebnis))

print(time.process_time())
