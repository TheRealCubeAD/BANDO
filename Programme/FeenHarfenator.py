from tkinter import *
from PIL import Image, ImageDraw

noten = []
verb = []
werte = ["G", "G#", "A", "Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#", "G2", "G#2", "A2", "Bb2", "B2", "C2", "C#2",
         "D2", "Eb2", "E2", "F2", "F#2", "G3"]
current = [1, 0, 0, 0, 0, 0]
curverb = 0
notenbutton = []
beinotenbutton = []
langbutton = []


def notenknopfreset():
    global notenbutton
    for notenknopf in notenbutton:
        notenknopf.configure(bg="grey")


def beinotenknopfreset():
    global beinotenbutton
    for notenknopf in beinotenbutton:
        notenknopf.configure(bg="grey")


def langknopfreset():
    global langbutton
    for knopf in langbutton:
        knopf.configure(bg="grey")


def langkonpfaktion0():
    global current
    global langbutton
    current[3] = 1
    langknopfreset()
    langbutton[0].configure(bg="green")


def langkonpfaktion1():
    global current
    global langbutton
    current[3] = 2
    langknopfreset()
    langbutton[1].configure(bg="green")


def langkonpfaktion2():
    global current
    global langbutton
    current[3] = 4
    langknopfreset()
    langbutton[2].configure(bg="green")


def langkonpfaktion3():
    global current
    global langbutton
    current[3] = 8
    langknopfreset()
    langbutton[3].configure(bg="green")


def konpfaktion0():
    nid = 0
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion1():
    nid = 1
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion2():
    nid = 2
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion3():
    nid = 3
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion4():
    nid = 4
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion5():
    nid = 5
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion6():
    nid = 6
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion7():
    nid = 7
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion8():
    nid = 8
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion9():
    nid = 9
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion10():
    nid = 10
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion11():
    nid = 11
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion12():
    nid = 12
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion13():
    nid = 13
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion14():
    nid = 14
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion15():
    nid = 15
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion16():
    nid = 16
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion17():
    nid = 17
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion18():
    nid = 18
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion19():
    nid = 19
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion20():
    nid = 20
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion21():
    nid = 21
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion22():
    nid = 22
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion23():
    nid = 23
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def konpfaktion24():
    nid = 24
    global current
    global notenbutton
    current[1] = nid + 1
    notenknopfreset()
    notenbutton[nid].configure(bg="green")


def beikonpfaktion0():
    nid = 0
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion1():
    nid = 1
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion2():
    nid = 2
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion3():
    nid = 3
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion4():
    nid = 4
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion5():
    nid = 5
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion6():
    nid = 6
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion7():
    nid = 7
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion8():
    nid = 8
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion9():
    nid = 9
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion10():
    nid = 10
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion11():
    nid = 11
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion12():
    nid = 12
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion13():
    nid = 13
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion14():
    nid = 14
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion15():
    nid = 15
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion16():
    nid = 16
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion17():
    nid = 17
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion18():
    nid = 18
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion19():
    nid = 19
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion20():
    nid = 20
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion21():
    nid = 21
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion22():
    nid = 22
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion23():
    nid = 23
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def beikonpfaktion24():
    nid = 24
    global current
    global beinotenbutton
    current[4] = nid + 1
    beinotenknopfreset()
    beinotenbutton[nid].configure(bg="green")


def pause():
    global current
    if current[0] == 1:
        current[0] = 2
        pausebutton.configure(text="Pause")
    else:
        current[0] = 1
        pausebutton.configure(text="Note")


def beikonpfaktionnone():
    global current
    current[4] = 0
    beinotenknopfreset()
    beinotenbutton[25].configure(bg="green")


def anfangknopf():
    global curverb
    curverb = 1
    anfangbutton.configure(bg="green")
    endebutton.configure(bg="grey")


def endeknopf():
    global curverb
    curverb = 2
    anfangbutton.configure(bg="grey")
    endebutton.configure(bg="green")


