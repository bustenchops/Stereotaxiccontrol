import time
import threading
from os.path import relpath
import RPi.GPIO as GPIO

# setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#DEFINE STEPPER CONTROL PINS
enableAll = 1

directionAP = 2
stepAP = 3

directionMV = 4
stepMV = 5

directionDV = 6
stepDV = 7

#DEFINE LIMIT SWITCH PINS
limitAP = 8
limitMV = 9
limitDV = 10

#DEFINE EMERGENCY STOP
emergstop = 11

#DEFINE SHIFT REGISTER PINS
latchpin = 12
clockpin = 13
datapin = 14

#DEFINE NUMBER OF BUTTONS AND ORDER IN ARRAY
buttonarray = ['movefast','moveslow','buttontohome','relativeALL','relativeAP','relativeMV','relativeDV','buttonaction','rotoclick_AP','rotoclick_MV','rotoclick_DV']

#BUTTON POSITION IN SHIFT REGISTER ARRAY
movefast = 0
moveslow = 1
buttontohome = 2
relativeALL = 3
relativeAP = 4
relativeMV = 5
relativeDV = 6
buttonaction = 7
rotoclick_AP = 8
rotoclick_MV = 9
rotoclick_DV = 10

#DEFINE ROTARY ENCODERS
rotoA_AP = 16
rotoB_AP = 17

rotoA_MV = 19
rotoB_MV = 20

rotoA_DV = 22
rotoB_DV = 23

#DEFINE GLOBAL VARIABLES
APsteps = 0
MVsteps = 0
DVsteps = 0
AP


#INITIALIZE PINS

GPIO.setup(latchpin,GPIO.OUT)
GPIO.setup(datapin,GPIO.OUT)


GPIO.setup(enableAll, GPIO.OUT, initial=1)

GPIO.setup(limitAP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(limitMV, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(limitDV, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(directionAP, GPIO.OUT, initial=0)
GPIO.setup(directionMV, GPIO.OUT, initial=0)
GPIO.setup(directionDV, GPIO.OUT, initial=0)

GPIO.setup(stepAP, GPIO.OUT, initial=0)
GPIO.setup(stepMV, GPIO.OUT, initial=0)
GPIO.setup(stepDV, GPIO.OUT, initial=0)

GPIO.setup(movefast, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(moveslow, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(emergstop, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(buttontohome, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(buttonaction, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(rotoA_AP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rotoB_AP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rotoA_MV, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rotoB_MV, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rotoA_DV, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rotoB_DV, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(rotoclick_AP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rotoclick_MV, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rotoclick_DV, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#SCRIPT
numberofsteps = 1200

def getshiftregisterdata():
    #get number of buttons
    x = len(buttonarray)
    #LOAD DATA
    GPIO.output(latchpin,GPIO.LOW)
    time.sleep(0.01)
    GPIO.output(latchpin,GPIO.HIGH)
    #READ DATA
    for i in range(x):
        GPIO.output(clockpin,GPIO.LOW)
        time.sleep(0.01)
        shiftvalues[i] = GPIO.input(datapin)
        GPIO.output(clockpin, GPIO.HIGH)
        time.sleep(0.01)
    return shiftvalues

def zerorig():
    while GPIO.input(limitDV):
        GPIO.output(directionDV,1)
        GPIO.output(stepDV, 1)
        time.sleep(0.0001)
        GPIO.output(stepDV, 0)
        time.sleep(0.0001)
        DVsteps = 0

    while GPIO.input(limitAP):
        GPIO.output(directionAP,1)
        GPIO.output(stepAP, 1)
        time.sleep(0.0001)
        GPIO.output(stepAP, 0)
        time.sleep(0.0001)
        APsteps = 0

    while GPIO.input(limitMV):
        GPIO.output(directionMV,1)
        GPIO.output(stepMV, 1)
        time.sleep(0.0001)
        GPIO.output(stepMV, 0)
        time.sleep(0.0001)
        MVsteps = 0

    def calibratedistance()
        APstart = input



#MAIN CODE








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