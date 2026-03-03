class var_list:

#From UI
    countoflistwidget = 0
    list_toggle = 9999

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

    FiberAPmm = float(-5.069)
    FiberMLmm = float(31.22)
    FiberDVmm = float(1.1)

# variable to let program know which offset of toggled on. 1-drill,2-syringe,3-probe
    TOGGLEoff = 1

# DEFINE NUMBER OF BUTTONS AND ORDER IN ARRAY
    buttonarray = ['moveslow', 'movefast', 'offposone', 'offpostwo', 'rezero',
                   'relativeAP', 'relativeML', 'relativeDV', 'relativeALLset', 'fullretract',
                   'bregmahome', 'bregmahomeDVabs', 'bregmahomeDVupfive', 'gotolambdabut', 'ratselect',
                   'mouseselect','gotopreset', 'selectup', 'selectdown', 'armbut',
                   'engagebut', 'makeitsobut', 'withdrawl', 'DVinsert', 'retractAP',
                   'returnAP', 'retactDV', 'returnDV', 'functionone', 'functiontwo',
                   'ABSzero', 'unassigned']

    lastbuttonstate = [0 for x in range(len(buttonarray))]

# BUTTON POSITION IN SHIFT REGISTER ARRAY (0 to 31)
    moveslow = 0
    movefast = 4
    offposone = 2
    offpostwo = 10
    rezero = 5

    relativeAP = 7
    relativeML = 11
    relativeDV = 12
    relativeALL = 9
    fullretract = 3

    bregmahome = 6
    bregmahomeDVabs = 8
    bregmahomeDVupfive = 1
    gotolambdabut = 1
    ratselect = 13

    mouseselect = 1
    gotopreset = 14
    selectup = 1
    selectdown = 1
    armbut = 1

    engagebut = 1
    makeitsobut = 1
    withdrawl = 1
    DVinsert = 1
    retractAP = 1

    returnAP = 1
    retractDV = 1
    returnDV = 1
    functionone = 1
    functiontwo = 1

    ABSzero = 1

#DEFINE EMERGENCY STOP and hard wired buttons GPIO
    emergstop = 26
    safetybut = 10
    disablestepperbut = 11
    fourthhardwarebutton = 9 #encoder 4 depress?

#DEFINE SHIFT REGISTER PINS
    latchpin = 18
    clockpin = 23
    datapin = 24

#DEFINE STEPPER SPEEDS - number of steps per call
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

    APworking = 6400
    MLworking = 6070
    DVworking = 3500

    fullretract = 7650
    fullretractML = 9500

    DVup_bregramhome = 268 #about 0.2cm
    DVup_lambdabregma = 200 # about 0.15cm
    DVup_five = 675 # about 5 mm

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
    rotoA_AP = 25
    rotoB_AP =  8
    rotoA_ML = 12
    rotoB_ML = 16
    rotoA_DV = 20
    rotoB_DV = 21
    rotoA_fourth = 7
    rotoB_fourth =  1


#DEFINE STEPPER DIRECTIONS
    APback = 1
    APforward = 0
    MLleft = 1
    MLright = 0
    DVup = 0
    DVdown = 1

    calibfilename = 'CalibrationLH.txt'
    offsetfilename = 'offsetsLH.txt'

    lastenablestate = 1

    emergencystopflag = 0

    engagebuttons = 0
    safetybutton = 0

    withdrawinsertstop = 0
    dvinsertstop = 0

    DVinsertindicator = 0
    Withdrawlindicator = 0
    Makeitsoindicator = 0

    ratormouseselect = 1  #1 is mouse 2 is rat (mouse default)
    ratlambda = 1208   # steps for 9mm at 0.0745 per step
    mouselambda = 550  # steps for 4.1mm at 0.0745 per step
    rellambda = 0

# For timerthread safety timeouts
    timeoutlength = 3

    DVinserttimeouttime = None
    Safetytimeouttime = None
    Withdrawltimeouttime = None
    Makeitsobuttimeouttime = None

# concept and code created by Kirk Mulatz (original code https://github.com/bustenchops/Stereotaxiccontrol (experiment branch)
