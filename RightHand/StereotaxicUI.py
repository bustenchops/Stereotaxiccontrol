# -*- coding: utf-8 -*-
import sys
from PySide6.QtCore import (QRect, QThreadPool, Slot, QObject, Signal, QThread)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QFrame, QLCDNumber, QMainWindow, QMenuBar, QRadioButton, QStatusBar,
                               QWidget, QLabel, QPlainTextEdit, QCheckBox, QPushButton, QListWidget,QFileDialog)

from StepperControlv1 import Steppercontrol
from Buttonclassv1 import buttonprogram
from ThreadedControlsv1 import threadedcontrols
from VariableList import var_list





class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.stepperstepsper = None

#Setup GUI LAYOUT

        self.setObjectName(u"MainWindow")
        self.resize(800, 480)

        self.widget = QWidget()

        self.APstepLCD = QLCDNumber(self.widget)
        self.APstepLCD.setObjectName(u"APstepLCD")
        self.APstepLCD.setGeometry(QRect(170, 37, 131, 61))
        self.APstepLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.APstepLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.APstepLCD.setLineWidth(1)
        self.APstepLCD.setDigitCount(7)
        self.APstepLCD.setProperty(u"value", 888.888)

        self.MLstepLCD = QLCDNumber(self.widget)
        self.MLstepLCD.setObjectName(u"MLstepLCD")
        self.MLstepLCD.setGeometry(QRect(340, 37, 131, 61))
        self.MLstepLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.MLstepLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.MLstepLCD.setLineWidth(1)
        self.MLstepLCD.setDigitCount(7)
        self.MLstepLCD.setProperty(u"value", 888.888)

        self.DVstepLCD = QLCDNumber(self.widget)
        self.DVstepLCD.setObjectName(u"DVstepLCD")
        self.DVstepLCD.setGeometry(QRect(500, 37, 131, 61))
        self.DVstepLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.DVstepLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.DVstepLCD.setLineWidth(1)
        self.DVstepLCD.setDigitCount(7)
        self.DVstepLCD.setProperty(u"value", 888.888)

        self.APABSposLCD = QLCDNumber(self.widget)
        self.APABSposLCD.setObjectName(u"APABSposLCD")
        self.APABSposLCD.setGeometry(QRect(170, 107, 131, 61))
        self.APABSposLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.APABSposLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.APABSposLCD.setLineWidth(1)
        self.APABSposLCD.setDigitCount(7)
        self.APABSposLCD.setProperty(u"value", 888.888)

        self.MLABSposLCD = QLCDNumber(self.widget)
        self.MLABSposLCD.setObjectName(u"MLABSposLCD")
        self.MLABSposLCD.setGeometry(QRect(340, 107, 131, 61))
        self.MLABSposLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.MLABSposLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.MLABSposLCD.setLineWidth(1)
        self.MLABSposLCD.setDigitCount(7)
        self.MLABSposLCD.setProperty(u"value", 888.888)

        self.DVABSposLCD = QLCDNumber(self.widget)
        self.DVABSposLCD.setObjectName(u"DVABSposLCD")
        self.DVABSposLCD.setGeometry(QRect(500, 107, 131, 61))
        self.DVABSposLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.DVABSposLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.DVABSposLCD.setLineWidth(1)
        self.DVABSposLCD.setDigitCount(7)
        self.DVABSposLCD.setProperty(u"value", 888.888)

        self.APRelposLCD = QLCDNumber(self.widget)
        self.APRelposLCD.setObjectName(u"APRelposLCD")
        self.APRelposLCD.setGeometry(QRect(170, 177, 131, 61))
        self.APRelposLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.APRelposLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.APRelposLCD.setLineWidth(1)
        self.APRelposLCD.setDigitCount(7)
        self.APRelposLCD.setProperty(u"value", 888.888)

        self.MLRelposLCD = QLCDNumber(self.widget)
        self.MLRelposLCD.setObjectName(u"MLRelposLCD")
        self.MLRelposLCD.setGeometry(QRect(340, 177, 131, 61))
        self.MLRelposLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.MLRelposLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.MLRelposLCD.setLineWidth(1)
        self.MLRelposLCD.setDigitCount(7)
        self.MLRelposLCD.setProperty(u"value", 888.888)

        self.DVRelposLCD = QLCDNumber(self.widget)
        self.DVRelposLCD.setObjectName(u"DVRelposLCD")
        self.DVRelposLCD.setGeometry(QRect(500, 177, 131, 61))
        self.DVRelposLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.DVRelposLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.DVRelposLCD.setLineWidth(1)
        self.DVRelposLCD.setDigitCount(7)
        self.DVRelposLCD.setProperty(u"value", 888.888)

        toplabelfont = QFont()
        toplabelfont.setPointSize(18)
        toplabelfont.setBold(True)

        self.APlabel = QLabel("AP", self.widget)
        self.APlabel.setObjectName(u"APlabel")
        self.APlabel.setGeometry(QRect(220, -3, 41, 41))
        self.APlabel.setFont(toplabelfont)

        self.MLlabel = QLabel("ML", self.widget)
        self.MLlabel.setObjectName(u"MLlabel")
        self.MLlabel.setGeometry(QRect(390, -3, 41, 41))
        self.MLlabel.setFont(toplabelfont)

        self.DVlabel = QLabel("DV", self.widget)
        self.DVlabel.setObjectName(u"DVlabel")
        self.DVlabel.setGeometry(QRect(550, -3, 41, 41))
        self.DVlabel.setFont(toplabelfont)

        stepposlabelfont = QFont()
        stepposlabelfont.setPointSize(12)
        stepposlabelfont.setBold(False)

        self.stepposlabel = QLabel("Step position:", self.widget)
        self.stepposlabel.setObjectName(u"stepposlabel")
        self.stepposlabel.setGeometry(QRect(60, 47, 111, 41))
        self.stepposlabel.setFont(stepposlabelfont)

        poslabelfont = QFont()
        poslabelfont.setPointSize(20)
        poslabelfont.setBold(False)

        self.ABSposLabel = QLabel("ABS pos:", self.widget)
        self.ABSposLabel.setObjectName(u"ABSposlabel")
        self.ABSposLabel.setGeometry(QRect(60, 107, 111, 61))
        self.ABSposLabel.setFont(poslabelfont)

        self.RELposLabel = QLabel("REL pos:", self.widget)
        self.RELposLabel.setObjectName(u"RELposlabel")
        self.RELposLabel.setGeometry(QRect(60, 177, 111, 61))
        self.RELposLabel.setFont(poslabelfont)

        manualenterfont = QFont()
        manualenterfont.setPointSize(16)
        manualenterfont.setBold(False)

        self.APmanualenter = QPlainTextEdit(self.widget)
        self.APmanualenter.setObjectName(u"APmanualenter")
        self.APmanualenter.setGeometry(QRect(420, 260, 91, 40))
        self.APmanualenter.setFont(manualenterfont)

        self.MLmanualenter = QPlainTextEdit(self.widget)
        self.MLmanualenter.setObjectName(u"MLmanualenter")
        self.MLmanualenter.setGeometry(QRect(420, 310, 91, 40))
        self.MLmanualenter.setFont(manualenterfont)

        self.DVmanualenter = QPlainTextEdit(self.widget)
        self.DVmanualenter.setObjectName(u"DVmanualenter")
        self.DVmanualenter.setGeometry(QRect(420, 360, 91, 40))
        self.DVmanualenter.setFont(manualenterfont)

        self.APlabel = QLabel("AP", self.widget)
        self.APlabel.setObjectName(u"APlabelmanual")
        self.APlabel.setGeometry(QRect(370, 260, 41, 40))
        self.APlabel.setFont(toplabelfont)

        self.MLlabel = QLabel("ML", self.widget)
        self.MLlabel.setObjectName(u"MLlabelmanual")
        self.MLlabel.setGeometry(QRect(370, 310, 41, 40))
        self.MLlabel.setFont(toplabelfont)

        self.DVlabel = QLabel("DV", self.widget)
        self.DVlabel.setObjectName(u"DVlabelmanual")
        self.DVlabel.setGeometry(QRect(370, 360, 41, 40))
        self.DVlabel.setFont(toplabelfont)

        radiobuttonfont = QFont()
        radiobuttonfont.setPointSize(12)
        radiobuttonfont.setBold(False)


        self.radiolabel = QLabel("Current Offset", self.widget)
        self.radiolabel.setObjectName(u"DVlabelmanual")
        self.radiolabel.setGeometry(QRect(652, 140, 111, 16))
        self.radiolabel.setFont(radiobuttonfont)

        self.drilloffsetcheck = QRadioButton("Drill", self.widget)
        self.drilloffsetcheck.setObjectName(u"drillradio")
        self.drilloffsetcheck.setGeometry(QRect(662, 170, 92, 20))
        self.drilloffsetcheck.setFont(radiobuttonfont)

        self.needleoffsetcheck = QRadioButton("Syringe", self.widget)
        self.needleoffsetcheck.setObjectName(u"needleradio")
        self.needleoffsetcheck.setGeometry(QRect(662, 200, 92, 20))
        self.needleoffsetcheck.setFont(radiobuttonfont)

        self.fiberoffsetcheck = QRadioButton("Probe", self.widget)
        self.fiberoffsetcheck.setObjectName(u"proberadio")
        self.fiberoffsetcheck.setGeometry(QRect(662, 230, 92, 20))
        self.fiberoffsetcheck.setFont(radiobuttonfont)

        self.checkBox = QCheckBox("Make it so", self.widget)
        self.checkBox.setObjectName(u"engagecheckbox")
        self.checkBox.setGeometry(QRect(530, 270, 105, 20))
        self.checkBox.setFont(radiobuttonfont)

        self.armcoordinatebutton = QPushButton("Arm Coordinates", self.widget)
        self.armcoordinatebutton.setObjectName(u"armcoordinatebutton")
        self.armcoordinatebutton.setGeometry(QRect(110, 380, 161, 31))
        self.armcoordinatebutton.setFont(stepposlabelfont)
        self.armcoordinatebutton.clicked.connect(self.selectlistcoordinates)

        self.loadpresetbutton = QPushButton("Load Preset File", self.widget)
        self.loadpresetbutton.setObjectName(u"loadpresetbutton")
        self.loadpresetbutton.setGeometry(QRect(110, 243, 171, 31))
        self.loadpresetbutton.setFont(stepposlabelfont)
        self.loadpresetbutton.clicked.connect(self.choseafile)

        self.movebutton = QPushButton("Engage", self.widget)
        self.movebutton.setObjectName(u"movebutton")
        self.movebutton.setGeometry(QRect(540, 310, 101, 81))
        self.movebutton.setFont(stepposlabelfont)
        self.movebutton.clicked.connect(self.plaintextgrab)

        self.listWidget = QListWidget(self.widget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(40, 273, 311, 110))
        self.listWidget.setFont(stepposlabelfont)

        self.menubar = QMenuBar()
        self.menubar.setGeometry(QRect(0, 0, 800, 33))

        self.statusbar = QStatusBar()
        self.setCentralWidget(self.widget)

