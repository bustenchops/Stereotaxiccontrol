import RPi.GPIO as GPIO
import time

from VariableList import var_list

class Steppercontrol:

    def __init__(self,enablepin,steppin,directionpin,limitpin,Axis,Plusdir,Minusdir,Stepcon_sendtoUI):
        self.enable = enablepin
        self.step = steppin
        self.direction = directionpin
        self.limit = limitpin
            # Axis defined:
            # AP = 1
            # ML = 2
            # DV = 3
        self.axis = Axis
            # NOTE plus and minus direction relative to stereo coordinates
        self.goplus = Plusdir
        self.gominus = Minusdir
        var_list.lastenablestate = 1
        self.sendtoUI = Stepcon_sendtoUI

        # setup GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(self.enable, GPIO.OUT, initial=1)
        GPIO.setup(self.step, GPIO.OUT, initial=0)
        GPIO.setup(self.direction, GPIO.OUT, initial=0)
        GPIO.setup(self.limit, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def steppgo(self,move_direction, speed, btwnsteps):

        if var_list.emergencystopflag == 0:
            #print('stop flag cleared and zero limit cleared')
            if var_list.lastenablestate == 1:
                GPIO.output(self.enable, 0)

            for x in range (speed):

                if GPIO.input(self.limit):
                    GPIO.output(self.direction,move_direction)
                    GPIO.output(self.step, 1)
                    time.sleep(btwnsteps)
                    GPIO.output(self.step, 0)
                    time.sleep(btwnsteps)


                    if self.axis == 1:
                        if move_direction == self.gominus: #AP steps up and AP measure on the frame goes up
                            var_list.APsteps += 1
                        else:
                            var_list.APsteps -= 1
                    elif self.axis == 2:
                        if move_direction == self.goplus: #MV steps up and MV measure on the frame goes minus
                            var_list.MLsteps += 1
                        else:
                            var_list.MLsteps -= 1
                    elif self.axis == 3:
                        if move_direction == self.goplus: #DV steps up and DV measure on the frame goes minus
                            var_list.DVsteps += 1
                        else:
                            var_list.DVsteps -= 1
                else:
                    print("ERROR - limit reached")

                    if self.axis == 1:
                        if move_direction == self.gominus:  # AP steps up and AP measure goes up
                            GPIO.output(self.direction, move_direction)
                            GPIO.output(self.step, 1)
                            time.sleep(btwnsteps)
                            GPIO.output(self.step, 0)
                            time.sleep(btwnsteps)

                            var_list.APsteps += 1
                    elif self.axis == 2:
                        if move_direction == self.goplus:  # MV steps up and MV measure goes minus
                            GPIO.output(self.direction, move_direction)
                            GPIO.output(self.step, 1)
                            time.sleep(btwnsteps)
                            GPIO.output(self.step, 0)
                            time.sleep(btwnsteps)

                            var_list.MLsteps += 1
                    elif self.axis == 3:
                        if move_direction == self.goplus:  # DV steps up and DV measure goes minus
                            GPIO.output(self.direction, move_direction)
                            GPIO.output(self.step, 1)
                            time.sleep(btwnsteps)
                            GPIO.output(self.step, 0)
                            time.sleep(btwnsteps)
                            var_list.DVsteps += 1

        else:
            print("Emergency Stopped - Cannot move until re-zeroed")

# to clear the limit switch and zeros
    def backoffafterzero(self, backoff, speed, btwnsteps):
        if var_list.lastenablestate == 1:
            GPIO.output(self.enable, 0)

        if self.axis == 1:
            print('backoff AP:',backoff,' steps')
            for x in range(backoff):
                GPIO.output(self.direction, var_list.APback)
                GPIO.output(self.step, 1)
                time.sleep(btwnsteps)
                GPIO.output(self.step, 0)
                time.sleep(btwnsteps)
        elif self.axis == 2:
            print('backoff ML',backoff,' steps')
            for x in range(backoff):
                GPIO.output(self.direction, var_list.MLleft)
                GPIO.output(self.step, 1)
                time.sleep(btwnsteps)
                GPIO.output(self.step, 0)
                time.sleep(btwnsteps)
        elif self.axis == 3:
            print('backoff DV',backoff,' steps')
            for x in range(backoff):
                GPIO.output(self.direction, var_list.DVdown)
                GPIO.output(self.step, 1)
                time.sleep(btwnsteps)
                GPIO.output(self.step, 0)
                time.sleep(btwnsteps)

#at calibration further advances the steps so there is a bit of working room
    def APadvanceafterbackoff(self, speed, btwnsteps):
        if var_list.lastenablestate == 1:
            GPIO.output(self.enable, 0)

        for x in range(var_list.APadvance):
            GPIO.output(self.direction, var_list.APback)
            GPIO.output(self.step, 1)
            time.sleep(btwnsteps)
            GPIO.output(self.step, 0)
            time.sleep(btwnsteps)

    def DVadvanceafterbackoff(self, speed, btwnsteps):
        if var_list.lastenablestate == 1:
            GPIO.output(self.enable, 0)

        for x in range(var_list.DVadvance):
            GPIO.output(self.direction, var_list.DVdown)
            GPIO.output(self.step, 1)
            time.sleep(btwnsteps)
            GPIO.output(self.step, 0)
            time.sleep(btwnsteps)

    def MLadvanceafterbackoff(self, speed, btwnsteps):
        if var_list.lastenablestate == 1:
            GPIO.output(self.enable, 0)

        for x in range(var_list.MLadvance):
            GPIO.output(self.direction, var_list.MLleft)
            GPIO.output(self.step, 1)
            time.sleep(btwnsteps)
            GPIO.output(self.step, 0)
            time.sleep(btwnsteps)


    def PosRelAbsCalc(self):
        print('doing position calculation')
        if self.axis == 1:
            print('AP calculation')
            var_list.APcurRELdist = round(((var_list.APsteps - var_list.APrelpos) * var_list.APstepdistance), 3)
            var_list.APcurABSdist = round((var_list.APsteps * var_list.APstepdistance), 3)
            # print(var_list.APcurRELdist)
            # print(var_list.APcurABSdist)
            # self.sendtoUI.updateAPstepLCD(var_list.APsteps)
            # self.sendtoUI.updateAPabsposLCD(var_list.APcurABSdist)
            # self.sendtoUI.updateAPrelposLCD(var_list.APcurRELdist)
            self.sendtoUI.updateAPLCD(var_list.APsteps, var_list.APcurABSdist, var_list.APcurRELdist)

        if self.axis == 2:
            print('ML calculation')
            var_list.MLcurRELdist = round(
                ((var_list.MLsteps - var_list.MLrelpos) * var_list.MLstepdistance * -1), 3)
            var_list.MLcurABSdist = round((var_list.MLsteps * var_list.MLstepdistance * -1), 3)
            # self.sendtoUI.updateMLstepLCD(var_list.MLsteps)
            # self.sendtoUI.updateMLabsposLCD(var_list.MLcurABSdist)
            # self.sendtoUI.updateMLrelposLCD(var_list.MLcurRELdist)
            self.sendtoUI.updateMLLCD(var_list.MLsteps, var_list.MLcurABSdist, var_list.MLcurRELdist)

        if self.axis == 3:
            print('DV calculation')
            var_list.DVcurRELdist = round(
                ((var_list.DVsteps - var_list.DVrelpos) * var_list.DVstepdistance * -1), 3)
            var_list.DVcurABSdist = round((var_list.DVsteps * var_list.DVstepdistance * -1), 3)
            # self.sendtoUI.updateDVstepLCD(var_list.DVsteps)
            # self.sendtoUI.updateDVabsposLCD(var_list.DVcurABSdist)
            # self.sendtoUI.updateDVrelposLCD(var_list.DVcurRELdist)
            self.sendtoUI.updateDVLCD(var_list.DVsteps, var_list.DVcurABSdist, var_list.DVcurRELdist)

# concept and code created by Kirk Mulatz (original code https://github.com/bustenchops/Stereotaxiccontrol (experiment branch)