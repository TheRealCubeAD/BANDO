import machine
import esp
import network
import socket
import time


NetworkName = "OnePlus2"
NetworkPass = "dasPasswort"
serveripadr = "192.168.43.100"

sta_if = None
sock = None

button = machine.Pin(0,machine.Pin.IN,machine.Pin.PULL_UP)
led = machine.Pin(2,machine.Pin.OUT)


def init():
    global sta_if
    global sock

    sta_if = network.WLAN(network.STA_IF)
    time.sleep(2)
    sta_if.connect(NetworkName,NetworkPass)
    time.sleep(2)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time.sleep(2)
    sock.connect(("192.168.43.100", 10000))


def pressed():
    led.value(not led.value())
    sock.send(bytes("TERROR! HILFE","utf-8"))

init()
while 1:
    if not button.value():
        print("pressed")
        pressed()
        while not button.value():
            pass
        print("release")

