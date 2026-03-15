class var_list:
#FROM BUTTONCLASS *********************************************************

#Main while loop condition
    keepalive = True

#Stepper instances
    APmove = None
    MLmove = None
    DVmove = None


# OFFSETS FOR THE DRILL, Syringe, Needle (minus values is back, left or up)
# in mm using the drill as 0

# Change in the file offsetsXX.txt (XX is LH or RH)
    DrillAPmm = float(0)
    DrillMLmm = float(0)
    DrillDVmm = float(0)

    NeedleAPmm = float(11.1)
    NeedleMLmm = float(-31.22)
    NeedleDVmm = float(5)

    FiberAPmm = float(-20)
    FiberMLmm = float(-21.22)
    FiberDVmm = float(-2)

# variable to let program know which offset of toggled on. 1-drill,2-syringe,3-probe
    TOGGLEoff = 1

# DEFINE NUMBER OF BUTTONS AND ORDER IN ARRAY
    buttonarray = ['movefast', 'bregmahome', 'relativeML', 'relativeAP', 'moveslow',
                   'HomeToABSzero', 'recalibrate', 'miscbuttonA', 'presetworking', 'FiberOffset',
                   'needleoffset', 'drilloffset', 'relativeDV', 'relativeALLset', 'HomerelativeZero',
                   'miscbuttonC']
    lastbuttonstate = [0 for x in range(len(buttonarray))]

# BUTTON POSITION IN SHIFT REGISTER ARRAY
    movefast = 6
    bregmahome = 14
    relativeML = 11
    relativeAP = 9
    moveslow = 7
    homeABSzero =
    recalibrate = 10
    miscbuttonA =  1# speciesselect
    miscbuttonB =  3 # gotoworking preset
    fiberoff = 4
    needleoff = 15
    drilloff = 5
    relativeDV = 0
    relativeALL = 13
    homeRELzero = 12 #gotolambda
    miscbuttonC = 2 #unassigned

#DEFINE EMERGENCY STOP and hard wired buttons
    emergstop = 10
    misc_eventbuttonA = 26
    misc_eventbuttonB = 11

#DEFINE SHIFT REGISTER PINS
    latchpin = 18
    clockpin = 23
    datapin = 24

#DEFINE STEPPER SPEEDS - number of steps per call (should be fine, medium, coarse but its already written)
    finespeed = 1
    normalspeed = 10
    fastspeed = 50

#stepper_speed initializes as 1 BUT changes according to the state of the speed switch
    stepper_speed = finespeed

#FROM StepperControl class *********************************************************
    btnSteps = 0.001

    APsteps = 0
    MLsteps = 0
    DVsteps = 0

    APrelpos = 0
    MLrelpos = 0
    DVrelpos = 0

    DVinitREL_holdvalue = 0
    MLinitREL_holdvalue = 0
    APinitREL_holdvalue = 0

    DVcurrentoffsset = 0
    MLcurrentoffsset = 0
    APcurrentoffsset = 0

    APstepdistance = float(0.0075)
    MLstepdistance = float(0.0075)
    DVstepdistance = float(0.0075)

    APcurABSdist = float(0)
    MLcurABSdist = float(0)
    DVcurABSdist = float(0)

    APcurRELdist = float(0)
    MLcurRELdist = float(0)
    DVcurRELdist = float(0)

#FROM Threadedcontrol class *********************************************************

#Variables that may need tweaking
    calibrationsteps = 4000
    backoff = 200
    APadvance = 2000
    DVadvance = 400
    MLadvance = 400

    APworking = 4550
    MLworking = 5990
    DVworking = 4900

    fullretract = 7650
    fullretractML = 9500

    DVup_bregramhome = 268 #about 0.2cm

# how many steps DV goes up and then back when changing the offsets to avoid scrapping the skull
    DVup_OffsetSafety = 1340 #about 1cm


#DEFINE STEPPER CONTROL PINS
    enableAll = 2

    directionAP = 3
    stepAP = 4

    directionML = 17
    stepML = 27

    directionDV = 5
    stepDV = 6

#DEFINE LIMIT SWITCH PINS
    limitAP = 22
    limitML = 13
    limitDV = 19

#DEFINE ROTARY ENCODER PINS
    rotoA_AP = 20
    rotoB_AP = 21
    rotoA_ML = 16
    rotoB_ML = 12
    rotoA_DV = 25
    rotoB_DV = 8

#DEFINE STEPPER DIRECTIONS
    APback = 0
    APforward = 1
    MLleft = 1
    MLright = 0
    DVup = 0
    DVdown = 1

    calibfilename = 'CalibrationRH.txt'
    offsetfilename = 'offsetsRH.txt'

    lastenablestate = 1
    emergencystopflag = 0
    engagebutton = 0
    safetybutton = 0

    ratormouseselect = 1  #1 is mouse 2 is rat (mouse default)
    ratlambda = 1208   # steps for 9mm at 0.0745 per step
    mouselambda = 550  # steps for 4.1mm at 0.0745 per step
    rellambda = 0

# concept and code created by Kirk Mulatz (original code https://github.com/bustenchops/Stereotaxiccontrol (experiment branch)
