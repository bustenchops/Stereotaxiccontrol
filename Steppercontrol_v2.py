import sys
import time
from os.path import relpath
import RPi.GPIO as GPIO
from motorcontrolclass_v2 import StepperSetup
from rotary_class import RotaryEncoder

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

#DEFINE EMERGENCY STOP and hard wired buttons
emergstop = 11
misc_eventbuttonA = 15
misc_eventbuttonB = 24

#DEFINE SHIFT REGISTER PINS
latchpin = 12
clockpin = 13
datapin = 14

#DEFINE NUMBER OF BUTTONS AND ORDER IN ARRAY
buttonarray = ['movefast','moveslow','buttontohome','relativeALL','relativeAP','relativeMV','relativeDV','buttonaction','rotoclick_AP','rotoclick_MV','rotoclick_DV','zerobutton','calibratebutton','miscbuttonA','miscbuttonB']

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
zerobutton = 11
calibratebutton = 12
miscbuttonA = 13
miscbuttonB = 14

#DEFINE ROTARY ENCODERS
rotoA_AP = 16
rotoB_AP = 17

rotoA_MV = 19
rotoB_MV = 20

rotoA_DV = 22
rotoB_DV = 23

#DEFINE GLOBAL VARIABLES
# defined in motorcontrolclass APsteps = 0
# defined in motorcontrolclass MVsteps = 0
# defined in motorcontrolclass DVsteps = 0

APrelOffset = 0
MVrelOffset = 0
DVrelOffset= 0

calibrationsteps = 4000

backoff = 20

keepalive = True

#DEFINE STEPPER DIRECTIONS
APback = 0
APforward = 1
MVleft = 0
MVright = 1
DVup = 0
DVdown = 1

#DEFINE STEPPER SPPEEDS
finespeed = 1
normalspeed = 5
fastspeed = 10

stepper_speed = 1

#INITIALIZE PINS
GPIO.setup(latchpin,GPIO.OUT)
GPIO.setup(datapin,GPIO.OUT)

