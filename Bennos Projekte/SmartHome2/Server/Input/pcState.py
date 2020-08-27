import RPi.GPIO as GPIO
import time
import threading
import wakeonlan
from IOevent import INPUT_EVENT

class PCSTATE:

    def __init__(self, callback):
        self.pin_state = 24
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_state,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.callback = callback

        self.state = False
        self.messure = [0 for _ in range(90)]

        thread = threading.Thread(target=self.run)
        thread.daemon = True
        thread.start()
        print("pcState started")

    def activate(self):
        pass

    def deactivate(self):
        pass

    def read(self):
        self.messure.append(GPIO.input(self.pin_state))
        del(self.messure[0])

    def run(self):
        while True:
            self.read()
            if not self.state:
                if all(self.messure):
                    self.state = True
                    event = INPUT_EVENT()
                    event.set_device("PC")
                    event.get_message("power_on")
                    event.set_prio_high()
                    #self.callback(event)
            else:
                if not all(self.messure):
                    self.state = False
                    event = INPUT_EVENT()
                    event.set_device("PC")
                    event.get_message("power_off")
                    event.set_prio_high()
                    self.callback(event)
            time.sleep(0.1)


if __name__ == '__main__':
    pass