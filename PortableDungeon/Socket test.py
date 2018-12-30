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


    def handler(self,c,a):
        while True:
            data = c.recv(1024)
            data = str(data,"utf-8")
            out([data])

    def run(self):
        while True:
            c,a = self.sock.accept()
            cThread = threading.Thread(target=self.handler,args=(c,a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(self.connections)

    def send(self,ID,data):
        self.connections[ID].send(bytes(data,"utf-8"))

    def getInput(self,ID):
        self.connections[ID].send(bytes("*INPUT*","utf-8"))


class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        print("IP-Adresse")
        address = input(">>> ")
        self.sock.connect((address,10000))
        recThread = threading.Thread(target=self.recv)
        recThread.daemon = True
        recThread.start()
        while True:
            pass

    def inp(self):
        self.send(input(">>> "))

    def send(self,data):
        self.sock.send(bytes(data,"utf-8"))

    def recv(self):
        while True:
            data = self.sock.recv(1024)
            if data:
                data = str(data, "utf-8")
                if data == "*INPUT*":
                    self.inp()
                else:
                    out(data.split("#"))




def out(prints):
    for printLine in prints:
        print(printLine)
        #for i in printLine:
            #sys.stdout.write(i)
            #time.sleep(0.05)


if input("Host?") == "y":
    S = Server()
    while 1:
        S.send(0,input(">>> "))
else:
    C = Client()