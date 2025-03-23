import time
import RPi.GPIO as GPIO
from rotary_class import RotaryEncoder

class mainprogram:
    #Main while loop condition
    keepalive = True

    #Variables that may need tweaking
    calibrationsteps = 4000
    backoff = 150


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
    #DEFINE EMERGENCY STOP and hard wired buttons
    emergstop = 26
    misc_eventbuttonA = 10
    misc_eventbuttonB = 11


    #DEFINE ROTARY ENCODER PINS
    rotoA_AP = 25
    rotoB_AP =  8
    rotoA_MV = 12
    rotoB_MV = 16
    rotoA_DV = 20
    rotoB_DV = 21

    #DEFINE STEPPER DIRECTIONS
    APback = 0
    APforward = 1
    MVleft = 0
    MVright = 1
    DVup = 0
    DVdown = 1



    def __init__(self):
        #INITIALIZE PINS

        GPIO.setup(mainprogram.emergstop, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(mainprogram.misc_eventbuttonA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(mainprogram.misc_eventbuttonB, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        #EMPTY variables to initialize
        self.shiftvalues = []
        self.quest = "none"

        # INITIALIZE ENCODERS
        self.AProto = RotaryEncoder(mainprogram.rotoA_AP, mainprogram.rotoB_AP, mainprogram.emergstop, mainprogram.AP_event)
        self.MVroto = RotaryEncoder(mainprogram.rotoA_MV, mainprogram.rotoB_MV, mainprogram.misc_eventbuttonA, mainprogram.MV_event)
        self.DVroto = RotaryEncoder(mainprogram.rotoA_DV, mainprogram.rotoB_DV, mainprogram.misc_eventbuttonB, mainprogram.DV_event)


        #INITIALIZE STEPPERS


        GPIO.setup(mainprogram.enableAll, GPIO.OUT, initial=1)
        GPIO.setup(mainprogram.stepAP, GPIO.OUT, initial=0)
        GPIO.setup(mainprogram.directionAP, GPIO.OUT, initial=0)
        GPIO.setup(mainprogram.limitAP, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.setup(mainprogram.stepMV, GPIO.OUT, initial=0)
        GPIO.setup(mainprogram.directionMV, GPIO.OUT, initial=0)
        GPIO.setup(mainprogram.limitMV, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.setup(mainprogram.stepDV, GPIO.OUT, initial=0)
        GPIO.setup(mainprogram.directionDV, GPIO.OUT, initial=0)
        GPIO.setup(mainprogram.limitDV, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Import the offsets
        self.offsetimport = []
        self.importfile_name = 'offsets.txt'

        file = open(self.importfile_name, 'r')
        r = 0
        while True:
            line = file.readline()
            if not line:
                break
            self.offsetimport[r] = line.strip()
            r += 1
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

        print('offset values')
        print(mainprogram.APDRILL)
        print(mainprogram.MVDRILL)
        print(mainprogram.DVDRILL)
        print(mainprogram.APneedle)
        print(mainprogram.MVneedle)
        print(mainprogram.MVneedle)
        print(mainprogram.APfiber)
        print(mainprogram.MVfiber)
        print(mainprogram.DVfiber)



    #Shuts down steppers regardless of what they were doing direction - restart by re-zeroing
    def emergencystop(self):
        GPIO.output(mainprogram.enableAll, 0)
        print("!EMERGENCY STOP!")
        print("Re-Zero axis to enable movement again")
# I dont think I need a doubt check on this and sending "event" was giving an error.
#        if event == RotaryEncoder.BUTTONDOWN:
#            print("Re-Zero axis to enable movement again")
#            GPIO.output(mainprogram.enableAll,0)
#        else:
#            return
        return


    #Event handling for the encoders and hard wired buttons each encoder
    def AP_event(self,event):

        if event == RotaryEncoder.CLOCKWISE:
            print('AP clockwise')
        elif event == RotaryEncoder.ANTICLOCKWISE:
            print('AP counterclock')
        #This is a hard wired button note the encoder switch
        elif event == RotaryEncoder.BUTTONDOWN:
            mainprogram.emergencystop(self)
        elif event == RotaryEncoder.BUTTONUP:
            return
        return


    #Event handling for the encoders and hard wired buttons each encoder
    def MV_event(self, event):

        if event == RotaryEncoder.CLOCKWISE:
            print('MV clockwise')
        elif event == RotaryEncoder.ANTICLOCKWISE:
            print('MV counterclock')
        elif event == RotaryEncoder.BUTTONDOWN:
            print("event 1st misc buttonclicked")
            return
        elif event == RotaryEncoder.BUTTONUP:
            return
        return


    #Event handling for the encoders and hard wired buttons each encoder
    def DV_event(self, event):

        if event == RotaryEncoder.CLOCKWISE:
            print('DV clockwise')
        elif event == RotaryEncoder.ANTICLOCKWISE:
            print('DV counterclock')
        elif event == RotaryEncoder.BUTTONDOWN:
            print("event 2nd misc buttonclicked")
            return
        elif event == RotaryEncoder.BUTTONUP:
            return
        return

    def executerrrr(self):
    quest=input('TEST limitswitches - any key to cont')
    while GPIO.input(limitAP) == 1 or GPIO.input(limitMV) == 1:
        if GPIO.input(limitAP == 0):
            print('AP limit reached')
        if GPIO.input(limitMV == 0):
            print('MV limit reached')
        if GPIO.input(limitDV == 0):
            print('DV limit reached')

    quest = input('Test the AP stepper 1500 steps using direction forward')
    print('direction set to 1')
    count = 1
    while GPIO.input(limitAP) == 1:
        if count >= 1500:
            GPIO.output(enableAll, 1)
            GPIO.output(directionAP, APforward)
            GPIO.output(stepAP, 1)
            time.sleep(0.001)
            GPIO.output(stepAP, 0)

    quest = input('Test the AP stepper 1500 steps using direction back')
    print('direction set to 0')
    count = 1
    while GPIO.input(limitAP) == 1:
        if count >= 1500:
            GPIO.output(enableAll, 1)
            GPIO.output(directionAP, APback)
            GPIO.output(stepAP, 1)
            time.sleep(0.001)
            GPIO.output(stepAP, 0)

    quest = input('Test the MV stepper 1500 steps using direction right')
    print('direction set to 1')
    count = 1
    while GPIO.input(limitMV) == 1:
        if count >= 1500:
            GPIO.output(enableAll, 1)
            GPIO.output(directionMV, MVright)
            GPIO.output(stepMV, 1)
            time.sleep(0.001)
            GPIO.output(stepMV, 0)

    quest = input('Test the MV stepper 1500 steps using direction left')
    print('direction set to 0')
    count = 1
    while GPIO.input(limitMV) == 1:
        if count >= 1500:
            GPIO.output(enableAll, 1)
            GPIO.output(directionMV, MVleft)
            GPIO.output(stepMV, 1)
            time.sleep(0.001)
            GPIO.output(stepMV, 0)

    quest = input('Test the DV stepper 1500 steps using direction down')
    print('direction set to 1')
    count = 1
    while GPIO.input(limitDV) == 1:
        if count >= 1500:
            GPIO.output(enableAll, 1)
            GPIO.output(directionDV, DVdown)
            GPIO.output(stepDV, 1)
            time.sleep(0.001)
            GPIO.output(stepDV, 0)

    quest = input('Test the DV stepper 1500 steps using direction up')
    print('direction set to 0')
    count = 1
    while GPIO.input(limitDV) == 1:
        if count >= 1500:
            GPIO.output(enableAll, 1)
            GPIO.output(directionDV, DVup)
            GPIO.output(stepDV, 1)
            time.sleep(0.001)
            GPIO.output(stepDV, 0)

#this is the executer
Letsgonow = mainprogram()
Letsgonow.executerrrr()

