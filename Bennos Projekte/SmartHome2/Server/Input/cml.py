import os
import threading

class CML:

    def __init__(self):
        process = threading.Thread(target=self.run)
        process.daemon = True
        process.start()

    def run(self):
        while 1:
            while os.path.exists("buffer.ln"):
                pass
            inp = input(">>>")
            with open("buffer.ln", "w") as file:
                file.write(inp)

if __name__ == '__main__':
    cml = CML()
    while 1:
        pass