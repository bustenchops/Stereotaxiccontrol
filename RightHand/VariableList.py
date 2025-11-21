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

    DrillAPmm = float(0)
    DrillMLmm = float(0)
    DrillDVmm = float(0.2)

    NeedleAPmm = float(11.1)
    NeedleMLmm = float(31.22)
    NeedleDVmm = float(5)

    FiberAPmm = float(-5.069)
    FiberMLmm = float(31.22)
    FiberDVmm = float(1.1)

# variable to let program know which offset of toggled on. 1-drill,2-syringe,3-probe
    TOGGLEoff = 1

# DEFINE NUMBER OF BUTTONS AND ORDER IN ARRAY
    buttonarray = ['movefast', 'bregmahome', 'relativeML', 'relativeAP', 'moveslow', 'HomeToABSzero', 'recalibrate',
                   'miscbuttonA', 'presetworking', 'FiberOffset', 'needleoffset', 'drilloffset', 'relativeDV', 'relativeALLset', 'HomerelativeZero'
                   ]
    lastbuttonstate = [0 for x in range(len(buttonarray))]

# BUTTON POSITION IN SHIFT REGISTER ARRAY
    movefast = 0
    bregmahome = 1
    relativeML = 2
    relativeAP = 3
    moveslow = 4
    homeABSzero = 5
    recalibrate = 6
    miscbuttonA = 7
    miscbuttonB = 8
    fiberoff = 9
    needleoff = 10
    drilloff = 11
    relativeDV = 12
    relativeALL = 13
    homeRELzero = 14

#DEFINE EMERGENCY STOP and hard wired buttons
    emergstop = 11
    misc_eventbuttonA = 10
    misc_eventbuttonB = 26

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

    APstepdistance = float(0.006725)
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
    APadvance = 400 #8500
    DVadvance = 400
    MLadvance = 400

    APworking = 13600
    MLworking = 11455
    DVworking = 4000

    DVup_bregramhome = 1340 #about 0.5cm

# how many steps DV goes up and then back when changing the offsets to avoid scrapping the skull
    DVup_OffsetSafety = 1340 #about 0.5cm


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
    rotoA_AP = 25
    rotoB_AP =  8
    rotoA_ML = 20
    rotoB_ML = 21
    rotoA_DV = 16
    rotoB_DV = 12

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
# concept and code created by Kirk Mulatz (original code https://github.com/bustenchops/Stereotaxiccontrol (experiment branch)
