import threading
import socket
from IOevent import INPUT_EVENT


class SOCK:

    def __init__(self, callback):
        self.callback = callback
        self.sck = None
        self.thread = None

    def activate(self):
        self.pc = PC(callback)
        self.addrs = {"192.168.0.173": self.pc}
        self.start_sck()
        print("Socket started")


    def deactivate(self):
        if self.sck != None:
            self.sck.detach()
            self.sck.close()
        del self.thread
        del self.pc



    def start_sck(self):
        self.sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
        self.host = "0.0.0.0"  # Get local machine name
        self.port = 10010  # Reserve a port for your service.
        self.sck.bind((self.host, self.port))
        self.sck.listen(1)
        self.thread = threading.Thread(target=self.accept_conns)
        self.thread.daemon = True
        self.thread.start()


    def accept_conns(self):
        while 1:
            try:
                con, addr = self.sck.accept()
                obj = self.addrs[addr[0]]
                obj.establish_conn(con,addr)
            except KeyError:
                print("Unknown IP")
            except:
                print("Error accepting connection")


class PC:

    def __init__(self, callback):
        self.callback = callback
        self.addr = None
        self.con = None
        self.active = False
        self.recver = threading.Thread(target=self.recv)
        self.recver.daemon = True
        self.recver.start()

    def establish_conn(self,con,addr):
        self.addr = addr
        self.con = con
        self.active = True
        event = INPUT_EVENT()
        event.set_device("PC")
        event.set_message("connected")
        self.callback(event)


    def recv(self):
        while 1:
            if self.active:
                try:
                    data = self.con.recv(1024)
                    data = str(data,"utf-8")
                    self.handle_data(data)
                except ConnectionResetError:
                    event.set_device("PC")
                    event.set_message("disconnected")
                    self.callback(event)
                    self.active = False

    def handle_data(self,data):
        try:
            print(data)
            app, cont = data.split(":::")
            if app == "SPOTIFY":
                event.set_device("Spotify")
                event.set_message(cont)
                self.callback(event)
        except:
            print("RECV ERROR")


