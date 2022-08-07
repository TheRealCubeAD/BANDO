from machine import Pin, reset
import network
import socket
import time
import sys

network.WLAN(network.AP_IF).active(False)
station = network.WLAN(network.STA_IF)
station.active(True)

ssid = "LAN Solo"
pw = "Bn@IK2019"
ip = "192.168.0.55"
port = 1234

led_ac = Pin(12, Pin.OUT) # D6
led_nac = Pin(13, Pin.OUT) # D7

byte_check = b'\x01'
byte_on = b'\xF0'
byte_off = b'\xA0'

sock = None

def reboot():
    print("RESET")
    reset()
    time.sleep(1)

def recv(inp, to):
    inp.setblocking(False)
    inp.settimeout(1)
    for i in range(to):
        try:
            m = inp.recv(1)
            print(m)
            if m:
                return m
            time.sleep(1)
        except OSError as e:
            if (not "EAGAIN" in str(e)) and (not "ETIMEDOUT" in str(e)):
                raise OSError(str(e))
            time.sleep(1)
            continue
    raise ValueError()

while 1:
    led_ac.off()
    led_nac.off()
    try:
        sock.close()
    except:
        pass

    # CONNECT WLAN
    while not station.isconnected():
        print("connecting")
        station.connect(ssid, pw)
        time.sleep(5)
    if station.ifconfig()[0] != ip:
        print("reconfig")
        config = (ip,) + station.ifconfig()[1:]
        station.disconnect()
        station.ifconfig(config)
        while not station.isconnected():
            print("connecting")
            station.connect(ssid, pw)
            time.sleep(5)
    print(station.config("mac"))
    print(station.ifconfig())
    led_ac.on()
    led_nac.on()
    time.sleep(1)
    led_ac.off()
    led_nac.off()

    # CONNECT CLIENT
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(True)
        sock.bind(("0.0.0.0", port))
        sock.listen(1)
        print("listening")
        conn, addr = sock.accept()
        sock.setblocking(False)
        print("connected")
        conn.send(recv(conn, 5))
    except OSError as e:
        print(e)
        reboot()
    except ValueError:
        continue
    print("good conn")

    # LISTEN
    while 1:
        try:
            message = recv(conn, 20)
        except OSError as e:
            print(e)
            reboot()
        except ValueError:
            break
        if message == byte_on:
            print("ON")
            led_ac.on()
            led_nac.off()
        elif message == byte_off:
            print("OFF")
            led_ac.off()
            led_nac.on()
        try:
            conn.send(message)
        except OSError as e:
            print(e)
            reboot()


