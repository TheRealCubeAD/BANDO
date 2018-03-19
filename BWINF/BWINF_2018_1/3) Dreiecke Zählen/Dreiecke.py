from PIL import Image, ImageDraw  # Importiere zwei Module von PIL zum erstellen und zeichnen von Bildern

doc = open("C:/PyCharm/dreiecke1.txt")  # Öffne die txt Datei mit den Koordinaten der Linien

n = input("nummer >>>")  # Frage nach der Nummer des Ordners
resolution = 50  # Die Auflösung des Bildes kann beliebig verändert werden (höhere Auflösung -> längere Rechenzeit)
m = 0  # Erstelle die Variable m um die größte Koordinate zu speichern
linien = []  # Erstelle die Liste linien um die Koordinaten aller Linien zu speichern
for line in doc:  # Durchlaufe jede Zeile in doc als line
    l = line.split()  # Alle Koordinaten werden in der Liste l gespeichert
    for z in range(0, len(l)):  # Durchlaufe 0 - länge von l als z
        l[z] = float(l[z])  # Konvertiere l[z] zu einem float
        if l[z] > m:  # Wenn derzeitige Koordinate größer als m ist:
            m = l[z]  # setze m auf derzeitige Koordinate
    linien.append(l)  # füge linien die Koordinaten hinzu

del (linien[0])  # Lösche den ersten Eintrag in linien (Anzahl der Linien)
m = int(m + 10)*resolution  # multipliziere m mit der Auflösung
for a in range(len(linien)):  # durchlaufe 0 - länge von linien als a
    for b in range(len(linien[a])):  # durchlaufe 0 - länge von linien[a] als b
        linien[a][b] *= resolution  # multipliziere die aktuelle Koordinate mit der Auflösung

pic = Image.new("RGB", (m, m), (255, 255, 255))  # Erstelle ein weißes Bild pic mit der Auflösung m*m
draw = ImageDraw.Draw(pic)  # weise das ImageDraw Modul dem Bild pic zu
w = int(resolution/10)  # lege die Dicke der Linien fest
for line in linien:  # durchlaufe linien als line
    draw.line((line[0]+resolution, m-line[1]-resolution, line[2]+resolution, m-line[3]-resolution),width=w , fill=(0, 0, 0))  # zeichne die aktuelle Linie in schwarz mit Abstand zum Rand

pic.save("Dreiecke"+n+"/Dreiecke0.png")  # Speichere das Bild ab


def max_(x, y):  # Gibt die groessere von zwei Zahlen a und b zurueck
    if x >= y:  # Ueberprueft, ob a groesser oder gleich b ist
        return x  # Gibt a zurueck
    else:  # Fuer den Fall, dass a kleiner als b ist:
        return y  # Gibt b zurueck


def min_(x, y):  # Gibt die kleinere von zwei Zahlen a und b zurueck
    if x <= y:  # Ueberprueft, ob a kleiner oder gleich b ist
        return x  # Gibt a zurueck
    else:  # Fuer den Fall, dass a groesser als b ist:
        return y  # Gibt b zurueck


def imIntervall(x, Intervall):  # Ueberprueft, ob eine Zahl x in einem gegebenem Intervall liegt
    if Intervall[0] <= x <= Intervall[1]:  # Ueberprueft, ob x zwischen den Intervallenden liegt
        return True  # Gibt Wahr zurueck
    else:  # An sonsten
        return False  # Gibt Falsch zurueck


