from machine import Pin, PWM
import time



def read_notes():
    global notes
    global freqs
    res_notes = []
    res_freq = []
    t = open("note_edit.txt","r")
    for line in t:
        n, f = line.split()
        res_notes.append(n)
        res_freq.append(int(f))
    t.close()
    print(res_notes)
    print(res_freq)
    notes = res_notes
    freqs = res_freq


def speaker_off():
    speaker.duty(0)

def speaker_on():
    speaker.duty(512)

def trigger(sec):
    speaker_on()
    time.sleep(sec)
    speaker_off()


def get_freq(note):
    try:
        return freqs[notes.index(note)]
    except:
        return 0


def play_tone(note,sec):
    freq = get_freq(note)
    print(freq)
    speaker.freq(freq)
    trigger(sec)


def play_tones(notes,sec):
    for i in range(sec*10):
        for note in notes:
            play_tone(note, 0.1)



speaker_pin = 15
speaker = PWM(Pin(speaker_pin))
speaker_off()
notes = []
freqs = []


print("start")
read_notes()

play_tone("C5",1)
play_tone("E5",1)
play_tone("G5",1)

play_tones(["C5","E5","G5"],1)
play_tones(["D4","F4","A4"],1)
play_tones(["E5","G5","B5"],1)
