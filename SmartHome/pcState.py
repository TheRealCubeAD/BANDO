import RPi.GPIO as GPIO
import time
import threading
import wa

class PCSTATE:

    def __init__(self, callback_function):
        self.pin_state = 24
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_state,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.callback = callback_function

        self.state = False
        self.messure = [0 for _ in range(30)]

        thread = threading.Thread(target=self.run)
        thread.daemon = True
        thread.start()

    def read(self):
        self.messure.append(GPIO.input(self.pin_state))
        del(self.messure[0])

    def run(self):
        while True:
            self.read()
            if not self.state:
                if all(self.messure):
                    self.state = True
                    self.callback(True)
            else:
                if not all(self.messure):
                    self.state = False
                    self.callback(False)
            time.sleep(0.1)

    def turn_on(self):



if __name__ == '__main__':
    pass