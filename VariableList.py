class var_list:
#FROM BUTTONCLASS *********************************************************

#Main while loop condition
    keepalive = True

#Stepper instances
    APmove = None
    MLmove = None
    DVmove = None


# OFFSETS FOR THE DRILL, Syringe, Needle (minus values is back, left or up)
    APDRILL = 0
    MLDRILL = 0
    DVDRILL = -1333

    APfiber = 0
    MLfiber = 0
    DVfiber = 0

    APneedle = 0
    MLneedle = 0
    DVneedle = 0

# DEFINE NUMBER OF BUTTONS AND ORDER IN ARRAY
    buttonarray = ['moveslow', 'needleoffset', 'drilloffset', 'HomeToABSzero', 'movefast', 'recalibrate', 'relativeDV',
                   'relativeALLset', 'relativeAP', 'relativeML', 'FiberOffset', 'HomerelativeZero', 'bregmahome',
                   'miscbuttonA', 'miscbuttonB']
    lastbuttonstate = [0 for x in range(len(buttonarray))]

# BUTTON POSITION IN SHIFT REGISTER ARRAY
    moveslow = 0
    needleoff = 1
    drilloff = 2
    homeABSzero = 3
    movefast = 4
    recalibrate = 5
    relativeDV = 6
    relativeALL = 7
    relativeAP = 8
    relativeML = 9
    fiberoff = 10
    homeRELzero = 11
    bregmahome = 12
    miscbuttonA = 13
    miscbuttonB = 14

#DEFINE EMERGENCY STOP and hard wired buttons
    emergstop = 26
    misc_eventbuttonA = 10
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
    btnSteps = 0.002

    APsteps = 0
    MLsteps = 0
    DVsteps = 0

    APrelpos = 0
    MLrelpos = 0
    DVrelpos = 0

    DVinitREL_holdvalue = 0
    MLinitREL_holdvalue = 0
    APinitREL_holdvalue = 0

    APstepdistance = float(0.00625)
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
    rotoA_ML = 12
    rotoB_ML = 16
    rotoA_DV = 20
    rotoB_DV = 21

#DEFINE STEPPER DIRECTIONS
    APback = 0
    APforward = 1
    MLleft = 0
    MLright = 1
    DVup = 0
    DVdown = 1

    calibfilename = 'Calibration.txt'

    lastenablestate = 1
