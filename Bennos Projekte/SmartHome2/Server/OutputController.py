from Output import disp, fan, sound
import wakeonlan


class OUTCON:
    def __init__(self):
        self.screen = disp.DISPLAY()
        self.speaker = sound.SOUND()
        self.fan = fan.FAN()

    def text(self, text):
        self.screen.add_text(text)

    def speak(self, text):
        self.speaker.speak(text)

    def sound(self, sound):
        pass

    def start_pc(self):
        wakeonlan.send_magic_packet("B4-2E-99-49-22-9F")

    def activate(self):
        self.screen.activate()
        self.speak("Smarthome is starting")
        self.fan.turn_on()

    def deactivate(self):
        self.screen.deactivate()
        self.speak("Smarthome is shutting down")
        self.fan.turn_off()

