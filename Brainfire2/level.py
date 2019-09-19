import random
import time
import raum


class LEVEL:
    sx = None
    sy = None

    matrix = None

    def __init__(self):
        self.sx = 6
        self.sy = 6

        rooms = raum.massProduction(self.sx*self.sy)

        self.matrix = [rooms[i:i + self.sx] for i in range(0,len(rooms),self.sx)]
        print(self.matrix)

if __name__ == '__main__':
    l = LEVEL()