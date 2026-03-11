import time
import RPi.GPIO as GPIO

class mainprogram:
    # Main while loop condition
    keepalive = True

    # DEFINE NUMBER OF BUTTONS AND ORDER IN ARRAY

    # setup GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # DEFINE EMERGENCY STOP and hard wired buttons
    testA = 26
    testB = 10
    testC = 11
    testD = 7


    def __init__(self):
        # INITIALIZE PINS
        GPIO.setup(mainprogram.testA, GPIO.IN)
        GPIO.setup(mainprogram.testB, GPIO.IN)
        GPIO.setup(mainprogram.testC, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(mainprogram.testD, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # MAIN CODE ################################################################################################
    def intializethesystem_andrun(self):
        while mainprogram.keepalive:
            # reading the buttons
            Aresult = GPIO.input(testA)
            Bresult = GPIO.input(testB)
            Cresult = GPIO.input(testC)
            Dresult = GPIO.input(testD)

            print ('pin ', testA, ' is', Aresult, 'just wired')
            print('pin ', testB, ' is', Bresult, 'just wired through trigger')
            print('pin ', testC, ' is', Cresult, 'trigger with pullup')
            print('pin ', testD, ' is', Dresult, 'trigger with pulldown')
            time.sleep(0.5)

letsgo = mainprogram()
letsgo.intializethesystem_andrun()