def punkt():
    global current
    if current[5] == 0:
        current[5] = 1
        punktbutton.configure(bg="green")
    else:
        current[5] = 0
        punktbutton.configure(bg="grey")


def verbanwenden():
    global curverb
    global verb
    global noten
    ae = curverb
    vid = verbid.get()
    if ae != 0:
        if vid is not "":
            try:
                vid = int(vid)
                ae -= 1
                while vid > len(verb):
                    verb.append([0, 0])
                vid -= 1
                verb[vid][ae] = len(noten)
                anfangbutton.configure(bg="grey")
                endebutton.configure(bg="grey")
                verbid.delete(0, END)
                curverb = 0
                say("Verbindung hinzugefügt", "darkgreen")
            except ValueError:
                say("Bitte gib eine Zahl als ID an", "red")
        else:
            say("Bitte gib die ID der Verbindung an", "red")
    else:
        say("Bitte gib die Art der Verbindung an", "red")


notenmethoden = [konpfaktion0, konpfaktion1, konpfaktion2, konpfaktion3, konpfaktion4, konpfaktion5,
                 konpfaktion6, konpfaktion7, konpfaktion8, konpfaktion9, konpfaktion10, konpfaktion11,
                 konpfaktion12, konpfaktion13, konpfaktion14, konpfaktion15, konpfaktion16, konpfaktion17,
                 konpfaktion18, konpfaktion19, konpfaktion20, konpfaktion21, konpfaktion22, konpfaktion23,
                 konpfaktion24]

beinotenmethoden = [beikonpfaktion0, beikonpfaktion1, beikonpfaktion2, beikonpfaktion3, beikonpfaktion4,
                    beikonpfaktion5, beikonpfaktion6, beikonpfaktion7, beikonpfaktion8, beikonpfaktion9,
                    beikonpfaktion10, beikonpfaktion11, beikonpfaktion12, beikonpfaktion13, beikonpfaktion14,
                    beikonpfaktion15, beikonpfaktion16, beikonpfaktion17, beikonpfaktion18, beikonpfaktion19,
                    beikonpfaktion20, beikonpfaktion21, beikonpfaktion22, beikonpfaktion23, beikonpfaktion24,
                    beikonpfaktionnone]

langmethoden = [langkonpfaktion0, langkonpfaktion1, langkonpfaktion2, langkonpfaktion3]


def abfrage():
    f = 1
    while f == 1:
        eingabe = input(">>>")
        if eingabe == "n":
            neu(1)
        elif eingabe == "p":
            neu(2)
        elif eingabe == "v":
            verbindung()
        elif eingabe == "fertig":
            f = 0


def verbindung():
    global verb
    global noten
    index = int(input("ID der Verbindung: "))
    while index > len(verb):
        verb.append([0, 0])
    index -= 1
    ae = ""
    while ae != "a" and ae != "e":
        ae = input("Anfang oder Ende? (a/e) >>>")
    if ae == "a":
        ae = 0
    elif ae == "e":
        ae = 1
    if verb[index][ae] == 0:
        verb[index][ae] = len(noten) - 1
    else:
        print("Bereits belegt")


def verbindungz():
    global pic
    global draw
    global noten
    global verb
    verx = []
    for ver in verb:
        lo = [noten[ver[0]][1] + 100, noten[ver[0]][2]]
        lu = [noten[ver[1]][1] + 100, noten[ver[1]][2]]
        x = 0
        ma = max(ver[0], ver[1])
        mi = min(ver[0], ver[1])
        for i in range(mi, ma + 1):
            if noten[i][1] > x:
                x = noten[i][1]
        x += 300
        while x > 2590:
            x -= 5
        ok = False
        while not ok:
            ok = True
            for i in verx:
                if i - 3 < x < i + 3:
                    ok = False
            if not ok:
                x -= 5
        del ok
        verx.append(x)
        ro = [x, lo[1]]
        ru = [x, lu[1]]
        draw.line((lo[0], lo[1], ro[0], ro[1]), 0, 3)
        draw.line((ru[0], ru[1], ro[0], ro[1]), 0, 3)
        draw.line((lu[0], lu[1], ru[0], ru[1]), 0, 3)
        draw.line((lu[0], lu[1], lu[0] + 50, lu[1] + 25), 0, 3)
        draw.line((lu[0], lu[1], lu[0] + 50, lu[1] - 25), 0, 3)
        draw.line((lo[0], lo[1] + 25, lo[0] + 50, lo[1]), 0, 3)
        draw.line((lo[0], lo[1] - 25, lo[0] + 50, lo[1]), 0, 3)


