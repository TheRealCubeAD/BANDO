from PIL import Image


path1 = "C:/Users/benni/PycharmProjects/BANDO/Saskia/B10001.png"  #text
path2 = "C:/Users/benni/PycharmProjects/BANDO/Saskia/B20001.png"  #hintergrund
path3 = "C:/Users/benni/PycharmProjects/BANDO/Saskia/B30001.png"  #ergebniss


text = Image.open(path1)
hint = Image.open(path2)


x,y = text.size


res = Image.new("RGB",(x,y))


for xx in range(x):
    for yy in range(y):

        pixT = text.getpixel((xx,yy))
        pixH = hint.getpixel((xx,yy))

        pixR = (pixT[0]+pixH[0],pixT[1]+pixH[1],pixT[2]+pixH[2])

        res.putpixel((xx,yy),pixR)

res.save(path3)