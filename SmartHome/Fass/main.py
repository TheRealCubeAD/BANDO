from machine import Pin, PWM
from time import sleep
from HRC import HCSR04


active = 1
pressed = False

pBut = Pin(15,Pin.IN,Pin.PULL_UP)
pError = Pin(13,Pin.OUT)

pR = PWM(Pin(5))
pG = PWM(Pin(4))
pB = PWM(Pin(0))

sonic = HCSR04(trigger_pin=14,echo_pin=12)

pR.freq(50)
pG.freq(50)
pB.freq(50)

maxD = 1023
sleepTime = 0.07

pR.duty(maxD)
pG.duty(0)
pB.duty(0)

iteration = [0,0]
pinOrder = (pR,pG,pB,pR,pG)

messures = [0 for _ in range(40)]
last = 0

def iter(Dis):
    global iteration
    pin1 = pinOrder[iteration[0] + 0]
    pin2 = pinOrder[iteration[0] + 1]
    pin3 = pinOrder[iteration[0] + 2]

    c1 = Dis
    c2 = Dis
    c3 = Dis

    if active:
        c2 += iteration[1]
        c1 += maxD - iteration[1]
        c1 = min(c1, maxD)
        c2 = min(c2, maxD)

    setFD(pin1, c1)
    setFD(pin2, c2)
    setFD(pin3, c3)

    iteration[1] += 2
    if iteration[1] > maxD:
        iteration[1] = 0

        iteration[0] += 1
        if iteration[0] > 2:
            iteration[0] = 0


def setFD(pin,d):
    pin.duty(d)
    dis = abs(d - maxD / 2) / 10
    dis = 51 - dis
    dis = int(dis) + 75
    pin.freq(dis)

def recv():
    pass

def push(item):
    for i in range(len(messures)-1):
        messures[i] = messures[i+1]
    messures[-1] = item

def messure():
    try:
        dis = sonic.distance_cm()
    except:
        dis = 400
    return dis

def smoothing(item,mode):
    global messures
    global last
    if item < 0:
        pError.on()
    else:
        pError.off()
    if mode == 1:
        if item > 0:
            push(item)
        avg = sum(messures) / len(messures)
        avg -= 50
        avg = max(0,avg)
        avg = min(200,avg)
        avg /= 200
        avg = 1 - avg
        return avg
    if mode == 2:
        if item > 0:
            vel = (item-last)
            push(vel)
        avgVel = sum(messures) / len(messures)
        calPos = last + avgVel
        calPos -= 50
        calPos = max(0,calPos)
        calPos = min(200,calPos)
        calPos /= 200
        calPos = 1 - calPos
        last = calPos
        return calPos


def button():
    global pressed
    global active
    bp = pBut.value()
    if not pressed:
        if bp:
            pressed = True
            active = not active
            print(active)
    else:
        if not bp:
            pressed = False

#clock
while True:
    recv()
    valueDis = int(smoothing(messure(),1) * maxD)
    iter(valueDis)
    button()
    sleep(sleepTime)

