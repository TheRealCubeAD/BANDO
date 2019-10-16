import os
#import led
import disp
import fan
import pcState

#LED = led.LED()
#LED.all((0,255,0))
#LED.flow((255,0,0),(0,255,0),0,90,9,0.5)


class SYSTEM:
    #SENSORS


    #ACTUATORS
    #LED = None
    DISP = None

    def __init__(self):
        # SENSORS
        self.PC_STATE = pcState.PCSTATE(self.pc_state_response)

        # ACTUATORS

        #self.LED = led.LED()
        self.DISP = disp.DISPLAY()
        self.FAN = fan.FAN()


    def activate(self):
        self.FAN.turn_on()
        self.DISP.activate()
        self.DISP.add("beg")

    def deactivate(self):
        self.FAN.turn_off()
        self.DISP.deactivate()

    def pc_state_response(self,value):
        if value:
            self.activate()
        else:
            self.deactivate()


if __name__ == '__main__':
    sys = SYSTEM()
    input()



