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

                #button to home to ABS zero
                if lastbut[var_list.homeABSzero] == 1:
                    print('HOME to ABS Zero')
                    self.hometoABSzero()

                #set relative zero for ALL
                if lastbut[var_list.relativeALL] == 1:
                    print('set relative positions for all three')
                    self.setrelforall()
                        # and then update LCDS

                #set only AP relative zero
                if lastbut[var_list.relativeAP] == 1:
                    print('set relative AP')
                    self.setrelforAP()

                # set only ML relative zero
                if lastbut[var_list.relativeML] == 1:
                    print('set relative ML')
                    self.setrelforML()

                # set only DV relative zero
                if lastbut[var_list.relativeDV] == 1:
                    print('set relative DV')
                    self.setrelforDV()

                #button action - Home to Rel zero for AP and ML BUT DV goes all up
                if lastbut[var_list.homeRELzero] == 1:
                    print('DV up AP and ML homed to rel')
                    self.upDVrelhomeAP_ML()

                #miscbuttonC - DRILL to relative zero for AP and ML - DV up 0.5cm but still sets the relative pos
                if lastbut[var_list.drilloff] == 1:
                    print('Drill offset start thread')
                    self.drillmovetooffset()

                #miscbuttonD - needle to relative zero for AP and ML - DV up 0.5cm but still sets the relative pos
                if lastbut[var_list.needleoff] == 1:
                    print('Needle offset start thread')
                    self.needlemovetooffset()

                #miscbuttonE - fiber to relative zero for AP and ML - DV up 0.5cm but still sets the relative pos
                if lastbut[var_list.fiberoff] == 1:
                    print('Fiber offset start thread')
                    self.fibermovetooffset()

                #home to bregma (relative) moves DV up ~10mm, positions AP and ML to relative home
                if lastbut[var_list.bregmahome] == 1:
                    print("That's bregma G!")
                    self.bregmahome()

                #re-calibrate button
                if lastbut[var_list.recalibrate] == 1:
                    print("Trying to recalibrate")
                    self.sendtoUI.uitest()
                    self.sendtoUI.recalibrateaxis()

                #miscbuttonA - unused
                if lastbut[var_list.miscbuttonA] == 1:
                    print('unused button A')
                    self.sendtoUI.uitest()


                #miscbuttonB - unused
                if lastbut[var_list.miscbuttonB] == 1:
                    print('send to drill working (AP,ML and DV advance')
                    self.sendtoworking()


                lastbut[i] = newbut[i]

        # Speed switch (steps per rotation)
        # note 1 is pressed and 0 is released
        # stepper_speed (pos 0 and pos 1)
        if lastbut[var_list.movefast] == 0 and lastbut[var_list.moveslow] == 0:
            if var_list.stepper_speed != var_list.normalspeed:
                var_list.stepper_speed = var_list.normalspeed
                print('switch set to: ', var_list.normalspeed)
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

        return lastbut

