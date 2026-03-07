import time
import RPi.GPIO as GPIO

class mainprogram:
    #Main while loop condition
    keepalive = True

    #DEFINE NUMBER OF BUTTONS AND ORDER IN ARRAY
    buttonarray = ['moveslow', 'movefast', 'offposone', 'offpostwo', 'rezero',
                   'relativeAP', 'relativeML', 'relativeDV', 'relativeALLset', 'fullretract',
                   'bregmahome', 'bregmahomeDVabs', 'bregmahomeDVupfive', 'gotolambdabut', 'ratselect',
                   'mouseselect', 'gotopreset', 'selectup', 'selectdown', 'armbut',
                   'engagebut', 'makeitsobut', 'withdrawl', 'DVinsert', 'retractAP',
                   'returnAP', 'retactDV', 'returnDV', 'functionone', 'functiontwo',
                   'ABSzero', 'unassigned']
    lastbuttonstate = [len(buttonarray)]

    #BUTTON POSITION IN SHIFT REGISTER ARRAY
        # 2 position switch (3 states 1/2 and all off)
    moveslow = 0
    movefast = 4
    offposone = 2
    offpostwo = 10
    rezero = 5

    relativeAP = 7
    relativeML = 11
    relativeDV = 12
    relativeALL = 9
    fullretract = 3

    bregmahome = 6
    bregmahomeDVabs = 8
    bregmahomeDVupfive = 1
    gotolambdabut = 1
    ratselect = 13

    mouseselect = 1
    gotopreset = 14
    selectup = 1
    selectdown = 1
    armbut = 1

    engagebut = 1
    makeitsobut = 1
    withdrawl = 1
    DVinsert = 1
    retractAP = 1

    returnAP = 1
    retractDV = 1
    returnDV = 1
    functionone = 1
    functiontwo = 1

    ABSzero = 1


    # setup GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)


    #DEFINE EMERGENCY STOP and hard wired buttons
    emergstop = 26
    safetybut = 10
    disablestepperbut = 11
    fourthhardwarebutton = 9 #encoder 4 depress?

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


