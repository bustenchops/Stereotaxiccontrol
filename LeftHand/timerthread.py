import time
import RPi.GPIO as GPIO

from VariableList import var_list

class threadedtimer:

# setup GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    def __init__(self, UIinstance):
        self.sendtoUI = UIinstance

    def runtimerthread(self):
        # note this will send the time now every 250ms to the varlist
        # will reset the timed functions after x time