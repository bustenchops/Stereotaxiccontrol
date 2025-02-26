import RPi.GPIO as GPIO
import time

from Steppercontrol_v2 import APsteps, MVsteps, DVsteps


class StepperSetup:

    APsteps = 0
    MVsteps = 0
    DVsteps = 0

    def __init__(self,enable,step,direction,limit,Axis,startstep):
        self.enable = enable
        self.step = step
        self.direction = direction
        self.limit = limit
        self.cursteps = 0
        self.axis = Axis

        #Axis defined:
        # AP = 1
        # MV = 2
        # DV = 3

        # setup GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(self.enable, GPIO.OUT, initial=1)
        GPIO.setup(self.step, GPIO.OUT, initial=0)
        GPIO.setup(self.direction, GPIO.OUT, initial=0)
        GPIO.setup(self.limit, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    def exportsteps(self):
        if self.axis == 1:
            return APsteps
        elif self.axis == 2:
            return MVsteps
        elif self.axis == 3:
            return DVsteps


    def steppgo(self,spindir,speed):

        for x in range (speed):
            if GPIO.input(self.limit):
                GPIO.output(self.enable,1)
                GPIO.output(self.direction,spindir)
                GPIO.output(self.step, 1)
                time.sleep(0.0001)
                GPIO.output(self.step, 0)
                time.sleep(0.0001)

                if spindir == 1:
                    stepmodifier = 1
                else:
                    stepmodifier = -1

                if self.axis == 1:
                    StepperSetup.APsteps += stepmodifier
                elif self.axis == 2:
                    StepperSetup.MVsteps += stepmodifier
                elif self.axis == 3:
                    StepperSteup.DVsteps += stepmodifier

            else:
                print("ERROR - limit reached")


    def zerostep(self,backoff):

        GPIO.output(self.enable,1)
        while GPIO.input(self.limit):
            self.steppgo(0,1)
            if self.axis == 1:
                StepperSetup.APsteps -= 1
            elif self.axis == 2:
                StepperSetup.MVsteps -= 1
            elif self.axis == 3:
                StepperSteup.DVsteps -= 1

        for x in range(backoff):
            GPIO.output(self.enable, 1)
            GPIO.output(self.direction, 1)
            GPIO.output(self.step, 1)
            time.sleep(0.0001)
            GPIO.output(self.step, 0)
            time.sleep(0.0001)

            if self.axis == 1:
                StepperSetup.APsteps += 1
            elif self.axis == 2:
                StepperSetup.MVsteps += 1
            elif self.axis == 3:
                StepperSteup.DVsteps += 1

        StepperSetup.APsteps = 0
        StepperSetup.MVsteps = 0
        StepperSetup.DVsteps = 0

        
    def hometo(self,spindir,curstep,stepto):
        self.cursteps = curstep
        if self.cursteps > stepto:
            while self.cursteps > stepto:
                if GPIO.input(self.limit):
                    self.steppgo(spindir,1)
                    self.cursteps -= 1
                else:
                    print("ERROR - limit reached")
            
            return self.cursteps
        
        else:
            while self.cursteps < stepto:
                if GPIO.input(self.limit):
                    self.steppgo(spindir,1)
                    self.cursteps += 1
            
            return self.cursteps


    def PosAbsCalc(self, APstppos, MVstppos, DVstppos, APrelpos, MVrelpos, DVrelpos, APcalbval, MVcalbval, DVcalbval):
        global APsteps
        global MVsteps
        global DVsteps

        global APcurABSdist
        global MVcurABSdist
        global DVcurABSdist
        global APcurRELdist
        global MVcurRELdist
        global DVcurRELdist

        self.APstppos = APstppos
        self.MVstppos = MVstppos
        self.DVstppos = DVstppos
        self.APrelpos = APrelpos
        self.MVrelpos = MVrelpos
        self.DVrelpos = DVrelpos
        self.APcalbval = APcalbval
        self.MVcalbval = MVcalbval
        self.DVcalbval = DVcalbval

        APcurRELdist = round(((self.APstppos - self.APrelpos) * self.APcalbval), 4)
        MVcurRELdist = round(((self.MVstppos - self.MVrelpos) * self.MVcalbval), 4)
        DVcurRELdist = round(((self.DVstppos - self.DVrelpos) * self.DVcalbval), 4)

        APcurABSdist = round((self.APstppos * self.APcalbval), 4)
        MVcurABSdist = round((self.MVstppos * self.MVcalbval), 4)
        DVcurABSdist = round((self.DVstppos * self.DVcalbval), 4)