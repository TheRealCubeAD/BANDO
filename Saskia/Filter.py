from PIL import Image


path1 = "Saskia.png"  #text
path2 = "B20001.png"  #hintergrund
path3 = "RES2.png"  #ergebniss


text = Image.open(path2)
hint = Image.open(path1)

x,y = text.size
verd = 50
verd2 = 0

res = Image.new("RGB",(x,y))


for xx in range(x):
    for yy in range(y):

        pixT = text.getpixel((xx,yy))
        pixH = hint.getpixel((xx,yy))
        pixR = (pixT[0]+pixH[0],pixT[1]+pixH[1],pixT[2]+pixH[2])

        if pixT[0] < 240:
            mi = int(min(pixR[0],pixR[1],pixR[2])/2)
            pixR = (pixR[0]-mi,pixR[1]-mi,pixR[2]-mi)

        res.putpixel((xx,yy),pixR)

res.save(path3)