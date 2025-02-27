import RPi.GPIO as GPIO
import time


class StepperSetup:

    APsteps = 0
    MVsteps = 0
    DVsteps = 0

    APstepdistance = float(0.000625)
    MVstepdistance = float(0.00075)
    DVstepdistance = float(0.00075)

    APcurABSdist = float(0)
    MVcurABSdist = float(0)
    DVcurABSdist = float(0)

    APcurRELdist = float(0)
    MVcurRELdist = float(0)
    DVcurRELdist = float(0)


    def __init__(self,enable,step,direction,limit,Axis,Plusdir,Minusdir):
        self.enable = enable
        self.step = step
        self.direction = direction
        self.limit = limit
        self.cursteps = 0
        self.axis = Axis
        self.goplus = Plusdir
        self.gominus = Minusdir
        self.iliketomoveit = "none"

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

#may not need but put in in case I need to export the steps to the main program
    def exportsteps(self):
        if self.axis == 1:
            return StepperSetup.APsteps
        elif self.axis == 2:
            return StepperSetup.MVsteps
        elif self.axis == 3:
            return StepperSetup.DVsteps


    def receive_instance(self,maininstance):
        self.iliketomoveit = maininstance


    def steppgo(self,spindir,speed):

        self.stepmodifier = 0

        for x in range (speed):
            if GPIO.input(self.limit):
                GPIO.output(self.enable,1)
                GPIO.output(self.direction,spindir)
                GPIO.output(self.step, 1)
                time.sleep(0.0001)
                GPIO.output(self.step, 0)
                time.sleep(0.0001)

                if spindir == 1:
                    self.stepmodifier = 1
                else:
                    self.stepmodifier = -1

                if self.axis == 1:
                    StepperSetup.APsteps += self.stepmodifier
                elif self.axis == 2:
                    StepperSetup.MVsteps += self.stepmodifier
                elif self.axis == 3:
                    StepperSetup.DVsteps += self.stepmodifier

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
                StepperSetup.DVsteps -= 1

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
                StepperSetup.DVsteps += 1

            print(f"APsteps: {StepperSetup.APsteps} MVsteps: {StepperSetup.MVsteps} DVsteps {StepperSetup.DVsteps}")

        StepperSetup.APsteps = 0
        StepperSetup.MVsteps = 0
        StepperSetup.DVsteps = 0

        print(f"Zeroed: APsteps: {StepperSetup.APsteps} MVsteps: {StepperSetup.MVsteps} DVsteps {StepperSetup.DVsteps}")


    def CalibrateDistance(self, calsteps, rollback):

        self.calibratetemp = []
        file_name = 'calibration.txt'
        file = open(file_name, 'r')
        r = 0
        while True:
            line = file.readline()
            if not line:
                break
            self.calibratetemp[r] = line.strip()
            r += 1
        file.close()

        StepperSetup.APstepdistance = float(self.calibratetemp[0])
        StepperSetup.MVstepdistance = float(self.calibratetemp[1])
        StepperSetup.DVstepdistance = float(self.calibratetemp[2])

        print("Current calibration values are:")
        print("AP distance per step:", " ", StepperSetup.APstepdistance, "mm")
        print("MV distance per step:", " ", StepperSetup.MVstepdistance, "mm")
        print("DV distance per step:", " ", StepperSetup.DVstepdistance, "mm")

        yesno = input("Perform calibration? (y/n)")

        self.APinput = 0
        self.MVinput = 0
        self.DVinput = 0
        self.APinputend = 0
        self.MVinputend = 0
        self.DVinputend = 0

        if yesno == "y":
            notation = input("!!!Make sure to remove all attachments from rig!!!")
            if self.axis == 1:
                self.APinput = input("Enter the AP starting position in millimeters.")

                for x in range(calsteps):
                    if 0 < StepperSetup.APsteps < 6000:
                        self.iliketomoveit.steppgo(self.goplus, 1)

                self.APinputend = input("Enter the AP final position in millimeters.")
                # converted to float values
                flAPinput = float(self.APinput)
                flAPinputend = float(self.APinputend)
                # calculated distance moved per step
                StepperSetup.APstepdistance = (flAPinputend - flAPinput) / calsteps

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
                print("AP distance per step:", " ", StepperSetup.APstepdistance, "mm")
                print(f"Variable has been written to {file_name}")

            elif self.axis == 2:
                self.MVinput = input("Enter the MV starting position in millimeters.")

                for x in range(calsteps):
                    if 0 < StepperSetup.MVsteps < 6000:
                        self.iliketomoveit.steppgo(self.goplus, 1)

                self.MVinputend = input("Enter the MV final position in millimeters.")
                # converted to float values
                flMVinput = float(self.MVinput)
                flMVinputend = float(self.MVinputend)
                # calculated distance moved per step
                StepperSetup.MVstepdistance = (flMVinputend - flMVinput) / calsteps

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

                for x in range(calsteps):
                    if 0 < StepperSetup.DVsteps < 6000:
                        self.iliketomoveit.steppgo(self.gominus, 1)

                self.DVinputend = input("Enter the DV final position in millimeters.")
                # converted to float values
                flDVinput = float(self.DVinput)
                flDVinputend = float(self.DVinputend)
                # calculated distance moved per step
                StepperSetup.DVstepdistance = (flDVinput - flDVinputend) / calsteps

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


    def PosRelAbsCalc(self):

        StepperSetup.APcurRELdist = round(((StepperSetup.APsteps - StepperSetup.APrelpos) * StepperSetup.APstepdistance), 4)
        StepperSetup.MVcurRELdist = round(((StepperSetup.MVsteps - StepperSetup.MVrelpos) * StepperSetup.MVstepdistance), 4)
        StepperSetup.DVcurRELdist = round(((StepperSetup.DVsteps - StepperSetup.DVrelpos) * StepperSetup.DVstepdistance), 4)

        StepperSetup.APcurABSdist = round((StepperSetup.APsteps * StepperSetup.APstepdistance), 4)
        StepperSetup.MVcurABSdist = round((StepperSetup.MVsteps * StepperSetup.MVstepdistance), 4)
        StepperSetup.DVcurABSdist = round((StepperSetup.MVsteps * StepperSetup.DVstepdistance), 4)