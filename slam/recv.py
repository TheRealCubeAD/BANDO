import socket
from breezyslam.algorithms import RMHC_SLAM, Deterministic_SLAM
from breezyslam.sensors import Laser
import tkinter
import threading
from roboviz import MapVisualizer
import math

class OwnLaser(Laser):
    def __init__(self):
        " scan_size, scan_rate_hz, detection_angle_degrees, distance_no_detection_mm, detection_margin=0, offset_mm=0"
        Laser.__init__(self, 37, 0.5, 180, 8000)

HOST = "localhost"
PORT = 9998
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
try:
    s.bind((HOST, PORT))
except socket.error as err:
    print('Bind failed. Error Code : ' .format(err))

MAP_SIZE_PIXELS         = 500
MAP_SIZE_METERS         = 10

slam = Deterministic_SLAM(OwnLaser(), MAP_SIZE_PIXELS, MAP_SIZE_METERS)
viz = MapVisualizer(MAP_SIZE_PIXELS, MAP_SIZE_METERS, 'SLAM')

map = bytearray(MAP_SIZE_PIXELS * MAP_SIZE_PIXELS)
old_map = map

old_left = 0
old_right = 0

old_x = 0
old_y = 0
r_x = 0
r_y = 0
delta_angle = 0
delta_time = 0

def update(data):
    global old_left, old_right, map, old_map, old_x, old_y, delta_angle, delta_time, r_x, r_y
    try:
        values = [int(x) for x in data.rstrip().rstrip(",").split(",")]
        if values.pop(0) == -2:
            left, right, new_delta_time = values

            right = -right

            old_angle = -(old_left - old_right) * 3.751 / 2
            new_angle = -(left - right) * 3.751 / 2
            delta_angle += new_angle - old_angle
            old_angle = new_angle

            forward = (((left - old_left) + (right - old_right)) / 2) * 3.25
            r_y += math.cos(new_angle * math.pi/180) * forward
            r_x += math.sin(new_angle * math.pi/180) * forward

            old_left = left
            old_right = right

            delta_time += new_delta_time

        else:
            if len(values) != 37:
                print("wrong size")
                return

            for i in range(len(values)):
                if values[i] > 8000:
                    values[i] = -1

            delta_xy = ((r_x - old_x) + (r_y - old_y))/2

            slam.update(values, pose_change=(delta_xy, delta_angle, delta_time), should_update_map=True)

            delta_angle = 0
            delta_time = 0
            old_x = r_x
            old_y = r_y
            x, y, theta = slam.getpos()
            print("--", x, y, theta)
            slam.getmap(map)
            changes = []
            for i, pixel in enumerate(map):
                if pixel != old_map[i]:
                    y = i/MAP_SIZE_PIXELS
                    x = i%MAP_SIZE_PIXELS
                    changes.append((y,x,pixel))

            #update_map(changes, x/20, y/20)
            viz.display(x / 1000., y / 1000., theta, map)

    except ValueError:
        pass


def update_map(changes, rx, ry):
    print(changes)
    can.create_oval(rx - 1, ry - 1, rx + 1, ry + 1)
    for change in changes:
        y, x, color = change
        can.create_oval(x - 1, y - 1, x + 1, y + 1, fill=(color,color,color), outline=(color,color,color))

def acceptor():
    s.listen(10)
    while True:
        print("Socket Listening")
        try:
            conn, addr = s.accept()
            print("CONNECTED\n")
            while True:
                data = conn.recv(1024)
                enc = data.decode(encoding='UTF-8')
                print(enc)
                update(enc)
        except ConnectionError:
            print("CONNECTION LOST\n")


#tk = tkinter.Tk()
#can = tkinter.Canvas(tk,  width=MAP_SIZE_PIXELS,
#           height=MAP_SIZE_PIXELS, bg="white")
#can.pack(expand=tkinter.YES, fill=tkinter.BOTH)

#t = threading.Thread(target=acceptor)
#t.daemon = True
#t.start()
#tk.mainloop()
acceptor()
