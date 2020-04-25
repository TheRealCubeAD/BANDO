from PIL import Image
import math

path = input("Filename >>>")

main_im = Image.open(path)

tresh = int(2600/math.sqrt(2) * (11/12)) #1838

left = Image.new("1", (int(2600/math.sqrt(2)), 2600), 1)
right = Image.new("1", (int(2600/math.sqrt(2)), 2600), 1)

for y in range(2600):
    for x in range(int(2600 * (12/11))):
        color = main_im.getpixel((x * (11/12), y))
        if x < 1838:
            left.putpixel((x, y), color)
        else:
            right.putpixel((x-1838, y), color)

left.save("left.png")
right.save("right.png")