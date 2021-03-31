import math
import socket
import tkinter
import threading
import copy

class point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __sub__(self, other):
        return point(self.x - other.x, self.y - other.y)


class cluster(point):
    c_range = 100
    show_limit = 1

    def __init__(self, point):
        self.x = point.x
        self.y = point.y
        self.size = 1
        self.suc = []
        self.showing = False
        self.death_timer = 200

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def union(self, other):
        if self.showing:
            self.clear()
        if other.showing:
            other.clear()
        self.x = (self.x * self.size + other.x * other.size) / (self.size + other.size)
        self.y = (self.y * self.size + other.y * other.size) / (self.size + other.size)
        self.size += other.size
        for c in other.suc:
            c.suc.remove(other)
        clusters.remove(other)
        self.update()


    def belongs(self, point):
        return abs(self - point) <= self.c_range

    def update(self):
        if self.size >= self.show_limit:
            if not self.showing:
                self.showing = True
                draw_point(self)
                self.line_update()
        else:
            self.death_timer -= 1
            if self.death_timer <= 0:
                clusters.remove(self)
                print("killed")
                return
            if self.showing:
                self.showing = False
                self.clear()
                self.line_update()

    def clear(self):
        self.showing = False
        clear_point(self)
        for s in self.suc:
            clear_line(self, s)

    def append(self, point):
        if self.size >= 15:
            return
        if self.showing:
            self.clear()
        self.x = (self.x * self.size/2 + point.x) / (self.size/2 + 1)
        self.y = (self.y * self.size/2 + point.y) / (self.size/2 + 1)
        self.size += 1
        self.update()


    def line_update(self):

        cls = []
        for c in clusters:
            if c == self:
                continue
            distance = abs(self - c)
            if distance <= 100:
                self.union(c)
            elif distance < 200:
                cls.append((distance, c))
        cls.sort(key=lambda tup: tup[0])
        for tup in cls:
            c = tup[1]
            if c in self.suc:
                continue
            self.suc.append(c)
            c.suc.append(self)
        if self.showing:
            for s in self.suc:
                if s.showing:
                    draw_line(self, s)


def myreceive():
    while 1:
        try:
            chunk = s.recv(2048).decode("UTF-8")
            print("not start")
            if "start" in chunk:
                print("start")
                break
        except:
            pass
    for _ in range(10):
        print("ignoring")
        chunk = s.recv(2048).decode("UTF-8")
    while 1:
        # print(chunk)
        try:
            try:
                chunks = s.recv(2048).decode("UTF-8").split(";")
            except:
                continue
            for chunk in chunks:
                chunk = chunk.rstrip()
                #print(chunk)
                try:
                    p, l = chunk.split(":")
                    left, right = p.split(",")
                    a, d = l.split(",")
                except:
                    continue
                left = int(left)
                right = int(right)
                a = int(a)
                d = int(d)
                r_angle = get_r_cord(left, right)
                a -= 10*r_angle
                draw_point(point(r_x, r_y))
                if d < 8000:
                    x, y = get_xy(a, d)
                    x += r_x
                    y += r_y
                    add_point(point(x, y))
            update_limit()
        except ConnectionError:
            pass


def get_r_cord(l, r):
    global l_left, l_right, r_x, r_y
    r = -r
    r_angle = (l - r) * 3.751/2
    f = ((l - l_left) + (r - l_right))/2
    dy = math.cos(r_angle * math.pi/180) * f * 3.25
    dx = math.sin(r_angle * math.pi/180) * f * 3.25
    l_left = l
    l_right = r
    r_x += dx
    r_y += dy
    return r_angle


def add_point(point):
    for c in clusters:
        if c.belongs(point):
            c.append(point)
            return
    clusters.append(cluster(point))


def get_xy(angle, distance):
    y = math.sin((angle/10)*math.pi/180) * distance
    x = math.cos((angle/10)*math.pi/180) * distance
    return x, y


def draw_point(point):
    x = point.x * zoom + middle
    y = point.y * zoom + middle
    w.create_oval(x - 1, y - 1, x + 1, y + 1, fill="black")

def clear_point(point):
    x = point.x * zoom + middle
    y = point.y * zoom + middle
    w.create_oval(x - 1, y - 1, x + 1, y + 1, fill="white", outline="white")

def draw_line(point1, point2):
    x1 = point1.x * zoom + middle
    x2 = point2.x * zoom + middle
    y1 = point1.y * zoom + middle
    y2 = point2.y * zoom + middle
    w.create_line(x1, y1, x2, y2)

def clear_line(point1, point2):
    x1 = point1.x * zoom + middle
    x2 = point2.x * zoom + middle
    y1 = point1.y * zoom + middle
    y2 = point2.y * zoom + middle
    w.create_line(x1, y1, x2, y2, fill="white")

def update_limit():
    if not clusters:
        return
    res = 0
    for c in clusters:
        res += c.size
    res /= len(clusters)
    cluster.show_limit = res/4
    for c in clusters:
        c.update()

l_left = 0
l_right = 0
r_x = 0
r_y = 0

zoom = 1 / 5
middle = 500

clusters = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.4.1", 23))
print("connected")

master = tkinter.Tk()
w = tkinter.Canvas(master,
           width=1000,
           height=1000, bg="white")
w.pack(expand=tkinter.YES, fill=tkinter.BOTH)

t = threading.Thread(target=myreceive)
t.daemon = True
t.start()
master.mainloop()