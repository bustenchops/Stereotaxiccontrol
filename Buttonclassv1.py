import time
import RPi.GPIO as GPIO

from VariableList import var_list

class buttonprogram:

    def __init__(self, UIinstance):
        self.sendtoUI = UIinstance
        #INITIALIZE PINS
        GPIO.setup(var_list.latchpin, GPIO.OUT)
        GPIO.setup(var_list.clockpin, GPIO.OUT)
        GPIO.setup(var_list.datapin, GPIO.IN)


#Get the shift register data
    def getshiftregisterdata(self):
        self.shiftvalues = []
        #get number of buttons
        x = len(var_list.buttonarray)
    #    print("button array length=", x)
        for k in range(x):
            self.shiftvalues.append(0)
        #LOAD DATA
        GPIO.output(var_list.latchpin, GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(var_list.latchpin, GPIO.HIGH)
        #READ DATA
        for i in range(x):
            GPIO.output(var_list.clockpin, GPIO.LOW)
            self.shiftvalues[i] = GPIO.input(var_list.datapin)
            GPIO.output(var_list.clockpin, GPIO.HIGH)
            time.sleep(0.001)
        return self.shiftvalues

#transfer shift values to an array
    def buttonvalues(self, lastbut, newbut, butarr):
        x = len(lastbut)
        y = len(newbut)
        if x != y:
            print("the last button array and new button array are not equal")
        for i in range(x):
            if lastbut[i] != newbut[i]:

                print("button ", butarr[i], " state change", lastbut[i], ' to ', newbut[i])

                #Speed switch (steps per rotation)
                    # note 1 is pressed and 0 is released
                    # stepper_speed (pos 0 and pos 1)
                if lastbut[var_list.movefast] == 0 and lastbut[var_list.moveslow] == 0:
                    if var_list.stepper_speed != var_list.normalspeed:
                        var_list.stepper_speed = var_list.normalspeed
                        print('switch set to: ',var_list.normalspeed)
                        self.sendtoUI.currentspeed(var_list.stepper_speed)
                elif lastbut[var_list.movefast] == 1 and lastbut[var_list.moveslow] == 0:
                    if var_list.stepper_speed != var_list.fastspeed:
                        var_list.stepper_speed = var_list.fastspeed
                        print('switch set to: ', var_list.fastspeed)
                        self.sendtoUI.currentspeed(var_list.stepper_speed)
                elif lastbut[var_list.movefast] == 0 and lastbut[var_list.moveslow] == 1:
                    if var_list.stepper_speed != var_list.finespeed:
                        var_list.stepper_speed = var_list.finespeed
                        print('switch set to: ', var_list.finespeed)
                        self.sendtoUI.currentspeed(var_list.stepper_speed)
                    else:
                        print('switch not working right')

                #button to home to ABS zero
                if lastbut[var_list.homeABSzero] == 1:
                    print('HOME to ABS Zero')
                    self.sendtoUI.thread_start('hometoABSzero')

                #set relative zero for ALL
                if lastbut[var_list.relativeALL] == 1:
                    print('set relative positions form all three')
                    self.sendtoUI.thread_start('setrelforall')
                        # and then update LCDS

                #set only AP relative zero
                if lastbut[var_list.relativeAP] == 1:
                    print('set relative AP')
                    self.sendtoUI.thread_start('setrelforAP')

                # set only ML relative zero
                if lastbut[var_list.relativeML] == 1:
                    print('set relative ML')
                    self.sendtoUI.thread_start('setrelforML')

                # set only DV relative zero
                if lastbut[var_list.relativeDV] == 1:
                    print('set relative DV')
                    self.sendtoUI.thread_start('setrelforDV')

                #button action - Home to Rel zero for AP and ML BUT DV goes all up
                if lastbut[var_list.homeRELzero] == 1:
                    print('DV up AP and ML homed to rel')
                    self.sendtoUI.thread_start('upDVrelhomeAP_ML')

                #miscbuttonC - DRILL to relative zero for AP and ML BUT DV homed ABS zero but still sets the relative pos
                if lastbut[var_list.drilloff] == 1:
                    print('Drill offset start thread')
                    self.sendtoUI.thread_start('drillmovetooffset')

                #miscbuttonD - needle to relative zero for AP and ML BUT DV homed ABS zero but still sets the relative pos
                if lastbut[var_list.needleoff] == 1:
                    print('Needle offset start thread')
                    self.sendtoUI.thread_start('needlemovetooffset')

                #miscbuttonE - fiber to relative zero for AP and ML BUT DV homed ABS zero but still sets the relative pos
                if lastbut[var_list.fiberoff] == 1:
                    print('Fiber offset start thread')
                    self.sendtoUI.thread_start('fibermovetooffset')

                #home to bregma (relative) moves DV up ~10mm, positions AP and ML to relative home
                if lastbut[var_list.bregmahome] == 1:
                    print("That's bregma G!")
                    self.sendtoUI.thread_start('bregmahome')

                #re-calibrate button
                if lastbut[var_list.recalibrate] == 1:
                    print("Trying to recalibrate")
                    self.sendtoUI.thread_start('recalibrateaxis')

                #miscbuttonA - unused
                if lastbut[var_list.miscbuttonA] == 1:
                    print('unused button A')

                #miscbuttonB - unused
                if lastbut[var_list.miscbuttonB] == 1:
                    print('unused button B')

                lastbut[i] = newbut[i]


    # #Speed switch (steps per rotation)
    #     # note 1 is pressed and 0 is released
    #     # stepper_speed (pos 0 and pos 1)
    #     if lastbut[var_list.movefast] == 0 and lastbut[var_list.moveslow] == 0:
    #         if var_list.stepper_speed != var_list.normalspeed:
    #             var_list.stepper_speed = var_list.normalspeed
    #             print('switch set to: ',var_list.normalspeed)
    #             self.sendtoUI.currentspeed(var_list.stepper_speed)
    #     elif lastbut[var_list.movefast] == 1 and lastbut[var_list.moveslow] == 0:
    #         if var_list.stepper_speed != var_list.fastspeed:
    #             var_list.stepper_speed = var_list.fastspeed
    #             print('switch set to: ', var_list.fastspeed)
    #             self.sendtoUI.currentspeed(var_list.stepper_speed)
    #     elif lastbut[var_list.movefast] == 0 and lastbut[var_list.moveslow] == 1:
    #         if var_list.stepper_speed != var_list.finespeed:
    #             var_list.stepper_speed = var_list.finespeed
    #             print('switch set to: ', var_list.finespeed)
    #             self.sendtoUI.currentspeed(var_list.stepper_speed)
    #     else:
    #         print('switch not working right')
    #
    # #button to home to ABS zero
    #     if lastbut[var_list.homeABSzero] == 1:
    #         print('HOME to ABS Zero')
    #         self.sendtoUI.thread_start('hometoABSzero')
    #
    # #set relative zero for ALL
    #     if lastbut[var_list.relativeALL] == 1:
    #         print('set relative positions form all three')
    #         self.sendtoUI.thread_start('setrelforall')
    #         # and then update LCDS
    #
    # #set only AP relative zero
    #     if lastbut[var_list.relativeAP] == 1:
    #         print('set relative AP')
    #         self.sendtoUI.thread_start('setrelforAP')
    #
    # # set only ML relative zero
    #     if lastbut[var_list.relativeML] == 1:
    #         print('set relative ML')
    #         self.sendtoUI.thread_start('setrelforML')
    #
    # # set only DV relative zero
    #     if lastbut[var_list.relativeDV] == 1:
    #         print('set relative DV')
    #         self.sendtoUI.thread_start('setrelforDV')
    #
    # #button action - Home to Rel zero for AP and ML BUT DV goes all up
    #     if lastbut[var_list.homeRELzero] == 1:
    #         print('DV up AP and ML homed to rel')
    #         self.sendtoUI.thread_start('upDVrelhomeAP_ML')
    #
    # #miscbuttonC - DRILL to relative zero for AP and ML BUT DV homed ABS zero but still sets the relative pos
    #     if lastbut[var_list.drilloff] == 1:
    #         print('Drill offset start thread')
    #         self.sendtoUI.thread_start('drillmovetooffset')
    #
    # #miscbuttonD - needle to relative zero for AP and ML BUT DV homed ABS zero but still sets the relative pos
    #     if lastbut[var_list.needleoff] == 1:
    #         print('Needle offset start thread')
    #         self.sendtoUI.thread_start('needlemovetooffset')
    #
    # #miscbuttonE - fiber to relative zero for AP and ML BUT DV homed ABS zero but still sets the relative pos
    #     if lastbut[var_list.fiberoff] == 1:
    #         print('Fiber offset start thread')
    #         self.sendtoUI.thread_start('fibermovetooffset')
    #
    # #home to bregma (relative) moves DV up ~10mm, positions AP and ML to relative home
    #     if lastbut[var_list.bregmahome] == 1:
    #         print("That's bregma G!")
    #         self.sendtoUI.thread_start('bregmahome')
    #
    # #re-calibrate button
    #     if lastbut[var_list.recalibrate] == 1:
    #         print("Trying to recalibrate")
    #         self.sendtoUI.thread_start('recalibrateaxis')
    #
    # #miscbuttonA - unused
    #     if lastbut[var_list.miscbuttonA] == 1:
    #         print('unused button A')
    #
    # #miscbuttonB - unused
    #     if lastbut[var_list.miscbuttonB] == 1:
    #         print('unused button B')

        return lastbut


    #MAIN CODE ################################################################################################
    def runbuttonthread(self):

        while var_list.keepalive:
        #reading the buttons
            newbuttonstate = self.getshiftregisterdata()
            var_list.lastbuttonstate = self.buttonvalues(var_list.lastbuttonstate, newbuttonstate, var_list.buttonarray)