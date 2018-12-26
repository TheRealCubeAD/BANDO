
from copy import deepcopy


# Beginn des Programms
print()
print("- - - - - Programmstart - - - - -")
print()
print()


Buchstabenliste = ["a","b","c","d","e","f","g","h"]
Aufrufe = 0
Wege = []
Probleme = []
vorgekommeneAufrufe = []




def posAlsString( tupel ):
    x = Buchstabenliste[ tupel[1] ]
    y = str( 8 - tupel[0] )
    return x + y


def posAlsTupel( string ):
    x = Buchstabenliste.index( string[0] )
    y = 8 - int( string[1] )
    return ( y, x )


def printProblemstellung( Problemstellung ):
    for i in range(len(Problemstellung)):
        reihe = Problemstellung[i]
        print(reihe)


def printWege( W ):
    for w in W:
        s = "( "
        for i in w:
            s += posAlsString(i) + ", "
        s = s[:-2]
        s += " )"
        print(s)


def getAnzahlSteine(Problemstellung):
    return sum(sum(i) for i in Problemstellung)

def printProblemMitLoesung( P, W, A ):
    print()
    print()
    printProblemstellung(P)
    print()
    printWege(W)
    print()
    print(A)
    print()
    print()


# Eine Problemstellung ist eine 8x8-Matrix bestehend aus 1 und 0.
# Eine 1 steht dabei fuer einen Spielstein.

Felder = []
FelderAlsTupel = []
for x in Buchstabenliste:
    for y in range(8):
        Felder.append( x + str(y+1) )
        FelderAlsTupel.append( posAlsTupel( x + str(y+1) ) )

def problemstellungEingeben():
    print("Geben Sie die Positionen aller Spielsteine an.")
    print("Die Eingabe erfolgt ueber die uebliche Schachnotation.")
    print("Tippen Sie 'zwischenstand', wenn Sie Ihre bisherige Eingabe ueberpruefen moechten.")
    print("Tippen Sie 'fertig', wenn die Eingabe abgeschlossen ist.")
    Problemstellung = [ [ 0 for x in range(8) ] for y in range(8) ]
    while 1:
        a = input(">>> ")
        if a == "zwischenstand":
            printProblemstellung(Problemstellung)
        elif a == "fertig":
            return Problemstellung
        elif Felder.count(a) == 1:
            t = posAlsTupel(a)
            Problemstellung[ t[0] ][ t[1] ] = int( not Problemstellung[ t[0] ][ t[1] ] )
        else:
            print("Ungueltige Eingabe.")


# Bestimme die Anzahl aller Spielsteine, die von einer bestimmten Position aus erreichbar sind.
def getNachbarn(stein, Problemstellung):
    local_nachbarn = []
    i = 0
    while stein[0] - i > 0:
        i += 1
        if Problemstellung[stein[0] - i][stein[1]]:
            local_nachbarn.append((stein[0]-i, stein[1]))
            break
    i = 0
    while stein[0] + i < 7:
        i += 1
        if Problemstellung[stein[0] + i][stein[1]]:
            local_nachbarn.append((stein[0]+i, stein[1]))
            break
    i = 0
    while stein[1] - i > 0:
        i += 1
        if Problemstellung[stein[0]][stein[1] - i]:
            local_nachbarn.append((stein[0], stein[1]-i))
            break
    i = 0
    while stein[1] + i < 7:
        i += 1
        if Problemstellung[stein[0]][stein[1] + i]:
            local_nachbarn.append((stein[0], stein[1]+i))
            break
    return local_nachbarn


def richtungErlaubt( letzterStein, aktuellerStein, naechsterStein ):
    if letzterStein[0] == aktuellerStein[0] == naechsterStein[0]:
            if naechsterStein[1] > letzterStein[1] > aktuellerStein[1]:
                return False
            elif naechsterStein[1] < letzterStein[1] < aktuellerStein[1]:
                return False
            else:
                return True
    elif letzterStein[1] == aktuellerStein[1] == naechsterStein[1]:
        if naechsterStein[0] > letzterStein[0] > aktuellerStein[0]:
            return False
        elif naechsterStein[0] < letzterStein[0] < aktuellerStein[0]:
            return False
        else:
            return True
    else:
        return True



