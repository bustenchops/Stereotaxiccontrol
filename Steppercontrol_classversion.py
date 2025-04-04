import time
import RPi.GPIO as GPIO

from motorcontrolclass_v2 import StepperSetup
from rotary_classv2 import RotaryEncoder
import tkinter as tk
from tkinter import simpledialog

class mainprogram:
    #Main while loop condition
    keepalive = True

    #Variables that may need tweaking
    calibrationsteps = 4000
    backoff = 200

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
    buttonarray = ['moveslow','needleoffset','drilloffset','HomeToABSzero','movefast','recalibrate','relativeDV','relativeALLset','relativeAP','relativeMV','FIberOffset','HomerelativeZero','bregmahome','miscbuttonA','miscbuttonB']
    lastbuttonstate = [0 for x in range(len(buttonarray))]

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
    enableAll = 2

    directionAP = 3
    stepAP = 4

    directionMV = 17
    stepMV = 27

    directionDV = 5
    stepDV = 6

    #DEFINE LIMIT SWITCH PINS
    limitAP = 22
    limitMV = 13
    limitDV = 19

    #DEFINE EMERGENCY STOP and hard wired buttons
    emergstop = 26
    misc_eventbuttonA = 10
    misc_eventbuttonB = 11

    #DEFINE SHIFT REGISTER PINS
    latchpin = 18
    clockpin = 23
    datapin = 24

    #DEFINE ROTARY ENCODER PINS
    rotoA_AP = 25
    rotoB_AP =  8
    rotoA_MV = 12
    rotoB_MV = 16
    rotoA_DV = 20
    rotoB_DV = 21

    #Relative Offset variables --> unused
    # APrelOffset = 0
    # MVrelOffset = 0
    # DVrelOffset= 0

    #DEFINE STEPPER DIRECTIONS
    APback = 0
    APforward = 1
    MVleft = 0
    MVright = 1
    DVup = 0
    DVdown = 1

    #DEFINE STEPPER SPEEDS - number of steps per call (should be fine, medium, coarse but its already written)
    finespeed = 1
    normalspeed = 5
    fastspeed = 10
        #stepper_speed initializes as 1 BUT changes according to the state of the speed switch
    stepper_speed = finespeed

    def __init__(self):
        #INITIALIZE PINS
        GPIO.setup(mainprogram.latchpin,GPIO.OUT)
        GPIO.setup(mainprogram.clockpin,GPIO.OUT)
        GPIO.setup(mainprogram.datapin,GPIO.IN)

#   Need to test rotary encoder setup to see if Hard Wired Buttons are working
#        GPIO.setup(mainprogram.emergstop, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#        GPIO.setup(mainprogram.misc_eventbuttonA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#        GPIO.setup(mainprogram.misc_eventbuttonB, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        #EMPTY variables to initialize
        self.quest = "none"

# encoders were here
#stepper init was here


#Import the offsets
        self.offsetimport = []
        self.importfile_name = 'offsets.txt'

        file = open(self.importfile_name, 'r')
        while True:
            line = file.readline()
            if not line:
                break
            self.offsetimport.append(line.strip())
        file.close()
        mainprogram.APDRILL = self.offsetimport[0]
        mainprogram.MVDRILL = self.offsetimport[1]
        mainprogram.DVDRILL = self.offsetimport[2]

        mainprogram.APneedle = self.offsetimport[3]
        mainprogram.MVneedle = self.offsetimport[4]
        mainprogram.DVneedle = self.offsetimport[5]

        mainprogram.APfiber = self.offsetimport[6]
        mainprogram.MVfiber = self.offsetimport[7]
        mainprogram.DVfiber = self.offsetimport[8]

