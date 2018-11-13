from PIL import Image
from tkinter import filedialog

def compress(pic1):
    nx,ny = (int(x/2) for x in pic1.size)
    pic2 = Image.new("RGB",(nx,ny))
    for y in range(ny):
        ay = y*2
        for x in range(nx):
            ax = x*2
            field = [pic1.getpixel((ax,ay)),pic1.getpixel((ax+1,ay)),pic1.getpixel((ax,ay+1)),pic1.getpixel((ax+1,ay+1))]
            r,g,b = ((int(sum((x[y] for x in field))/3) for y in range(3)))
            pic2.putpixel((x,y),(r,g,b))
    pic2.save(filedialog.asksaveasfilename(title="Save Picture"),filetypes=("Picture file",".jpg",".png",".pgm"))


while 1:
    file = filedialog.askopenfilename(title="Select Picture")
    if file == "":
        exit()
    print(file)
    try:
        pic = Image.open(file)
        compress(pic)
    except ZeroDivisionError:
        print("Error")
