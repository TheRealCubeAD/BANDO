from IOevent import INPUT_EVENT
import time
import os
import threading

class READ:
    def __init__(self, callback):
        self.callback = callback
        self.process = None
        self.running = False

    def activate(self):
        self.running = True
        self.process = threading.Thread(target=self.run)
        self.process.daemon = True
        self.process.start()
        print("CML started")

    def deactivate(self):
        self.running = False

    def run(self):
        while self.running:
            while not os.path.exists("buffer.ln"):
                time.sleep(0.5)
            time.sleep(0.5)
            line = None
            with open("buffer.ln", 'r') as file:
                line = file.readline()
            print("CML read:", line)
            os.remove("buffer.ln")
            event = INPUT_EVENT()
            event.set_device("CML")
            event.set_message(line)
            event.set_prio_high()
            self.callback(event)
        print("CML killed")
