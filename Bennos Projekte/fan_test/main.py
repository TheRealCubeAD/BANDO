from machine import Pin, PWM
import time
import network

pin = PWM(Pin(5))
pin.freq(25000)

for i in range(10):
    pin.duty(i*100)
    print(i*100)
    time.sleep(5)
pin.duty(0)