def neu(art):
    global werte
    global noten
    print("")
    if art == 1:
        print("Hauptnote:")
    elif art == 2:
        print("Pause:")
    note = [art, finden("Wert: ", werte), len(noten)]
    while 1:
        la = str(input("Laenge: 1/"))
        if int(la[0]) == 1 or int(la[0]) == 2 or int(la[0]) == 4 or int(la[0]) == 8:
            break
        else:
            print("keine gueltige laenge!")
    note.append(la)
    print("")
    if input("Beinote? (j/n) >>>") == "j":
        print("Beinote:")
        bn = finden("Wert: ", werte)
    else:
        bn = 0
    note.append(bn)
    if len(note) != 5:
        print("ERROR")
    else:
        noten.append(note)


def finden(text, l):
    while 1:
        x = input(text)
        for index in range(0, len(l)):
            if l[index] == x:
                return index + 1
        print("nicht gefunden!")


def kord():
    global noten
    xm = 100
    ym = 2330 / (len(noten) - 1)
    for i in noten:
        i[1] = int(i[1] * xm)
        i[2] = 90 + int(i[2] * ym)
        i[4] = int(i[4] * xm)


def linien():
    global noten
    global draw
    global pic
    for i in range(1, len(noten)):
        draw.line((noten[i - 1][1], noten[i - 1][2], noten[i][1], noten[i][2]), 0, 7)
    for i in noten:
        if i[4] != 0:
            draw.line((i[1], i[2], i[4], i[2]), 0, 4)


def kreis(x, y, a):
    global pic
    global draw
    art = int(a[0])
    punkt = False
    try:
        if a[1] == ".":
            punkt = True
    except IndexError:
        punkt = False
    r = 0
    f = False
    if art == 1:
        r = 50
        f = False
    elif art == 2:
        r = 40
        f = False
    elif art == 4:
        r = 35
        f = True
    elif art == 8:
        r = 25
        f = True
    draw.ellipse((x - r, y - r / 1.5, x + r, y + r / 1.5), 0)
    if not f:
        r -= 8
        draw.ellipse((x - r, y - r / 1.5, x + r, y + r / 1.5), 1)
        r += 8
    if punkt:
        xk = x + r + 7
        yk = y + r / 1.5 - r / 5
        r /= 5
        draw.ellipse((xk - r, yk - r, xk + r, yk + r), 0)


def pausez(x, y, a):
    global pic
    global draw
    art = int(a[0])
    punkt = False
    try:
        if a[1] == ".":
            punkt = True
    except IndexError:
        punkt = False
    r = 0
    f = False
    if art == 1:
        r = 50
        f = False
    elif art == 2:
        r = 40
        f = False
    elif art == 4:
        r = 35
        f = True
    elif art == 8:
        r = 25
        f = True
    draw.rectangle((x - r / 2, y - r, x + r / 2, y + r), 0)
    if not f:
        r -= 7
        draw.rectangle((x - r / 2, y - r, x + r / 2, y + r), 1)
    if punkt:
        xk = x + r
        yk = y + r / 1.5 - r / 5
        r /= 5
        draw.ellipse((xk - r, yk - r, xk + r, yk + r), 0)


def notenz():
    global noten
    for i in noten:
        if i[0] == 1:
            kreis(i[1], i[2], i[3])
        elif i[0] == 2:
            pausez(i[1], i[2], i[3])
        if i[4] != 0:
            kreis(i[4], i[2], i[3])


