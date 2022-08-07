import os
import subprocess
import socket
import warnings
from win10toast import ToastNotifier
from PIL import Image
import tray
import time

class DETECTOR:
    byte_check = b'\x01'
    byte_on = b'\xF0'
    byte_off = b'\xA0'

    ssids = ["meisen", "meisen 5Ghz", "LAN Solo"]

    host_ip = "192.168.0.55"
    host_port = 1234

    def __init__(self, use_notifications=True, use_gui=True):
        self.state = 1
        self.do_close = False
        self.use_notifications = use_notifications
        self.in_meeting = False
        self.use_gui = use_gui
        self.window = None
        self.toast = ToastNotifier()
        if self.use_gui:
            self.icon = tray.Icon("led_grey.png", lambda : self.change(True), lambda : self.change(False), self.close)
            self.set_icon(0)

        self.sock = None



    def loop(self):
        con_alerted = False
        while not self.do_close:

            # STATE 1 (no wlan)
            if self.state == 1:
                print("checking")
                if self.check_home():
                    self.state = 2
                else:
                    time.sleep(30)

            # STATE 2 (wlan but no host)
            elif self.state == 2:
                if self.connect():
                    con_alerted = False
                    self.notify("Connected")
                    self.state = 3
                    self.change(False)
                else:
                    if self.check_home():
                        if not con_alerted:
                            self.notify("Connection Error\nDetector offline?")
                            con_alerted = True
                        time.sleep(10)
                    else:
                        con_alerted = False
                        self.state = 1

            # STATE 3 (running)
            elif self.state == 3:
                if self.check_meeting() != self.in_meeting:
                    self.in_meeting = not self.in_meeting
                    if not self.change(self.in_meeting):
                        self.state = 2
                        self.set_icon(0)
                else:
                    if not self.check_conn():
                        self.state = 2
                        self.set_icon(0)
                time.sleep(5)

    def close(self):
        self.do_close = True
        self.icon.stop()

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(5)
        try:
            self.sock.connect((self.host_ip, self.host_port))
            time.sleep(1)
            print("connected")
            if self.check_conn():
                return True
        except socket.timeout:
            self.sock.close()
            return False
        except ConnectionError:
            self.sock.close()
            return False


    def check_conn(self):
        try:
            self.sock.settimeout(5)
            self.sock.send(self.byte_check)
            if self.sock.recv(1) == self.byte_check:
                print("hs")
                return True
            else:
                return False
        except socket.timeout:
            print("to")
            return False
        except ConnectionError:
            print("ce")
            return False

    def change(self, acive):
        if self.state != 3:
            self.notify("Error: not connected")
            return False
        if self.send(self.byte_on if acive else self.byte_off):
            self.set_icon(int(acive) + 1)
            if acive:
                self.notify("meeting started")
            return True
        else:
            self.set_icon(0)
            return False

    def send(self, byte):
        try:
            self.sock.settimeout(5)
            self.sock.send(byte)
            if self.sock.recv(1) == byte:
                return True
        except socket.timeout:
            self.sock.close()
            return False
        except ConnectionError:
            self.sock.close()
            return False

    def check_meeting(self, check_teams=True, check_zoom=True):
        result = False
        if check_teams:
            if os.system("check_teams.bat") == 2:
                print("Teams active")
                result = True
        if check_zoom:
            if os.system("check_zoom.bat") == 2:
                print("Zoom active")
                result = True
        return result

    def check_home(self):
        interfaces = subprocess.check_output("netsh wlan show interfaces").decode("UTF-8", errors="ignore")
        return any([name in interfaces for name in self.ssids])

    def set_icon(self, color):
        """
        :param color: 0:grey 1:green 2:yellow
        """
        paths = {0:"led_grey.png", 1:"led_green.png", 2:"led_yellow.png"}
        titles = {0:"DISCONNECTED", 1:"NO MEETING", 2:"IN MEETING"}
        self.icon.change(paths[color], titles[color])

    def notify(self, message):
        if self.use_notifications:
            self.toast.show_toast("MeetDetector", message, "led_grey.png", 5, True)


if __name__ == "__main__":
    d = DETECTOR()
    d.loop()

