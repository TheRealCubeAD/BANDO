from machine import Pin, PWM
import time
import network
from ntptime import settime
import clock as CLOCK


class SPEAKER:

    def __init__(self):
        self.speaker_pin = 15
        self.speaker = PWM(Pin(self.speaker_pin))
        self.speaker_off()
        self.notes = []
        self.freqs = []
        self.read_notes()
        self.first_ = []
        self.second_ = []
        self.affirm_ = []
        self.read_melody("first.txt", self.first_)
        self.read_melody("second.txt", self.second_)
        self.read_melody("affirm.txt", self.affirm_)


    def first(self):
        self.play_melody(self.first_)

    def second(self):
        self.play_melody(self.second_)

    def affirmative(self):
        self.play_melody(self.affirm_)


    def read_melody(self, path, var):
        with open(path) as file:
            for line in file:
                note, duration = line.split()
                note = self.get_freq(note)
                duration = float(duration)
                var.append([note, duration])


    def play_melody(self, var):
        for line in var:
            freq, duration = line
            if freq == 0:
                time.sleep(duration)
            else:
                self.play_tone(freq, duration)


    def read_notes(self):
        self.notes = ["0"]
        self.freqs = [0]
        t = open("note_edit.txt","r")
        for line in t:
            n, f = line.split()
            self.notes.append(n)
            self.freqs.append(int(f))
        t.close()

    def speaker_off(self):
        self.speaker.duty(0)

    def speaker_on(self):
        self.speaker.duty(512)

    def trigger(self,sec):
        self.speaker_on()
        time.sleep(sec)
        self.speaker_off()


    def get_freq(self,note):
        try:
            return self.freqs[self.notes.index(note)]
        except:
            return 0


    def set_freq(self,note):
        if type(note) == int:
            self.speaker.freq(note)
        else:
            self.speaker.freq(self.get_freq(note))


    def play_tone(self,note,sec):
        self.set_freq(note)
        self.trigger(sec)


    def play_tones(self,notes,sec):
        self.speaker_on()
        for i in range(sec*10):
            for note in notes:
                self.set_freq(note)
                time.sleep(0.1)
        self.speaker_off()


    def error(self):
        self.play_tone("G4", 2)



class LED:

    def __init__(self):
        self.led_pin = 14
        self.led = Pin(self.led_pin, Pin.OUT)
        self.led_off()


    def led_on(self):
        self.led.on()


    def led_off(self):
        self.led.off()


    def toggle(self,sec):
        self.led_on()
        time.sleep(sec)
        self.led_off()


    def flash(self):
        self.toggle(0.1)


    def flash_inverse(self):
        self.led_off()
        time.sleep(0.5)
        self.led_on()



class SYSTEM:

    def __init__(self):
        # Devices
        self.speaker = SPEAKER()
        self.led = LED()
        self.clock = CLOCK.DS3231()
        self.button = Pin(9999, Pin.IN)

        # Data
        self.sleep = ((23,00), (6,00))
        self.reminds = []
        self.second_time = (00, 1)
        self.next_remind = None
        self.affirmed = False

        # Init
        self.read_times()
        self.reset_clock()
        self.speaker.affirmative()


    def read_times(self):
        try:
            with open("remind_times.txt") as file:
                for line in file:
                    try:
                        hh, mm = line.split(':')
                        hh = int(hh)
                        mm = int(mm)
                        hh -= 1
                        if hh == -1:
                            hh = 23
                        self.reminds.append((hh,mm))
                    except:
                        print("Error while reading time:", line)
        except:
            print("fatal error while reading remind-times")
            self.speaker.error()


    def reset_clock(self):
        try:
            sta_if = network.WLAN(network.STA_IF)
            if True:
                print('connecting to network...')
                sta_if.active(True)
                sta_if.connect('Lan Solo', 'Bn@IK209')
                time.sleep(5)
            print('network config:', sta_if.ifconfig())
            try:
                settime()
                try:
                    self.clock.save_time()
                except:
                    print("error while trying to send time to clock")
            except:
                print("no connection to internet-clock")

        except:
            print("non-fatal error while trying to reset time")


    def is_sleep(self, time):
        h1, m1 = self.sleep[0]
        h2, m2 = self.sleep[1]
        hh, mm = time
        m1 -= mm
        m2 -= mm
        if m1 < 0:
            m1 += 60
            h1 -= 1
        if m2 < 0:
            m2 += 60
            h2 -= 1
        h1 -= hh
        if h1 < 0 or (h1 == 0 and m1 == 0):
            return False
        if h2 > 0 or (h2 == 0 and m2 == 0):
            return False
        return True


    def button_callback(self):
        if not self.affirmed:
            self.affirmed = True
            self.speaker.affirmative()
            self.led.led_off()


    def add(self, a, b):
        mm = a[1] + b[1]
        hh = a[0] + b[0]
        if mm >= 60:
            mm -= 60
            hh += 1
        if hh >= 24:
            hh -= 24
        return (hh,mm)


    def main(self):
        while 1:
            try:
                cur_time = self.clock.get_time()
                print(cur_time)
                hh = cur_time[3]
                mm = cur_time[4]
                if (hh,mm) in self.reminds:
                    self.affirmed = False
                    self.next_remind = self.add((hh,mm), self.second_time)
                    print("next at", self.next_remind)
                    self.led.led_on()
                    if self.is_sleep((hh,mm)):
                        self.speaker.first()
                    self.led.led_off()
                    time.sleep(0.5)
                    self.led.flash()
                    time.sleep(0.5)
                    self.led.led_on()
                    time.sleep(60)


                elif (hh,mm) == self.next_remind and not self.affirmed:
                    self.next_remind = self.add(self.next_remind, self.second_time)
                    self.led.flash_inverse()
                    if self.is_sleep((hh, mm)):
                        self.speaker.second()
                time.sleep(3)
            except:
                print("Fatal Error in main code")
                self.speaker.error()





s = SYSTEM()
s.main()