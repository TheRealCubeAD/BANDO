from inputs import get_gamepad
import socket
import time
import threading
import sys

def send():
    l = y
    r = y
    l += x
    r -= x
    if l > 100:
        r -= l - 100
        l = 100
    if r > 100:
        l -= l - 100
        r = 100
    if l < -100:
        r -= l + 100
        l = -100
    if r < -100:
        l -= r + 100
        r = -100
    print(l, r)
    s.send(l.to_bytes(1, sys.byteorder, True))
    s.send(r.to_bytes(1, sys.byteorder, True))
    time.sleep(1)


m = 32767
x = 0
y = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.4.1", 23))
s.send(b'\xff')
print("connected")
t = threading.Thread(target=send)
t.daemon = True
t.start()
while 1:
    try:
        events = get_gamepad()
        for event in events:
            if "ABS_Y" in event.code:
                val = int(event.state)
                per = int(val*100/m)
                y = per
            elif "ABS_X" in event.code:
                val = int(event.state)
                per = int(val * 100 / m)
                x = per
    except:
        pass

