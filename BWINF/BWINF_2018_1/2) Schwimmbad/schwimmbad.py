import math  # Importiere Mathe


def gueltigkeit(o, u, t, f, p, g):  # Prueft, ob die Zusammenstellung von Tickets gueltig ist
    if p > g:  # Wenn ein Gutschein fuer den 10% Rabatt-Bonus gebraucht wird, ohne dass ein Gutschein da ist,
        return False  # Dann gib False zurueck

    for i in range(f + 1):
        A = i  # Anzahl Familienkarten Typ A: 2 o16 + 2 u16
        B = f - i  # Anzahl Familienkarten Typ B: 1 o16 + 3 u16
        f_u = 2 * A + 3 * B  # Anzahl der u16er, die durch die Familienkarten mitgenommen werden koennen
        f_o = 2 * A + 1 * B  # Anzahl der o16er, die durch die Familienkarten mitgenommen werden koennen
        z_u = u16 - u - f_u  # Anzahl der u16er, die nicht durch Einzel- oder Familienkarte reinkommen
        z_o = o16 - o - f_o  # Anzahl der o16er, die nicht durch Einzel- oder Familienkarte reinkommen
        if z_u < 0:  # Wenn zu viele u16er Tickets da sind,
            z_u = 0  # Dann sind alle u16er drin
        if z_o < 0:  # Wenn zu viele o16er Tickets da sind,
            z_o = 0  # Dann sind alle o16er drin
        z_ges = z_u + z_o  # Anzahl der noch unterzubringenden Personen
        if z_ges <= 6 * t + g - p:  # Wenn diese Anzahl kleiner ist als die noch zur Verfuegung stehenden Freikarten
            return True  # Dann gib True zurueck
    return False  # Gib False zurueck


def preis(o, u, t, f, p, g):  # Berechnet aus der gegebenen Kombination von Tickets den Gesamtpreis
    if wo:  # Wenn der Termin am Wochenende ist,
        preis_ges = o * 3.5 + u * 2.5 + t * 11 + f * 8  # Dann Berechnung des Preises mit dem Normal-Preisen
    else:  # Sonst:
        preis_ges = o * 2.8 + u * 2 + t * 11 + f * 8  # Berechnung des Preises mit den -20Prozent-Preisen
    if p:  # Wenn p gleich 1 ist bzw. Wenn ein -10Prozent-Gutschein verwendet wird:
        preis_ges -= preis_ges * 0.1  # Dann ziehe vom Gesamtpreis 10 Prozent ab
    return preis_ges  # Gebe den Gesamtpreis zurück


print("Anzahl")                         # Frage die Anzahl der
u4 = int(input("unter 4 jährigen: "))   # Unter 4 Jaehrigen ab
u16 = int(input("4 bis 16 jährigen: "))   # 4 bis 16 Jaehrigen ab
o16 = int(input("über 16 jährigen: "))  # Ueber 16 Jaehrigen ab
G = int(input("Gutscheine: "))  # Der Gutscheine ab

if u4 > 0 and o16 == 0:  # Wenn es eine unter 4 Jaehrige, und keine über 16 Jaehrige Person gibt:
    print("Der u4er hat keine Begleitperson.")
    print(" - Programmende - ")
    while True:  # Dann wird das Programm "beendet"
        pass

wo = int(input("Ist Wochenende: "))  # Frage ab, ob der Termin am Wochenende ist
fe = int(input("Ist Ferien: "))  # Frage ab, ob der Termin in den Ferien ist

O_max = o16  # Maximale Anzahl der Ueber-16-Tickets
U_max = u16  # Maximale Anzahl der Unter-16-Tickets
T_max = int(math.ceil((o16 + u16) / 6))  # Maximale Anzahl der Tageskarten
if o16 >= u16:  # Wenn Anzahl der Ueber-16er groesser/gleich Anzahl der Unter-16er
    F_max = int(math.ceil(o16/2))  # Dann Maximale Anzahl der Familientickets
else:  # Sonst
    F_max = int(math.ceil(u16/2))  # Maximale Anzahl der Familientickets
P_max = 1  # Maximale Anzahl der 10Prozent-Gutscheine

if wo:  # Wenn Termin am Wochenende:
    T_max = 0  # Dann Maximale Anzahl der Tageskarten ist 0

if fe:  # Wenn Termin in den Ferien:
    G = 0  # Dann Anzahl der Gutscheine ist 0
    P_max = 0  # Dann Maximale Anzahl der 10Prozent-Ticktets ist 0

m_preis = -1  # Minimaler Preis ist -1
m_eintritt = []  # Als Liste realisierter 6-Tuppel des billigsten Ticketeinkaufs
for O in range(O_max + 1):  # Durchlaufe 0 bis O_max als O
    for U in range(U_max + 1):  # Durchlaufe 0 bis U_max als U
        for T in range(T_max + 1):  # Durchlaufe 0 bis T_max als T
            for F in range(F_max + 1):  # Durchlaufe 0 bis F_max als F
                for P in range(P_max + 1):  # Durchlaufe 0 bis P_max als P
                    if gueltigkeit(O, U, T, F, P, G):  # Wenn diese Kombination von Tickets gueltig ist
                        z_preis = preis(O, U, T, F, P, G)  # Dann berechne den Preis dieser Kombination
                        # Wenn dieser Preis kleiner als der bisher billigste Preis ist:
                        if z_preis < m_preis or m_preis == -1:
                            m_preis = z_preis  # Dann ueberschreibe den billigsten Preis mit dem eben berechneten
                            # Ueberschreibe die Liste mit dem billigerem 6-Tuppel
                            m_eintritt = [O, U, T, F, P, u16+o16-O-U-6*T-4*F]

tickets = ["Einzelkarten Ueber 16", "Einzelkarten Unter 16", "Tageskarten", "Familientickets", "10% Gutschein",
           "Ticket-Gutscheine"]  # Liste die das Ausgeben der Tickets vereinfacht
print("-----")
print("Zu kaufende Tickets:")
print()
for i in range(len(tickets)):  # Gebe alle zu kaufenden Tickets aus
    print(tickets[i] + ": " + str(m_eintritt[i]))
print("-----")
print("Das macht einen Gesamtpreis von " + str(m_preis) + "€")  # Gebe den Gesamtpreis aus
print("")
print(" - Programmende - ")