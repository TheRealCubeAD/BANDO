import neopixel
import machine
import time


class LED:
    #PARAMETERS
    n = None #Anzahl LEDs
    p = None #GPIO pin fuer din
    NP = None #NeoPixel-Control

    def __init__(self,aLEDs = 90,GPIO = 4):
        self.n = aLEDs
        self.p = GPIO

        self.NP = neopixel.NeoPixel(machine.Pin(self.p),self.n)

    def divied(self,color,fac):
        return (int(color[0]/fac),int(color[1]/fac),int(color[2]/fac))

    def mix(self,c1,c2,fac=0.5):
        r = int(c1[0] * fac + c2[0] * (1 - fac))
        g = int(c1[1] * fac + c2[1] * (1 - fac))
        b = int(c1[2] * fac + c2[2] * (1 - fac))
        return (r,g,b)

    def all(self,color):
        for pixel in range(self.n):
            self.NP[pixel] = color
        self.send()

    def forewardOnly(self,color,reColor = (0,0,0),amount = 9):
        for mPixel in range(self.n+(amount-1)/2):
            for pixel in range(amount):
                pixel -= int((amount-1)/2)
                if mPixel + pixel in range(0,self.n):
                    print(mPixel,pixel)
                    self.NP[mPixel+pixel] = self.mix(reColor,color,fac=abs(pixel)/((amount-1)/2))
            self.send()
            time.sleep(0.01)

    def inRange(self,a1,a2,b):
        if min(a1,a2) <= b <= max(a1,a2):
            return True
        else:
            return False

    def flow(self,color,reColor,start,end,length,stepSize):
        if start < end:
            tStart = start - int((length + 3) / 2)
            tEnd = end + int((length + 3) / 2)
        else:
            tStart = start + int((length + 3) / 2)
            tEnd = end - int((length + 3) / 2)

        i = tStart
        while self.inRange(tStart,tEnd,i):
            for pixel in range(start,end):
                distance = abs(i-pixel)
                self.NP[pixel] = self.mix(reColor,color,min(1,distance/length))
            self.send()
            i += stepSize



    def send(self):
        self.NP.write()


