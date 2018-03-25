from PIL import Image
import random


def inp(text):
    while 1:
        try:
            print(text)
            return int(input(">>>"))
        except ValueError:
            print("Keine gültige Eingabe!")


def zufall():
    global fix
    return random.randint(0, (len(fix)-1))


def mittel():
    global px
    global py
    global fix
    z = zufall()
    px = (px + fix[z][0]) / 2
    py = (py + fix[z][1]) / 2
    raw.putpixel((int(px), int(py)), 1)


res = inp("Anzahl der Pixel")
raw = Image.new("1", (res, res))
bild = raw.load()

fix = []

for i in range(0, inp("Anzahl der Fixpunkte")):
    print("Fixpunkt", i, ":")
    while 1:
        x = inp("X-Koordinate")
        if x <= res:
            break
    while 1:
        y = inp("Y-Koordinate")
        if y <= res:
            break
    fix.append([x, y])

    raw.putpixel((x, y), 1)

    print("")

print("Startpunkt")
px = inp("X-Koordinate")
py = inp("Y-Koordinate")

for a in range(1, inp("Anzahl der Durchläufe")):
    mittel()

raw.save("Sierpinski.jpg")
