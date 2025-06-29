import time
import RPi.GPIO as GPIO

from VariableList import var_list
from RotatryEnocderv1 import RotaryEncoder
import tkinter as tk
from tkinter import simpledialog

class threadedcontrols:

# setup GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    def __init__(self, UIinstance):
        self.sendtoUI = UIinstance

#Import the offset values from file
        self.offsetimport = []
        self.importfile_name = 'offsets.txt'
        file = open(self.importfile_name, 'r')
        while True:
            line = file.readline()
            if not line:
                break
            self.offsetimport.append(line.strip())
        file.close()
        var_list.APDRILL = self.offsetimport[0]
        var_list.MLDRILL = self.offsetimport[1]
        var_list.DVDRILL = self.offsetimport[2]

        var_list.APneedle = self.offsetimport[3]
        var_list.MLneedle = self.offsetimport[4]
        var_list.DVneedle = self.offsetimport[5]

        var_list.APfiber = self.offsetimport[6]
        var_list.MLfiber = self.offsetimport[7]
        var_list.DVfiber = self.offsetimport[8]


# Shuts down steppers regardless of what they were doing direction - restart by re-zeroing
    def emergencystop(self):
        GPIO.output(var_list.enableAll, 1)
        var_list.emergencystopflag = 1
        print("!EMERGENCY STOP!")
        print("Re-Zero axis to enable movement again")
        return

# Event handling for the encoders and hard wired buttons each encoder
    def AP_event(self, event):

        if event == RotaryEncoder.CLOCKWISE:
            var_list.APmove.steppgo(var_list.APforward, var_list.stepper_speed, var_list.btnSteps)
            # var_list.APmove.PosRelAbsCalc()
        if event == RotaryEncoder.ANTICLOCKWISE:
            var_list.APmove.steppgo(var_list.APback, var_list.stepper_speed, var_list.btnSteps)
            # var_list.APmove.PosRelAbsCalc()
        # This is a hard wired button note the encoder switch
        elif event == RotaryEncoder.BUTTONDOWN:
            self.emergencystop()
            return
        elif event == RotaryEncoder.BUTTONUP:
            return
        return

# Event handling for the encoders and hard wired buttons each encoder
    def ML_event(self, event):
        if event == RotaryEncoder.CLOCKWISE:
            print('test clockwise')
            var_list.MLmove.steppgo(var_list.MLright, var_list.stepper_speed, var_list.btnSteps)
            # var_list.MLmove.PosRelAbsCalc()
        elif event == RotaryEncoder.ANTICLOCKWISE:
            print('test anticlock')
            var_list.MLmove.steppgo(var_list.MLleft, var_list.stepper_speed, var_list.btnSteps)
            # var_list.MLmove.PosRelAbsCalc()
        elif event == RotaryEncoder.BUTTONDOWN:
            print("event button A clicked")
            return
        elif event == RotaryEncoder.BUTTONUP:
            return
        return

