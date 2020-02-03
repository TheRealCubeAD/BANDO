from machine import Pin, PWM
from time import sleep
from HRC import HCSR04


active = 1
pressed = False
last_active = 0
anim = 0
last_mes = 0
last_mes_count = 0

tresh = 30

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

messures = [0 for _ in range(10)]
last = 0

def iter(Dis):
    global iteration
    pin1 = pinOrder[iteration[0] + 0]
    pin2 = pinOrder[iteration[0] + 1]
    pin3 = pinOrder[iteration[0] + 2]

    c1 = Dis
    c2 = Dis
    c3 = Dis
    if iteration[0] == 0:
        c2 *= 0.8
        c3 *= 0.8
    elif iteration[0] == 1:
        c1 *= 0.8
        c2 *= 0.8
    elif iteration[0] == 2:
        c1 *= 0.8
        c3 *= 0.8
    c1 = int(c1)
    c2 = int(c2)
    c3 = int(c3)

    if active == 2:
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
    print(dis)
    return dis

def check(new):
    global messures
    global last_active
    global anim

    if new > 0:
        pError.off()
        push(new)
    else:
        pError.on()

    res = True
    for i in messures:
        if i > tresh:
            res = False
            break
    if res:
        last_active = 143
        anim = min(anim+20,maxD)

    else:
        last_active = max(last_active-1,0)
        if last_active == 0:
            anim = max(anim-15,0)

def button():
    global pressed
    global active
    bp = pBut.value()
    if not pressed:
        if bp:
            pressed = True
            active += 1
            if active == 3:
                active = 0
    else:
        if not bp:
            pressed = False

#clock
while True:
    button()
    if active:
        recv()
        if last_mes_count == 0:
            last_mes = messure()
            last_mes_count = 5
        else:
            last_mes_count -= 1
        check(last_mes)
        iter(anim)
    else:
        iter(0)
    sleep(sleepTime)

