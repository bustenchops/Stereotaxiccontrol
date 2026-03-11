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
            count = 1
            # reading the buttons
            Aresult = GPIO.input(mainprogram.testA)
            Bresult = GPIO.input(mainprogram.testB)
            Cresult = GPIO.input(mainprogram.testC)
            Dresult = GPIO.input(mainprogram.testD)

            print ('rep:', count)
            print ('pin ', mainprogram.testA, ' is', Aresult, 'just wired')
            print('pin ', mainprogram.testB, ' is', Bresult, 'just wired through trigger')
            print('pin ', mainprogram.testC, ' is', Cresult, 'trigger with pullup')
            print('pin ', mainprogram.testD, ' is', Dresult, 'trigger with pulldown')
            time.sleep(0.25)
            count += 1

letsgo = mainprogram()
letsgo.intializethesystem_andrun()
