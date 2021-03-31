import socket
import tkinter
import threading
import math


def myreceive():
    s.listen(10)
    while True:
        print("Socket Listening")
        try:
            conn, addr = s.accept()
            print("CONNECTED\n")
            while True:
                data = conn.recv(1024)
                enc = data.decode(encoding='UTF-8')

                try:
                    l, r, a, d, t = [int(x) for x in enc.split(",")]
                    point(l, r, a, d)
                except:
                    pass
        except ConnectionError:
            print("CONNECTION LOST\n")


l_left = 0
l_right = 0
r_x = 0
r_y = 0

def point(l, r, a, d):
    global l_left, l_right, r_x, r_y
    a /= 10
    a -= 90

    r = -r
    r_angle = -(l - r) * 3.751/2
    a += r_angle
    f = ((l - l_left) + (r - l_right))/2
    dy = math.cos(r_angle * math.pi/180) * f * 3.25
    dx = math.sin(r_angle * math.pi/180) * f * 3.25
    l_left = l
    l_right = r
    r_x += dx
    r_y += dy

    ly = math.sin((a)*math.pi/180) * d
    lx = math.cos((a) * math.pi / 180) * d
    print(l, r, r_angle, "   ", a, d)
    draw(r_x, r_y, ly, lx, d)


def draw(x, y, lx, ly, d):
    fac = 1/20
    x *= fac
    y *= fac
    lx *= fac
    ly *= fac
    x += 250
    y += 250
    print(x, y, lx, ly)
    w.create_oval(x - 1, y - 1, x + 1, y + 1, fill="red")
    if d < 8000:
        w.create_oval(x + lx - 1, y + ly - 1, x + lx + 1, y + ly + 1, fill="green")


HOST = "localhost"
PORT = 9998
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
try:
    s.bind((HOST, PORT))
except socket.error as err:
    print('Bind failed. Error Code : ' .format(err))

master = tkinter.Tk()
w = tkinter.Canvas(master,
           width=500,
           height=500)
w.pack(expand=tkinter.YES, fill=tkinter.BOTH)
w.create_oval(249, 249, 251, 251, fill="red")
t = threading.Thread(target=myreceive)
t.daemon = True
t.start()
master.mainloop()



