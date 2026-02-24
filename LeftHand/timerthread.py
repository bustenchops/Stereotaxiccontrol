import time
import RPi.GPIO as GPIO

from VariableList import var_list

class threadedtimer:

# setup GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    def __init__(self, UIinstance):
        self.sendtoUI = UIinstance
        self.DVinsertiontimeout = None
        self.Withdrawtimeout = None
        self.Safetytimeout = None
        self.Makeitsotimeout = None
        self.timerlength = var_list.timeoutlength
        print("timer thread started")

    def runtimerthread(self):
        self.DVinsertiontimeout = var_list.DVinserttimeouttime
        self.Withdrawtimeout = var_list.Withdrawltimeouttime
        self.Safetytimeout = var_list.Safetytimeouttime
        self.Makeitsotimeout = var_list.Makeitsobuttimeouttime
        counter = 0
        while True:
            print("start thread true loop")
            # check to see if the box is checked first then run the checks
            if counter == 8:
                print ("timer 2sec")
                counter = 0
            if var_list.safetybutton == 1:
                if self.Safetytimeout != var_list.Safetytimeouttime:
                    self.Safetytimeout = var_list.Safetytimeouttime
                currenttime = time.time()
                timecruncherSafe = currenttime - self.Safetytimeout
                if timecruncherSafe > self.timerlength:
                    print('Safety disengage timed out')
                    var_list.safetybutton = 0
                    self.sendtoUI.makeitsoBox.setChecked(False)

            if var_list.Withdrawlindicator == 1:
                if self.Withdrawtimeout != var_list.Withdrawltimeouttime:
                    self.Withdrawtimeout = var_list.Withdrawltimeouttime
                currenttime = time.time()
                timecruncherWith = currenttime - self.Withdrawtimeout
                if timecruncherWith > self.timerlength:
                    print('Withdrawltime engage timed out')
                    var_list.Withdrawlindicator = 0
                    #also uncheck the box

            if var_list.DVinsertindicator == 1:
                if self.DVinsertiontimeout != var_list.DVinserttimeouttime:
                    self.DVinsertiontimeout = var_list.DVinserttimeouttime
                currenttime = time.time()
                timecruncherDV = currenttime - self.DVinsertiontimeout
                if timecruncherDV > self.timerlength:
                    print('DVinsert engage timed out')
                    var_list.DVinsertindicator = 0
                    # also uncheck the box

            if var_list.Makeitsoindicator == 1:
                if self.Makeitsotimeout != var_list.Makeitsobuttimeouttime:
                    self.Makeitsotimeout = var_list.Makeitsobuttimeouttime
                currenttime = time.time()
                timecruncherMakeit = currenttime - self.Makeitsotimeout
                if timecruncherMakeit > self.timerlength:
                    print('Makeitso checkbox timed out')
                    var_list.Makeitsoindicator = 0
                    # also uncheck the box
            counter += 1
            time.sleep(0.250)



# note this will send the time now every 250ms to the varlist
        # will reset the timed functions after x time