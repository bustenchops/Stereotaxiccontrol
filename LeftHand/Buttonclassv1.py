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
        self.offtoggleold = 1


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
            print("Button Array detected state change")
        for i in range(x):
            if lastbut[i] != newbut[i]:

                print("button ", butarr[i], " state change", lastbut[i], ' to ', newbut[i])

                if var_list.engagebuttons == 1:
                    #full retract
                    if lastbut[var_list.fullretract] == 1:
                        if var_list.safetybutton == 1:
                            print('retract all manipulators')
                            self.fullretract()
                            var_list.safetybutton = 0
                            self.sendtoUI.uncheckstuff(4)


                    #set relative zero for ALL
                    if lastbut[var_list.relativeALL] == 1:
                        print('set relative positions for all axis')
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

                    #gotolambda
                    if lastbut[var_list.gotolambdabut] == 1:
                        if var_list.safetybutton == 1:
                            print('DV up AP and ML homed to rel')
                            self.gotolambda()
                            var_list.safetybutton = 0
                            self.sendtoUI.uncheckstuff(4)

                    #offset select
                    if lastbut[var_list.offposone] == 1 & lastbut[var_list.offpostwo] == 0:
                        var_list.TOGGLEoff = 1
                    if lastbut[var_list.offposone] == 0 & lastbut[var_list.offpostwo] == 0:
                        var_list.TOGGLEoff = 2
                    if lastbut[var_list.offposone] == 0 & lastbut[var_list.offpostwo] == 1:
                        var_list.TOGGLEoff = 3

                    #ratormouse select
                    if lastbut[var_list.ratselect] == 1 & lastbut[var_list.mouseselect] == 0:
                        var_list.ratormouseselect = 1
                        self.ratormouse()
                    if lastbut[var_list.offposone] == 0 & lastbut[var_list.offpostwo] == 0:
                        var_list.ratormouseselect = 3
                    if lastbut[var_list.ratselect] == 0 & lastbut[var_list.mouseselect] == 1:
                        var_list.ratormouseselect = 2
                        self.ratormouse()


                    #home to bregma (relative) moves DV up by value in variable list, positions AP and ML to relative home
                    if lastbut[var_list.bregmahome] == 1:
                        if var_list.safetybutton == 1:
                            print("Home to Bregma (DV up buy set value)")
                            self.bregmahome()
                            var_list.safetybutton = 0
                            self.sendtoUI.uncheckstuff(4)

                    #rezero button
                    if lastbut[var_list.rezero] == 1:
                        if var_list.safetybutton == 1:
                            print("Re-Zero the steppers")
                            self.sendtoUI.recalibrateaxis()
                            var_list.safetybutton = 0
                            self.sendtoUI.uncheckstuff(4)

                    #home to ABS zero
                    if lastbut[var_list.ABSzero] == 1:
                        if var_list.safetybutton == 1:
                            self.hometoABSzero()
                            var_list.safetybutton = 0
                            self.sendtoUI.uncheckstuff(4)

                    #home AP and ML, DV goes to ABS
                    if lastbut[var_list.bregmahomeDVabs] == 1:
                        if var_list.safetybutton == 1:
                            self.upDVrelhomeAP_ML()
                            var_list.safetybutton = 0
                            self.sendtoUI.uncheckstuff(4)

                    #Hmome AP and ML to bregma and DV up 5.
                    if lastbut[var_list.bregmahomeDVupfive] == 1:
                        if var_list.safetybutton == 1:
                            self.homeDVupfive()
                            var_list.safetybutton = 0
                            self.sendtoUI.uncheckstuff(4)

                    #go to preset
                    if lastbut[var_list.gotopreset] == 1:
                        if var_list.safetybutton == 1:
                            if self.offtoggleold != var_list.TOGGLEoff:
                                self.offtoggleold = var_list.TOGGLEoff
                                if self.offtoggleold == 1:
                                    self.drillmovetooffset()
                                    print('send to drill working')
                                if self.offtoggleold == 2:
                                    self.needlemovetooffset()
                                    print('send to needle working')
                                if self.offtoggleold == 3:
                                    self.fibermovetooffset()
                                    print('send to probe working')

                            else:
                                self.sendtoworking()
                                var_list.safetybutton = 0
                                self.sendtoUI.uncheckstuff(4)


                    #selectup

                    #selectdown

                    #armbut

                    #engagebut

                    #makeitsobut

                    #DVinsert

                    #withdrawl

                    #retractAP

                    #returnAP

                    #retractDV

                    #returnDV

                    #functionone

                    #functiontwo



                lastbut[i] = newbut[i]

        # Speed switch
        if lastbut[var_list.movefast] == 0 and lastbut[var_list.moveslow] == 0:
            if var_list.stepper_speed != var_list.normalspeed:
                var_list.stepper_speed = var_list.normalspeed
                print('Speed set to: ', var_list.normalspeed)
                self.sendtoUI.currentspeed(var_list.stepper_speed)
                self.sendtoUI.setmedspeed()
        elif lastbut[var_list.movefast] == 1 and lastbut[var_list.moveslow] == 0:
            if var_list.stepper_speed != var_list.fastspeed:
                var_list.stepper_speed = var_list.fastspeed
                print('Speed set to: ', var_list.fastspeed)
                self.sendtoUI.currentspeed(var_list.stepper_speed)
                self.sendtoUI.setcoarsespeed()
        elif lastbut[var_list.movefast] == 0 and lastbut[var_list.moveslow] == 1:
            if var_list.stepper_speed != var_list.finespeed:
                var_list.stepper_speed = var_list.finespeed
                print('Speed set to: ', var_list.finespeed)
                self.sendtoUI.currentspeed(var_list.stepper_speed)
                self.sendtoUI.setfinespeed()
        else:
            print('speedswitch not working right')

        return lastbut

