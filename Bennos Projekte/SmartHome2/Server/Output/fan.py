import RPi.GPIO as GPIO

class FAN:

    def __init__(self):
        self.pin_fan = 23
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_fan,GPIO.OUT)

    def turn_on(self):
        GPIO.output(self.pin_fan,GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self.pin_fan,GPIO.LOW)


if __name__ == '__main__':
    f = FAN()
    input()
    f.turn_on()
    input()
    f.turn_off()
