import time
import RPi.GPIO as GPIO


from RightHand.RotatryEncoderv1 import RotaryEncoder

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

        print('what the fuck')
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
        print(mainprogram.limitAP)
        testss = GPIO.input(mainprogram.limitAP)
        print(testss)

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
        GPIO.output(mainprogram.enableAll, 1)
        print("!EMERGENCY STOP!")
        print("Re-Zero axis to enable movement again")
# I dont think I need a doubt check on this and sending "event" was giving an error.
#        if event == RotaryEncoder.BUTTONDOWN:
#            print("Re-Zero axis to enable movement again")
#            GPIO.output(buttonprogram.enableAll,0)
#        else:
#            return
        return


    #Event handling for the encoders and hard wired buttons each encoder
    def AP_event(self, event):

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
        stateAP = GPIO.input(mainprogram.limitAP)
        stateMV = GPIO.input(mainprogram.limitMV)
        stateDV = GPIO.input(mainprogram.limitDV)

        while GPIO.input(mainprogram.limitAP) == 1 or GPIO.input(mainprogram.limitMV) == 1:
            newAP = GPIO.input(mainprogram.limitAP)
            newMV = GPIO.input(mainprogram.limitMV)
            newDV = GPIO.input(mainprogram.limitDV)

            if newAP != stateAP:
                if GPIO.input(mainprogram.limitAP) == 0:
                    print('AP limit reached:', GPIO.input(mainprogram.limitAP))
                if GPIO.input(mainprogram.limitAP) == 1:
                    print('AP limit reached:', GPIO.input(mainprogram.limitAP))
                stateAP = newAP

            if newMV != stateMV:
                if GPIO.input(mainprogram.limitMV) == 0:
                    print('MV limit reached', GPIO.input(mainprogram.limitMV))
                if GPIO.input(mainprogram.limitMV) == 1:
                    print('MV limit reached', GPIO.input(mainprogram.limitMV))

                stateMV = newMV

            if newDV != stateDV:
                if GPIO.input(mainprogram.limitDV) == 0:
                    print('DV limit reached', GPIO.input(mainprogram.limitDV))
                if GPIO.input(mainprogram.limitDV) == 1:
                    print('DV limit reached', GPIO.input(mainprogram.limitDV))
                stateDV = newDV

        quest = input('Test the AP stepper 1500 steps using direction forward')
        print('direction set to 1')
        count = 1
        GPIO.output(mainprogram.enableAll, 0)
        GPIO.output(mainprogram.directionAP, mainprogram.APforward)

        while count <= 1500:
            print("start")
            if GPIO.input(mainprogram.limitAP) == 1:
                GPIO.output(mainprogram.stepAP, 1)
                time.sleep(0.001)
                GPIO.output(mainprogram.stepAP, 0)
                time.sleep(0.001)
                print('step', count)
                count += 1

        quest = input('Test the AP stepper 1500 steps using direction back')
        print('direction set to 0')
        count = 1
        GPIO.output(mainprogram.enableAll, 0)
        GPIO.output(mainprogram.directionAP, mainprogram.APback)

        while count <= 1500:
            if GPIO.input(mainprogram.limitAP) == 1:
                GPIO.output(mainprogram.stepAP, 1)
                time.sleep(0.001)
                GPIO.output(mainprogram.stepAP, 0)
                time.sleep(0.001)
                print('step', count)
                count += 1

        quest = input('Test the MV stepper 1500 steps using direction forward')
        print('direction set to 1')
        count = 1
        GPIO.output(mainprogram.enableAll, 0)
        GPIO.output(mainprogram.directionMV, mainprogram.MVleft)

        while count <= 1500:
            print("start")
            if GPIO.input(mainprogram.limitMV) == 1:
                GPIO.output(mainprogram.stepMV, 1)
                time.sleep(0.001)
                GPIO.output(mainprogram.stepMV, 0)
                time.sleep(0.001)
                print('step', count)
                count += 1

        quest = input('Test the MV stepper 1500 steps using direction back')
        print('direction set to 0')
        count = 1
        GPIO.output(mainprogram.enableAll, 0)
        GPIO.output(mainprogram.directionMV, mainprogram.MVright)

        while count <= 1500:
            if GPIO.input(mainprogram.limitMV) == 1:
                GPIO.output(mainprogram.stepMV, 1)
                time.sleep(0.001)
                GPIO.output(mainprogram.stepMV, 0)
                time.sleep(0.001)
                print('step', count)
                count += 1

        quest = input('Test the MV stepper 1500 steps using direction forward')
        print('direction set to 1')
        count = 1
        GPIO.output(mainprogram.enableAll, 0)
        GPIO.output(mainprogram.directionDV, mainprogram.DVup)

        while count <= 1500:
            print("start")
            if GPIO.input(mainprogram.limitDV) == 1:
                GPIO.output(mainprogram.stepDV, 1)
                time.sleep(0.001)
                GPIO.output(mainprogram.stepDV, 0)
                time.sleep(0.001)
                print('step', count)
                count += 1

        quest = input('Test the DV stepper 1500 steps using direction back')
        print('direction set to 0')
        count = 1
        GPIO.output(mainprogram.enableAll, 0)
        GPIO.output(mainprogram.directionDV, mainprogram.DVdown)

        while count <= 1500:
            if GPIO.input(mainprogram.limitDV) == 1:
                GPIO.output(mainprogram.stepDV, 1)
                time.sleep(0.001)
                GPIO.output(mainprogram.stepDV, 0)
                time.sleep(0.001)
                print('step', count)
                count += 1

#this is the executer
Letsgonow = mainprogram()
Letsgonow.executerrrr()

