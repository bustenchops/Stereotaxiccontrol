import time
import RPi.GPIO as GPIO
from motorcontrolclass_v2 import StepperSetup
from rotary_class import RotaryEncoder

#Main while loop condition
keepalive = True

#Variables that may need tweaking
calibrationsteps = 4000
backoff = 150

#OFFSETS FOR THE DRILL, Syringe, Needle (minus values is back, left or up)
APDRILL = 0
MVDRILL = 0
DVDRILL = -1333

APfiber = 0
MVfiber = 0
DVfiber = 0

APneedle = 0
MVneedle = 0
DVneedle = 0


#DEFINE NUMBER OF BUTTONS AND ORDER IN ARRAY
buttonarray = ['movefast','moveslow','buttontohome','relativeALL','relativeAP','relativeMV','relativeDV','buttonaction','miscbuttonC','miscbuttonD','miscbuttonE','zerobutton','calibratebutton','miscbuttonA','miscbuttonB']
lastbuttonstate = [len(buttonarray)]

#BUTTON POSITION IN SHIFT REGISTER ARRAY
    # 2 position switch (3 states 1/2 and all off)
movefast = 0
moveslow = 1
buttontohome = 2
relativeALL = 3
relativeAP = 4
relativeMV = 5
relativeDV = 6
buttonaction = 7
miscbuttonC = 8
miscbuttonD = 9
miscbuttonE = 10
zerobutton = 11
calibratebutton = 12
miscbuttonA = 13
miscbuttonB = 14
#NOT USED because the risk of accidental pushes too high
    #rotoclick_AP = 8
    #rotoclick_MV = 9
    #rotoclick_DV = 10

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

#DEFINE ROTARY ENCODERS
rotoA_AP = 16
rotoB_AP = 17
rotoA_MV = 19
rotoB_MV = 20
rotoA_DV = 22
rotoB_DV = 23

#DEFINE STEPPER DIRECTIONS
APback = 0
APforward = 1
MVleft = 0
MVright = 1
DVup = 0
DVdown = 1

#DEFINE STEPPER SPEEDS
finespeed = 1
normalspeed = 5
fastspeed = 10
    #stepper_speed initializes as 1 BUT changes according to the state of the speed switch
stepper_speed = 1

#INITIALIZE PINS
GPIO.setup(latchpin,GPIO.OUT)
GPIO.setup(datapin,GPIO.OUT)

