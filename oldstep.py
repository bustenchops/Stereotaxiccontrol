import time
import RPi.GPIO as GPIO

# setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#DEFINE PINS
enablepin = 2
directionpin = 3
steppin = 4
limitpin = 22

#INITIALIZE PINS
GPIO.setup(limitpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(enablepin, GPIO.OUT, initial=1)
GPIO.setup(directionpin, GPIO.OUT, initial=0)
GPIO.setup(steppin, GPIO.OUT, initial=0)

#SCRIPT
numberofsteps = 1200

quest = input('enable (0) : direction (0)')
GPIO.output(enablepin, 0)
GPIO.output(directionpin, 0)
for x in range(numberofsteps):
    if GPIO.input(limitpin):
        GPIO.output(steppin, 1)
        time.sleep(0.0001)
        GPIO.output(steppin, 0)
        time.sleep(0.0001)
    else:
        print('LIMIT SWITCH TRIGGER')

quest = input('enable (1) : direction (0)')
GPIO.output(enablepin, 1)
GPIO.output(directionpin, 0)
for x in range(numberofsteps):
    if GPIO.input(limitpin):
        GPIO.output(steppin, 1)
        time.sleep(0.0001)
        GPIO.output(steppin, 0)
        time.sleep(0.0001)
    else:
        print('LIMIT SWITCH TRIGGER')