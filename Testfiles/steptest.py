import time
import RPi.GPIO as GPIO


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

        self.quest = "none"


        #INITIALIZE STEPPERS


        GPIO.setup(mainprogram.enableAll, GPIO.OUT, initial=1)
        GPIO.setup(mainprogram.stepAP, GPIO.OUT, initial=0)
        GPIO.setup(mainprogram.directionAP, GPIO.OUT, initial=1)
        GPIO.setup(mainprogram.limitAP, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.setup(mainprogram.enableAll, GPIO.OUT, initial=1)
        GPIO.setup(mainprogram.stepMV, GPIO.OUT, initial=0)
        GPIO.setup(mainprogram.directionMV, GPIO.OUT, initial=1)
        GPIO.setup(mainprogram.limitMV, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.setup(mainprogram.enableAll, GPIO.OUT, initial=1)
        GPIO.setup(mainprogram.stepDV, GPIO.OUT, initial=0)
        GPIO.setup(mainprogram.directionDV, GPIO.OUT, initial=1)
        GPIO.setup(mainprogram.limitDV, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def executerrrr(self):

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

