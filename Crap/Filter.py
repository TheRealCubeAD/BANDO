from PIL import Image


path1 = ""  #text
path2 = ""  #hintergrund
path3 = ""  #ergebniss


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