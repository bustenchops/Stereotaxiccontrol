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
APsteps = 0
MVsteps = 0
DVsteps = 0

APrelOffset = 0
MVrelOffset = 0
DVrelOffset= 0

calibrationsteps = 4000

APstepdistance = float(0.0005)
MVstepdistance = float(0.00075)
DVstepdistance = float(0.00075)

APcurABSdist = float(0)
MVcurABSdist = float(0)
DVcurABSdist = float(0)

APcurRELdist = float(0)
MVcurRELdist = float(0)
DVcurRELdist = float(0)

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
APmove = StepperSetup(enableAll,stepAP,directionAP,limitAP,1)
MVmove = StepperSetup(enableAll,stepMV,directionMV,limitMV,2)
DVmove = StepperSetup(enableAll,stepDV,directionDV,limitDV,3)

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
    return self.lastbuttemp


def CalibrateDistance(self,calsteps):

    global APsteps
    global MVsteps
    global DVsteps

    global APstepdistance
    global MVstepdistance
    global DVstepdistance

    file_name = 'calibration.txt'
    file = open(file_name, 'r')
    r = 0
    while True:
        line = file.readline()
        if not line:
            break
        self.calibratetemp[r] = line.strip()
        r += 1
    file.close()

    APstepdistance = float(self.calibratetemp[0])
    MVstepdistance = float(self.calibratetemp[1])
    DVstepdistance = float(self.calibratetemp[2])

    print("Current calibration values are:")
    print("AP distance per step:", " ", APstepdistance, "mm")
    print("MV distance per step:", " ", MVstepdistance, "mm")
    print("DV distance per step:", " ", DVstepdistance, "mm")

    yesno = input("Perform calibration? (y/n)")
    if yesno == "y":
        notation = input("!!!Make sure to remove any attachments from rig!!!")
        APinput = input("Enter the AP starting position in millimeters.")
        MVinput = input("Enter the MV starting position in millimeters.")
        DVinput = input("Enter the DV starting position in millimeters.")
        for x in range(calsteps):
            if  0 < APsteps < 6000:
                APmove.steppgo(APforward,finespeed)

        for x in range(calsteps):
            if  0 < DVsteps < 6000:
                DVmove.steppgo(DVdown,finespeed)

        for x in range(calsteps):
            if  0 < MVsteps < 6000:
                MVmove.steppgo(MVright,finespeed)

        APinputend = input("Enter the AP final position in millimeters.")
        MVinputend = input("Enter the MV final position in millimeters.")
        DVinputend = input("Enter the DV final position in millimeters.")

        #make sure all are converted to float values
        flAPinput = float(APinput)
        flMVinput = float(MVinput)
        flDVinput = float(DVinput)
        flAPinputend = float(APinputend)
        flMVinputend = float(MVinputend)
        flDVinputend = float(DVinputend)

        #calculated distance moved per step
        APstepdistance = (flAPinputend - flAPinput)/calibrationsteps
        MVstepdistance = (flMVinputend - flMVinput)/calibrationsteps
        DVstepdistance = (flDVinputend - flDVinput)/calibrationsteps

        #write values to file
        calibratetemp = [APstepdistance, MVstepdistance, DVstepdistance]
        # Open the file in write mode
        with open(file_name, "w") as file:
            # Write each variable to the file in Pine Script format
            for x, value in enumerate(calibratetemp):
                varvalue = calibratetemp[x]
                file.write(f"{varvalue}\n")
        file.close()

        print("NEW calibration values are:")
        print("AP distance per step:", " ", APstepdistance, "mm")
        print("MV distance per step:", " ", MVstepdistance, "mm")
        print("DV distance per step:", " ", DVstepdistance, "mm")
        print(f"Variables have been written to {file_name}")

        #Zero again
        DVsteps = DVmove.ZeroStep(DVup,backoff)
        APsteps = APmove.ZeroStep(APback,backoff)
        MVsteps = MVmove.ZeroStep(MVleft,backoff)


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
        APmove.SteppGo(APforward,stepper_speed)
        APsteps += stepper_speed
    elif event == RotaryEncoder.ANTICLOCKWISE:
        APmove.SteppGo(APback,stepper_speed)
        APsteps -= stepper_speed
    elif event == RotaryEncoder.BUTTONDOWN:
        emergencystop()        
    elif event == RotaryEncoder.BUTTONUP:
        return
    return


def MV_event(event):
    
    if event == RotaryEncoder.CLOCKWISE:
        MVmove.SteppGo(MVright,stepper_speed)
        MVsteps += stepper_speed
    elif event == RotaryEncoder.ANTICLOCKWISE:
        MVmove.SteppGo(MVleft,stepper_speed)
        MVsteps -= stepper_speed
    elif event == RotaryEncoder.BUTTONDOWN:
        print("event button B clicked")
        return  
    elif event == RotaryEncoder.BUTTONUP:
        return
    return


def DV_event(event):

    if event == RotaryEncoder.CLOCKWISE:
        DVmove.SteppGo(DVdown,stepper_speed)
        DVsteps += stepper_speed
    elif event == RotaryEncoder.ANTICLOCKWISE:
        DVmove.SteppGo(DVup,stepper_speed)
        DVsteps -= stepper_speed
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
DVsteps = DVmove.ZeroStep(DVup,backoff)
APsteps = APmove.ZeroStep(APback,backoff)
MVsteps = MVmove.ZeroStep(MVleft,backoff)

#calibration routine
CalibrateDistance()

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
            DVsteps = DVmove.zerostep(DVup, DVsteps,0)
        else:
            DVsteps = DVmove.zerostep(DVdown, DVsteps, 0)
        if MVsteps > 0:
            APsteps = MVmove.zerostep(APback, APsteps,0)
        else:
            APsteps = APmove.zerostep(APforward, APsteps, 0)
        if MVsteps > 0:
            MVsteps = MVmove.zerostep(MVleft, MVsteps, 0)
        else:
            MVsteps = MVmove.zerostep(MVright, MVsteps, 0)




need to figure out way to report distance every time a step is made
need to check buttons 

relative abs position
relative zreo
home
calibrate
button to save location
button to scroll through list of targets and action button

import target list ---- use rclone to pull list file.