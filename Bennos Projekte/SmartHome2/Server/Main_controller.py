from InputController import INPCON
from OutputController import OUTCON
import threading

class CONTROLLER:
    def __init__(self):
        self.in_con = INPCON(self)
        self.out_con = OUTCON()
        self.active = False
        self.process = None


    def new_input_event(self, event):
        if not self.active and not event.is_prio_high():
            return
        else:
            self.process = threading.Thread(target=self.process_input, name="process", args=event)
            self.process.daemon = True
            self.process.start()


    def acitvate(self):
        self.active = True
        self.in_con.activate()
        self.out_con.activate()

    def deacitvate(self):
        self.active = False
        self.in_con.deactivate()
        self.out_con.deactivate()


    def process_input(self, event):
        if event.get_device() == "PC":
            if event.get_message() == "power_on":
                self.acitvate()
            if event.get_message() == "power_off":
                self.deacitvate()
            if event.get_message() == "connected":
                self.out_con.text("PC connected")
            if event.get_message() == "disconnected":
                self.out_con.text("PC disconnected")
        if event.get_device() == "Spotify":
            self.out_con.text(event.get_message())
        if event.get_message() == "CML":
            self.out_con.start_pc()
        self.in_con.signal_finished()

if __name__ == '__main__':
    root = CONTROLLER()