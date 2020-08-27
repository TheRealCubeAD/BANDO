#import pyttsx3
from gtts import gTTS
import os
import threading
import time

class SOUND:


    def __init__(self):
        self.occupied = False
        self.keeper = threading.Thread(target=self.keep_alive)
        self.keeper.daemon = True
        self.keeper.start()


    def speak(self,text):
        thread = threading.Thread(target=self.TTS,args=[text])
        thread.daemon = False
        thread.start()


    def TTS(self,text):
        while self.occupied:
            pass
        self.occupied = True
        tts = gTTS(text, "en-uk")
        tts.save("temp.mp3")
        os.system("mpg123 temp.mp3")
        self.occupied = False


    def sound(self,num,opt="e"):
        path = "Mp3/"
        if opt == "e":
            path += "Click_Electronic/Click_Electronic_"

        path += num + ".mp3"

        os.system("mpg123 "+path)


    def keep_alive(self):
        while 1:
            os.system("mpg123 Mp3/output.wav")
            time.sleep(30)



if __name__ == "__main__":
    s = SOUND()
    s.speak("starting")
    s.sound("15")
