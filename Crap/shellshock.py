from PIL import ImageGrab, Image
import time

green = (range(0,75),range(200,256),range(0,75))
red = (range(200,256),range(0,75),range(0,75))

tolerance = 0.85

def is_green(pix):
    per = ((255-pix[0])/255 + pix[1]/255 + (255-pix[2])/255)/3
    if per > tolerance:
        return True
    else:
        return False

def is_red(pix):
    per = ( pix[0] / 255 + (255-pix[1]) / 255 + (255 - pix[2]) / 255) / 3
    if per > tolerance:
        return True
    else:
        return False

def run():
    pic = ImageGrab.grab()
    sx, sy = pic.size
    player = []
    enemy = None
    for y in range(sy):
        for x in range(sx):
            pixel = pic.getpixel((x,y))
            if is_green(pixel):
                player.append((x,y))
            elif is_red(pixel) and not enemy == None:
                enemy = (x,y)
    playerkord = (int(sum([i[0] for i in player])/len(player)),int(sum([i[1] for i in player])/len(player)))
    print(playerkord)

while 1:
    run()
