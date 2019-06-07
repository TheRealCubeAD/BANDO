import os
import led

LED = led.LED()
LED.all((0,255,0))
LED.flow((255,0,0),(0,255,0),0,90,9,0.5)