#Button executes
    def ratormouse(self):
        if var_list.ratormouseselect == 2:
            var_list.ratormouseselect = 1
            self.sendtoUI.mouseselected()
        elif var_list.ratormouseselect == 1:
            var_list.ratormouseselect = 2
            self.sendtoUI.ratselected()


    def gotolambda(self):
        if var_list.ratormouseselect == 1:
            var_list.rellambda = var_list.APrelpos - var_list.mouselambda
        if var_list.ratormouseselect == 2:
            var_list.rellambda = var_list.APrelpos - var_list.ratlambda
        if var_list.ratormouseselect == 3:
            var_list.rellambda = var_list.APrelpos

        go_upDVby = var_list.DVrelpos - var_list.DVup_lambdabregma
        if (var_list.DVsteps > go_upDVby):
            DVdiff = var_list.DVsteps - go_upDVby
            for x in range(DVdiff):
                var_list.DVmove.steppgo(var_list.DVup, var_list.finespeed, var_list.btnSteps)
        else:
            DVdiff = go_upDVby - var_list.DVsteps
            for x in range(DVdiff):
                var_list.DVmove.steppgo(var_list.DVdown, var_list.finespeed, var_list.btnSteps)

        print(var_list.APrelpos, "APRelative")
        print(var_list.APsteps, "APsteps")

        if var_list.rellambda > var_list.APsteps:
            APdiff = var_list.rellambda - var_list.APsteps
            print('back')
            for x in range(APdiff):
                var_list.APmove.steppgo(var_list.APback, var_list.finespeed, var_list.btnSteps)
        else:
            APdiff = var_list.APsteps - var_list.rellambda
            print('forward')
            for x in range(APdiff):
                var_list.APmove.steppgo(var_list.APforward, var_list.finespeed, var_list.btnSteps)

        print(var_list.MLrelpos, "mlRelative")
        print(var_list.MLsteps, "mlsteps")

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

        GPIO.output(var_list.enableAll, 1)
        var_list.lastenablestate = 1

    def hometoABSzero(self):
        print('home the ABS zero')
        for x in range(var_list.DVsteps):
            var_list.DVmove.steppgo(var_list.DVup, var_list.finespeed, var_list.btnSteps)
        for x in range(var_list.MLsteps):
            var_list.MLmove.steppgo(var_list.MLright, var_list.finespeed, var_list.btnSteps)
        for x in range(var_list.APsteps):
            var_list.APmove.steppgo(var_list.APforward, var_list.finespeed, var_list.btnSteps)
        var_list.APmove.PosRelAbsCalc()
        var_list.MLmove.PosRelAbsCalc()
        var_list.DVmove.PosRelAbsCalc()

        GPIO.output(var_list.enableAll, 1)
        var_list.lastenablestate = 1

    def upDVrelhomeAP_ML(self):
        print('relative home AP and ML homed DVup')
        for x in range(var_list.DVsteps):
            var_list.DVmove.steppgo(var_list.DVup, var_list.finespeed, var_list.btnSteps)

        if var_list.MLrelpos > var_list.MLsteps:
            shiftdistance = var_list.MLrelpos - var_list.MLsteps
            for x in range(shiftdistance):
                var_list.MLmove.steppgo(var_list.MLright, var_list.finespeed, var_list.btnSteps)
        elif var_list.MLsteps > var_list.MLrelpos:
            shiftdistance = var_list.MLsteps - var_list.MLrelpos
            for x in range(shiftdistance):
                var_list.MLmove.steppgo(var_list.MLleft, var_list.finespeed, var_list.btnSteps)

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

        GPIO.output(var_list.enableAll, 1)
        var_list.lastenablestate = 1

    # this if a function to disable the steppers...it has not seen much use so it does not currently have have a button call
    def endisstep(self):
        if var_list.safetybutton == 1:
            if var_list.lastenablestate == 1:
                GPIO.output(var_list.enableAll, 0)
                var_list.lastenablestate = 0
                print('steppers ENABLED manually')
            else:
                GPIO.output(var_list.enableAll, 1)
                var_list.lastenablestate = 1
                print('steppers DISABLED manually')
            var_list.safetybutton = 0


    def setrelforall(self):
        print('set relative for ALL - fromButtonthread')
        var_list.APrelpos = var_list.APsteps
        var_list.MLrelpos = var_list.MLsteps
        var_list.DVrelpos = var_list.DVsteps

        if var_list.TOGGLEoff == 1:
            var_list.APinitREL_holdvalue = var_list.APsteps
            var_list.MLinitREL_holdvalue = var_list.MLsteps
            var_list.DVinitREL_holdvalue = var_list.DVsteps

        var_list.APmove.PosRelAbsCalc()
        var_list.MLmove.PosRelAbsCalc()
        var_list.DVmove.PosRelAbsCalc()

    def setrelforAP(self):
        print('set relative for AP')
        var_list.APrelpos = var_list.APsteps
        if var_list.TOGGLEoff == 1:
            var_list.APinitREL_holdvalue = var_list.APsteps
        var_list.APmove.PosRelAbsCalc()

    def setrelforML(self):
        print('set relative for ML')
        var_list.MLrelpos = var_list.MLsteps
        if var_list.TOGGLEoff == 1:
            var_list.MLinitREL_holdvalue = var_list.MLsteps
        var_list.MLmove.PosRelAbsCalc()

    def setrelforDV(self):
        print('set relative for DV')
        var_list.DVrelpos = var_list.DVsteps
        if var_list.TOGGLEoff == 1:
            var_list.DVinitREL_holdvalue = var_list.DVsteps
        var_list.DVmove.PosRelAbsCalc()

    def fullretract(self):
        print('home to ABS zero')
        for x in range(var_list.DVsteps):
            var_list.DVmove.steppgo(var_list.DVup, var_list.finespeed, var_list.btnSteps)
        fullMLretractdiff = var_list.fullretractML - var_list.MLsteps
        for x in range(fullMLretractdiff):
            var_list.MLmove.steppgo(var_list.MLleft, var_list.finespeed, var_list.btnSteps)
        fullretraactdiff = var_list.fullretract - var_list.APsteps
        for x in range(fullretraactdiff):
            var_list.APmove.steppgo(var_list.APback, var_list.finespeed, var_list.btnSteps)
        var_list.APmove.PosRelAbsCalc()
        var_list.MLmove.PosRelAbsCalc()
        var_list.DVmove.PosRelAbsCalc()

        GPIO.output(var_list.enableAll, 1)
        var_list.lastenablestate = 1

    def upDVrelhomeAP_ML(self):
        print('relative home AP and ML homed DVup')
        for x in range(var_list.DVsteps):
            var_list.DVmove.steppgo(var_list.DVup, var_list.finespeed, var_list.btnSteps)

        if var_list.MLrelpos > var_list.MLsteps:
            shiftdistance = var_list.MLrelpos - var_list.MLsteps
            for x in range(shiftdistance):
                var_list.MLmove.steppgo(var_list.MLleft, var_list.finespeed, var_list.btnSteps)
        elif var_list.MLsteps > var_list.MLrelpos:
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

        GPIO.output(var_list.enableAll, 1)
        var_list.lastenablestate = 1

    def drillmovetooffset(self):
        #print('offset set to DRILL')
        #self.sendtoUI.uitest()
        print('Moving to home position first')
        self.bregmahome()
        print('Move to drill offset')
        self.sendtoUI.drilloffset()

        self.DrillAPmm = var_list.DrillAPmm
        self.DrillMLmm = var_list.DrillMLmm
        self.DrillDVmm = var_list.DrillDVmm

        if var_list.TOGGLEoff != 1:

            self.AP_Doffsetcalc = int(self.DrillAPmm / var_list.APstepdistance)
            self.ML_Doffsetcalc = int(self.DrillMLmm / var_list.MLstepdistance)
            self.DV_Doffsetcalc = int(self.DrillDVmm / var_list.DVstepdistance)

            print(self.AP_Doffsetcalc,'AP calc')
            print(self.ML_Doffsetcalc,'ML calc')
            print(self.DV_Doffsetcalc,'DV calc')

            self.DVdifferential = abs(var_list.DVcurrentoffsset)
            self.MLdifferential = abs(var_list.MLcurrentoffsset)
            self.APdifferential = abs(var_list.APcurrentoffsset)

            print(self.DVdifferential,"DV differential")
            print(self.MLdifferential,"ML differential")
            print(self.APdifferential,"AP differential")
            print(var_list.TOGGLEoff, 'toggle drill')

            for x in range(var_list.DVup_OffsetSafety):
                var_list.DVmove.steppgo(var_list.DVup, var_list.finespeed, var_list.btnSteps)

            if var_list.APcurrentoffsset > self.AP_Doffsetcalc:
                for x in range (self.APdifferential):
                    var_list.APmove.steppgo(var_list.APforward, var_list.finespeed, var_list.btnSteps)
            elif var_list.APcurrentoffsset < self.AP_Doffsetcalc:
                for x in range (self.APdifferential):
                    var_list.APmove.steppgo(var_list.APback, var_list.finespeed, var_list.btnSteps)

            if var_list.MLcurrentoffsset < self.ML_Doffsetcalc:
                for x in range (self.MLdifferential):
                    var_list.MLmove.steppgo(var_list.MLright, var_list.finespeed, var_list.btnSteps)
            elif var_list.MLcurrentoffsset > self.ML_Doffsetcalc:
                for x in range (self.MLdifferential):
                    var_list.MLmove.steppgo(var_list.MLleft, var_list.finespeed, var_list.btnSteps)

            if var_list.DVcurrentoffsset < self.DV_Doffsetcalc:
                for x in range (self.DVdifferential):
                    var_list.DVmove.steppgo(var_list.DVup, var_list.finespeed, var_list.btnSteps)
            elif var_list.DVcurrentoffsset > self.DV_Doffsetcalc:
                for x in range (self.DVdifferential):
                    var_list.DVmove.steppgo(var_list.DVdown, var_list.finespeed, var_list.btnSteps)

            for x in range(var_list.DVup_OffsetSafety):
                var_list.DVmove.steppgo(var_list.DVdown, var_list.finespeed, var_list.btnSteps)

            var_list.APcurrentoffsset = self.AP_Doffsetcalc
            var_list.MLcurrentoffsset = self.ML_Doffsetcalc
            var_list.DVcurrentoffsset = self.DV_Doffsetcalc

            print(var_list.APcurrentoffsset,"AP currentoffsset")
            print(var_list.MLcurrentoffsset,"ML currentoffsset")
            print(var_list.DVcurrentoffsset,"DV currentoffsset")

            var_list.APrelpos = var_list.APsteps
            var_list.MLrelpos = var_list.MLsteps
            var_list.DVrelpos = var_list.DVsteps

            var_list.APmove.PosRelAbsCalc()
            var_list.MLmove.PosRelAbsCalc()
            var_list.DVmove.PosRelAbsCalc()

            GPIO.output(var_list.enableAll, 1)
            var_list.lastenablestate = 1
            var_list.TOGGLEoff = 1

    def needlemovetooffset(self):
        # print('offset set to Needle')
        # self.sendtoUI.uitest()
        print('Moving to home position first')
        self.bregmahome()
        print('Move to Syringe Offset')
        self.sendtoUI.needleoffset()

        self.NeedleAPmm = var_list.NeedleAPmm
        self.NeedleMLmm = var_list.NeedleMLmm
        self.NeedleDVmm = var_list.NeedleDVmm

        if var_list.TOGGLEoff != 2:

            print (self.NeedleAPmm)
            print (self.NeedleMLmm)
            print (self.NeedleDVmm)

            self.AP_Noffsetcalc = int(self.NeedleAPmm/ var_list.APstepdistance)
            self.ML_Noffsetcalc = int(self.NeedleMLmm / var_list.MLstepdistance)
            self.DV_Noffsetcalc = int(self.NeedleDVmm / var_list.DVstepdistance)

            print(self.AP_Noffsetcalc,'AP calc')
            print(self.ML_Noffsetcalc,'ML calc')
            print(self.DV_Noffsetcalc,'DV calc')

            for x in range(var_list.DVup_OffsetSafety):
                var_list.DVmove.steppgo(var_list.DVup, var_list.finespeed, var_list.btnSteps)

            if self.AP_Noffsetcalc > var_list.APcurrentoffsset:
                self.APdifferential = abs(self.AP_Noffsetcalc - var_list.APcurrentoffsset)
                for x in range(self.APdifferential):
                    var_list.APmove.steppgo(var_list.APback, var_list.finespeed, var_list.btnSteps)
            elif self.AP_Noffsetcalc < var_list.APcurrentoffsset:
                self.APdifferential = abs(var_list.APcurrentoffsset - self.AP_Noffsetcalc)
                for x in range(self.APdifferential):
                    var_list.APmove.steppgo(var_list.APforward, var_list.finespeed, var_list.btnSteps)

            if self.ML_Noffsetcalc > var_list.MLcurrentoffsset:
                self.MLdifferential = abs(self.ML_Noffsetcalc - var_list.MLcurrentoffsset)
                for x in range(self.MLdifferential):
                    var_list.MLmove.steppgo(var_list.MLright, var_list.finespeed, var_list.btnSteps)
            elif self.ML_Noffsetcalc < var_list.MLcurrentoffsset:
                self.MLdifferential = abs(var_list.MLcurrentoffsset - self.ML_Noffsetcalc)
                for x in range(self.MLdifferential):
                    var_list.MLmove.steppgo(var_list.MLleft, var_list.finespeed, var_list.btnSteps)

            if self.DV_Noffsetcalc > var_list.DVcurrentoffsset:
                self.DVdifferential = abs(self.DV_Noffsetcalc - var_list.DVcurrentoffsset)
                for x in range(self.DVdifferential):
                    var_list.DVmove.steppgo(var_list.DVup, var_list.finespeed, var_list.btnSteps)
            elif self.DV_Noffsetcalc < var_list.DVcurrentoffsset:
                self.DVdifferential = abs(var_list.DVcurrentoffsset - self.DV_Noffsetcalc)
                for x in range(self.DVdifferential):
                    var_list.DVmove.steppgo(var_list.DVdown, var_list.finespeed, var_list.btnSteps)

            for x in range(var_list.DVup_OffsetSafety):
                var_list.DVmove.steppgo(var_list.DVdown, var_list.finespeed, var_list.btnSteps)

            print(self.DVdifferential,"DV differential")
            print(self.MLdifferential,"ML differential")
            print(self.APdifferential,"AP differential")
            print(var_list.TOGGLEoff, 'toggle')

            var_list.APcurrentoffsset = self.AP_Noffsetcalc
            var_list.MLcurrentoffsset = self.ML_Noffsetcalc
            var_list.DVcurrentoffsset = self.DV_Noffsetcalc

            print(var_list.APcurrentoffsset,"AP currentoffsset")
            print(var_list.MLcurrentoffsset,"ML currentoffsset")
            print(var_list.DVcurrentoffsset,"DV currentoffsset")

            var_list.APrelpos = var_list.APsteps
            var_list.MLrelpos = var_list.MLsteps
            var_list.DVrelpos = var_list.DVsteps

            var_list.APmove.PosRelAbsCalc()
            var_list.MLmove.PosRelAbsCalc()
            var_list.DVmove.PosRelAbsCalc()

            GPIO.output(var_list.enableAll, 1)
            var_list.lastenablestate = 1
            var_list.TOGGLEoff = 2

    def fibermovetooffset(self):
        # print('offset set to Fiber')
        # self.sendtoUI.uitest()
        print('Moving to home position first')
        self.bregmahome()
        print('Move to Probe offset')
        self.sendtoUI.probeoffset()

        self.FiberAPmm = var_list.FiberAPmm
        self.FiberMLmm = var_list.FiberMLmm
        self.FiberDVmm = var_list.FiberDVmm

        if var_list.TOGGLEoff != 3:

            print (self.FiberAPmm)
            print (self.FiberMLmm)
            print (self.FiberDVmm)

            self.AP_Foffsetcalc = int(self.FiberAPmm/ var_list.APstepdistance)
            self.ML_Foffsetcalc = int(self.FiberMLmm / var_list.MLstepdistance)
            self.DV_Foffsetcalc = int(self.FiberDVmm / var_list.DVstepdistance)

            print(self.AP_Foffsetcalc,'AP calc')
            print(self.ML_Foffsetcalc,'ML calc')
            print(self.DV_Foffsetcalc,'DV calc')

            for x in range(var_list.DVup_OffsetSafety):
                var_list.DVmove.steppgo(var_list.DVup, var_list.finespeed, var_list.btnSteps)

            if self.AP_Foffsetcalc > var_list.APcurrentoffsset:
                self.APdifferential = abs(self.AP_Foffsetcalc - var_list.APcurrentoffsset)
                for x in range(self.APdifferential):
                    var_list.APmove.steppgo(var_list.APback, var_list.finespeed, var_list.btnSteps)
            elif self.AP_Foffsetcalc < var_list.APcurrentoffsset:
                self.APdifferential = abs(var_list.APcurrentoffsset - self.AP_Foffsetcalc)
                for x in range(self.APdifferential):
                    var_list.APmove.steppgo(var_list.APforward, var_list.finespeed, var_list.btnSteps)

            if self.ML_Foffsetcalc > var_list.MLcurrentoffsset:
                self.MLdifferential = abs(self.ML_Foffsetcalc - var_list.MLcurrentoffsset)
                for x in range(self.MLdifferential):
                    var_list.MLmove.steppgo(var_list.MLright, var_list.finespeed, var_list.btnSteps)
            elif self.ML_Foffsetcalc < var_list.MLcurrentoffsset:
                self.MLdifferential = abs(var_list.MLcurrentoffsset - self.ML_Foffsetcalc)
                for x in range(self.MLdifferential):
                    var_list.MLmove.steppgo(var_list.MLleft, var_list.finespeed, var_list.btnSteps)

            if self.DV_Foffsetcalc > var_list.DVcurrentoffsset:
                self.DVdifferential = abs(self.DV_Foffsetcalc - var_list.DVcurrentoffsset)
                for x in range(self.DVdifferential):
                    var_list.DVmove.steppgo(var_list.DVup, var_list.finespeed, var_list.btnSteps)
            elif self.DV_Foffsetcalc < var_list.DVcurrentoffsset:
                self.DVdifferential = abs(var_list.DVcurrentoffsset - self.DV_Foffsetcalc)
                for x in range(self.DVdifferential):
                    var_list.DVmove.steppgo(var_list.DVdown, var_list.finespeed, var_list.btnSteps)

            for x in range(var_list.DVup_OffsetSafety):
                var_list.DVmove.steppgo(var_list.DVdown, var_list.finespeed, var_list.btnSteps)

            print(self.DVdifferential,"DV differential")
            print(self.MLdifferential,"ML differential")
            print(self.APdifferential,"AP differential")
            print(var_list.TOGGLEoff, 'toggle')


            var_list.APcurrentoffsset = self.AP_Foffsetcalc
            var_list.MLcurrentoffsset = self.ML_Foffsetcalc
            var_list.DVcurrentoffsset = self.DV_Foffsetcalc

            print(var_list.APcurrentoffsset,"AP currentoffsset")
            print(var_list.MLcurrentoffsset,"ML currentoffsset")
            print(var_list.DVcurrentoffsset,"DV currentoffsset")

            var_list.APrelpos = var_list.APsteps
            var_list.MLrelpos = var_list.MLsteps
            var_list.DVrelpos = var_list.DVsteps

            var_list.APmove.PosRelAbsCalc()
            var_list.MLmove.PosRelAbsCalc()
            var_list.DVmove.PosRelAbsCalc()

            GPIO.output(var_list.enableAll, 1)
            var_list.lastenablestate = 1
            var_list.TOGGLEoff = 3

    def homeDVupfive(self):
        print('goto bregma but lift DV up by value in variable list')
        for x in range(var_list.DVup_five):
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

        GPIO.output(var_list.enableAll, 1)
        var_list.lastenablestate = 1


    def bregmahome(self):
        print('goto bregma but lift DV up by value in variable list')
        go_upDVby = var_list.DVrelpos - var_list.DVup_bregramhome
        if (var_list.DVsteps > go_upDVby):
            DVdiff = var_list.DVsteps - go_upDVby
            for x in range(DVdiff):
                var_list.DVmove.steppgo(var_list.DVup, var_list.finespeed, var_list.btnSteps)
        else:
            DVdiff = go_upDVby - var_list.DVsteps
            for x in range(DVdiff):
                var_list.DVmove.steppgo(var_list.DVdown, var_list.finespeed, var_list.btnSteps)

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

        GPIO.output(var_list.enableAll, 1)
        var_list.lastenablestate = 1

    def sendtoworking(self):
        print('this is sendtoworking')

        self.MLstepdiff = abs(var_list.MLsteps - var_list.MLworking)
        self.APstepdiff = abs(var_list.APsteps - var_list.APworking)
        self.DVstepdiff = abs(var_list.DVsteps - var_list.DVworking)
        print('ml',self.MLstepdiff,'ap',self.APstepdiff,'dv',self.DVstepdiff)

        print(var_list.MLsteps,"MLsteps")
        print(var_list.MLworking,"MLworking")

        if var_list.MLsteps > var_list.MLworking:
            print('right')
            for x in range(self.MLstepdiff):
                var_list.MLmove.steppgo(var_list.MLright, var_list.finespeed, var_list.btnSteps)
        elif var_list.MLsteps < var_list.MLworking:
            print('left')
            for x in range(self.MLstepdiff):
                var_list.MLmove.steppgo(var_list.MLleft, var_list.finespeed, var_list.btnSteps)

        print(var_list.APsteps,"APsteps")
        print(var_list.APworking,"APworking")

        if var_list.APsteps > var_list.APworking:
            print('forward')
            for x in range(self.APstepdiff):
                var_list.APmove.steppgo(var_list.APforward, var_list.finespeed, var_list.btnSteps)
        elif var_list.APsteps < var_list.APworking:
            print('back')
            for x in range(self.APstepdiff):
                var_list.APmove.steppgo(var_list.APback, var_list.finespeed, var_list.btnSteps)

        print(var_list.DVsteps,"DVsteps")
        print(var_list.DVworking,"DVworking")

        if var_list.DVsteps > var_list.DVworking:
            print('up')
            for x in range(self.DVstepdiff):
                var_list.DVmove.steppgo(var_list.DVup, var_list.finespeed, var_list.btnSteps)
        elif var_list.DVsteps < var_list.DVworking:
            print('down')
            for x in range(self.DVstepdiff):
                var_list.DVmove.steppgo(var_list.DVdown, var_list.finespeed, var_list.btnSteps)

        var_list.APrelpos = var_list.APsteps
        var_list.MLrelpos = var_list.MLsteps
        var_list.DVrelpos = var_list.DVsteps

        var_list.APmove.PosRelAbsCalc()
        var_list.MLmove.PosRelAbsCalc()
        var_list.DVmove.PosRelAbsCalc()

        GPIO.output(var_list.enableAll, 1)
        var_list.lastenablestate = 1
        self.sendtoUI.drilloffset()
        var_list.TOGGLEoff = 1

# concept and code created by Kirk Mulatz (original code https://github.com/bustenchops/Stereotaxiccontrol (experiment branch)



    #MAIN CODE ################################################################################################
    def runbuttonthread(self):
        print('Button thread started')
        while var_list.keepalive:
        #reading the buttons
            newbuttonstate = self.getshiftregisterdata()
            var_list.lastbuttonstate = self.buttonvalues(var_list.lastbuttonstate, newbuttonstate, var_list.buttonarray)