def anwenden():
    global current
    global noten
    if current[1] != 0:
        if current[3] != 0:
            result = [current[0], current[1], len(noten), str(current[3]), current[4]]
            if current[5] == 1:
                result[3] += "."
            noten.append(result)
            notenknopfreset()
            beinotenknopfreset()
            langknopfreset()
            punktbutton.configure(bg="grey")
            pausebutton.configure(text="Note")
            beinotenbutton[25].configure(bg="green")
            anfangbutton.configure(bg="grey")
            endebutton.configure(bg="grey")
            verbid.delete(0, END)
            current = [1, 0, 0, 0, 0, 0]
            say("Note hinzugefügt", "darkgreen")
        else:
            say("Bitte gib die Länge der Note an", "red")
    else:
        say("Bitte gib den Wert der Note an", "red")


def say(text, color):
    text = ">>> "+text
    info.configure(text=text, fg=color)


def ende():
    global pic
    global fenster
    global noten
    na = name.get()
    if len(na) > 0:
        if len(noten) > 1:
            kord()
            linien()
            verbindungz()
            notenz()
            pic.save(na+".png")
            fenster.quit()
        else:
            say("Bitte gib mindestens 2 Noten an", "red")
    else:
        say("Bitte gib den Namen der Datei an", "red")


fenster = Tk()
fenster.title("FeenHarfenator 2000 (Benjamin Schaab) All rights reserved")

for i in range(25):
    notenbutton.append(Button(fenster, text=werte[i], command=notenmethoden[i], bg="grey", height=3, width=9))

for i in range(25):
    beinotenbutton.append(Button(fenster, text=werte[i], command=beinotenmethoden[i], bg="grey", height=3, width=9))
beinotenbutton.append(Button(fenster, text="", command=beinotenmethoden[25], bg="green", height=3, width=9))

for i in range(4):
    langbutton.append(Button(fenster, text="1/" + str(2 ** i), command=langmethoden[i], bg="grey", height=3, width=9))

label1 = Label(fenster, text="Hauptnote:")
label2 = Label(fenster, text="Beinote:")
label3 = Label(fenster, text="Länge:")
label4 = Label(fenster, text="Verbindung:")
label5 = Label(fenster, text="ID:")
label6 = Label(fenster, text="Name")
info = Label(fenster, text="")
verbid = Entry(fenster, width=9)
pausebutton = Button(fenster, text="Note", command=pause, height=3, width=9)
punktbutton = Button(fenster, text=".", command=punkt, bg="grey", height=3, width=9)
anfangbutton = Button(fenster, text="Anfang", command=anfangknopf, bg="grey", height=3, width=9)
endebutton = Button(fenster, text="Ende", command=endeknopf, bg="grey", height=3, width=9)
verbutton = Button(fenster, text="Hinzufügen", command=verbanwenden, bg="lightblue", height=1, width=9)
fertigbutton = Button(fenster, text="Fertig", command=anwenden, bg="lightgreen", height=1, width=270)
name = Entry(fenster, width=20)
save = Button(fenster, text="Speichern und Beenden", command=ende, bg="darkorange", height=1, width=20)

label1.grid(row=0, column=13, pady=10)
label2.grid(row=2, column=13, pady=10)
label3.grid(row=4, column=3, pady=10)
label4.grid(row=4, column=17, pady=10)
label5.grid(row=5, column=16, pady=2)
label6.place(x=60, y=378)
info.place(x=500, y=260)
verbid.grid(row=5, column=17, pady=2)

for i in range(25):
    notenbutton[i].grid(row=1, column=i, pady=2)

for i in range(26):
    beinotenbutton[i].grid(row=3, column=i, pady=2)

for i in range(4):
    langbutton[i].grid(row=5, column=i, pady=2)

fenster.geometry("1900x400")
pausebutton.grid(row=1, column=25, pady=2)
punktbutton.grid(row=5, column=5, pady=2)
anfangbutton.grid(row=5, column=18, pady=2)
endebutton.grid(row=5, column=19, pady=2)
verbutton.grid(row=5, column=21, pady=2)
fertigbutton.place(x=0, y=310)
name.place(x=20, y=360)
save.place(x=160, y=356)

pic = Image.new("1", (2600, 2600), 1)
draw = ImageDraw.Draw(pic)

fenster.mainloop()