def backtracking( stein, P, W ):
    global Aufrufe, Wege
    Aufrufe += 1
    Problemstellung = deepcopy(P)
    weg = deepcopy(W)
    Problemstellung[stein[0]][stein[1]] = 0
    weg.append(stein)
    nachbarn = getNachbarn(stein,Problemstellung)
    if len(nachbarn) == 0:
        if getAnzahlSteine(Problemstellung) == 0:
            Wege.append(weg)
    else:
        for N in nachbarn:
            if len(weg) == 1:
                backtracking(N, Problemstellung, weg)
            elif richtungErlaubt(weg[-2],stein,N):
                backtracking(N, Problemstellung,weg)



def findeLoesungen( Problemstellung ):
    # Lege eine Liste mit allen Spielsteinen an.
    global Aufrufe, Wege
    Aufrufe = 0
    Wege = []
    Moehrchenliste = []
    for x in range(8):
        for y in range(8):
            if Problemstellung[x][y]:
                Moehrchenliste.append( (x,y) )
    # Gehe alle Spielsteine durch und untersuche auf ausschliessende Kriterien
    Endsteine = []
    for stein in Moehrchenliste:
        Nachbarn = getNachbarn(stein, Problemstellung)
        if len(Nachbarn) == 0 and len(Moehrchenliste) == 1:
            Wege = [Moehrchenliste]
            return None
        elif len(Nachbarn) == 1:
            Endsteine.append( stein )
            if len(Endsteine) > 2:
                return []
    if len(Endsteine) == 2:
        Anfangssteine = Endsteine
    else:
        Anfangssteine = Moehrchenliste
    for anfangsstein in Anfangssteine:
        backtracking( anfangsstein, Problemstellung, [] )


def backtracking2( uebrigeAnzahl, P ):
    global Probleme, vorgekommeneAufrufe
    Problemstellung = deepcopy(P)
    if uebrigeAnzahl > 0:
        F = deepcopy(FelderAlsTupel)
        for i in FelderAlsTupel:
            if Problemstellung[i[0]][i[1]] == 1:
                while F[0] != i:
                    del( F[0] )
                del (F[0])
        for i in F:
            Problemstellung[i[0]][i[1]] = 1
            backtracking2( uebrigeAnzahl - 1, Problemstellung)
            Problemstellung[i[0]][i[1]] = 0
    else:
        findeLoesungen( Problemstellung )
        if len(Wege) ==  1 and vorgekommeneAufrufe.count( Aufrufe ) == 0:
            Probleme.append( (Problemstellung, Wege, Aufrufe) )
            vorgekommeneAufrufe.append(Aufrufe)
            printProblemMitLoesung(Problemstellung, Wege, Aufrufe)



def findeProbleme( problemgroesse, brettgroesse ):
    global Probleme, vorgekommeneAufrufe, FelderAlsTupel
    Probleme = []
    vorgekommeneAufrufe = []
    FelderAlsTupel = []
    for x in range(brettgroesse):
        for y in range(brettgroesse):
            Felder.append(Buchstabenliste[x] + str(y + 1))
            FelderAlsTupel.append(posAlsTupel(Buchstabenliste[x] + str(y + 1)))
    Problemstellung = [ [ 0 for x in range(8) ] for y in range(8) ]
    backtracking2( problemgroesse, Problemstellung )



zuVieleLoesungen = False


