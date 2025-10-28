import time
import RPi.GPIO as GPIO

class mainprogram:
    #Main while loop condition
    keepalive = True

    # DEFINE NUMBER OF BUTTONS AND ORDER IN ARRAY
    buttonarray = ['movefast', 'bregmahome', 'relativeML', 'relativeAP', 'moveslow', 'HomeToABSzero', 'recalibrate',
                   'miscbuttonA', 'miscbuttonB', 'FiberOffset', 'needleoffset', 'drilloffset',
                   'relativeALLset', 'HomerelativeZero'
                   ]
    lastbuttonstate = [0 for x in range(len(buttonarray))]

    # BUTTON POSITION IN SHIFT REGISTER ARRAY
    movefast = 1
    bregmahome = 2
    relativeML = 3
    relativeAP = 4
    moveslow = 5
    homeABSzero = 6
    recalibrate = 7
    miscbuttonA = 8
    miscbuttonB = 9
    fiberoff = 10
    needleoff = 11
    drilloff = 12
    relativeDV = 13
    relativeALL = 14
    homeRELzero = 15


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

        GPIO.setup(mainprogram.emergstop, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(mainprogram.misc_eventbuttonA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(mainprogram.misc_eventbuttonB, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        #EMPTY variables to initialize
        self.quest = "none"


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

    #MAIN CODE ################################################################################################
    def intializethesystem_andrun(self):
        while mainprogram.keepalive:

        #reading the buttons
            newbuttonstate = self.getshiftregisterdata()
            print(newbuttonstate)
            for x in newbuttonstate:
                if x == 1:
                    buttonitis = mainprogram.buttonarray[x]
                    print('button for '+buttonitis+' is pressed')



letsgo = mainprogram()
letsgo.intializethesystem_andrun()
