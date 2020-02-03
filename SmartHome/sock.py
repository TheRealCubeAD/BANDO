import threading
import socket
import sound

class SOCK:

    def __init__(self,main):
        self.main = main
        self.pc = PC(main)
        self.start_sck()
        self.addrs = {"192.168.0.173":self.pc}
        self.thread = None



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

    def __init__(self,main):
        self.main = main
        self.addr = None
        self.con = None
        self.active = False
        self.recver = threading.Thread(target=self.recv)
        self.recver.daemon = True
        self.recver.start()
        self.SOUND = sound.SOUND()

    def establish_conn(self,con,addr):
        self.addr = addr
        self.con = con
        self.active = True
        print("PC connected")
        self.SOUND.TTS("connected")

    def recv(self):
        while 1:
            if self.active:
                try:
                    data = self.con.recv(1024)
                    data = str(data,"utf-8")
                    self.handle_data(data)
                except ConnectionResetError:
                    print("PC disconnected")
                    self.SOUND.TTS("disconnected")
                    self.active = False

    def handle_data(self,data):
        try:
            print(data)
            app, cont = data.split(":::")
            if app == "SPOTIFY":
                self.main.d_print(cont,5)
        except:
            print("RECV ERROR")


