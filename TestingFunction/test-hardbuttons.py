import time
import RPi.GPIO as GPIO

class mainprogram:
    #Main while loop condition
    keepalive = True

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


    # setup GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)


    #DEFINE EMERGENCY STOP and hard wired buttons
    emergstop = 11
    misc_eventbuttonA = 10
    misc_eventbuttonB = 26

    #DEFINE SHIFT REGISTER PINS
    latchpin = 18
    clockpin = 23
    datapin = 24


    def __init__(self):
        #INITIALIZE PINS
        GPIO.setup(mainprogram.latchpin,GPIO.OUT)
        GPIO.setup(mainprogram.clockpin,GPIO.OUT)
        GPIO.setup(mainprogram.datapin,GPIO.IN)

        GPIO.setup(mainprogram.emergstop, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(mainprogram.misc_eventbuttonA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(mainprogram.misc_eventbuttonB, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        #EMPTY variables to initialize
        self.quest = "none"




    #MAIN CODE ################################################################################################
    def intializethesystem_andrun(self):
        while mainprogram.keepalive:
            emerginput = str(GPIO.input(mainprogram.emergstop))
            hardA = str(GPIO.input(mainprogram.misc_eventbuttonA))
            hardB = str(GPIO.input(mainprogram.misc_eventbuttonB))

            print('emerg=' + emerginput + '  hardA=' + hardA + '  hardB=' + hardB)


letsgo = mainprogram()
letsgo.intializethesystem_andrun()


