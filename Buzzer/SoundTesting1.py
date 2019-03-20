import pyaudio
import wave
chunk = 1024
f = wave.open("BuzzLeft.wav","rb")
p = pyaudio.PyAudio()



while 1:
    f = wave.open("BuzzLeft.wav", "rb")
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    data = f.readframes(chunk)
    input(">>>")
    while data:
        stream.write(data)
        data = f.readframes(chunk)
