from IOevent import INPUT_EVENT
import time
import os
import threading

class READ:
    def __init__(self, callback):
        self.callback = callback
        self.process = threading.Thread(target=self.run)
        self.process.daemon = True
        self.process.start()

    def run(self):
        while 1:
            while not os.path.exists("buffer.ln"):
                time.sleep(0.5)
            time.sleep(0.5)
            line = None
            with open("buffer.ln", 'r') as file:
                line = file.readline()
            os.remove("buffer.ln")
            event = INPUT_EVENT()
            event.set_device("CML")
            event.set_message(line)
            event.set_prio_high()
            self.callback(event)