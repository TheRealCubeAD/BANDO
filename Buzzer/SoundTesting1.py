import pyaudio
import wave
from copy import copy,deepcopy
chunk = 1024
f = wave.open("BuzzLeft.wav","rb")
p = pyaudio.PyAudio()
f = wave.open("BuzzLeft.wav", "rb")
stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                channels=f.getnchannels(),
                rate=f.getframerate(),
                output=True)
data = f.readframes(chunk)

def s(Stream,Data,F):
    while Data:
        Stream.write(Data)
        Data = F.readframes(chunk)
while 1:
    input(">>>")
    s(stream,data,f)
