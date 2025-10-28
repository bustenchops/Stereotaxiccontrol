import time
import RPi.GPIO as GPIO
from rotary_classv2 import RotaryEncoder

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

    directionML = 17
    stepML = 27

    directionDV = 5
    stepDV = 6

    #DEFINE LIMIT SWITCH PINS
    limitAP = 22
    limitML = 13
    limitDV = 19

    #OFFSETS FOR THE DRILL, Syringe, Needle (minus values is back, left or up)
    APDRILL = 0
    MLDRILL = 0
    DVDRILL = -1333

    APfiber = 0
    MLfiber = 0
    DVfiber = 0

    APneedle = 0
    MLneedle = 0
    DVneedle = 0
    #DEFINE EMERGENCY STOP and hard wired buttons
    emergstop = 11
    misc_eventbuttonA = 10
    misc_eventbuttonB = 26


    #DEFINE ROTARY ENCODER PINS
    rotoA_AP = 25
    rotoB_AP =  8
    rotoA_ML = 12
    rotoB_ML = 16
    rotoA_DV = 20
    rotoB_DV = 21

    #DEFINE STEPPER DIRECTIONS
    APback = 1
    APforward = 0
    MLleft = 0
    MLright = 1
    DVup = 0
    DVdown = 1



    def __init__(self):
        #INITIALIZE PINS

        print('initialize hardwired buttons')
        GPIO.setup(mainprogram.emergstop, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(mainprogram.misc_eventbuttonA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(mainprogram.misc_eventbuttonB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print('done')

        self.quest = "none"

        # INITIALIZE ENCODERS
 #       self.AProto = RotaryEncoder(buttonprogram.rotoA_AP, buttonprogram.rotoB_AP, buttonprogram.emergstop, Letsgonow.AP_event)
 #       self.MLroto = RotaryEncoder(buttonprogram.rotoA_ML, buttonprogram.rotoB_ML, buttonprogram.misc_eventbuttonA, Letsgonow.ML_event)
 #       self.DVroto = RotaryEncoder(buttonprogram.rotoA_DV, buttonprogram.rotoB_DV, buttonprogram.misc_eventbuttonB, Letsgonow.DV_event)


        #INITIALIZE STEPPERS

        print('setup AP stepper')
        GPIO.setup(mainprogram.enableAll, GPIO.OUT, initial=1)
        GPIO.setup(mainprogram.stepAP, GPIO.OUT, initial=0)
        GPIO.setup(mainprogram.directionAP, GPIO.OUT, initial=0)
        GPIO.setup(mainprogram.limitAP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print('done')

        print('setup ML stepper')
        GPIO.setup(mainprogram.stepML, GPIO.OUT, initial=0)
        GPIO.setup(mainprogram.directionML, GPIO.OUT, initial=0)
        GPIO.setup(mainprogram.limitML, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print('done')

        print('setup DV stepper')
        GPIO.setup(mainprogram.stepDV, GPIO.OUT, initial=0)
        GPIO.setup(mainprogram.directionDV, GPIO.OUT, initial=0)
        GPIO.setup(mainprogram.limitDV, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print('done')



    #Shuts down steppers regardless of what they were doing - restart by re-zeroing
    def emergencystop(self):
        GPIO.output(mainprogram.enableAll, 1)
        print("!EMERGENCY STOP!")
        print("Re-Zero axis to enable movement again")
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
    def ML_event(self, event):
        if event == RotaryEncoder.CLOCKWISE:
            print('ML clockwise')
        elif event == RotaryEncoder.ANTICLOCKWISE:
            print('ML counterclock')
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
        stateML = GPIO.input(mainprogram.limitML)
        stateDV = GPIO.input(mainprogram.limitDV)

        while GPIO.input(mainprogram.limitAP) == 1 or GPIO.input(mainprogram.limitML) == 1:
            newAP = GPIO.input(mainprogram.limitAP)
            newML = GPIO.input(mainprogram.limitML)
            newDV = GPIO.input(mainprogram.limitDV)

            if newAP != stateAP:
                if GPIO.input(mainprogram.limitAP) == 0:
                    print('AP limit reached:', GPIO.input(mainprogram.limitAP))
                if GPIO.input(mainprogram.limitAP) == 1:
                    print('AP limit reached:', GPIO.input(mainprogram.limitAP))
                stateAP = newAP

            if newML != stateML:
                if GPIO.input(mainprogram.limitML) == 0:
                    print('ML limit reached', GPIO.input(mainprogram.limitML))
                if GPIO.input(mainprogram.limitML) == 1:
                    print('ML limit reached', GPIO.input(mainprogram.limitML))
                stateML = newML

            if newDV != stateDV:
                if GPIO.input(mainprogram.limitDV) == 0:
                    print('DV limit reached', GPIO.input(mainprogram.limitDV))
                if GPIO.input(mainprogram.limitDV) == 1:
                    print('DV limit reached', GPIO.input(mainprogram.limitDV))
                stateDV = newDV

        quest = input('Test the AP stepper 400 steps using direction forward')
        print('direction set to', mainprogram.APforward)
        count = 1
        GPIO.output(mainprogram.enableAll, 0)
#        GPIO.output(buttonprogram.directionAP, buttonprogram.APforward)

        while count <= 400:
            print("start")
            if GPIO.input(mainprogram.limitAP) == 1:
                GPIO.output(mainprogram.directionAP, mainprogram.APforward)
                GPIO.output(mainprogram.stepAP, 1)
                time.sleep(0.001)
                GPIO.output(mainprogram.stepAP, 0)
                time.sleep(0.001)
                print('step', count)
                count += 1

        quest = input('Test the AP stepper 400 steps using direction back')
        print('direction set to', mainprogram.APback)
        count = 1
        GPIO.output(mainprogram.enableAll, 0)


        while count <= 400:
            if GPIO.input(mainprogram.limitAP) == 1:
                GPIO.output(mainprogram.directionAP, mainprogram.APback)
                GPIO.output(mainprogram.stepAP, 1)
                time.sleep(0.001)
                GPIO.output(mainprogram.stepAP, 0)
                time.sleep(0.001)
                print('step', count)
                count += 1

        quest = input('Test the ML stepper 400 steps using direction left')
        print('direction set to', mainprogram.MLleft)
        count = 1
        GPIO.output(mainprogram.enableAll, 0)
        GPIO.output(mainprogram.directionML, mainprogram.MLleft)

        while count <= 400:
            print("start")
            if GPIO.input(mainprogram.limitML) == 1:
                GPIO.output(mainprogram.stepML, 1)
                time.sleep(0.001)
                GPIO.output(mainprogram.stepML, 0)
                time.sleep(0.001)
                print('step', count)
                count += 1

        quest = input('Test the ML stepper 400 steps using direction right')
        print('direction set to', mainprogram.MLright)
        count = 1
        GPIO.output(mainprogram.enableAll, 0)
        GPIO.output(mainprogram.directionML, mainprogram.MLright)

        while count <= 400:
            if GPIO.input(mainprogram.limitML) == 1:
                GPIO.output(mainprogram.stepML, 1)
                time.sleep(0.001)
                GPIO.output(mainprogram.stepML, 0)
                time.sleep(0.001)
                print('step', count)
                count += 1

        quest = input('Test the ML stepper 400 steps using direction up')
        print('direction set to', mainprogram.DVup)
        count = 1
        GPIO.output(mainprogram.enableAll, 0)
        GPIO.output(mainprogram.directionDV, mainprogram.DVup)

        while count <= 400:
            print("start")
            if GPIO.input(mainprogram.limitDV) == 1:
                GPIO.output(mainprogram.stepDV, 1)
                time.sleep(0.001)
                GPIO.output(mainprogram.stepDV, 0)
                time.sleep(0.001)
                print('step', count)
                count += 1

        quest = input('Test the DV stepper 400 steps using direction down')
        print('direction set to', mainprogram.DVdown)
        count = 1
        GPIO.output(mainprogram.enableAll, 0)
        GPIO.output(mainprogram.directionDV, mainprogram.DVdown)

        while count <= 400:
            if GPIO.input(mainprogram.limitDV) == 1:
                GPIO.output(mainprogram.stepDV, 1)
                time.sleep(0.001)
                GPIO.output(mainprogram.stepDV, 0)
                time.sleep(0.001)
                print('step', count)
                count += 1

    def encoderinit(self):
        print('initialize encoders')
        self.AProto = RotaryEncoder(mainprogram.rotoA_AP, mainprogram.rotoB_AP, mainprogram.emergstop,Letsgonow.AP_event)
        self.MLroto = RotaryEncoder(mainprogram.rotoA_ML, mainprogram.rotoB_ML, mainprogram.misc_eventbuttonA,Letsgonow.ML_event)
        self.DVroto = RotaryEncoder(mainprogram.rotoA_DV, mainprogram.rotoB_DV, mainprogram.misc_eventbuttonB,Letsgonow.DV_event)
        print('done')


Letsgonow = mainprogram()
#  RotaryEncoder.receive_instance(Letsgonow)
Letsgonow.encoderinit()
Letsgonow.executerrrr()

