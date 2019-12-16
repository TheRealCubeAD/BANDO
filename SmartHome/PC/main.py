import socket
import threading
import time
from SwSpotify import spotify

class CONNECT:

    def __init__(self):
        self.server_ip = "192.168.0.45"
        self.port = 10010
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.connected = False

        self.thread = threading.Thread(target=self.main)
        self.thread.daemon = True
        self.thread.start()


    def main(self):
        while 1:
            while not self.connected:
                print("Connecting...")
                self.connect()
                time.sleep(5)
            time.sleep(5)


    def connect(self):
        try:
            self.sock.connect((self.server_ip,self.port))
            self.connected = True
        except:
            print("Error connecting")


    def send(self,data):
        if not self.connected:
            return
        data = bytes(data,"utf-8")
        try:
            self.sock.send(data)
        except:
            print("Disconnected")
            self.connected = False


class SPOTIFY:

    def __init__(self,control):
        self.control = control
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

    def run(self):
        last = None
        time.sleep(3)
        while 1:
            try:
                inf = spotify.song() + "##" + spotify.artist()
                if inf != last and inf:
                    text = "SPOTIFY:::" + inf
                    c.send(text)
                    last = inf
            except:
                pass
            time.sleep(1)




if __name__ == "__main__":
    c = CONNECT()
    s = SPOTIFY(c)
    input()

