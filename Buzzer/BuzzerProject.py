from pyudmx import pyudmx
from playsound import playsound
import time
import threading
import socket
from termcolor import cprint

dev = None
sock = None
connections = []
buzzColor = "R"


def recv(c, side):
    try:
        while True:
            data = c.recv(1024)
            print(data)
            data = str(data,"utf-8")
            cprint(("Data recived from",side,":",data),"blue")
            if data == "TERROR! HILFE":
                interpreter(side)
    except ConnectionResetError:
        cprint("--Buzzer disconeccted--","red")
        del (connections[connections.index(c)])


def run():
    while True:
        c,a = sock.accept()
        connections.append([c,a])
        cprint("--Buzzer connected--","green")
        if len(connections) == 1:
            print("Buzzer is left")
            left = threading.Thread(target=recv,name="left",args=(c,"left"))
            left.daemon = True
            left.start()
            print()
            cprint("Buzzer R can now be connected","green")
        elif len(connections) == 2:
            print("Buzzer is right")
            right = threading.Thread(target=recv, name="right", args=(c,"right"))
            right.daemon = True
            right.start()


def init():
    global dev
    global sock
    cprint("...INITALIZING...","blue")
    print("Starting Server")
    print()
    print("Creating Socket...")
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Binding Socket...")
    sock.bind(("0.0.0.0", 10000))
    sock.listen(1)
    time.sleep(2)
    cprint("Server started","green")
    print("Starting Thread: Connections")
    runThread = threading.Thread(target=run)
    runThread.daemon = True
    runThread.start()
    time.sleep(1)
    cprint("Thread started","green")
    print()
    print("Connecting DMX-Controller")
    time.sleep(1)
    try:
        dev = pyudmx.uDMXDevice()
        cprint("Connected","green")
        print()
    except:
        cprint("Error during connect","red")
        cprint("shutting down","red")
        raise ConnectionError
    cprint("FINISHED","blue")
    print()
    cprint("Sever is running. Buzzer L can now be connected","green")
    print()


def sendDMX(device,color,value):
    global dev
    print()
    cprint("Sending to DMX:","blue")
    print()
    print("got:",device,color,value)
    ch = 0
    colors = {"R":0,"G":1,"B":2,"W":3}
    if device == "left":
        ch = 1
    elif device == "right":
        ch = 5
    else:
        cprint("Error: unknown device","red")
        print()
        return
    print("Device is:",ch)
    print("Color is:",colors[color])
    try:
        ch += colors[color]
    except KeyError:
        cprint("Error: unknown color","red")
        print()
        return
    print("-> Channel is:",ch)

    if not(1<=ch<=8 and 0<=value<=255):
        cprint("Error: Values are not accepted","red")
        return
    print()
    print("Values are normal")
    print()
    cprint("Sending...","blue")
    print()

    try:
        dev.open()
        print("Connection opend")
    except:
        cprint("DMX could not be opend! Abording...","red")
    try:
        dev.send_single_value(ch,value)
        cprint(("Value:",value,"sent at:",ch),"blue")
    except:
        cprint("USBError occured during sending. Continuing anyways...","red")
    finally:
        dev.close()
        print("Connection closed")

    print()
    cprint("Sending completet","green")
    print()


def LightBuzz(side,lock):
    buzzIntensity = 255
    buzzLenght = 1
    print()
    print("Buzzing on",side,"side")
    print()
    print("Sending Full")
    print()
    sendDMX(side,buzzColor,buzzIntensity)
    print("Waiting",buzzLenght,"seconds")
    print()
    time.sleep(buzzLenght)
    print("Sending Off")
    sendDMX(side,buzzColor,0)
    print()
    cprint("Buzz completet","green")
    print()


def SoundBuzz(side,lock):
    print()
    cprint(("Playing sound on",side,"side"),"blue")
    if side == "left":
        playsound("C:/Users/benni/PycharmProjects/BANDO/Buzzer/BuzzLeft.wav")
    elif side == "right":
        playsound("C:/Users/benni/PycharmProjects/BANDO/Buzzer/BuzzRight.wav")


def interpreter(side):
    if side == "n":
        side = "left"
    elif side == "m":
        side = "right"
    elif side == "nm":
        interpreter("left")
        side = "right"
    elif side in ("R","G","B","W"):
        global buzzColor
        buzzColor = side
        cprint("Color set to "+side,"blue")
        return
    elif side not in ("left","right"):
        cprint("Unknown device","red")
        return
    print("Starting Threads")
    lock = threading.Lock()
    Thread_Light = threading.Thread(target=LightBuzz,name="1",args=(side,lock))
    Thread_Light.daemon = True
    Thread_Light.start()

    Thread_Sound = threading.Thread(target=SoundBuzz,name="2",args=(side,lock))
    Thread_Sound.daemon = True
    Thread_Sound.start()
    print("Threads started")

init()
while 1:
    interpreter(input(">>>"))