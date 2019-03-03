from pyudmx import pyudmx
import time

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


def sendV(device,color,value):
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


def buzz(side):
    buzzColor = "R"
    buzzIntensity = 255
    buzzLenght = 1
    print()
    print("Buzzing on",side,"side")
    print()
    print("Sending Full")
    print()
    sendV(side,buzzColor,buzzIntensity)
    print("Waiting",buzzLenght,"seconds")
    print()
    time.sleep(buzzLenght)
    print("Sending Off")
    sendV(side,buzzColor,0)
    print()
    print("Buzz completet")
    print()


init()
while 1:
    buzz(input("Side:"))