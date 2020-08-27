import serial, time, threading
from IOevent import INPUT_EVENT

class Z14:

    def __init__(self, callback):
        self.callback = callback
        self.thread = None
        self.running = False

    def activate(self):
        self.running = True
        self.thread = threading.Thread(target=self.main)
        self.thread.daemon = True
        self.thread.start()

    def deactivate(self):
        self.running = False

    def read(self):
        con = serial.Serial(port="/dev/serial0",baudrate=9600)
        con.write(serial.to_bytes([0xFF, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79]))
        result = con.read(size=9)
        con.close()
        return result[2] * 256 + result[3]

    def main(self):
        warned = 0
        time.sleep(5)
        while self.running:
            reading = self.read()
            print(reading)
            if reading >= 1100:
                if warned == 0:
                    warned = 1
                    event = INPUT_EVENT()
                    event.set_device("CO2")
                    event.set_message("f:::" + reading)
                    self.callback(event)
            elif reading < 700:
                warned = 0

            if warned == 1:
                event = INPUT_EVENT()
                event.set_device("CO2")
                event.set_message("s:::" + reading)
                self.callback(event)
            time.sleep(20)

if __name__ == "__main__":
    z = Z14(None)
    while 1:
        print(z.read())
        time.sleep(5)