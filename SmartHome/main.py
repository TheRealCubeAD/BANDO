#import led
from Output import disp, fan, sound
import pcState
import sock


class SYSTEM:
    #SENSORS


    #ACTUATORS
    #LED = None
    DISP = None

    def __init__(self):
        # SENSORS
        self.PC_STATE = pcState.PCSTATE(self.pc_state_response)
        self.PC_sock = sock.SOCK(self)

        # ACTUATORS

        #self.LED = led.LED()
        self.DISP = disp.DISPLAY()
        self.FAN = fan.FAN()
        self.SOUND = sound.SOUND()
        print("init")


    def activate(self):
        self.FAN.turn_on()
        self.DISP.activate()
        self.DISP.add_frame("beg")
        self.SOUND.sound("08")


    def deactivate(self):
        self.FAN.turn_off()
        self.DISP.deactivate()
        self.SOUND.sound("16")

    def pc_state_response(self,value):
        if value:
            self.activate()
        else:
            self.deactivate()

    def input_response(self,value):
        if value == "###":
            self.DISP.print_starter()
            self.PC_STATE.turn_on()
        elif value == "end":
            self.deactivate()
            exit("Closed by user")
        else:
            print("unknown command")

    def d_print(self,content,t):
        self.DISP.add_frame("pout", arg=(content, t))


if __name__ == '__main__':
    sys = SYSTEM()
    while 1:
        print()
        sys.input_response(input(">>>"))



