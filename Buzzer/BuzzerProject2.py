from pyudmx import pyudmx
import pyaudio
import wave
import time
import threading
import socket
from termcolor import cprint

dev = None
sock = None
connections = []
chunk = 1024
pathL = "BuzzLeft.wav"
pathR = "BuzzRight.wav"
bLeft = None
bRight = None
pyaud = None
streamL = None
streamR = None
sDataL = None
sDataR = None
buzzColor = "R"


def test():
    t = 0.2
    print("Testing left Buzzer...")
    for r in range(25):
        if not sendDMX("left","R",r*10):
            print("Left Buzzer is not working")
            return False
        time.sleep(t)
    print("Left Buzzer is working")
    time.sleep(1)
    for r in range(25):
        if not sendDMX("right","R",r*10):
            print("Right Buzzer is not working")
            return False
        time.sleep(t)
    print("Right Buzzer is working")
    time.sleep(2)
    sendDMX("left", "R", 0)
    sendDMX("right", "R", 0)
    sendDMX("left", "G", 255)
    sendDMX("right", "G", 255)
    time.sleep(3)
    sendDMX("left", "G", 0)
    sendDMX("right", "G", 0)
    time.sleep(1)
    print("Testing left Sound")
    if not SoundBuzz("left",None):
        print("Left sound is not working")
        return False
    print("Left sound is working")
    time.sleep(1)
    print("Testing right Sound")
    if not SoundBuzz("right",None):
        print("Right sound is not working")
        return False
    print("Right sound is working")
    time.sleep(1)
    print("All systems are running")
    return True

def recv(c, side):
    try:
        while True:
            data = c.recv(1024)
            print(data)
            data = str(data,"utf-8")
            cprint(("Data recived from",side,":",data),"blue")
            if "TERROR" in data:
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
    global pyaud
    global bLeft
    global bRight
    global streamL
    global streamR
    global sDataL
    global sDataR

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
    print()
    print("Loading Sound")
    bLeft = wave.open(pathL,"rb")
    bRight = wave.open(pathR,"rb")
    print("Initializing Audio-Module")
    pyaud = pyaudio.PyAudio()
    streamL = pyaud.open(format = pyaud.get_format_from_width(bLeft.getsampwidth()),
                channels = bLeft.getnchannels(),
                rate = bLeft.getframerate(),
                output = True)
    streamR = pyaud.open(format=pyaud.get_format_from_width(bRight.getsampwidth()),
                         channels=bRight.getnchannels(),
                         rate=bRight.getframerate(),
                         output=True)
    sDataL = bLeft.readframes(chunk)
    sDataR = bRight.readframes(chunk)
    if input("silent?") == "":
        if not test():
            print("Not all Systems are running...")
            exit()
    cprint("FINISHED","blue")
    print()
    cprint("Sever is running. Buzzer L can now be connected","green")
    print()


def sendDMX(device,color,value):
    global dev
    print()
    print()
    ch = 0
    colors = {"R":0,"G":1,"B":2,"W":3}
    if device == "left":
        ch = 1
    elif device == "right":
        ch = 5
    else:
        cprint("Error: unknown device","red")
        print()
        return False
    try:
        ch += colors[color]
    except KeyError:
        cprint("Error: unknown color","red")
        print()
        return False

    if not(1<=ch<=8 and 0<=value<=255):
        cprint("Error: Values are not accepted","red")
        return False
    print()
    print("Values are normal")
    print()
    cprint("Sending...","blue")
    print()

    try:
        dev.open()
    except:
        cprint("DMX could not be opend! Abording...","red")
        return False
    try:
        dev.send_single_value(ch,value)
        cprint(("Value:",value,"sent at:",ch),"blue")
    except:
        cprint("USBError occured during sending. Continuing anyways...","red")
    finally:
        dev.close()
    cprint("Sending completet","green")
    print()
    return True


def LightBuzz(side,lock):
    buzzIntensity = 255
    buzzLenght = 1
    print()
    print("Buzzing on",side,"side")
    print()
    sendDMX(side,buzzColor,buzzIntensity)
    time.sleep(buzzLenght)
    sendDMX(side,buzzColor,0)
    cprint("Buzz completet","green")
    print()


def SoundBuzz(side,lock):
    global sDataL
    global sDataR
    global streamL
    global streamR
    global bLeft
    global bRight
    if side == "left":
        try:
            while sDataL:
                streamL.write(sDataL)
                sDataL = bLeft.readframes(chunk)
        except:
            return False
        finally:
            bLeft = wave.open(pathL, "rb")
            streamL = pyaud.open(format=pyaud.get_format_from_width(bLeft.getsampwidth()),
                                 channels=bLeft.getnchannels(),
                                 rate=bLeft.getframerate(),
                                 output=True)
            sDataL = bLeft.readframes(chunk)
    elif side == "right":
        try:
            while sDataR:
                streamR.write(sDataR)
                sDataR = bRight.readframes(chunk)
        except:
            return False
        finally:
            bRight = wave.open(pathR, "rb")
            streamR = pyaud.open(format=pyaud.get_format_from_width(bRight.getsampwidth()),
                                 channels=bRight.getnchannels(),
                                 rate=bRight.getframerate(),
                                 output=True)
            sDataR = bRight.readframes(chunk)
    return True


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

init()
while 1:
    interpreter(input(">>>"))