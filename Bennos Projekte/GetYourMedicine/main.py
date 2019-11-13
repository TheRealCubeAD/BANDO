from machine import Pin, PWM
import time


class SPEAKER:

    def __init__(self):
        self.speaker_pin = 15
        self.speaker = PWM(Pin(self.speaker_pin))
        self.speaker_off()
        self.notes = []
        self.freqs = []
        self.read_notes()


    def read_notes(self):
        self.notes = []
        self.freqs = []
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



class LED:

    def __init__(self):
        self.led_pin = 14
        self.led = Pin(self.led_pin, Pin.OUT)


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



print("start")
speaker = SPEAKER()
led = LED()

speaker.play_tone("C5",1)
led.flash()


