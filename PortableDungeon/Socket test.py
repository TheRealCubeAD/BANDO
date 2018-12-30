import socket
import threading
import sys
import time


class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.sock.bind(("0.0.0.0",10000))
        self.sock.listen(1)
        runThread = threading.Thread(target=self.run)
        runThread.daemon = True
        runThread.start()


    def recv(self, conn):
        c,a = conn
        try:
            while True:
                data = c.recv(1024)
                data = str(data,"utf-8")
                return data
        except ConnectionResetError:
            print("--Player disconeccted--")
            del (self.connections[self.connections.index(c)])
            return None

    def run(self):
        while True:
            c,a = self.sock.accept()
            self.connections.append([c,a])
            print("--Player connected--")

    def sendRecive(self,ID,data):
        data += "§*INPUT*"
        if self.send(ID,data):
            answer = self.recv(self.connections[ID])
            out(answer)

    def send(self,ID,data):
        try:
            self.connections[ID][0].send(bytes(data,"utf-8"))
            return True
        except ConnectionResetError:
            print("--Player disconeccted--")
            del (self.connections[ID])
            return False






class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    printCue = []

    def __init__(self):
        print("IP-Adresse")
        address = input(">>> ")
        self.sock.connect((address,10000))
        recThread = threading.Thread(target=self.recv)
        recThread.daemon = True
        recThread.start()
        while True:
            if len(self.printCue) > 0:
                line = self.printCue[0]
                del(self.printCue[0])
                if line == "*INPUT*":
                    self.inp()
                    print()
                else:
                    out(line)

    def inp(self):
        self.send(input(">>> "))

    def send(self,data):
        self.sock.send(bytes(data,"utf-8"))

    def recv(self):
        while True:
            data = self.sock.recv(1024)
            if data:
                data = str(data, "utf-8")
                data = data.split("§")
                self.printCue += data





def out(printLine):
    for i in printLine:
        sys.stdout.write(i)
        time.sleep(0.05)
    print()

#TESTING
if input("Host?") == "y":
    S = Server()
    while 1:
        if input() == "r":
            S.sendRecive(0,input(">>> "))
        else:
            S.send(0,input(">>> "))
else:
    C = Client()