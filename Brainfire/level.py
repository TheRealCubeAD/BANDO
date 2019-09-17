import time
import random
import raum

class PSEUDOROOM:
    z = None
    y = None
    x = None

    p_connections = None

    p_IO = None

    def __init__(self,zyx,level_size):
        self.z, self.y, self.x = zyx
        p_IO = raum.all_doors
        #if self.y == 0:
        #    p_IO.remove(raum.door_up)
        #if self.y == level_size[1]-1:
        #    p_IO.remove(raum.door_down)
        #if self.x == 0:
        #    p_IO.remove(raum.door_left)
        #if self.x == level_size[2]-1:
        #    p_IO.remove(raum.door_right)
        self.p_connections = []


    def addPconn(self,start,end,value):
        self.p_connections.append((start,end,value))



class LEVEL:
    sz = None
    sy = None
    sx = None

    matrix = None

    start = None
    end = None

    path = None

    def __init__(self,size):
        self.sz,self.sy,self.sx = size
        self.matrix = []

        nz = random.randint(0,self.sz-1)
        if random.randint(0,1):
            ny = random.choice((0,self.sy-1))
            if ny == 0:
                ey = random.randint(int(self.sy /2 ),self.sy - 1)
            else:
                ey = random.randint(0, int(self.sy / 2))
            nx = random.randint(0,self.sx-1)
            ex = random.randint(0,self.sx-1)

        else:
            nx = random.choice((0,self.sx-1))
            if nx == 0:
                ex = random.randint(int(self.sx /2 ),self.sx - 1)
            else:
                ex = random.randint(0, int(self.sx / 2))
            ny = random.randint(0,self.sy-1)
            ey = random.randint(0, self.sy - 1)

        ez = random.randint(0, self.sz - 1)
        self.start = (nz,ny,nx)
        self.end = (ez,ey,ex)

        for z in range(self.sz):
            ry = []
            for y in range(self.sy):
                rx = []
                for x in range(self.sx):
                    rx.append(PSEUDOROOM((z,y,x),size))
                ry.append(rx)
            self.matrix.append(ry)


    def createPath(self):
        self.path = []
        room_amount = self.sz * self.sy * self.sx
        point_amount = int(room_amount/16)
        points = []
        for _ in range(point_amount):
            z = random.randint(0,self.sz-1)
            y = random.randint(0,self.sy-1)
            x = random.randint(0,self.sx-1)
            zyx = (z,y,x)
            if not zyx in points and zyx != self.start and zyx != self.end:
                points.append((z,y,x))

        self.path.append(self.start)
        while points:
            near = self.nearest(self.path[-1],points)
            points.remove(near)
            self.path.append(near)

        self.path.append(self.end)


    def nearest(self,point,points):
        deltas = []
        for p in points:
            dz = abs(p[0] - point[0])
            dy = abs(p[1] - point[1])
            dx = abs(p[2] - point[2])
            d = dz+dy+dx
            deltas.append(d)
        return points[deltas.index(min(deltas))]

L = LEVEL((2,6,6))
print(L.start)
print(L.end)
L.createPath()
print(L.path)
