# -*- coding: utf-8 -*-
import sys
from PySide6.QtCore import (QRect, QThreadPool, Slot, QObject, Signal, QThread)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QFrame, QLCDNumber, QMainWindow, QMenuBar, QRadioButton, QStatusBar,
                               QWidget, QLabel, QPlainTextEdit, QCheckBox, QPushButton, QListWidget,QFileDialog, QButtonGroup)

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
        self.resize(1240, 550)

        self.widget = QWidget()

        self.APstepLCD = QLCDNumber(self.widget)
        self.APstepLCD.setObjectName(u"APstepLCD")
        self.APstepLCD.setGeometry(QRect(110, 37, 90, 45))
        self.APstepLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.APstepLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.APstepLCD.setLineWidth(1)
        self.APstepLCD.setDigitCount(7)
        self.APstepLCD.setProperty(u"value", 888.888)

        self.MLstepLCD = QLCDNumber(self.widget)
        self.MLstepLCD.setObjectName(u"MLstepLCD")
        self.MLstepLCD.setGeometry(QRect(270, 37, 90, 45))
        self.MLstepLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.MLstepLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.MLstepLCD.setLineWidth(1)
        self.MLstepLCD.setDigitCount(7)
        self.MLstepLCD.setProperty(u"value", 888.888)

        self.DVstepLCD = QLCDNumber(self.widget)
        self.DVstepLCD.setObjectName(u"DVstepLCD")
        self.DVstepLCD.setGeometry(QRect(430, 37, 90, 45))
        self.DVstepLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.DVstepLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.DVstepLCD.setLineWidth(1)
        self.DVstepLCD.setDigitCount(7)
        self.DVstepLCD.setProperty(u"value", 888.888)

        self.APABSposLCD = QLCDNumber(self.widget)
        self.APABSposLCD.setObjectName(u"APABSposLCD")
        self.APABSposLCD.setGeometry(QRect(110, 92, 90, 45))
        self.APABSposLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.APABSposLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.APABSposLCD.setLineWidth(1)
        self.APABSposLCD.setDigitCount(7)
        self.APABSposLCD.setProperty(u"value", 888.888)

        self.MLABSposLCD = QLCDNumber(self.widget)
        self.MLABSposLCD.setObjectName(u"MLABSposLCD")
        self.MLABSposLCD.setGeometry(QRect(270, 92, 90, 45))
        self.MLABSposLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.MLABSposLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.MLABSposLCD.setLineWidth(1)
        self.MLABSposLCD.setDigitCount(7)
        self.MLABSposLCD.setProperty(u"value", 888.888)

        self.DVABSposLCD = QLCDNumber(self.widget)
        self.DVABSposLCD.setObjectName(u"DVABSposLCD")
        self.DVABSposLCD.setGeometry(QRect(430, 92, 90, 45))
        self.DVABSposLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.DVABSposLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.DVABSposLCD.setLineWidth(1)
        self.DVABSposLCD.setDigitCount(7)
        self.DVABSposLCD.setProperty(u"value", 888.888)

        self.APRelposLCD = QLCDNumber(self.widget)
        self.APRelposLCD.setObjectName(u"APRelposLCD")
        self.APRelposLCD.setGeometry(QRect(90, 150, 131, 61))
        self.APRelposLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.APRelposLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.APRelposLCD.setLineWidth(1)
        self.APRelposLCD.setDigitCount(7)
        self.APRelposLCD.setProperty(u"value", 888.888)

        self.MLRelposLCD = QLCDNumber(self.widget)
        self.MLRelposLCD.setObjectName(u"MLRelposLCD")
        self.MLRelposLCD.setGeometry(QRect(250, 150, 131, 61))
        self.MLRelposLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.MLRelposLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.MLRelposLCD.setLineWidth(1)
        self.MLRelposLCD.setDigitCount(7)
        self.MLRelposLCD.setProperty(u"value", 888.888)

        self.DVRelposLCD = QLCDNumber(self.widget)
        self.DVRelposLCD.setObjectName(u"DVRelposLCD")
        self.DVRelposLCD.setGeometry(QRect(410, 150, 131, 61))
        self.DVRelposLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.DVRelposLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.DVRelposLCD.setLineWidth(1)
        self.DVRelposLCD.setDigitCount(7)
        self.DVRelposLCD.setProperty(u"value", 888.888)

        toplabelfont = QFont()
        toplabelfont.setPointSize(18)
        toplabelfont.setBold(True)

        smalllabelfont = QFont()
        smalllabelfont.setPointSize(8)
        smalllabelfont.setBold(False)

        smalllmanualfont = QFont()
        smalllmanualfont.setPointSize(10)
        smalllmanualfont.setBold(False)

        poslabelfont = QFont()
        poslabelfont.setPointSize(20)
        poslabelfont.setBold(False)

        manualenterfont = QFont()
        manualenterfont.setPointSize(16)
        manualenterfont.setBold(False)

        coordlabelfont = QFont()
        coordlabelfont.setPointSize(16)
        coordlabelfont.setBold(True)

        radiobuttonfont = QFont()
        radiobuttonfont.setPointSize(12)
        radiobuttonfont.setBold(False)

        self.APlabel = QLabel("AP", self.widget)
        self.APlabel.setObjectName(u"APlabel")
        self.APlabel.setGeometry(QRect(142, -3, 41, 41))
        self.APlabel.setFont(toplabelfont)

        self.MLlabel = QLabel("ML", self.widget)
        self.MLlabel.setObjectName(u"MLlabel")
        self.MLlabel.setGeometry(QRect(297, -3, 41, 41))
        self.MLlabel.setFont(toplabelfont)

        self.DVlabel = QLabel("DV", self.widget)
        self.DVlabel.setObjectName(u"DVlabel")
        self.DVlabel.setGeometry(QRect(460, -3, 41, 41))
        self.DVlabel.setFont(toplabelfont)

        self.stepposlabel = QLabel("Steps:", self.widget)
        self.stepposlabel.setObjectName(u"stepposlabel")
        self.stepposlabel.setGeometry(QRect(15, 37, 111, 41))
        self.stepposlabel.setFont(poslabelfont)

        self.ABSposLabel = QLabel("ABS:", self.widget)
        self.ABSposLabel.setObjectName(u"ABSposlabel")
        self.ABSposLabel.setGeometry(QRect(15, 80, 111, 61))
        self.ABSposLabel.setFont(poslabelfont)

        self.RELposLabel = QLabel("REL:", self.widget)
        self.RELposLabel.setObjectName(u"RELposlabel")
        self.RELposLabel.setGeometry(QRect(15, 148, 111, 61))
        self.RELposLabel.setFont(poslabelfont)

        self.APmanualenter = QPlainTextEdit(self.widget)
        self.APmanualenter.setObjectName(u"APmanualenter")
        self.APmanualenter.setGeometry(QRect(525, 370, 75, 40))
        self.APmanualenter.setFont(manualenterfont)

        self.MLmanualenter = QPlainTextEdit(self.widget)
        self.MLmanualenter.setObjectName(u"MLmanualenter")
        self.MLmanualenter.setGeometry(QRect(525, 420, 75, 40))
        self.MLmanualenter.setFont(manualenterfont)

        self.DVmanualenter = QPlainTextEdit(self.widget)
        self.DVmanualenter.setObjectName(u"DVmanualenter")
        self.DVmanualenter.setGeometry(QRect(525, 470, 75, 40))
        self.DVmanualenter.setFont(manualenterfont)


        self.APlabel = QLabel("AP", self.widget)
        self.APlabel.setObjectName(u"APlabelmanual")
        self.APlabel.setGeometry(QRect(490, 370, 41, 40))
        self.APlabel.setFont(coordlabelfont)

        self.MLlabel = QLabel("ML", self.widget)
        self.MLlabel.setObjectName(u"MLlabelmanual")
        self.MLlabel.setGeometry(QRect(490, 420, 41, 40))
        self.MLlabel.setFont(coordlabelfont)

        self.DVlabel = QLabel("DV", self.widget)
        self.DVlabel.setObjectName(u"DVlabelmanual")
        self.DVlabel.setGeometry(QRect(490, 470, 41, 40))
        self.DVlabel.setFont(coordlabelfont)

        self.targetname = QPlainTextEdit(self.widget)
        self.targetname.setObjectName(u"targetnameselected")
        self.targetname.setGeometry(QRect(500, 298, 275, 33))
        self.targetname.setFont(radiobuttonfont)


        self.speciesgroup = QButtonGroup(self)
        self.speciesgroup.setExclusive(True)
        self.offsetgroup = QButtonGroup(self)
        self.offsetgroup.setExclusive(True)
        self.speedgroup = QButtonGroup(self)
        self.speedgroup.setExclusive(True)


        self.targetlabel = QLabel("Selected Target:", self)
        self.targetlabel.setObjectName(u"selectedtargetlabel")
        self.targetlabel.setGeometry(QRect(375, 305, 130, 20))
        self.targetlabel.setFont(radiobuttonfont)

        self.coordinatelabel = QLabel("Coordinates:", self)
        self.coordinatelabel.setObjectName(u"coordinateslabel")
        self.coordinatelabel.setGeometry(QRect(495, 340, 130, 20))
        self.coordinatelabel.setFont(radiobuttonfont)

        self.DVinsertcheckbox = QCheckBox("DV insert:", self.widget)
        self.DVinsertcheckbox.setObjectName(u"DVinsertionbox")
        self.DVinsertcheckbox.setGeometry(QRect(640, 340, 130, 20))
        self.DVinsertcheckbox.setFont(radiobuttonfont)

        self.DVinsertratelabel = QLabel("Rate (mm/min):", self)
        self.DVinsertratelabel.setObjectName(u"dvinsertrate")
        self.DVinsertratelabel.setGeometry(QRect(615, 365, 130, 20))
        self.DVinsertratelabel.setFont(smalllabelfont)

        self.DVinsertpausetimelabel = QLabel("Pause time:", self)
        self.DVinsertpausetimelabel.setObjectName(u"dvpausetime")
        self.DVinsertpausetimelabel.setGeometry(QRect(701, 418, 130, 20))
        self.DVinsertpausetimelabel.setFont(smalllabelfont)

        self.DVinsertpauselabel = QLabel("Num. pauses:", self)
        self.DVinsertpauselabel.setObjectName(u"dvnumpauses")
        self.DVinsertpauselabel.setGeometry(QRect(701, 365, 130, 20))
        self.DVinsertpauselabel.setFont(smalllabelfont)

        self.DVinsertdepthlabel = QLabel("Target DV:", self)
        self.DVinsertdepthlabel.setObjectName(u"dvtargetdepth")
        self.DVinsertdepthlabel.setGeometry(QRect(615, 418, 130, 20))
        self.DVinsertdepthlabel.setFont(smalllabelfont)

        self.DVinsertcompenslabel = QLabel("Bevel comp. (mm):", self)
        self.DVinsertcompenslabel.setObjectName(u"DVinsertcompenslabel")
        self.DVinsertcompenslabel.setGeometry(QRect(615, 473, 130, 20))
        self.DVinsertcompenslabel.setFont(smalllabelfont)

        self.DVinsertmanrate = QPlainTextEdit(self.widget)
        self.DVinsertmanrate.setObjectName(u"DVinsertmanrate")
        self.DVinsertmanrate.setGeometry(QRect(627, 385, 50, 31))
        self.DVinsertmanrate.setFont(smalllmanualfont)

        self.DVinserttarget = QPlainTextEdit(self.widget)
        self.DVinserttarget.setObjectName(u"DVinserttarget")
        self.DVinserttarget.setGeometry(QRect(627, 438, 50, 31))
        self.DVinserttarget.setFont(smalllmanualfont)

        self.DVinsertcompens = QPlainTextEdit(self.widget)
        self.DVinsertcompens.setObjectName(u"DVinsertcompens")
        self.DVinsertcompens.setGeometry(QRect(627, 493, 50, 31))
        self.DVinsertcompens.setFont(smalllmanualfont)

        self.DVinsertnumpause = QPlainTextEdit(self.widget)
        self.DVinsertnumpause.setObjectName(u"DVinsertnumpause")
        self.DVinsertnumpause.setGeometry(QRect(711, 385, 50, 31))
        self.DVinsertnumpause.setFont(smalllmanualfont)

        self.DVinsertpausetime = QPlainTextEdit(self.widget)
        self.DVinsertpausetime.setObjectName(u"DVinsertpausetime")
        self.DVinsertpausetime.setGeometry(QRect(711, 438, 50, 31))
        self.DVinsertpausetime.setFont(smalllmanualfont)

        self.withdrawcheckbox = QCheckBox("Withdraw:", self.widget)
        self.withdrawcheckbox.setObjectName(u"withdrawcheckbox")
        self.withdrawcheckbox.setGeometry(QRect(808, 340, 130, 20))
        self.withdrawcheckbox.setFont(radiobuttonfont)

        self.withdrawratelabel = QLabel("Rate (mm/min):", self)
        self.withdrawratelabel.setObjectName(u"withdrawratelabel")
        self.withdrawratelabel.setGeometry(QRect(787, 365, 130, 20))
        self.withdrawratelabel.setFont(smalllabelfont)

        self.withdrawpausetimelabel = QLabel("Pause time:", self)
        self.withdrawpausetimelabel.setObjectName(u"withdrawpausetimelabel")
        self.withdrawpausetimelabel.setGeometry(QRect(787, 473, 130, 20))
        self.withdrawpausetimelabel.setFont(smalllabelfont)

        self.withdrawnumpauselabel = QLabel("Num. pauses:", self)
        self.withdrawnumpauselabel.setObjectName(u"withdrawnumpauselabel")
        self.withdrawnumpauselabel.setGeometry(QRect(787, 418, 130, 20))
        self.withdrawnumpauselabel.setFont(smalllabelfont)

        self.withdrawfirstwaitlabel = QLabel("First wait (s):", self)
        self.withdrawfirstwaitlabel.setObjectName(u"withdrawfirstwaitlabel")
        self.withdrawfirstwaitlabel.setGeometry(QRect(875, 365, 130, 20))
        self.withdrawfirstwaitlabel.setFont(smalllabelfont)

        self.withdrawtotalwaitlabel = QLabel("Total wait (s):", self)
        self.withdrawtotalwaitlabel.setObjectName(u"withdrawtotalwaitlabel")
        self.withdrawtotalwaitlabel.setGeometry(QRect(875, 473, 130, 20))
        self.withdrawtotalwaitlabel.setFont(smalllabelfont)

        self.withdrawfirstdistwaitlabel = QLabel("First Withdraw (mm):", self)
        self.withdrawfirstdistwaitlabel.setObjectName(u"withdrawfirstdistwaitlabel")
        self.withdrawfirstdistwaitlabel.setGeometry(QRect(875, 418, 130, 20))
        self.withdrawfirstdistwaitlabel.setFont(smalllabelfont)

        self.withdrawmanrate = QPlainTextEdit(self.widget)
        self.withdrawmanrate.setObjectName(u"withdrawmanrate")
        self.withdrawmanrate.setGeometry(QRect(799, 385, 50, 31))
        self.withdrawmanrate.setFont(smalllmanualfont)

        self.withdrawtotpause = QPlainTextEdit(self.widget)
        self.withdrawtotpause.setObjectName(u"withdrawtotpause")
        self.withdrawtotpause.setGeometry(QRect(887, 493, 50, 31))
        self.withdrawtotpause.setFont(smalllmanualfont)

        self.withdrawfirstdist = QPlainTextEdit(self.widget)
        self.withdrawfirstdist.setObjectName(u"withdrawfirstdist")
        self.withdrawfirstdist.setGeometry(QRect(887, 438, 50, 31))
        self.withdrawfirstdist.setFont(smalllmanualfont)

        self.withdrawnumpause = QPlainTextEdit(self.widget)
        self.withdrawnumpause.setObjectName(u"withdrawnumpause")
        self.withdrawnumpause.setGeometry(QRect(799, 438, 50, 31))
        self.withdrawnumpause.setFont(smalllmanualfont)

        self.withdrawpausetime = QPlainTextEdit(self.widget)
        self.withdrawpausetime.setObjectName(u"withdrawpausetime")
        self.withdrawpausetime.setGeometry(QRect(799, 493, 50, 31))
        self.withdrawpausetime.setFont(smalllmanualfont)

        self.withdrawfirstwait = QPlainTextEdit(self.widget)
        self.withdrawfirstwait.setObjectName(u"withdrawfirstwait")
        self.withdrawfirstwait.setGeometry(QRect(887, 385, 50, 31))
        self.withdrawfirstwait.setFont(smalllmanualfont)

        self.speciesgrouplabel = QLabel("Set Species:", self)
        self.speciesgrouplabel.setObjectName(u"speciesgrouplabel")
        self.speciesgrouplabel.setGeometry(QRect(575, 35, 111, 16))
        self.speciesgrouplabel.setFont(radiobuttonfont)


        self.ratradio = QRadioButton("Rat", self)
        self.ratradio.setGeometry(QRect(580, 65, 92, 20))
        self.ratradio.setFont(radiobuttonfont)

        self.mouseradio = QRadioButton("Mouse", self)
        self.mouseradio.setGeometry(QRect(580, 95, 92, 20))
        self.mouseradio.setFont(radiobuttonfont)

        self.speciesgroup.addButton(self.ratradio)
        self.speciesgroup.addButton(self.mouseradio)

        self.offsetgrouplabel = QLabel("Current Offset:", self)
        self.offsetgrouplabel.setObjectName(u"offsetgrouplabel")
        self.offsetgrouplabel.setGeometry(QRect(716, 35, 111, 16))
        self.offsetgrouplabel.setFont(radiobuttonfont)

        self.drillradio = QRadioButton("Drill", self)
        self.drillradio.setGeometry(QRect(721, 65, 92, 20))
        self.drillradio.setFont(radiobuttonfont)

        self.needleradio = QRadioButton("Syringe", self)
        self.needleradio.setGeometry(QRect(721, 95, 92, 20))
        self.needleradio.setFont(radiobuttonfont)

        self.fiberradio = QRadioButton("Probe", self)
        self.fiberradio.setGeometry(QRect(721, 125, 92, 20))
        self.fiberradio.setFont(radiobuttonfont)

        self.offsetgroup.addButton(self.drillradio)
        self.offsetgroup.addButton(self.needleradio)
        self.offsetgroup.addButton(self.fiberradio)

        self.speedgrouplabel = QLabel("Current Speed:", self)
        self.speedgrouplabel.setObjectName(u"speedgrouplabel")
        self.speedgrouplabel.setGeometry(QRect(860, 35, 111, 16))
        self.speedgrouplabel.setFont(radiobuttonfont)

        self.finespeedset = QRadioButton("Fine", self)
        self.finespeedset.setGeometry(QRect(865, 65, 92, 20))
        self.finespeedset.setFont(radiobuttonfont)

        self.medspeedset = QRadioButton("Medium", self)
        self.medspeedset.setGeometry(QRect(865, 95, 92, 20))
        self.medspeedset.setFont(radiobuttonfont)

        self.coarsespeedset = QRadioButton("Coarse", self)
        self.coarsespeedset.setGeometry(QRect(865, 125, 92, 20))
        self.coarsespeedset.setFont(radiobuttonfont)

        self.speedgroup.addButton(self.finespeedset)
        self.speedgroup.addButton(self.medspeedset)
        self.speedgroup.addButton(self.coarsespeedset)

        self.checkBox = QCheckBox("Make it so", self.widget)
        self.checkBox.setObjectName(u"engagecheckbox")
        self.checkBox.setGeometry(QRect(375, 355, 105, 20))
        self.checkBox.setFont(radiobuttonfont)

        self.movebutton = QPushButton("Engage", self.widget)
        self.movebutton.setObjectName(u"movebutton")
        self.movebutton.setGeometry(QRect(375, 398, 101, 81))
        self.movebutton.setFont(radiobuttonfont)
        self.movebutton.clicked.connect(self.plaintextgrab)

        self.safetyBox = QCheckBox("Safety Disengaged", self.widget)
        self.safetyBox.setObjectName(u"safetycheckbox")
        self.safetyBox.setGeometry(QRect(105, 490, 175, 20))
        self.safetyBox.setFont(radiobuttonfont)

        self.armcoordinatebutton = QPushButton("Arm Coordinates", self.widget)
        self.armcoordinatebutton.setObjectName(u"armcoordinatebutton")
        self.armcoordinatebutton.setGeometry(QRect(105, 445, 161, 31))
        self.armcoordinatebutton.setFont(radiobuttonfont)
        self.armcoordinatebutton.clicked.connect(self.selectlistcoordinates)

        self.loadpresetbutton = QPushButton("Load Preset File", self.widget)
        self.loadpresetbutton.setObjectName(u"loadpresetbutton")
        self.loadpresetbutton.setGeometry(QRect(105, 230, 171, 31))
        self.loadpresetbutton.setFont(radiobuttonfont)
        self.loadpresetbutton.clicked.connect(self.choseafile)

        self.listWidget = QListWidget(self.widget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(35, 273, 320, 160))
        self.listWidget.setFont(radiobuttonfont)

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
        # here - this is where the if statements checking which boxes are checked and engages the various functions.
        #alo resets the checkboxes
        APcooord = self.APmanualenter.toPlainText()
        MLcooord = self.MLmanualenter.toPlainText()
        DVcooord = self.DVmanualenter.toPlainText()
        if self.checkBox.isChecked():
            print(f"Grad text to go to AP:{APcooord}, ML:{MLcooord}, DV:{DVcooord}")
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

        # with open(self.selected_file, 'r') as file:
        #    self.listWidget.clear()
        #    for line in file:
        #         self.listWidget.addItem(line.strip())

    #loads the coordinates from the list to the text boxes
    @Slot()
    def selectlistcoordinates(self):
        selected_items = self.listWidget.selectedItems()
        selected_text = selected_items[0].text()
        name, APlist, MLlist, DVlist = selected_text.split(' ')
        self.APmanualenter.setPlainText(APlist)
        self.MLmanualenter.setPlainText(MLlist)
        self.DVmanualenter.setPlainText(DVlist)