#Button executes

    def setrelforall(self):
        print('set relative for ALL - fromButtonthread')
        var_list.APrelpos = var_list.APsteps
        var_list.MLrelpos = var_list.MLsteps
        var_list.DVrelpos = var_list.DVsteps

        if var_list.APinitREL_holdvalue == 0:
            var_list.APinitREL_holdvalue = var_list.APsteps
        if var_list.MLinitREL_holdvalue == 0:
            var_list.MLinitREL_holdvalue = var_list.MLsteps
        if var_list.DVinitREL_holdvalue == 0:
            var_list.DVinitREL_holdvalue = var_list.DVsteps

        var_list.APmove.PosRelAbsCalc()
        var_list.MLmove.PosRelAbsCalc()
        var_list.DVmove.PosRelAbsCalc()

    def setrelforAP(self):
        print('set relative for AP - fromButtonthread')
        var_list.APrelpos = var_list.APsteps
        var_list.APinitREL_holdvalue = var_list.APsteps
        var_list.APmove.PosRelAbsCalc()

    def setrelforML(self):
        print('set relative for ML - fromButtonthread')
        var_list.MLrelpos = var_list.MLsteps
        var_list.MLinitREL_holdvalue = var_list.MLsteps
        var_list.MLmove.PosRelAbsCalc()

    def setrelforDV(self):
        print('set relative for DV - fromButtonthread')
        var_list.DVrelpos = var_list.DVsteps
        var_list.DVinitREL_holdvalue = var_list.DVsteps
        var_list.DVmove.PosRelAbsCalc()

    def hometoABSzero(self):
        print('home the ABS zero - fromButtonthread')
        for x in range(var_list.DVsteps):
            var_list.DVmove.steppgo(var_list.DVup, var_list.finespeed, var_list.btnSteps)
        for x in range(var_list.MLsteps):
            var_list.MLmove.steppgo(var_list.MLright, var_list.finespeed, var_list.btnSteps)
            var_list.MLmove.steppgo(var_list.MLright, var_list.finespeed, var_list.btnSteps)
        for x in range(var_list.APsteps):
            var_list.APmove.steppgo(var_list.APforward, var_list.finespeed, var_list.btnSteps)
        var_list.APmove.PosRelAbsCalc()
        var_list.MLmove.PosRelAbsCalc()
        var_list.DVmove.PosRelAbsCalc()

    def upDVrelhomeAP_ML(self):
        print('AP and ML homed DVup - from buttonthread')
        for x in range(var_list.DVsteps):
            var_list.DVmove.steppgo(var_list.DVup, var_list.finespeed, var_list.btnSteps)

        print(var_list.MLrelpos,"ML relative")
        print(var_list.MLsteps,"ML steps")

        if var_list.MLrelpos > var_list.MLsteps:
            print('go left')
            shiftdistance = var_list.MLrelpos - var_list.MLsteps
            for x in range(shiftdistance):
                var_list.MLmove.steppgo(var_list.MLleft, var_list.finespeed, var_list.btnSteps)
        elif var_list.MLsteps > var_list.MLrelpos:
            print('go right')
            shiftdistance = var_list.MLsteps - var_list.MLrelpos
            for x in range(shiftdistance):
                var_list.MLmove.steppgo(var_list.MLright, var_list.finespeed, var_list.btnSteps)

        if var_list.APsteps < var_list.APrelpos:
            shiftdistance = var_list.APrelpos - var_list.APsteps
            for x in range(shiftdistance):
                var_list.APmove.steppgo(var_list.APback, var_list.finespeed, var_list.btnSteps)
        elif var_list.APsteps > var_list.APrelpos:
            shiftdistance = var_list.APsteps - var_list.APrelpos
            for x in range(shiftdistance):
                var_list.APmove.steppgo(var_list.APforward, var_list.finespeed, var_list.btnSteps)

        var_list.APmove.PosRelAbsCalc()
        var_list.MLmove.PosRelAbsCalc()
        var_list.DVmove.PosRelAbsCalc()

    def drillmovetooffset(self):
        print('offset set to DRILL')
        self.sendtoUI.uitest()
        self.sendtoUI.drilloffset()

    def needlemovetooffset(self):
        print('offset set to Needle')
        self.sendtoUI.uitest()
        self.sendtoUI.needleoffset()

    def fibermovetooffset(self):
        print('offset set to Fiber')
        self.sendtoUI.uitest()
        self.sendtoUI.probeoffset()

    def bregmahome(self):
        print('goto bregma but lift 1.0cm ~1333 steps')
        if (var_list.DVsteps > 1333):
            for x in range(1333):
                var_list.DVmove.steppgo(var_list.DVup, var_list.finespeed, var_list.btnSteps)
        else:
            for x in range(var_list.DVsteps):
                var_list.DVmove.steppgo(var_list.DVup, var_list.finespeed, var_list.btnSteps)

        print(var_list.APrelpos,"APRelative")
        print(var_list.APsteps,"APsteps")

        if var_list.APrelpos > var_list.APsteps:
            APdiff = var_list.APrelpos - var_list.APsteps
            print('back')
            for x in range(APdiff):
                var_list.APmove.steppgo(var_list.APback, var_list.finespeed, var_list.btnSteps)
        else:
            APdiff = var_list.APsteps - var_list.APrelpos
            print('forward')
            for x in range(APdiff):
                var_list.APmove.steppgo(var_list.APforward, var_list.finespeed, var_list.btnSteps)

        print(var_list.MLrelpos,"mlRelative")
        print(var_list.MLsteps,"mlsteps")

        if var_list.MLrelpos > var_list.MLsteps:
            MLdiff = var_list.MLrelpos - var_list.MLsteps
            print('left')
            for x in range(MLdiff):
                var_list.MLmove.steppgo(var_list.MLleft, var_list.finespeed, var_list.btnSteps)
        else:
            MLdiff = var_list.MLsteps - var_list.MLrelpos
            print('right')
            for x in range(MLdiff):
                var_list.MLmove.steppgo(var_list.MLright, var_list.finespeed, var_list.btnSteps)
        var_list.APmove.PosRelAbsCalc()
        var_list.MLmove.PosRelAbsCalc()
        var_list.DVmove.PosRelAbsCalc()

    def sendtoworking(self):
        print('this is sendtoworking')

        print(var_list.MLsteps,"MLsteps")
        print(var_list.MLworking,"MLworking")

        if var_list.MLsteps > var_list.MLworking:
            print('left')
            self.MLstepdiff = var_list.MLsteps - var_list.MLadvance
            for x in range(self.MLstepdiff):
                var_list.MLmove(var_list.MLleft, var_list.finespeed, var_list.btnSteps)
        elif var_list.MLsteps < var_list.MLadvance:
            print('right')
            self.MLstepdiff = var_list.MLadvance - var_list.MLsteps
            for x in range(self.MLstepdiff):
                var_list.MLmove(var_list.MLright, var_list.finespeed, var_list.btnSteps)

        print(var_list.APsteps,"APsteps")
        print(var_list.APworking,"APworking")

        if var_list.APsteps > var_list.APadvance:
            print('back')
            self.APstepdiff = var_list.APsteps - var_list.APadvance
            for x in range(self.APstepdiff):
                var_list.APmove(var_list.APback, var_list.finespeed, var_list.btnSteps)
        elif var_list.APsteps < var_list.APadvance:
            print('forward')
            self.APstepdiff = var_list.APadvance - var_list.APsteps
            for x in range(self.APstepdiff):
                var_list.APmove(var_list.APforward, var_list.finespeed, var_list.btnSteps)

        print(var_list.DVsteps,"DVsteps")
        print(var_list.DVworking,"DVworking")

        if var_list.DVsteps > var_list.DVworking:
            print('up')
            self.DVstepdiff = var_list.DVsteps - var_list.DVadvance
            for x in range(self.DVstepdiff):
                var_list.DVmove(var_list.DVup, var_list.finespeed, var_list.btnSteps)
        elif var_list.DVsteps < var_list.DVadvance:
            print('down')
            self.DVstepdiff = var_list.DVadvance - var_list.DVsteps
            for x in range(self.DVstepdiff):
                var_list.DVmove(var_list.DVdown, var_list.finespeed, var_list.btnSteps)

        var_list.APmove.PosRelAbsCalc()
        var_list.MLmove.PosRelAbsCalc()
        var_list.DVmove.PosRelAbsCalc()

    #MAIN CODE ################################################################################################
    def runbuttonthread(self):

        while var_list.keepalive:
        #reading the buttons
            newbuttonstate = self.getshiftregisterdata()
            var_list.lastbuttonstate = self.buttonvalues(var_list.lastbuttonstate, newbuttonstate, var_list.buttonarray)