#UPDATE the LCDS
    def updateAPLCD(self, stepAP,ABS_AP,REL_AP):
        print('updated AP steps')
        self.APstepLCD.display(stepAP)
        self.APABSposLCD.display(ABS_AP)
        self.APRelposLCD.display(REL_AP)
        return

    def updateMLLCD(self, stepML,ABS_ML,REL_ML):
        print('updated ML steps')
        self.MLstepLCD.display(stepML)
        self.MLABSposLCD.display(ABS_ML)
        self.MLRelposLCD.display(REL_ML)
        return

    def updateDVLCD(self, stepDV,ABS_DV,REL_DV):
        print('updated DV steps')
        self.DVstepLCD.display(stepDV)
        self.DVABSposLCD.display(ABS_DV)
        self.DVRelposLCD.display(REL_DV)
        return

    def uitest(self):
        print('the send to UI was good')

#grabs the plaintext from the text boxes only if the checkbox is selected
    @Slot()
    def plaintextgrab(self):
        APcooord = self.APmanualenter.toPlainText()
        MLcooord = self.MLmanualenter.toPlainText()
        DVcooord = self.DVmanualenter.toPlainText()
        if self.checkBox.isChecked():
            print(f"Grad text to go to AP:{APcooord}, ML:{MLcooord}, DV:{DVcooord}")
            #self.gototargetnow = threadedcontrols(window)
            #threadpool.start(self.gototargetnow.movetoTargetList(APcooord,MLcooord,DVcooord))
            controlthread.movetoTargetList(APcooord,MLcooord,DVcooord)
            self.checkBox.setChecked(False)