def einSchnittpunkt(a1, b1, a2, b2, c1, d1, c2, d2):  # Ueberprueft, ob zwei Strecken genau einen Schnittpunkt haben

    # P1( a1 / b1 )
    # P2( a2 / b2 )
    # Q1( c1 / d1 )
    # Q2( c2 / d2 )

    # Betrachtung der Strecken P1P2 und Q1Q2:
    # p(x) ist die lineare Funktion, auf der P1P2 liegt
    # q(x) ist die lineare Funktion, auf der Q1Q2 liegt

    Dp = [min_(a1, a2), max_(a1, a2)]  # Definitionsmenge von p
    Wp = [min_(b1, b2), max_(b1, b2)]  # Wertemenge von p
    Dq = [min_(c1, c2), max_(c1, c2)]  # Definitionsmenge von q
    Wq = [min_(d1, d2), max_(d1, d2)]  # Wertemenge von q

    try:
        # p(x) = mp * x + tp
        mp = (b1 - b2) / (a1 - a2)  # Steigung von p
        tp = b1 - a1 * mp  # Erhoehung von p

    except ZeroDivisionError:  # => Die Strecke P1P2 steht senkrecht auf der x-Achse

        try:
            # q(x) = mq * x + tq
            mq = (d1 - d2) / (c1 - c2)  # Steigung von q
            tq = d1 - c1 * mq  # Erhoehung von q

        except ZeroDivisionError:  # => Die Strecke Q1Q2 steht senkrecht auf der x-Achse
            return False  # => kein Schnittpunkt

        x = a1  # Schnittpunkt mit der Gerade, die durch x = a1 = a2 verlaueft und senkrecht auf der x-Achse steht
        y = mq * x + tq  # y-Wert des Schnittpunkts, y = p(x)

        # Ueberpruefe, ob x in beiden Definitionsbereichen liegt und y in beiden Wertemengen
        if imIntervall(x, Dp) and imIntervall(x, Dq) and imIntervall(y, Wp) and imIntervall(y, Wq):
            return [x, y]  # => Es gibt genau einen Schnittpunkt bei (x, y)
        else:
            return False  # => Es gibt genau einen Schnittpunkt, der jedoch nicht auf den Strecken liegt

    try:
        # q(x) = mq * x + tq
        mq = (d1 - d2) / (c1 - c2)  # Steigung von q
        tq = d1 - c1 * mq  # Erhoehung von q

    except ZeroDivisionError:  # => Die Strecke Q1Q2 steht senkrecht auf der x-Achse

        x = c1  # Schnittpunkt mit der Gerade, die durch x = c1 = c2 verlaueft und senkrecht auf der x-Achse steht
        y = mp * x + tp  # y-Wert des Schnittpunkts, y = p(x)

        # Ueberpruefe, ob x in beiden Definitionsbereichen liegt und y in beiden Wertemengen
        if imIntervall(x, Dp) and imIntervall(x, Dq) and imIntervall(y, Wp) and imIntervall(y, Wq):
            return [x, y]  # => Es gibt genau einen Schnittpunkt
        else:
            return False  # => Es gibt genau einen Schnittpunkt, der jedoch nicht auf den Strecken liegt

    try:
        x = (tq - tp) / (mp - mq)  # x-Koordinate des Schnittpunkts
        y = mp * x + tp  # y-Koordinate des Schnittpunkts

    except ZeroDivisionError:  # => Beide Strecken sind parallel zueinander
        return False  # => kein Schnittpunkt

    # Ueberpruefe, ob x in beiden Definitionsbereichen liegt und y in beiden Wertemengen
    if imIntervall(x, Dp) and imIntervall(x, Dq) and imIntervall(y, Wp) and imIntervall(y, Wq):
        return [x, y]  # => Es gibt genau einen Schnittpunkt
    else:
        return False  # => Es gibt genau einen Schnittpunkt, der jedoch nicht auf den Strecken liegt


dreiecke = []  # Erstelle eine Liste mit allen Dreiecken
le = len(linien)  # le ist die Länge von linien
print(linien)  # gebe alle Linien aus
for a in range(0, le - 2):  # durchlaufe 0 bis le-2 als a
    for b in range(a + 1, le - 1):  # durchlaufe a+1 bis le-1 als b
        for c in range(b + 1, le):  # durchlaufe b+1 bis le als c
            print(a, b, c)  # gebe a,b und c aus
            A = linien[a]  # A ist die Linie an der Stelle a
            B = linien[b]  # B ist die Linie an der Stelle b
            C = linien[c]  # C ist die Linie an der Stelle c
            s1 = einSchnittpunkt(A[0], A[1], A[2], A[3], B[0], B[1], B[2], B[3])  # suche nach Schnittpunkt von A und B
            s2 = einSchnittpunkt(A[0], A[1], A[2], A[3], C[0], C[1], C[2], C[3])  # suche nach Schnittpunkt von A und C
            s3 = einSchnittpunkt(C[0], C[1], C[2], C[3], B[0], B[1], B[2], B[3])  # suche nach Schnittpunkt von C und B
            print(s1, s2, s3)  # gebe die Schnittpunkte aus
            if (s1 != False) and (s2 != False) and (s3 != False):  # prüfe ob sich alle 3 Linien schneiden
                if (s1 != s2) and (s1 != s2) and (s2 != s3):  # prüfe ob die Schnittpunkte an verschiedenen Orten sind
                    dreiecke.append([s1, s2, s3])  # Füge dreiecke die Schnittpunkte hinzu
                    # Die Verbindungen der Schnittpunkte werden in Rot eingezeichnet (also das Dreieck):
                    draw.line((s1[0]+resolution, m - s1[1] - resolution, s2[0]+resolution, m - s2[1] - resolution),width=w , fill=(255, 0, 0))
                    draw.line((s1[0]+resolution, m - s1[1] - resolution, s3[0]+resolution, m - s3[1] - resolution),width=w , fill=(255, 0, 0))
                    draw.line((s3[0]+resolution, m - s3[1] - resolution, s2[0]+resolution, m - s2[1] - resolution),width=w , fill=(255, 0, 0))
                    pic.save("Dreiecke"+n+"/Dreieck" + str(len(dreiecke)) + ".png")  # Speichere das Bild
                    # Die eben gezeichneten Linien werden wieder mit Schwarz übermalt:
                    draw.line((s1[0]+resolution, m - s1[1] - resolution, s2[0]+resolution, m - s2[1] - resolution),width=w , fill=(0, 0, 0))
                    draw.line((s1[0]+resolution, m - s1[1] - resolution, s3[0]+resolution, m - s3[1] - resolution),width=w , fill=(0, 0, 0))
                    draw.line((s3[0]+resolution, m - s3[1] - resolution, s2[0]+resolution, m - s2[1] - resolution),width=w , fill=(0, 0, 0))

print(dreiecke)  # Gebe alle Dreiecke aus
print(len(dreiecke))  # Gebe die Anzahl der Dreiecke aus