# Event handling for the encoders and hard wired buttons each encoder
    def DV_event(self, event):

        if event == RotaryEncoder.CLOCKWISE:
            var_list.DVmove.steppgo(var_list.DVdown, var_list.stepper_speed, var_list.btnSteps)
            # var_list.DVmove.PosRelAbsCalc()
        elif event == RotaryEncoder.ANTICLOCKWISE:
            var_list.DVmove.steppgo(var_list.DVup, var_list.stepper_speed, var_list.btnSteps)
            # var_list.DVmove.PosRelAbsCalc()
        elif event == RotaryEncoder.BUTTONDOWN:
            print("event button B clicked")
            return
        elif event == RotaryEncoder.BUTTONUP:
            return
        return

    def get_user_input(self,giventitle,givenprompt):
        # Create the root window
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        # Prompt the user for input
        user_input = simpledialog.askstring(title=giventitle, prompt=givenprompt)

        # Print the user input
        if user_input is not None:
            print(f"User input: {user_input}")
            return user_input

        else:
            print("No input provided")

        # Destroy the root window
        root.destroy()


    def zerosteppers(self, axis, backoff, btwnsteps):
        # print('zero step called')
        var_list.zerotrigger = 1
        var_list.emergencystopflag = 0
        GPIO.output(var_list.enableAll, 0)
        if axis == 1:
            print('AP zeroing')
            while GPIO.input(var_list.limitAP):
                var_list.APmove.steppgo(var_list.APback, var_list.finespeed, btwnsteps)
                if GPIO.input(var_list.limitAP) != True:
                    print('zero while loop limit')
                    break
            print('run backoff')
            var_list.APmove.backoffafterzero(backoff,var_list.finespeed,var_list.btnSteps)
        elif axis == 2:
            print('ML zeroing')
            while GPIO.input(var_list.limitML):
                var_list.MLmove.steppgo(var_list.MLleft, var_list.finespeed, btwnsteps)
                if GPIO.input(var_list.limitML) != True:
                    print('zero while loop limit')
                    break
            print('run backoff')
            var_list.MLmove.backoffafterzero(backoff, var_list.finespeed, var_list.btnSteps)
        elif axis == 3:
            print('DV zeroing')
            while GPIO.input(var_list.limitDV):
                var_list.DVmove.steppgo(var_list.DVup, var_list.finespeed, btwnsteps)
                if GPIO.input(var_list.limitDV) != True:
                    print('zero while loop limit')
                    break
            print('run backoff')
            var_list.DVmove.backoffafterzero(backoff, var_list.finespeed, var_list.btnSteps)

        if axis == 1:
            var_list.APsteps = 0
            var_list.APmove.PosRelAbsCalc()
            print('sent to calculationville')
        elif axis == 2:
            var_list.MLsteps = 0
            var_list.MLmove.PosRelAbsCalc()
        elif axis == 3:
            var_list.DVsteps = 0
            var_list.DVmove.PosRelAbsCalc()
        print('should report the step values now')
        # print(f"Zeroed: APsteps: {var_list.APsteps} MLsteps: {var_list.MLsteps} DVsteps {var_list.DVsteps}")
        time.sleep(0.200)
        print('disable steppers')
        GPIO.output(var_list.enableAll, 1)
        var_list.lastenablestate = 1
        var_list.zerotrigger = 0

    def importcalibrationfile(self, filenameis):
        self.calibratetemp = []
        file = open(filenameis, 'r')

        while True:
            line = file.readline()
            if not line:
                break
            self.calibratetemp.append(line.strip())

        file.close()

        var_list.APstepdistance = float(self.calibratetemp[0])
        var_list.MLstepdistance = float(self.calibratetemp[1])
        var_list.DVstepdistance = float(self.calibratetemp[2])

        print("Current calibration values are:")
        print("AP distance per step: ", var_list.APstepdistance, "mm")
        print("ML distance per step: ", var_list.MLstepdistance, "mm")
        print("DV distance per step: ", var_list.DVstepdistance, "mm")


    def exportcalibrationfile(self, filenamewas):
        with open(filenamewas, "w") as file:
            # Write each variable to the file in Pine Script format
            for x, value in enumerate(self.calibratetemp):
                varvalue = self.calibratetemp[x]
                file.write(f"{varvalue}\n")
        file.close()


    def CalibrateDistance(self, axisno, filecalled, calibrationsteps, rollback, btwnSteps):
        self.file_name = filecalled
        self.importcalibrationfile(self.file_name)
        if axisno == 1:
            self.APinput = 0
            self.APinputend = 0
            yesno = self.get_user_input('Calibration:', 'Perform re-calibration on AP axis? (y/n)')
            notation = self.get_user_input('MESSAGE:',
                                       '!!!Make sure to remove all attachments from rig!!! ENTER key to continue')
            if yesno == "y":
                self.APinput = self.get_user_input('INPUT:', 'Enter the AP starting position in millimeters.')
                for x in range(calibrationsteps):
                    if 0 <= var_list.APsteps < 6000:
                        var_list.APmove.steppgo(var_list.APforward, var_list.finespeed, btwnSteps)
                        # var_list.APmove.PosRelAbsCalc()
                self.APinputend = self.get_user_input('INPUT:', 'Enter the AP final position in millimeters.')
                flAPinput = float(self.APinput)
                flAPinputend = float(self.APinputend)
                var_list.APstepdistance = (flAPinputend - flAPinput) / calibrationsteps
                print("send to file AP step distance", var_list.APstepdistance)
                self.calibratetemp = [var_list.APstepdistance, var_list.MLstepdistance,
                                      var_list.DVstepdistance]
                self.exportcalibrationfile(self.file_name)
        if axisno == 2:
            self.MLinput = 0
            self.MLinputend = 0
            yesno = self.get_user_input('Calibration:', 'Perform re-calibration on ML axis? (y/n)')
            notation = self.get_user_input('MESSAGE:',
                                       '!!!Make sure to remove all attachments from rig!!! ENTER key to continue')
            if yesno == "y":
                self.MLinput = self.get_user_input('INPUT:', 'Enter the ML starting position in millimeters.')
                for x in range(calibrationsteps):
                    if 0 <= var_list.MLsteps < 6000:
                        var_list.MLmove.steppgo(var_list.MLright, var_list.finespeed, btwnSteps)
                        # var_list.MLmove.PosRelAbsCalc()
                self.MLinputend = self.get_user_input('INPUT:', 'Enter the ML final position in millimeters.')
                flMLinput = float(self.MLinput)
                flMLinputend = float(self.MLinputend)
                var_list.MLstepdistance = (flMLinputend - flMLinput) / calibrationsteps
                print("send to file ML step distance", var_list.MLstepdistance)
                self.calibratetemp = [var_list.APstepdistance, var_list.MLstepdistance,
                                      var_list.DVstepdistance]
                self.exportcalibrationfile(self.file_name)
        if axisno == 3:
            self.DVinput = 0
            self.DVinputend = 0
            yesno = self.get_user_input('Calibration:', 'Perform re-calibration on DV axis? (y/n)')
            notation = self.get_user_input('MESSAGE:',
                                           '!!!Make sure to remove all attachments from rig!!! ENTER key to continue')
            if yesno == "y":
                self.DVinput = self.get_user_input('INPUT:', 'Enter the DV starting position in millimeters.')
                for x in range(calibrationsteps):
                    if 0 <= var_list.DVsteps < 6000:
                        var_list.DVmove.steppgo(var_list.DVdown, var_list.finespeed, btwnSteps)
                        # var_list.DVmove.PosRelAbsCalc()
                self.DVinputend = self.get_user_input('INPUT:', 'Enter the DV final position in millimeters.')
                flDVinput = float(self.DVinput)
                flDVinputend = float(self.DVinputend)
                var_list.DVstepdistance = (flDVinput - flDVinputend) / calibrationsteps
                print("send to file DV step distance", var_list.DVstepdistance)
                self.calibratetemp = [var_list.APstepdistance, var_list.MLstepdistance,
                                      var_list.DVstepdistance]
                self.exportcalibrationfile(self.file_name)

    def reportcalib_values(self, filename):
        self.tempfilename = filename
        self.importcalibrationfile(self.file_name)
        print("NEW calibration values are:")
        print("AP distance per step:", " ", var_list.APstepdistance, "mm")
        print("ML distance per step:", " ", var_list.MLstepdistance, "mm")
        print("DV distance per step:", " ", var_list.DVstepdistance, "mm")
        print(f"Variable has been written to {self.tempfilename}")