#to use  parts of the main stereotaxic window
    def receive_frommaincontrol(self, comingfrommainA):
        self.sendingtomainA = comingfrommainA

    def getshiftregisterdata(self):

        self.shiftvalues = []
        #get number of buttons
        x = len(mainprogram.buttonarray)
        print("button array lenght=", x)
        for k in range(x):
            self.shiftvalues.append(0)
        #LOAD DATA
        GPIO.output(mainprogram.latchpin,GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(mainprogram.latchpin,GPIO.HIGH)
        #READ DATA
        for i in range(x):
            GPIO.output(mainprogram.clockpin,GPIO.LOW)
            self.shiftvalues[i] = GPIO.input(mainprogram.datapin)
            GPIO.output(mainprogram.clockpin, GPIO.HIGH)
            time.sleep(0.001)
        return self.shiftvalues


    def buttonvalues(self, lastbut, newbut, butarr):

        x = len(lastbut)
        y = len(newbut)
        if x != y:
            print("the last button array and new button array are not equal")
        for i in range(x):
            if lastbut[i] != newbut[i]:
                lastbut[i] = newbut[i]
                print("button ", butarr[i], " state change", lastbut[i], ' to ', newbut[i])

# note 1 is pressed and 0 is released
        # stepper_speed (pos 0 and pos 1)
        if lastbut[0] == 0 and lastbut[4] == 0:
            mainprogram.stepper_speed = mainprogram.normalspeed
        elif lastbut[0] == 1 and lastbut[4] == 0:
            mainprogram.stepper_speed = mainprogram.fastspeed
        elif lastbut[0] == 0 and lastbut[4] == 1:
            mainprogram.stepper_speed = mainprogram.finespeed

        #button to home to ABS zero
        if lastbut[3] == 1:

            for x in range(StepperSetup.DVsteps):
                self.DVmove.steppgo(mainprogram.DVup, 1,StepperSetup.btnSteps)
            for x in range(StepperSetup.MVsteps):
                self.MVmove.steppgo(mainprogram.MVleft, 1,StepperSetup.btnSteps)
            for x in range(StepperSetup.APsteps):
                self.APmove.steppgo(mainprogram.APback,1,StepperSetup.btnSteps)

        #set relative zero for ALL
        if lastbut[7] == 0:
            StepperSetup.APrelpos = StepperSetup.APsteps
            StepperSetup.MVrelpos = StepperSetup.MVsteps
            StepperSetup.DVrelpos = StepperSetup.DVsteps
            StepperSetup.APinitREL_holdvalue = StepperSetup.APsteps
            StepperSetup.MVinitREL_holdvalue = StepperSetup.MVsteps
            StepperSetup.DVinitREL_holdvalue = StepperSetup.DVsteps

            self.APmove.PosRelAbsCalc()
            self.MVmove.PosRelAbsCalc()
            self.DVmove.PosRelAbsCalc()

        #set only AP relative zero
        if lastbut[8] == 0:
            StepperSetup.APrelpos = StepperSetup.APsteps
            StepperSetup.APinitREL_holdvalue = StepperSetup.APsteps
            self.APmove.PosRelAbsCalc()
        # set only MV relative zero
        if lastbut[9] == 0:
            StepperSetup.MVrelpos = StepperSetup.MVsteps
            StepperSetup.MVinitREL_holdvalue = StepperSetup.MVsteps
            self.MVmove.PosRelAbsCalc()
        # set only DV relative zero
        if lastbut[6] == 0:
            StepperSetup.DVrelpos = StepperSetup.DVsteps
            StepperSetup.DVinitREL_holdvalue = StepperSetup.DVsteps
            self.DVmove.PosRelAbsCalc()

        #button action - Home to Rel zero for AP and MV BUT DV goes all up
        if lastbut[11] == 0:
          for x in range(StepperSetup.DVsteps):
              self.DVmove.steppgo(mainprogram.DVup,mainprogram.finespeed,StepperSetup.btnSteps)

          if StepperSetup.MVsteps < StepperSetup.MVrelpos:
              shiftdistance = StepperSetup.MVrelpos - StepperSetup.MVsteps
              for x in range(shiftdistance):
                  self.MVmove.steppgo(mainprogram.MVright, mainprogram.finespeed, StepperSetup.btnSteps)
          elif StepperSetup.MVsteps > StepperSetup.DVrelpos:
              shiftdistance = StepperSetup.MVsteps - StepperSetup.MVrelpos
              for x in range(shiftdistance):
                  self.MVmove.steppgo(mainprogram.MVleft, mainprogram.finespeed, StepperSetup.btnSteps)

          if StepperSetup.APsteps < StepperSetup.APrelpos:
              shiftdistance = StepperSetup.APrelpos- StepperSetup.APsteps
              for x in range(shiftdistance):
                  self.APmove.steppgo(mainprogram.APforward, mainprogram.finespeed, StepperSetup.btnSteps)
          elif StepperSetup.APsteps > StepperSetup.APrelpos:
              shiftdistance = StepperSetup.APsteps - StepperSetup.APrelpos
              for x in range(shiftdistance):
                  self.APmove.steppgo(mainprogram.APback, mainprogram.finespeed, StepperSetup.btnSteps)


        #miscbuttonC - DRILL to relative zero for AP and MV BUT DV homed ABS zero but still sets the relative pos
        if lastbut[2] == 0:
            StepperSetup.APrelpos = StepperSetup.APinitREL_holdvalue
            StepperSetup.MVrelpos = StepperSetup.MVinitREL_holdvalue
            StepperSetup.DVrelpos = StepperSetup.DVinitREL_holdvalue

    #        if StepperSetup.DVsteps < (StepperSetup.DVrelpos + DVDRILL):
    #            shiftdistance = (StepperSetup.DVrelpos + DVDRILL) - StepperSetup.DVsteps
            for x in range(StepperSetup.DVsteps):
    #                DVmove.steppgo(DVdown,finespeed,StepperSetup.btnSteps)
    #        elif StepperSetup.DVsteps > (StepperSetup.DVrelpos + DVDRILL):
    #            shiftdistance = StepperSetup.DVsteps - (StepperSetup.DVrelpos + DVDRILL)
    #            for x in range(shiftdistance):
                self.DVmove.steppgo(mainprogram.DVup, mainprogram.finespeed, StepperSetup.btnSteps)
            if StepperSetup.MVsteps < (StepperSetup.MVrelpos + mainprogram.MVDRILL):
                shiftdistance = (StepperSetup.MVrelpos + mainprogram.MVDRILL) - StepperSetup.MVsteps
                for x in range(shiftdistance):
                    self.MVmove.steppgo(mainprogram.MVright,mainprogram.finespeed,StepperSetup.btnSteps)
            elif StepperSetup.MVsteps > (StepperSetup.DVrelpos + mainprogram.MVDRILL):
                shiftdistance = StepperSetup.MVsteps - (StepperSetup.MVrelpos + mainprogram.MVDRILL)
                for x in range(shiftdistance):
                    self.MVmove.steppgo(mainprogram.MVleft, mainprogram.finespeed, StepperSetup.btnSteps)

            if StepperSetup.APsteps < (StepperSetup.APrelpos + mainprogram.APDRILL):
                shiftdistance = (StepperSetup.APrelpos + mainprogram.APDRILL) - StepperSetup.APsteps
                for x in range(shiftdistance):
                    self.APmove.steppgo(mainprogram.APforward, mainprogram.finespeed, StepperSetup.btnSteps)
            elif StepperSetup.APsteps > (StepperSetup.APrelpos + mainprogram.APDRILL):
                shiftdistance = StepperSetup.APsteps - (StepperSetup.APrelpos + mainprogram.APDRILL)
                for x in range(shiftdistance):
                    self.APmove.steppgo(mainprogram.APback, mainprogram.finespeed, StepperSetup.btnSteps)

            self.sendingtomainA.drilloffset()

        #miscbuttonD - needle to relative zero for AP and MV BUT DV homed ABS zero but still sets the relative pos
        if lastbut[1] == 0:
    #        if StepperSetup.DVsteps < (StepperSetup.DVrelpos + DVneedle):
    #            shiftdistance = (StepperSetup.DVrelpos + DVneedle) - StepperSetup.DVsteps
            for x in range(StepperSetup.DVsteps):
    #            DVmove.steppgo(DVdown,finespeed,StepperSetup.btnSteps)
    #        elif StepperSetup.DVsteps > (StepperSetup.DVrelpos + DVneedle):
    #            shiftdistance = StepperSetup.DVsteps - (StepperSetup.DVrelpos + DVneedle)
    #            for x in range(shiftdistance):
                self.DVmove.steppgo(mainprogram.DVup, mainprogram.finespeed, StepperSetup.btnSteps)
            StepperSetup.DVrelpos = StepperSetup.DVrelpos + mainprogram.DVneedle
            if StepperSetup.MVsteps < (StepperSetup.MVrelpos + mainprogram.MVneedle):
                shiftdistance = (StepperSetup.MVrelpos + mainprogram.MVneedle) - StepperSetup.MVsteps
                for x in range(shiftdistance):
                    self.MVmove.steppgo(mainprogram.MVright, mainprogram.finespeed,StepperSetup.btnSteps)
            elif StepperSetup.MVsteps > (StepperSetup.DVrelpos + mainprogram.MVneedle):
                shiftdistance = StepperSetup.MVsteps - (StepperSetup.MVrelpos + mainprogram.MVneedle)
                for x in range(shiftdistance):
                    self.MVmove.steppgo(mainprogram.MVleft, mainprogram.finespeed, StepperSetup.btnSteps)
            StepperSetup.MVrelpos = StepperSetup.MVsteps + mainprogram.MVneedle

            if StepperSetup.APsteps < (StepperSetup.APrelpos + mainprogram.APneedle):
                shiftdistance = (StepperSetup.APrelpos + mainprogram.APneedle) - StepperSetup.APsteps
                for x in range(shiftdistance):
                    self.APmove.steppgo(mainprogram.APforward, mainprogram.finespeed,StepperSetup.btnSteps)
            elif StepperSetup.APsteps > (StepperSetup.APrelpos + mainprogram.APneedle):
                shiftdistance = StepperSetup.APsteps - (StepperSetup.APrelpos + mainprogram.APneedle)
                for x in range(shiftdistance):
                    self.APmove.steppgo(mainprogram.APback, mainprogram.finespeed, StepperSetup.btnSteps)
            StepperSetup.APrelpos = StepperSetup.APsteps + mainprogram.APneedle

            self.sendingtomainA.needleoffset()

        #miscbuttonE - fiber to relative zero for AP and MV BUT DV homed ABS zero but still sets the relative pos
        if lastbut[10] == 0:
    #        if StepperSetup.DVsteps < (StepperSetup.DVrelpos + DVfiber):
    #            shiftdistance = (StepperSetup.DVrelpos + DVfiber) - StepperSetup.DVsteps
            for x in range(StepperSetup.DVsteps):
    #                DVmove.steppgo(DVdown,finespeed,StepperSetup.btnSteps)
    #        elif StepperSetup.DVsteps > (StepperSetup.DVrelpos + DVfiber):
    #            shiftdistance = StepperSetup.DVsteps - (StepperSetup.DVrelpos + DVfiber)
    #            for x in range(shiftdistance):
                self.DVmove.steppgo(mainprogram.DVup, mainprogram.finespeed, StepperSetup.btnSteps)
            StepperSetup.DVrelpos = StepperSetup.DVsteps + mainprogram.DVfiber
            if StepperSetup.MVsteps < (StepperSetup.MVrelpos + mainprogram.MVfiber):
                shiftdistance = (StepperSetup.MVrelpos + mainprogram.MVfiber) - StepperSetup.MVsteps
                for x in range(shiftdistance):
                    self.MVmove.steppgo(mainprogram.MVright, mainprogram.finespeed, StepperSetup.btnSteps)
            elif StepperSetup.MVsteps > (StepperSetup.DVrelpos + mainprogram.MVfiber):
                shiftdistance = StepperSetup.MVsteps - (StepperSetup.MVrelpos + mainprogram.MVfiber)
                for x in range(shiftdistance):
                    self.MVmove.steppgo(mainprogram.MVleft, mainprogram.finespeed, StepperSetup.btnSteps)
            StepperSetup.MVrelpos = StepperSetup.MVsteps + mainprogram.MVfiber
            if StepperSetup.APsteps < (StepperSetup.APrelpos + mainprogram.APfiber):
                shiftdistance = (StepperSetup.APrelpos + mainprogram.APfiber) - StepperSetup.APsteps
                for x in range(shiftdistance):
                    self.APmove.steppgo(mainprogram.APforward, mainprogram.finespeed, StepperSetup.btnSteps)
            elif StepperSetup.APsteps > (StepperSetup.APrelpos + mainprogram.APfiber):
                shiftdistance = StepperSetup.APsteps - (StepperSetup.APrelpos + mainprogram.APfiber)
                for x in range(shiftdistance):
                    self.APmove.steppgo(mainprogram.APback, mainprogram.finespeed, StepperSetup.btnSteps)
            StepperSetup.APrelpos = StepperSetup.APsteps + mainprogram.APfiber

            self.sendingtomainA.probeoffset()

        #home to bregma (relative) moves DV up ~10mm, positions AP and MV to relative home
        if lastbut[12] == 0:
            if (StepperSetup.DVsteps > 1333):
                for x in range(1333):
                    self.DVmove.steppgo(mainprogram.DVup, mainprogram.finespeed, StepperSetup.btnSteps)
            else:
                for x in range(StepperSetup.DVsteps):
                    self.DVmove.steppgo(mainprogram.DVup, mainprogram.finespeed, StepperSetup.btnSteps)

            if StepperSetup.APrelpos > StepperSetup.APsteps:
                APdiff = StepperSetup.APrelpos - StepperSetup.APsteps
                for x in range(APdiff):
                    self.APmove.steppgo(mainprogram.APforward, mainprogram.finespeed, StepperSetup.btnSteps)
            else:
                APdiff = StepperSetup.APsteps - StepperSetup.APrelpos
                for x in range(APdiff):
                    self.APmove.steppgo(mainprogram.APback, mainprogram.finespeed, StepperSetup.btnSteps)

            if StepperSetup.MVrelpos > StepperSetup.MVsteps:
                MVdiff = StepperSetup.MVrelpos - StepperSetup.MVsteps
                for x in range(MVdiff):
                    self.MVmove.steppgo(mainprogram.MVright, mainprogram.finespeed, StepperSetup.btnSteps)
            else:
                MVdiff = StepperSetup.MVsteps - StepperSetup.MVrelpos
                for x in range(MVdiff):
                    self.MVmove.steppgo(mainprogram.MVleft, mainprogram.finespeed, StepperSetup.btnSteps)

            print("That's bregma G!")

        #re-calibrate button
        if lastbut[5] == 0:

            print("Let us re-calibrate this biz-E-ness")
            for x in range(StepperSetup.DVsteps):
                self.DVmove.steppgo(mainprogram.DVup, mainprogram.finespeed, StepperSetup.btnSteps)
            for x in range(StepperSetup.MVsteps):
                self.MVmove.steppgo(mainprogram.MVleft, mainprogram.finespeed, StepperSetup.btnSteps)
            for x in range(StepperSetup.APsteps):
                self.APmove.steppgo(mainprogram.APback, mainprogram.finespeed, StepperSetup.btnSteps)

            self.APmove.CalibrateDistance(mainprogram.calibrationsteps, mainprogram.backoff, StepperSetup.btnSteps)
            self.MVmove.CalibrateDistance(mainprogram.calibrationsteps, mainprogram.backoff, StepperSetup.btnSteps)
            self.DVmove.CalibrateDistance(mainprogram.calibrationsteps, mainprogram.backoff, StepperSetup.btnSteps)

        #miscbuttonA - unused
        #if lastbut[13] == 0:
        #miscbuttonB - unused
        # if lastbut[14] == 0:

        return lastbut



        # Shuts down steppers regardless of what they were doing direction - restart by re-zeroing
    def emergencystop(self):
        GPIO.output(mainprogram.enableAll, 1)
        print("!EMERGENCY STOP!")
        print("Re-Zero axis to enable movement again")
        # I dont think I need a doubt check on this and sending "event" was giving an error.
        #        if event == RotaryEncoder.BUTTONDOWN:
        #            print("Re-Zero axis to enable movement again")
        #            GPIO.output(mainprogram.enableAll,0)
        #        else:
        #            return
        return

    # Event handling for the encoders and hard wired buttons each encoder
    def AP_event(self, event):

        if event == RotaryEncoder.CLOCKWISE:
            self.APmove.steppgo(mainprogram.APforward, mainprogram.stepper_speed, StepperSetup.btnSteps)
        if event == RotaryEncoder.ANTICLOCKWISE:
            self.APmove.steppgo(mainprogram.APback, mainprogram.stepper_speed, StepperSetup.btnSteps)
        # This is a hard wired button note the encoder switch
        elif event == RotaryEncoder.BUTTONDOWN:
            mainprogram.emergencystop(self)
        elif event == RotaryEncoder.BUTTONUP:
            return
        return

    # Event handling for the encoders and hard wired buttons each encoder
    def MV_event(self, event):
        if event == RotaryEncoder.CLOCKWISE:
            self.MVmove.steppgo(mainprogram.MVright, mainprogram.stepper_speed, StepperSetup.btnSteps)
        elif event == RotaryEncoder.ANTICLOCKWISE:
            self.MVmove.steppgo(mainprogram.MVleft, mainprogram.stepper_speed, StepperSetup.btnSteps)
        elif event == RotaryEncoder.BUTTONDOWN:
            print("event button A clicked")
            return
        elif event == RotaryEncoder.BUTTONUP:
            return
        return

    # Event handling for the encoders and hard wired buttons each encoder
    def DV_event(self, event):

        if event == RotaryEncoder.CLOCKWISE:
            self.DVmove.steppgo(mainprogram.DVdown, mainprogram.stepper_speed, StepperSetup.btnSteps)
        elif event == RotaryEncoder.ANTICLOCKWISE:
            self.DVmove.steppgo(mainprogram.DVup, mainprogram.stepper_speed, StepperSetup.btnSteps)
        elif event == RotaryEncoder.BUTTONDOWN:
            print("event button B clicked")
            return
        elif event == RotaryEncoder.BUTTONUP:
            return
        return

    def get_user_input(self,giventitle,givenprompt):
        # Create the root window
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        # Prompt the user for input
        user_input = simpledialog.askstring(title=giventitle, prompt=givenprompt)

        # Print the user input
        if user_input is not None:
            print(f"User input: {user_input}")
            return user_input

        else:
            print("No input provided")

        # Destroy the root window
        root.destroy()

    #MAIN CODE ################################################################################################
    def intializethesystem_andrun(self):
        #print('shits on fire yo')
        #this gets used when initializing the encoders so the encoder can send the resutls back to this class
        self.incomefromencoder = mainprogram()
#        RotaryEncoder.receive_instance(self.incomefromencoder)

        #INITIALIZE STEPPERS

        self.APmove = StepperSetup(mainprogram.enableAll,mainprogram.stepAP,mainprogram.directionAP,mainprogram.limitAP,1,mainprogram.APback,mainprogram.APforward, self.sendingtomainA)
        self.MVmove = StepperSetup(mainprogram.enableAll,mainprogram.stepMV,mainprogram.directionMV,mainprogram.limitMV,2,mainprogram.MVright,mainprogram.MVleft, self.sendingtomainA)
        self.DVmove = StepperSetup(mainprogram.enableAll,mainprogram.stepDV,mainprogram.directionDV,mainprogram.limitDV,3,mainprogram.DVup,mainprogram.DVdown, self.sendingtomainA)
        #print('steppers are a go')
        #send to motorcontrol
        self.APmove.receive_instance(self.APmove)
        self.MVmove.receive_instance(self.MVmove)
        self.DVmove.receive_instance(self.DVmove)
        #print('send the instance to the motorcontrol class')

    # INITIALIZE ENCODERS
        self.AProto = RotaryEncoder(mainprogram.rotoA_AP, mainprogram.rotoB_AP, mainprogram.emergstop, self.incomefromencoder.MV_event)
        self.MVroto = RotaryEncoder(mainprogram.rotoA_MV, mainprogram.rotoB_MV, mainprogram.misc_eventbuttonA, self.incomefromencoder.MV_event)
        self.DVroto = RotaryEncoder(mainprogram.rotoA_DV, mainprogram.rotoB_DV, mainprogram.misc_eventbuttonB, self.incomefromencoder.DV_event)
        #print('if shits got this far YAY! and the encoders are started...maybe')

    #question and waits for ANY user input

    #    self.quest = input("Initialization Process ... ENTER to continue.")
    #    self.quest = input("CAUTION...Remove all attachments from frame arms! ENTER to continue.")
        self.quest = self.get_user_input('MESSAGE:','Initialization Process ... ENTER to continue')
        self.quest = self.get_user_input('MESSAGE:','CAUTION...Remove all attachments from frame arms! ENTER to continue.')


    #Zero steppers
        #print('calling zero function')
        self.DVmove.zerostep(mainprogram.backoff, StepperSetup.btnSteps)
        self.APmove.zerostep(mainprogram.backoff, StepperSetup.btnSteps)
        self.MVmove.zerostep(mainprogram.backoff, StepperSetup.btnSteps)

    #calibration routine
        #print('calling the calibration routine')
        self.APmove.CalibrateDistance(mainprogram.calibrationsteps, mainprogram.backoff, StepperSetup.btnSteps)
        self.MVmove.CalibrateDistance(mainprogram.calibrationsteps, mainprogram.backoff, StepperSetup.btnSteps)
        self.DVmove.CalibrateDistance(mainprogram.calibrationsteps, mainprogram.backoff, StepperSetup.btnSteps)

        while mainprogram.keepalive:

        #reading the buttons
            newbuttonstate = self.getshiftregisterdata()
            mainprogram.lastbuttonstate = self.buttonvalues(mainprogram.lastbuttonstate,newbuttonstate,mainprogram.buttonarray)


