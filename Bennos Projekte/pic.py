from PIL import Image

i = Image.open("nichts.png")
print(i.getpixel((0,0)))