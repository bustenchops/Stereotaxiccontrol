import time
import RPi.GPIO as GPIO

class mainprogram:
    #Main while loop condition
    keepalive = True

    # DEFINE NUMBER OF BUTTONS AND ORDER IN ARRAY
    buttonarray = ['movefast', 'bregmahome', 'relativeML', 'relativeAP', 'moveslow',
                   'HomeToABSzero', 'recalibrate', 'miscbuttonA', 'presetworking', 'FiberOffset',
                   'needleoffset', 'drilloffset', 'relactiveDV', 'relativeALLset', 'HomerelativeZero',
                   'miscbuttonC'
                   ]
    lastbuttonstate = [0 for x in range(len(buttonarray))]

    # BUTTON POSITION IN SHIFT REGISTER ARRAY
    movefast = 6
    bregmahome = 14
    relativeML = 11
    relativeAP = 9
    moveslow = 7
    homeABSzero =
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
    emergstop = 26
    misc_eventbuttonA = 10
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


    def getshiftregisterdata(self):
        self.shiftvalues = []
        #get number of buttons
        x = len(mainprogram.buttonarray)
        print("button array length=", x)
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
            # time.sleep(0.001)
            time.sleep(0.001)
        return self.shiftvalues

    #MAIN CODE ################################################################################################
    def intializethesystem_andrun(self):
        while mainprogram.keepalive:

        #reading the buttons
            newbuttonstate = self.getshiftregisterdata()
            print(newbuttonstate)



letsgo = mainprogram()
letsgo.intializethesystem_andrun()
