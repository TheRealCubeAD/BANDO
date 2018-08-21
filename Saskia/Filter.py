from PIL import Image


path1 = "Saskia.png"  #text
path2 = "Text.png"  #hintergrund
path3 = "RES.png"  #ergebniss


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

        if pixT[0] != 255:
            pixR = (pixR[0]-verd,pixR[1]-verd,pixR[2]-verd)
        else:
            pixR = (pixR[0] - verd2, pixR[1] - verd2, pixR[2] - verd2)

        res.putpixel((xx,yy),pixR)

res.save(path3)