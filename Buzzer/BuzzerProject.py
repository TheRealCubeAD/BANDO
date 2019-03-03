from pyudmx import pyudmx
from playsound import playsound
import time
import threading

dev = None

def init():
    global dev
    print("Initalizing")
    print()
    try:
        dev = pyudmx.uDMXDevice()
        print("Connected")
        print()
    except:
        print("Error during connect")
        print("shutting down")
        raise ConnectionError


def sendDMX(device,color,value):
    global dev
    print()
    print("Sending:")
    print()
    print("got:",device,color,value)
    ch = 0
    colors = {"R":0,"G":1,"B":2,"W":3}
    if device == "left":
        ch = 1
    elif device == "right":
        ch = 5
    else:
        print("Error: unknown device")
        print()
        return
    print("Device is:",ch)
    print("Color is:",colors[color])
    try:
        ch += colors[color]
    except KeyError:
        print("Error: unknown color")
        print()
        return
    print("-> Channel is:",ch)

    if not(1<=ch<=8 and 0<=value<=255):
        print("Error: Values are not accepted")
        return
    print()
    print("Values seem normal")
    print()
    print("Sending...")
    print()

    try:
        dev.open()
        print("Connection opend")
        dev.send_single_value(ch,value)
        print("Value:",value,"sent at:",ch)
    except:
        print("USBError occured during sending. Continuign anyways...")
    finally:
        dev.close()
        print("Connection closed")

    print()
    print("Sending completet")
    print()


def LightBuzz(side,lock):
    buzzColor = "R"
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
    print("Buzz completet")
    print()


def SoundBuzz(side,lock):
    print()
    print("Playing sound on",side,"side")
    if side == "left":
        playsound("C:/Users/benni/PycharmProjects/BANDO/Buzzer/BuzzLeft.wav")
    elif side == "right":
        playsound("C:/Users/benni/PycharmProjects/BANDO/Buzzer/BuzzRight.wav")


def interpreter(code):
    print()
    sides = {0:"left",1:"right"}
    try:
        side = sides[code]
        print("Interpreted Code",code,"as side",side)
    except KeyError:
        print("Error: Unknown code")

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
    interpreter(int(input(">>>")))