#to enumerate the items and put them in the list.
        # def enumerate_list_items_zero_based(self):
        #     """Print: index (0-based) and text for each QListWidget item."""
        #     for i in range(self.listWidget.count()):
        #         item = self.listWidget.item(i)
        #         print(f"{i}: {item.text()}")

    #sets the radio button for rat or mouse
    @Slot()
    def ratselected(self):
        self.ratradio.toggle()

    @Slot()
    def mouseselected(self):
        self.mouseradio.toggle()

#controls the toggles for the drill, needle and probe
    @Slot()
    def setfinespeed(self):
        self.finespeedset.toggle()

    @Slot()
    def setmedspeed(self):
        self.medspeedset.toggle()

    @Slot()
    def setcoarsespeed(self):
        self.coarsespeedset.toggle()

    @Slot()
    def drilloffset(self):
        self.drillradio.toggle()

    @Slot()
    def needleoffset(self):
        self.needleradio.toggle()

    @Slot()
    def probeoffset(self):
        self.fiberradio.toggle()

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
        var_list.MLmove = Steppercontrol(var_list.enableAll,var_list.stepML,var_list.directionML,var_list.limitML,2,var_list.MLleft,var_list.MLright, window)
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
# threadpool.start(mainbuttonthread.runbuttonthread)
# threadpool.start(controlthread.runcontrolthread)

window.show()

app.exec()