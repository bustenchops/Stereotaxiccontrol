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
    movefast = 6
    bregmahome = 14
    relativeML = 11
    relativeAP = 9
    moveslow = 7
    homeABSzero = 8 #fullretract
    recalibrate = 10
    miscbuttonA =  1# speciesselect
    miscbuttonB =  3 # gotoworking preset
    fiberoff = 4
    needleoff = 15
    drilloff = 5
    relativeDV = 0
    relativeALL = 13
    homeRELzero = 12 #gotolambda
    miscbuttonC = 2 #unassigned


    # setup GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)


    #DEFINE EMERGENCY STOP and hard wired buttons
    emergstop = 10
    misc_eventbuttonA = 26
    misc_eventbuttonB = 11

    #DEFINE SHIFT REGISTER PINS
    latchpin = 18
    clockpin = 23
    datapin = 24


    def __init__(self):
        #INITIALIZE PINS
        GPIO.setup(mainprogram.latchpin,GPIO.OUT)
        GPIO.setup(mainprogram.clockpin,GPIO.OUT)
        GPIO.setup(mainprogram.datapin,GPIO.IN)

        GPIO.setup(mainprogram.emergstop, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(mainprogram.misc_eventbuttonA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(mainprogram.misc_eventbuttonB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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


