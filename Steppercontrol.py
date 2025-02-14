import time
import RPi.GPIO as GPIO

# setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#DEFINE STEPPER CONTROL PINS
enableAll = 1

directionAV = 2
stepAV = 3

directionMV = 4
stepMV = 5

directionDV = 6
stepDV = 7

#DEFINE LIMIT SWITCH PINS
limitAP = 8
limitMV = 9
LimitDV = 10

#DEFINE SPEED PINS
movefast = 11
moveslow = 12

#DEFINE EMERGENCY STOP
emergstop = 13

#DEFINE HOME BUTTON
buttontohome = 14

#DEFINE ACTION BUTTON
buttonaction = 15

#DEFINE ROTARY ENCODERS
rotoA_AV = 16
rotoB_AV = 17
rotoclick_AV = 18

rotoA_MV = 19
rotoB_MV = 20
rotoclick_MV = 21

rotoA_DV = 22
rotoB_DV = 23
rotoclick_DV = 24

#INITIALIZE PINS
GPIO.setup(enableAll, GPIO.OUT, initial=1)

GPIO.setup(limitAP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(limitMV, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(limitDV, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(directionAV, GPIO.OUT, initial=0)
GPIO.setup(directionMV, GPIO.OUT, initial=0)
GPIO.setup(directionDV, GPIO.OUT, initial=0)

GPIO.setup(stepAV, GPIO.OUT, initial=0)
GPIO.setup(stepMV, GPIO.OUT, initial=0)
GPIO.setup(stepDV, GPIO.OUT, initial=0)

GPIO.setup(movefast, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(moveslow, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(emergstop, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(buttontohome, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(buttonaction, GPIO.IN, pull_up_down=GPIO.PUD_UP)

##NOTE: use signal OR thread to catch the encoder input?




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

quest = input('enable (0) : direction (1)')
GPIO.output(enablepin, 0)
GPIO.output(directionpin, 1)
for x in range(numberofsteps):
    if GPIO.input(limitpin):
        GPIO.output(steppin, 1)
        time.sleep(0.0001)
        GPIO.output(steppin, 0)
        time.sleep(0.0001)
    else:
        print('LIMIT SWITCH TRIGGER')

quest = input('enable (1) : direction (1)')
GPIO.output(enablepin, 1)
GPIO.output(directionpin, 1)
for x in range(numberofsteps):
    if GPIO.input(limitpin):
        GPIO.output(steppin, 1)
        time.sleep(0.0001)
        GPIO.output(steppin, 0)
        time.sleep(0.0001)
    else:
        print('LIMIT SWITCH TRIGGER')

print('ENDTEST')