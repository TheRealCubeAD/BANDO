import serial, time, threading

class Z14:

    def __init__(self, callback, disp):
        self.callback = callback
        self.disp = disp
        self.thread = threading.Thread(target=self.main)
        self.thread.daemon = True
        self.thread.start()

    def read(self):
        con = serial.Serial(port="/dev/serial0",baudrate=9600)
        con.write(serial.to_bytes([0xFF, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79]))
        result = con.read(size=9)
        con.close()
        return result[2] * 256 + result[3]

    def main(self):
        warned = 0
        time.sleep(5)
        while 1:
            reading = self.read()
            print(reading)
            if reading >= 1100:
                if warned == 0:
                    warned = 1
                    self.callback()
            elif reading < 700:
                warned = 0

            if warned == 1:
                warned = 8
                self.disp("CO2-Levels to high!##" + str(reading), 5)
            elif warned > 1:
                warned -= 1
            time.sleep(5)

if __name__ == "__main__":
    z = Z14(None)
    while 1:
        print(z.read())
        time.sleep(5)