# question and waits for user input
    def calibratethings(self):
        self.quest = self.get_user_input('MESSAGE:','Initialization Process ... ENTER to continue')
        self.quest = self.get_user_input('MESSAGE:','CAUTION...Remove all attachments from frame arms! ENTER to continue.')

#Zero all steppers
        self.zerosteppers(1,var_list.backoff, var_list.btnSteps)
        self.zerosteppers(2,var_list.backoff, var_list.btnSteps)
        self.zerosteppers(3, var_list.backoff, var_list.btnSteps)

        self.importcalibrationfile(var_list.calibfilename)
# calibrate steppers if needed
        tempAP = round(var_list.APstepdistance, 5)
        tempML = round(var_list.MLstepdistance, 5)
        tempDV = round(var_list.DVstepdistance, 5)
        yesno = self.get_user_input('Current Calibration:', f"AP: {tempAP}, ML: {tempML}, DV: {tempDV}. Proceed with calibration? (y/n)")
        if yesno == "y":
            self.CalibrateDistance(1, var_list.calibfilename, var_list.calibrationsteps, var_list.backoff, var_list.btnSteps)
            self.CalibrateDistance(2, var_list.calibfilename, var_list.calibrationsteps, var_list.backoff, var_list.btnSteps)
            self.CalibrateDistance(3, var_list.calibfilename, var_list.calibrationsteps, var_list.backoff, var_list.btnSteps)
            self.reportcalib_values(var_list.calibfilename)
#re-zero steppers
            self.zerosteppers(1, var_list.backoff, var_list.btnSteps)
            self.zerosteppers(2, var_list.backoff, var_list.btnSteps)
            self.zerosteppers(3, var_list.backoff, var_list.btnSteps)

    def runcontrolthread(self):
# INITIALIZE ENCODERS
        print('encoders init')
        self.AProto = RotaryEncoder(var_list.rotoA_AP, var_list.rotoB_AP, var_list.emergstop, self.AP_event)
        self.MLroto = RotaryEncoder(var_list.rotoA_ML, var_list.rotoB_ML, var_list.misc_eventbuttonA, self.ML_event)
        self.DVroto = RotaryEncoder(var_list.rotoA_DV, var_list.rotoB_DV, var_list.misc_eventbuttonB, self.DV_event)

        self.calibratethings()