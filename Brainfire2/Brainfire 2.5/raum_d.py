import random

class VEC:

    def __init__(self, z, y, x):
        self.z = z
        self.y = y
        self.x = x

    def __eq__(self, other):
        return self.z == other.z and self.y == other.y and self.x == other.y

    def __add__(self, other):
        return VEC(self.z + other.z, self.y + other.y, self.x + other.x)

    def __sub__(self, other):
        return VEC(self.z - other.z, self.y - other.y, self.x - other.x)

    def invert(self):
        return VEC(-self.z, -self.y, -self.x)

    def inText(self, bz=True):
        text = ""
        if bz:
            text += self.z
        text += " " + str(self.y) + " " + str(self.x)
        return text


class ROOM:

    def __init__(self, sy=16, sx=16, stone_treshold=0.2, portal_treshold=0.5):
        self.sy = sy
        self.sx = sx
        self.matrix = None
        self.init_matrix(stone_treshold)

        self.connections = [[False for x in range(8)] for y in range(8)]
        self.doors = [VEC(0, 0, self.sx / 2 - 1),
                      VEC(0, self.sy / 2, 0),
                      VEC(0, self.sy - 1, self.sx / 2),
                      VEC(0, self.sy / 2 - 1, self.sx - 1),
                      VEC(1, 0, self.sx / 2 - 1),
                      VEC(1, self.sy / 2, 0),
                      VEC(1, self.sy - 1, self.sx / 2),
                      VEC(1, self.sy / 2 - 1, self.sx - 1)
                      ]

    def init_matrix(self, s_treshold, p_treshold):
        for z in range(2):
            for y in range(self.sy):
                for x in range(self.sx):
                    self.matrix[z][y][x] = (random.random < s_treshold)

        if random.random



if __name__ == '__main__':
    v = VEC(1,2,3)
    v = -v