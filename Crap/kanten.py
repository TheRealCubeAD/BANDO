from PIL import Image
from copy import deepcopy

inp = Image.open("h.jpg", "r")
out = deepcopy(inp)

tresh = 100
tresh2 = 200
cy = [0 for _ in range(inp.size[1])]
cx = [0 for _ in range(inp.size[0])]

for y in range(inp.size[1]-1):
    for x in range(inp.size[0]-1):
        p1 = inp.getpixel((x, y))
        p2 = inp.getpixel((x + 1, y))
        p3 = inp.getpixel((x, y + 1))
        s1 = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])
        s2 = abs(p1[0] - p3[0]) + abs(p1[1] - p3[1]) + abs(p1[2] - p3[2])
        sr1 = s1 > tresh
        sr2 = s2 > tresh
        if sr1 and not sr2:
            cy[y] += 1
            out.putpixel((x, y), (255, 0, 0))
            out.putpixel((x, y + 1), (255, 0, 0))
        if sr2 and not sr1:
            cx[x] += 1
            out.putpixel((x, y), (255, 0, 0))
            out.putpixel((x + 1, y), (255, 0, 0))

for y in range(inp.size[1]):
    if cy[y] > tresh2:
        for x in range(inp.size[0]):
            out.putpixel((x, y), (0, 255, 0))

for x in range(inp.size[0]):
    if cx[x] > tresh2:
        for y in range(inp.size[1]):
            out.putpixel((x, y), (0, 255, 0))

out.show()