GPIO.setup(movefast, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(moveslow, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(emergstop, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#EMPTY variables to initialize
shiftvalues = []
laststate = []
quest = "none"


#INITIALIZE STEPPERS

APmove = StepperSetup(enableAll,stepAP,directionAP,limitAP,1,APforward,APback)
MVmove = StepperSetup(enableAll,stepMV,directionMV,limitMV,2,MVright,MVleft)
DVmove = StepperSetup(enableAll,stepDV,directionDV,limitDV,3,DVup,DVdown)

#send to object instances to motorcontrol
APmove.receive_instance(APmove)
MVmove.receive_instance(MVmove)
DVmove.receive_instance(DVmove)



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


#Shuts down steppers regardless of what they were doing direction - restart by re-zeroing
def emergencystop(event):

    if event == RotaryEncoder.BUTTONDOWN:
        print("!EMERGENCY STOP!")
        print("Re-Zero axis to enable movement again")
        GPIO.output(enableAll,0)
    else:
        return
    return


#Event handling for the encoders and hard wired buttons each encoder
def AP_event(event): 
 
    if event == RotaryEncoder.CLOCKWISE:
        APmove.steppgo(APforward,stepper_speed,StepperSetup.btnSteps)
    elif event == RotaryEncoder.ANTICLOCKWISE:
        APmove.steppgo(APback,stepper_speed,StepperSetup.btnSteps)
    #This is a hard wired button note the encoder switch
    elif event == RotaryEncoder.BUTTONDOWN:
        emergencystop(event)
    elif event == RotaryEncoder.BUTTONUP:
        return
    return


#Event handling for the encoders and hard wired buttons each encoder
def MV_event(event):
    
    if event == RotaryEncoder.CLOCKWISE:
        MVmove.steppgo(MVright,stepper_speed,StepperSetup.btnSteps)
    elif event == RotaryEncoder.ANTICLOCKWISE:
        MVmove.steppgo(MVleft,stepper_speed,StepperSetup.btnSteps)
    elif event == RotaryEncoder.BUTTONDOWN:
        print("event button B clicked")
        return  
    elif event == RotaryEncoder.BUTTONUP:
        return
    return


#Event handling for the encoders and hard wired buttons each encoder
def DV_event(event):

    if event == RotaryEncoder.CLOCKWISE:
        DVmove.steppgo(DVdown,stepper_speed,StepperSetup.btnSteps)
    elif event == RotaryEncoder.ANTICLOCKWISE:
        DVmove.steppgo(DVup,stepper_speed,StepperSetup.btnSteps)
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


def buttonvalues(lastbut, newbut, butarr):

    x = len(lastbut)

    for i in range(x):
        if lastbut[i] != newbut[i]:
            lastbut[i] = newbut[i]
            print("button ", butarr[i], " state change")

    # stepper_speed (pos 0 and pos 1)
    if lastbut[0] == 1 and lastbut[1] == 1:
        stepper_speed = normalspeed
    elif lastbuttonstate[0] == 0 and lastbut[1] == 1:
        stepper_speed = fastspeed
    elif lastbut[0] == 1 and lastbut[1] == 0:
        stepper_speed = finespeed

    #button to home to ABS zero
    if lastbut[2] == 0:

        for x in range(StepperSetup.DVsteps):
            DVmove.steppgo(DVup, 1,StepperSetup.btnSteps)
        for x in range(StepperSetup.MVsteps):
            MVmove.steppgo(MVleft, 1,StepperSetup.btnSteps)
        for x in range(StepperSetup.APsteps):
            APmove.steppgo(APback,1,StepperSetup.btnSteps)

    #set relative zero for ALL
    if lastbut[3] == 0:
        StepperSetup.APrelpos = StepperSetup.APsteps
        StepperSetup.MVrelpos = StepperSetup.MVsteps
        StepperSetup.DVrelpos = StepperSetup.DVsteps
        APinitREL_holdvalue = StepperSetup.APsteps
        MVinitREL_holdvalue = StepperSetup.MVsteps
        DVinitREL_holdvalue = StepperSetup.DVsteps

        APmove.PosRelAbsCalc()
        MVmove.PosRelAbsCalc()
        DVmove.PosRelAbsCalc()
    #set only AP relative zero
    if lastbut[4] == 0:
        StepperSetup.APrelpos = StepperSetup.APsteps
        APinitREL_holdvalue = StepperSetup.APsteps
        APmove.PosRelAbsCalc()
    # set only MV relative zero
    if lastbut[5] == 0:
        StepperSetup.MVrelpos = StepperSetup.MVsteps
        MVinitREL_holdvalue = StepperSetup.MVsteps
        MVmove.PosRelAbsCalc()
    # set only DV relative zero
    if lastbut[6] == 0:
        StepperSetup.DVrelpos = StepperSetup.DVsteps
        StepperSetup.DVinitREL_holdvalue = StepperSetup.DVsteps
        DVmove.PosRelAbsCalc()

    #button action - Home to Rel zero for AP and MV BUT DV goes all up
    if lastbut[7] == 0:
      for x in range(StepperSetup.DVsteps):
          DVmove.steppgo(DVup,finespeed,StepperSetup.btnSteps)

      if StepperSetup.MVsteps < StepperSetup.MVrelpos:
          shiftdistance = StepperSetup.MVrelpos - StepperSetup.MVsteps
          for x in range(shiftdistance):
              MVmove.steppgo(MVright, finespeed, StepperSetup.btnSteps)
      elif StepperSetup.MVsteps > StepperSetup.DVrelpos:
          shiftdistance = StepperSetup.MVsteps - StepperSetup.MVrelpos
          for x in range(shiftdistance):
              MVmove.steppgo(MVleft, finespeed, StepperSetup.btnSteps)

      if StepperSetup.APsteps < StepperSetup.APrelpos:
          shiftdistance = StepperSetup.APrelpos- StepperSetup.APsteps
          for x in range(shiftdistance):
              APmove.steppgo(APforward, finespeed, StepperSetup.btnSteps)
      elif StepperSetup.APsteps > StepperSetup.APrelpos:
          shiftdistance = StepperSetup.APsteps - StepperSetup.APrelpos
          for x in range(shiftdistance):
              APmove.steppgo(APback, finespeed, StepperSetup.btnSteps)


    #miscbuttonC - DRILL to relative zero for AP and MV BUT DV homed ABS zero but still sets the relative pos
    if lastbut[8] == 0:
        StepperSetup.APrelpos = APinitREL_holdvalue
        StepperSetup.MVrelpos = MVinitREL_holdvalue
        StepperSetup.DVrelpos = DVinitREL_holdvalue

#        if StepperSetup.DVsteps < (StepperSetup.DVrelpos + DVDRILL):
#            shiftdistance = (StepperSetup.DVrelpos + DVDRILL) - StepperSetup.DVsteps
        for x in range(StepperSetup.DVsteps):
#                DVmove.steppgo(DVdown,finespeed,StepperSetup.btnSteps)
#        elif StepperSetup.DVsteps > (StepperSetup.DVrelpos + DVDRILL):
#            shiftdistance = StepperSetup.DVsteps - (StepperSetup.DVrelpos + DVDRILL)
#            for x in range(shiftdistance):
            DVmove.steppgo(DVup, finespeed, StepperSetup.btnSteps)
        if StepperSetup.MVsteps < (StepperSetup.MVrelpos + MVDRILL):
            shiftdistance = (StepperSetup.MVrelpos + MVDRILL) - StepperSetup.MVsteps
            for x in range(shiftdistance):
                MVmove.steppgo(MVright,finespeed,StepperSetup.btnSteps)
        elif StepperSetup.MVsteps > (StepperSetup.DVrelpos + MVDRILL):
            shiftdistance = StepperSetup.MVsteps - (StepperSetup.MVrelpos + MVDRILL)
            for x in range(shiftdistance):
                MVmove.steppgo(MVleft, finespeed, StepperSetup.btnSteps)

        if StepperSetup.APsteps < (StepperSetup.APrelpos + APDRILL):
            shiftdistance = (StepperSetup.APrelpos + APDRILL) - StepperSetup.APsteps
            for x in range(shiftdistance):
                APmove.steppgo(APforward,finespeed,StepperSetup.btnSteps)
        elif StepperSetup.APsteps > (StepperSetup.APrelpos + APDRILL):
            shiftdistance = StepperSetup.APsteps - (StepperSetup.APrelpos + APDRILL)
            for x in range(shiftdistance):
                APmove.steppgo(APback, finespeed, StepperSetup.btnSteps)

    #miscbuttonD - needle to relative zero for AP and MV BUT DV homed ABS zero but still sets the relative pos
    if lastbut[9] == 0:
#        if StepperSetup.DVsteps < (StepperSetup.DVrelpos + DVneedle):
#            shiftdistance = (StepperSetup.DVrelpos + DVneedle) - StepperSetup.DVsteps
        for x in range(StepperSetup.DVsteps):
#            DVmove.steppgo(DVdown,finespeed,StepperSetup.btnSteps)
#        elif StepperSetup.DVsteps > (StepperSetup.DVrelpos + DVneedle):
#            shiftdistance = StepperSetup.DVsteps - (StepperSetup.DVrelpos + DVneedle)
#            for x in range(shiftdistance):
            DVmove.steppgo(DVup, finespeed, StepperSetup.btnSteps)
        StepperSetup.DVrelpos = StepperSetup.DVrelpos + DVneedle
        if StepperSetup.MVsteps < (StepperSetup.MVrelpos + MVneedle):
            shiftdistance = (StepperSetup.MVrelpos + MVneedle) - StepperSetup.MVsteps
            for x in range(shiftdistance):
                MVmove.steppgo(MVright,finespeed,StepperSetup.btnSteps)
        elif StepperSetup.MVsteps > (StepperSetup.DVrelpos + MVneedle):
            shiftdistance = StepperSetup.MVsteps - (StepperSetup.MVrelpos + MVneedle)
            for x in range(shiftdistance):
                MVmove.steppgo(MVleft, finespeed, StepperSetup.btnSteps)
        StepperSetup.MVrelpos = StepperSetup.MVsteps + MVneedle

        if StepperSetup.APsteps < (StepperSetup.APrelpos + APneedle):
            shiftdistance = (StepperSetup.APrelpos + APneedle) - StepperSetup.APsteps
            for x in range(shiftdistance):
                APmove.steppgo(APforward,finespeed,StepperSetup.btnSteps)
        elif StepperSetup.APsteps > (StepperSetup.APrelpos + APneedle):
            shiftdistance = StepperSetup.APsteps - (StepperSetup.APrelpos + APneedle)
            for x in range(shiftdistance):
                APmove.steppgo(APback, finespeed, StepperSetup.btnSteps)
        StepperSetup.APrelpos = StepperSetup.APsteps + APneedle


    #miscbuttonE - fiber to relative zero for AP and MV BUT DV homed ABS zero but still sets the relative pos
    if lastbut[10] == 0:
#        if StepperSetup.DVsteps < (StepperSetup.DVrelpos + DVfiber):
#            shiftdistance = (StepperSetup.DVrelpos + DVfiber) - StepperSetup.DVsteps
        for x in range(StepperSetup.DVsteps):
#                DVmove.steppgo(DVdown,finespeed,StepperSetup.btnSteps)
#        elif StepperSetup.DVsteps > (StepperSetup.DVrelpos + DVfiber):
#            shiftdistance = StepperSetup.DVsteps - (StepperSetup.DVrelpos + DVfiber)
#            for x in range(shiftdistance):
            DVmove.steppgo(DVup, finespeed, StepperSetup.btnSteps)
        StepperSetup.DVrelpos = StepperSetup.DVsteps + DVfiber
        if StepperSetup.MVsteps < (StepperSetup.MVrelpos + MVfiber):
            shiftdistance = (StepperSetup.MVrelpos + MVfiber) - StepperSetup.MVsteps
            for x in range(shiftdistance):
                MVmove.steppgo(MVright,finespeed,StepperSetup.btnSteps)
        elif StepperSetup.MVsteps > (StepperSetup.DVrelpos + MVfiber):
            shiftdistance = StepperSetup.MVsteps - (StepperSetup.MVrelpos + MVfiber)
            for x in range(shiftdistance):
                MVmove.steppgo(MVleft, finespeed, StepperSetup.btnSteps)
        StepperSetup.MVrelpos = StepperSetup.MVsteps + MVfiber
        if StepperSetup.APsteps < (StepperSetup.APrelpos + APfiber):
            shiftdistance = (StepperSetup.APrelpos + APfiber) - StepperSetup.APsteps
            for x in range(shiftdistance):
                APmove.steppgo(APforward,finespeed,StepperSetup.btnSteps)
        elif StepperSetup.APsteps > (StepperSetup.APrelpos + APfiber):
            shiftdistance = StepperSetup.APsteps - (StepperSetup.APrelpos + APfiber)
            for x in range(shiftdistance):
                APmove.steppgo(APback, finespeed, StepperSetup.btnSteps)
        StepperSetup.APrelpos = StepperSetup.APsteps + APfiber

    #zero to bregma (relative) but up ~10mm (relative home)
    if lastbut[11] == 0:
        for x in range(1333):
            DVmove.steppgo(DVup,finespeed,StepperSetup.btnSteps)

        if StepperSetup.APrelpos > StepperSetup.APsteps:
            APdiff = StepperSetup.APrelpos - StepperSetup.APsteps
            for x in range(APdiff):
                APmove.steppgo(APforward, finespeed, StepperSetup.btnSteps)
        else:
            APdiff = StepperSetup.APsteps - StepperSetup.APrelpos
            for x in range(APdiff):
                APmove.steppgo(APback, finespeed, StepperSetup.btnSteps)

        if StepperSetup.MVrelpos > StepperSetup.MVsteps:
            MVdiff = StepperSetup.MVrelpos - StepperSetup.MVsteps
            for x in range(MVdiff):
                MVmove.steppgo(MVright, finespeed, StepperSetup.btnSteps)
        else:
            MVdiff = StepperSetup.MVsteps - StepperSetup.MVrelpos
            for x in range(MVdiff):
                MVmove.steppgo(MVleft, finespeed, StepperSetup.btnSteps)

        print("That's bregma G!")

    #re-calibrate button
    if lastbut[12] == 0:

        print("Let us re-calibrate this biz-E-ness")
        for x in range(StepperSetup.DVsteps):
            DVmove.steppgo(DVup, finespeed, StepperSetup.btnSteps)
        for x in range(StepperSetup.MVsteps):
            MVmove.steppgo(MVleft, finespeed, StepperSetup.btnSteps)
        for x in range(StepperSetup.APsteps):
            APmove.steppgo(APback, finespeed, StepperSetup.btnSteps)

        APmove.CalibrateDistance(calibrationsteps, backoff, StepperSetup.btnSteps)
        MVmove.CalibrateDistance(calibrationsteps, backoff, StepperSetup.btnSteps)
        DVmove.CalibrateDistance(calibrationsteps, backoff, StepperSetup.btnSteps)

    #miscbuttonA - unused
    #if lastbut[13] == 0:
    #miscbuttonB - unused
    # if lastbut[14] == 0:

    return lastbut


#MAIN CODE ################################################################################################

def begin_setup (calibrationsteps, backoff):
    quest = input("Initialization Process ... anykey to continue.")
    quest = input("CAUTION...Remove all attachments from frame arms! anykey to continue.")

    #Zero steppers
    DVmove.zerostep(backoff,StepperSetup.btnSteps)
    APmove.zerostep(backoff,StepperSetup.btnSteps)
    MVmove.zerostep(backoff,StepperSetup.btnSteps)

    #calibration routine
    APmove.CalibrateDistance(calibrationsteps,backoff,StepperSetup.btnSteps)
    MVmove.CalibrateDistance(calibrationsteps,backoff,StepperSetup.btnSteps)
    DVmove.CalibrateDistance(calibrationsteps,backoff,StepperSetup.btnSteps)

def begin_in_thread(lastbuttonstate, buttonarray):
    while keepalive:

        newbuttonstate = getshiftregisterdata()
        lastbuttonstate = buttonvalues(lastbuttonstate,newbuttonstate,buttonarray)