def schnellesBacktracking1( stein, P, W ):
    global Aufrufe, Wege, zuVieleLoesungen
    if zuVieleLoesungen:
        return None
    Aufrufe += 1
    Problemstellung = deepcopy(P)
    weg = deepcopy(W)
    Problemstellung[stein[0]][stein[1]] = 0
    weg.append(stein)
    nachbarn = getNachbarn(stein,Problemstellung)
    if len(nachbarn) == 0:
        if getAnzahlSteine(Problemstellung) == 0:
            Wege.append(weg)
            if len(Wege) > 1:
                zuVieleLoesungen = True
    else:
        for N in nachbarn:
            if len(weg) == 1:
                schnellesBacktracking1(N, Problemstellung, weg)
            elif richtungErlaubt(weg[-2],stein,N):
                schnellesBacktracking1(N, Problemstellung,weg)




def findeSchnellLoesungen( Problemstellung ):
    # Lege eine Liste mit allen Spielsteinen an.
    global Aufrufe, Wege, zuVieleLoesungen
    zuVieleLoesungen = False
    Aufrufe = 0
    Wege = []
    Moehrchenliste = []
    for x in range(8):
        for y in range(8):
            if Problemstellung[x][y]:
                Moehrchenliste.append( (x,y) )
    # Gehe alle Spielsteine durch und untersuche auf ausschliessende Kriterien
    Endsteine = []
    for stein in Moehrchenliste:
        Nachbarn = getNachbarn(stein, Problemstellung)
        if len(Nachbarn) == 0 and len(Moehrchenliste) == 1:
            Wege = [Moehrchenliste]
            return None
        elif len(Nachbarn) == 1:
            Endsteine.append( stein )
            if len(Endsteine) > 2:
                return []
    if len(Endsteine) == 2:
        Anfangssteine = Endsteine
    else:
        Anfangssteine = Moehrchenliste
    for anfangsstein in Anfangssteine:
        schnellesBacktracking1( anfangsstein, Problemstellung, [] )




def scnellesBacktracking2( uebrigeAnzahl, P ):
    global Probleme, vorgekommeneAufrufe
    Problemstellung = deepcopy(P)
    if uebrigeAnzahl > 0:
        F = deepcopy(FelderAlsTupel)
        for i in FelderAlsTupel:
            if Problemstellung[i[0]][i[1]] == 1:
                while F[0] != i:
                    del( F[0] )
                del (F[0])
        for i in F:
            Problemstellung[i[0]][i[1]] = 1
            scnellesBacktracking2( uebrigeAnzahl - 1, Problemstellung)
            Problemstellung[i[0]][i[1]] = 0
    else:
        findeSchnellLoesungen( Problemstellung )
        if len(Wege) ==  1 and vorgekommeneAufrufe.count( Aufrufe ) == 0:
            Probleme.append( (Problemstellung, Wege, Aufrufe) )
            vorgekommeneAufrufe.append(Aufrufe)
            printProblemMitLoesung(Problemstellung, Wege, Aufrufe)




def findeSchnellProbleme( problemgroesse, brettgroesse ):
    global Probleme, vorgekommeneAufrufe, FelderAlsTupel
    Probleme = []
    vorgekommeneAufrufe = []
    FelderAlsTupel = []
    for x in range(brettgroesse):
        for y in range(brettgroesse):
            Felder.append(Buchstabenliste[x] + str(y + 1))
            FelderAlsTupel.append(posAlsTupel(Buchstabenliste[x] + str(y + 1)))
    Problemstellung = [ [ 0 for x in range(8) ] for y in range(8) ]
    scnellesBacktracking2( problemgroesse, Problemstellung )


def problemgenerator():
    n = 7
    g = 4
    while 1:
        print()
        print()
        print(" - - n = " + str(n) + " - - - g = " + str(g) + " - -")
        print()
        findeSchnellProbleme(n,g)
        if Probleme == []:
            g += 1
        else:
            n += 1

p = problemstellungEingeben()
findeLoesungen(p)
printProblemMitLoesung( p, Wege, Aufrufe )

# Programmende
print()
print()
print(" - - - - - Programmende - - - - -")
print()