from PIL import ImageGrab, Image
import time

green = (range(0,75),range(200,256),range(0,75))
red = (range(200,256),range(0,75),range(0,75))

tolerance = 0.85

def is_green(pix):
    per = ((255-pix[0])/255 + pix[1]/255 + (255-pix[2])/255)/3
    if per > tolerance:
        print(pix,per)
        return True
    else:
        return False

def is_red(pix):
    per = ( pix[0] / 255 + (255-pix[1]) / 255 + (255 - pix[2]) / 255) / 3
    if per > tolerance:
        print(pix,per)
        return True
    else:
        return False

time.sleep(5)
pic = ImageGrab.grab()
print("PIC grabbed")
sx,sy = pic.size
matrix = [[None for _ in range(sx)] for __ in range(sy)]
print("Matrix created")
for y in range(sy):
    for x in range(sx):
        pixel = pic.getpixel((x,y))
        if is_green(pixel):
            print("green at",y,x)
        elif is_red(pixel):
            print("red at",y,x)
        else:
            gr = int(sum(pixel)/3)
            pic.putpixel((x,y),(gr,gr,gr))
print("Matrix red")
pic.show()

