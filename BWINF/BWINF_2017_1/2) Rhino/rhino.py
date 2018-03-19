from PIL import Image

bildName = input("Name des Bildes: ")
file = "C:\\Users\\Public\\"
file = file + bildName

image = Image.open(file)
im = image.load()

breite, höhe = image.size
breite = breite - 1
höhe = höhe - 1

x = 1
y = 1
count = 0
white = ((255, 255, 255))

while y < höhe:
    while x < breite:
        if image.getpixel((x, y)) == image.getpixel(((x + 1), y)) == image.getpixel((x, (y + 1))) == image.getpixel(
                ((x + 1), (y + 1))):
            image.putpixel(((x, y)), white)
            image.putpixel(((x + 1, y)), white)
            image.putpixel(((x, y + 1)), white)
            image.putpixel(((x + 1, y + 1)), white)
            count = count + 1

        x = x + 1
    x = 1
    y = y + 1
image.save(bildName + "-entdeckt.png")
print("Fertig")
print("Zahl der gefundenen potentiellen Schuppen: ", count)
