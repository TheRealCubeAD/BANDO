import os
#import led
import disp
import fan
import pcState
import sock
import sound
import z14

class SYSTEM:
    #SENSORS


    #ACTUATORS
    #LED = None
    DISP = None

    def __init__(self):
        # SENSORS
        self.PC_STATE = pcState.PCSTATE(self.pc_state_response)
        self.PC_sock = sock.SOCK(self)
        self.z14 = z14.Z14(self.carbon1, self.d_print)

        # ACTUATORS

        #self.LED = led.LED()
        self.DISP = disp.DISPLAY()
        self.FAN = fan.FAN()
        self.SOUND = sound.SOUND()
        print("init")


    def activate(self):
        self.FAN.turn_on()
        self.DISP.activate()
        self.DISP.add("beg")
        self.SOUND.sound("08")


    def deactivate(self):
        self.FAN.turn_off()
        self.DISP.deactivate()
        self.SOUND.sound("16")


    def carbon1(self):
        self.SOUND.speak("Air-Quality critical!")


    def pc_state_response(self,value):
        if value:
            self.activate()
        else:
            self.deactivate()

    def input_response(self,value):
        if value == "###":
            self.DISP.print_starter()
            self.PC_STATE.turn_on()
            self.activate()
        elif value == "end":
            self.deactivate()
            exit("Closed by user")
        elif value == "fo":
            self.FAN.turn_on()
        elif value == "fu":
            self.FAN.turn_off()
        else:
            print("unknown command")

    def d_print(self,content,t):
        self.DISP.add("pout",arg=(content,t))


if __name__ == '__main__':
    sys = SYSTEM()
    while 1:
        print()
        sys.input_response(input(">>>"))