GPIO.setup(movefast, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(moveslow, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(emergstop, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#INITIALIZE STEPPERS

APmove = StepperSetup(enableAll,stepAP,directionAP,limitAP,1,APforward,APback)
MVmove = StepperSetup(enableAll,stepMV,directionMV,limitMV,2,MVright,MVleft)
DVmove = StepperSetup(enableAll,stepDV,directionDV,limitDV,3,DVup,DVdown)

#send to motorcontrol
APmove.iliketomoveit(APmove)
MVmove.iliketomoveit(MVmove)
DVmove.iliketomoveit(DVmove)


def getshiftregisterdata(self):

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
        self.shiftvalues[i] = GPIO.input(datapin)
        GPIO.output(clockpin, GPIO.HIGH)
        time.sleep(0.01)
    return self.shiftvalues


def laststatebuttonvalues_init(self):

    x = len(buttonarray)
    for i in range(x):
        self.laststate[i] = 0
    return self.laststate

def buttonvalues(self, lastbut, newbut, butarr):
    self.lastbuttemp = lastbut
    x = len(lastbut)

    for i in range(x):
        if lastbut[i] != newbut[i]:
            self.lastbuttemp[i] = newbut[i]
            print("button ", buttonarray[i], " state change")
            if lastbut[i] == movefast:
                REST OF BUTTONS
    return self.lastbuttemp


def emergencystop(event):

    if event == RotaryEncoder.BUTTONDOWN:
        print("!EMERGENCY STOP!")
        print("Re-Zero axis to enable movement again")
        GPIO.output(enableAll,0)
    else:
        return
    return


def AP_event(event): 
 
    if event == RotaryEncoder.CLOCKWISE:
        APmove.steppgo(APforward,stepper_speed)
        StepperSetup.APsteps += stepper_speed
    elif event == RotaryEncoder.ANTICLOCKWISE:
        APmove.steppgo(APback,stepper_speed)
        StepperSetup.APsteps -= stepper_speed
    elif event == RotaryEncoder.BUTTONDOWN:
        emergencystop(event)
    elif event == RotaryEncoder.BUTTONUP:
        return
    return


def MV_event(event):
    
    if event == RotaryEncoder.CLOCKWISE:
        MVmove.steppgo(MVright,stepper_speed)
        StepperSetup.MVsteps += stepper_speed
    elif event == RotaryEncoder.ANTICLOCKWISE:
        MVmove.steppgo(MVleft,stepper_speed)
        StepperSetup.MVsteps -= stepper_speed
    elif event == RotaryEncoder.BUTTONDOWN:
        print("event button B clicked")
        return  
    elif event == RotaryEncoder.BUTTONUP:
        return
    return


def DV_event(event):

    if event == RotaryEncoder.CLOCKWISE:
        DVmove.steppgo(DVdown,stepper_speed)
        StepperSetup.DVsteps += stepper_speed
    elif event == RotaryEncoder.ANTICLOCKWISE:
        DVmove.steppgo(DVup,stepper_speed)
        StepperSetup.DVsteps -= stepper_speed
    elif event == RotaryEncoder.BUTTONDOWN:
        print("event button B clicked")
        return  
    elif event == RotaryEncoder.BUTTONUP:
        return
    return

#INITIALIZE ENCODERS
AProto = RotaryEncoder(rotoA_AP,rotoB_AP,emergstop,AP_event)
MVroto = RotaryEncoder(rotoA_MV,rotoB_MV,misc_eventbuttonA,MV_event)
DVroto = RotaryEncoder(rotoA_DV,rotoB_DV,misc_eventbuttonB,DV_event)


#MAIN CODE ################################################################################################

# INITIALIZE BUTTON STATE
lastbuttonstate = laststatebuttonvalues_init()

quest = input("Initialization Process ... anykey to continue.")
quest = input("CAUTION...Remove all attachments from frame arms! Anykey to continue.")

#Zero steppers
DVmove.zerostep(backoff)
APmove.zerostep(backoff)
MVmove.zerostep(backoff)

#calibration routine
APmove.CalibrateDistance(calibrationsteps,backoff)
MVmove.CalibrateDistance(calibrationsteps,backoff)
DVmove.CalibrateDistance(calibrationsteps,backoff)

while keepalive:
    #button settings
    newbuttonstate = getshiftregisterdata()
    lastbuttonstate = buttonvalues(lastbuttonstate,newbuttonstate,buttonarray)

    #stepper_speed
    if lastbuttonstate[0] == 1 and lastbuttonstate[1] == 1:
        stepper_speed = normalspeed
    elif lastbuttonstate[0] == 0 and lastbuttonstate[1] == 1:
        stepper_speed = fastspeed
    elif lastbuttonstate[0] == 1 and lastbuttonstate[1] == 0:
        stepper_speed = finespeed
    #homebutton
    if lastbuttonstate[2] == 0:
        if APsteps > 0:
            StepperSetup.DVsteps = DVmove.zerostep(DVup, DVsteps,0)
        else:
            StepperSetup.DVsteps = DVmove.zerostep(DVdown, DVsteps, 0)
        if MVsteps > 0:
            StepperSetup.APsteps = MVmove.zerostep(APback, APsteps,0)
        else:
            StepperSetup.APsteps = APmove.zerostep(APforward, APsteps, 0)
        if MVsteps > 0:
            StepperSetup.MVsteps = MVmove.zerostep(MVleft, MVsteps, 0)
        else:
            StepperSetup.MVsteps = MVmove.zerostep(MVright, MVsteps, 0)




need to figure out way to report distance every time a step is made
need to check buttons 

relative abs position
relative zreo
home
calibrate
button to save location
button to scroll through list of targets and action button

import target list ---- use rclone to pull list file.