#select a TXT file to load and preloads the targets
    @Slot()
    def choseafile(self):
        print("click load file")
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Text Files (*.txt)")

        if file_dialog.exec():
            self.selected_file = file_dialog.selectedFiles()[0]
            print(f'Selected file: {self.selected_file}')

        with open(self.selected_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                self.listWidget.addItem(line.strip())

#loads the coordinates from the list to the text boxes
    @Slot()
    def selectlistcoordinates(self):
        selected_items = self.listWidget.selectedItems()
        selected_text = selected_items[0].text()
        name, APlist, MLlist, DVlist = selected_text.split(' ')
        self.APmanualenter.setPlainText(APlist)
        self.MLmanualenter.setPlainText(MLlist)
        self.DVmanualenter.setPlainText(DVlist)

#controls the toggles for the drill, needle and probe
    @Slot()
    def drilloffset(self):
        self.drilloffsetcheck.toggle()

    @Slot()
    def needleoffset(self):
        self.needleoffsetcheck.toggle()

    @Slot()
    def probeoffset(self):
        self.fiberoffsetcheck.toggle()

# Report Current Speed
    @Slot(int)
    def currentspeed(self, stepsper):  # not used yet but plan is to put it in the interface
        self.stepperstepsper = stepsper

# To send the recalibration to the control thread
    def recalibrateaxis(self):
        print('recalibration')
        #self.recalibrateall = threadedcontrols(window)
        #threadpool.start(self.recalibrateall.zerosteppers)
        print('UI got this')
        controlthread.questionzerosteppers()
        #controlthread.zerosteppers(3, var_list.backoff, var_list.btnSteps)
        #controlthread.zerosteppers(1,var_list.backoff, var_list.btnSteps)
        #controlthread.zerosteppers(2, var_list.backoff, var_list.btnSteps)

#INITIALIZE STEPPERS
    def initializesteppers(self):
        print('StereotaxicUI file')
        print('steppers initialize')
        #the plusdir and minusdir reflect the direction the arm moves when the steps advance
        print("AP start")
        var_list.APmove = Steppercontrol(var_list.enableAll,var_list.stepAP,var_list.directionAP,var_list.limitAP,1,var_list.APforward,var_list.APback, window)
        print('AP finished, ML start')
        var_list.MLmove = Steppercontrol(var_list.enableAll,var_list.stepML,var_list.directionML,var_list.limitML,2,var_list.MLright,var_list.MLleft, window)
        print('ML finished, DV start')
        var_list.DVmove = Steppercontrol(var_list.enableAll,var_list.stepDV,var_list.directionDV,var_list.limitDV,3,var_list.DVdown,var_list.DVup, window)
        print('steppers are a go')



# concept and code created by Kirk Mulatz (original code https://github.com/bustenchops/Stereotaxiccontrol (experiment branch)

#######program code############

app = QApplication(sys.argv)
window = MainWindow()

window.initializesteppers()

mainbuttonthread = buttonprogram(window)
#mainbuttonthread.sendtoUI(window)
controlthread = threadedcontrols(window)
#controlthread.sendtoUI(window)

#Start Threads
threadpool = QThreadPool()
threadpool.start(mainbuttonthread.runbuttonthread)
threadpool.start(controlthread.runcontrolthread)

window.show()

app.exec()