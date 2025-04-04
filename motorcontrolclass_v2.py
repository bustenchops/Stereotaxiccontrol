import RPi.GPIO as GPIO
import time

#from Steppercontrol_classversion import mainprogram


class StepperSetup:

    btnSteps = 0.001

    APsteps = 0
    MVsteps = 0
    DVsteps = 0

    APrelpos = 0
    MVrelpos = 0
    DVrelpos = 0

    DVinitREL_holdvalue = 0
    MVinitREL_holdvalue = 0
    APinitREL_holdvalue = 0

    APstepdistance = float(0.00625)
    MVstepdistance = float(0.0075)
    DVstepdistance = float(0.0075)

    APcurABSdist = float(0)
    MVcurABSdist = float(0)
    DVcurABSdist = float(0)

    APcurRELdist = float(0)
    MVcurRELdist = float(0)
    DVcurRELdist = float(0)


    def __init__(self,enablepin,steppin,directionpin,limitpin,Axis,Plusdir,Minusdir,tosendtoUI):
        print('setting up a stepper')
        self.enable = enablepin
        self.step = steppin
        self.direction = directionpin
        self.limit = limitpin
            # Axis defined:
            # AP = 1
            # MV = 2
            # DV = 3
        self.axis = Axis
            # NOTE plus and minus direction relative to stereo coordinates
        self.goplus = Plusdir
        self.gominus = Minusdir
        self.lastenablestate = 0
            # NOTE: placeholder to import object instances from main program
        self.iliketomoveit = "none"
        self.sendtoUI = tosendtoUI

        # setup GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(self.enable, GPIO.OUT, initial=1)
        GPIO.setup(self.step, GPIO.OUT, initial=0)
        GPIO.setup(self.direction, GPIO.OUT, initial=0)
        GPIO.setup(self.limit, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    #may not need but put it in case I need to export the steps to the main program
    def exportsteps(self):
        if self.axis == 1:
            return StepperSetup.APsteps
        elif self.axis == 2:
            return StepperSetup.MVsteps
        elif self.axis == 3:
            return StepperSetup.DVsteps


    #receives object instance from control  program so it can be utilized with this class APmove,MVmove and DVmove
        #Object instance calls on this function from within itself and sends itself here.
    def receive_instance(self, maininstance):
        self.iliketomoveit = maininstance

    #receives object instance from main program so it can be utilized with this class
    #Object instance calls on this function from within itself and sends itself here.
    #just to keep UIstuff apart from working stuff
    def receive_frommainstepper(self, comingfrommain):
        self.sendingtomain = comingfrommain


    def steppgo(self,move_direction, speed, btwnsteps):

        self.stepmodifier = 0

        if self.lastenablestate == 1:
            GPIO.output(self.enable, 0)

        for x in range (speed):
            if GPIO.input(self.limit):
                GPIO.output(self.direction,move_direction)
                GPIO.output(self.step, 1)
                time.sleep(btwnsteps)
                GPIO.output(self.step, 0)
                time.sleep(btwnsteps)


                if self.axis == 1:
                    if move_direction == self.gominus:
                        StepperSetup.APsteps += 1
                    else:
                        StepperSetup.APsteps -= 1
                elif self.axis == 2:
                    if move_direction == self.goplus:
                        StepperSetup.MVsteps += 1
                    else:
                        StepperSetup.MVsteps -= 1
                elif self.axis == 3:
                    if move_direction == self.gominus:
                        StepperSetup.DVsteps += 1
                    else:
                        StepperSetup.DVsteps -= 1

                self.iliketomoveit.PosRelAbsCalc()
            else:
                print("ERROR - limit reached")


    def zerostep(self, backoff, btwnsteps):
        print('zero step called')
        GPIO.output(self.enable,0)
        while GPIO.input(self.limit):

    #        print(self.axis)
            if self.axis == 1:
                self.steppgo(self.gominus, 1, btwnsteps)
                StepperSetup.APsteps -= 1
            elif self.axis == 2:
                self.steppgo(self.gominus, 1, btwnsteps)
                StepperSetup.MVsteps -= 1
            elif self.axis == 3:
                self.steppgo(self.goplus, 1, btwnsteps)
                StepperSetup.DVsteps -= 1
            if GPIO.input(self.limit) != True:
                break


        for x in range(backoff):
            if self.axis == 1:
                GPIO.output(self.direction, self.goplus)
                StepperSetup.APsteps += 1
            elif self.axis == 2:
                GPIO.output(self.direction, self.goplus)
                StepperSetup.MVsteps += 1
            elif self.axis == 3:
                GPIO.output(self.direction, self.gominus)
                StepperSetup.DVsteps += 1
            GPIO.output(self.step, 1)
            time.sleep(self.btnSteps)
            GPIO.output(self.step, 0)
            time.sleep(self.btnSteps)

#            print(f"APsteps: {StepperSetup.APsteps} MVsteps: {StepperSetup.MVsteps} DVsteps {StepperSetup.DVsteps}")

        #Sets the ABS steps for that axis to 0
        if self.axis == 1:
            StepperSetup.APsteps = 0
        elif self.axis == 2:
            StepperSetup.MVsteps = 0
        elif self.axis == 3:
            StepperSetup.DVsteps = 0

        print(f"Zeroed: APsteps: {StepperSetup.APsteps} MVsteps: {StepperSetup.MVsteps} DVsteps {StepperSetup.DVsteps}")

        self.iliketomoveit.PosRelAbsCalc()
        # shut down steppers so they cool
        GPIO.output(self.enable,1)
        print('stepper zeroed and shut down')


    def CalibrateDistance(self, calibrationsteps, rollback, btwnSteps):
        print('open file')
        self.calibratetemp = []
        file_name = 'Calibration.txt'
        file = open(file_name, 'r')
        print ('file openned')
        while True:
            print('reading')
            line = file.readline()
            if not line:
                break
            self.calibratetemp.append(line.strip())

        file.close()
        print('file closed')
        StepperSetup.APstepdistance = float(self.calibratetemp[0])
        StepperSetup.MVstepdistance = float(self.calibratetemp[1])
        StepperSetup.DVstepdistance = float(self.calibratetemp[2])

        print("Current calibration values are:")
        print("AP distance per step: ", StepperSetup.APstepdistance, "mm")
        print("MV distance per step: ", StepperSetup.MVstepdistance, "mm")
        print("DV distance per step: ", StepperSetup.DVstepdistance, "mm")

        yesno = input("Perform calibration? (y/n)")

        #init the input variables
        self.APinput = 0
        self.MVinput = 0
        self.DVinput = 0
        self.APinputend = 0
        self.MVinputend = 0
        self.DVinputend = 0

        if yesno == "y":
            notation = input("!!!Make sure to remove all attachments from rig!!! ENTER key to continue")
            if self.axis == 1:
                self.APinput = input("Enter the AP starting position in millimeters.")

                for x in range(calibrationsteps):
                    if 0 < StepperSetup.APsteps < 6000:
                        self.iliketomoveit.steppgo(self.goplus, 1, btwnSteps)

                self.APinputend = input("Enter the AP final position in millimeters.")
                # converted to float values
                flAPinput = float(self.APinput)
                flAPinputend = float(self.APinputend)
                # calculated distance moved per step
                StepperSetup.APstepdistance = (flAPinputend - flAPinput) / calibrationsteps

                # write values to file
                self.calibratetemp = [StepperSetup.APstepdistance, StepperSetup.MVstepdistance, StepperSetup.DVstepdistance]
                # Open the file in write mode
                with open(file_name, "w") as file:
                    # Write each variable to the file in Pine Script format
                    for x, value in enumerate(self.calibratetemp):
                        varvalue = self.calibratetemp[x]
                        file.write(f"{varvalue}\n")
                file.close()

                print("NEW calibration values are:")
                print("AP distance per step:", " ", StepperSetup.APstepdistance, "mm")
                print(f"Variable has been written to {file_name}")

            elif self.axis == 2:
                self.MVinput = input("Enter the MV starting position in millimeters.")

                for x in range(calibrationsteps):
                    if 0 < StepperSetup.MVsteps < 6000:
                        self.iliketomoveit.steppgo(self.goplus, 1,btwnSteps)

                self.MVinputend = input("Enter the MV final position in millimeters.")
                # converted to float values
                flMVinput = float(self.MVinput)
                flMVinputend = float(self.MVinputend)
                # calculated distance moved per step
                StepperSetup.MVstepdistance = (flMVinputend - flMVinput) / calibrationsteps

                # write values to file
                calibratetemp = [StepperSetup.APstepdistance, StepperSetup.MVstepdistance, StepperSetup.DVstepdistance]
                # Open the file in write mode
                with open(file_name, "w") as file:
                    # Write each variable to the file in Pine Script format
                    for x, value in enumerate(calibratetemp):
                        varvalue = calibratetemp[x]
                        file.write(f"{varvalue}\n")
                file.close()

                print("NEW calibration values are:")
                print("MV distance per step:", " ", StepperSetup.MVstepdistance, "mm")
                print(f"Variable has been written to {file_name}")

            elif self.axis == 3:
                self.DVinput = input("Enter the DV starting position in millimeters.")

                for x in range(calibrationsteps):
                    if 0 < StepperSetup.DVsteps < 6000:
                        self.iliketomoveit.steppgo(self.gominus, 1,btwnSteps)

                self.DVinputend = input("Enter the DV final position in millimeters.")
                # converted to float values
                flDVinput = float(self.DVinput)
                flDVinputend = float(self.DVinputend)
                # calculated distance moved per step
                StepperSetup.DVstepdistance = (flDVinput - flDVinputend) / calibrationsteps

                # write values to file
                calibratetemp = [StepperSetup.APstepdistance, StepperSetup.MVstepdistance, StepperSetup.DVstepdistance]
                # Open the file in write mode
                with open(file_name, "w") as file:
                    # Write each variable to the file in Pine Script format
                    for x, value in enumerate(calibratetemp):
                        varvalue = calibratetemp[x]
                        file.write(f"{varvalue}\n")
                file.close()

                print("NEW calibration values are:")
                print("DV distance per step:", " ", StepperSetup.DVstepdistance, "mm")
                print(f"Variable has been written to {file_name}")

            # Zero again
            self.iliketomoveit.zerostep(rollback)


    def PosRelAbsCalc(self):

        StepperSetup.APcurRELdist = round(((StepperSetup.APsteps - StepperSetup.APrelpos) * StepperSetup.APstepdistance), 4)
        StepperSetup.MVcurRELdist = round(((StepperSetup.MVsteps - StepperSetup.MVrelpos) * StepperSetup.MVstepdistance), 4)
        StepperSetup.DVcurRELdist = round(((StepperSetup.DVsteps - StepperSetup.DVrelpos) * StepperSetup.DVstepdistance * -1), 4)

        StepperSetup.APcurABSdist = round((StepperSetup.APsteps * StepperSetup.APstepdistance), 4)
        StepperSetup.MVcurABSdist = round((StepperSetup.MVsteps * StepperSetup.MVstepdistance), 4)
        StepperSetup.DVcurABSdist = round((StepperSetup.DVsteps * StepperSetup.DVstepdistance * -1), 4)

        self.sendtoUI.updatepositionLCD(StepperSetup.APsteps,StepperSetup.MVsteps,StepperSetup.DVsteps,StepperSetup.APcurABSdist,StepperSetup.MVcurABSdist,StepperSetup.DVcurABSdist,StepperSetup.APcurRELdist,StepperSetup.MVcurRELdist,StepperSetup.DVcurRELdist)

        print(f"Absolute position-|AP: {StepperSetup.APcurABSdist} | MV: {StepperSetup.MVcurABSdist} | DV: {StepperSetup.DVcurABSdist}")
        print(f"Relative position-|AP: {StepperSetup.APcurRELdist} | MV: {StepperSetup.MVcurRELdist} | DV: {StepperSetup.DVcurRELdist}")