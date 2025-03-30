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
    #NOT USED because the risk of accidental pushes too high
        #rotoclick_AP = 8
        #rotoclick_MV = 9
        #rotoclick_DV = 10

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

        for i in range(x):
            if lastbut[i] != newbut[i]:
                lastbut[i] = newbut[i]
                print("button ", butarr[i], " state change")

        # stepper_speed (pos 0 and pos 1)
        for u in range(x):
            if lastbut[u] == 0:
                print('Button pressed: ', u)


        return lastbut

    def receive_frommainA(self, comingfrommainA):
        self.sendingtomainA = comingfrommainA

    #MAIN CODE ################################################################################################
    def intializethesystem_andrun(self):
        while mainprogram.keepalive:

        #reading the buttons
            newbuttonstate = self.getshiftregisterdata()
            print(newbuttonstate)
 #           mainprogram.lastbuttonstate = self.buttonvalues(mainprogram.lastbuttonstate,newbuttonstate,mainprogram.buttonarray)

letsgo = mainprogram()
letsgo.intializethesystem_andrun()
