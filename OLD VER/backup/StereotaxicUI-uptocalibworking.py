# -*- coding: utf-8 -*-

from PySide6.QtCore import (QRect, QThreadPool)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QFrame, QLCDNumber, QMainWindow, QMenuBar, QRadioButton, QStatusBar,
                               QWidget, QLabel, QPlainTextEdit, QCheckBox, QPushButton, QListWidget,QFileDialog,QMessageBox)

#from motorcontrolclass_v2 import StepperSetup
#from rotary_class import RotaryEncoder
from ThreadedControlsv1 import mainprogram

import os
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

#        os.system('rclone copy onedrive:'Usask Job/Targetlists' /home/bustenchops/Stereotaxiccontrol/TargetLists')

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

        self.MVstepLCD = QLCDNumber(self.widget)
        self.MVstepLCD.setObjectName(u"MVstepLCD")
        self.MVstepLCD.setGeometry(QRect(340, 37, 131, 61))
        self.MVstepLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.MVstepLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.MVstepLCD.setLineWidth(1)
        self.MVstepLCD.setDigitCount(7)
        self.MVstepLCD.setProperty(u"value", 888.888)

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

        self.MVABSposLCD = QLCDNumber(self.widget)
        self.MVABSposLCD.setObjectName(u"MVABSposLCD")
        self.MVABSposLCD.setGeometry(QRect(340, 107, 131, 61))
        self.MVABSposLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.MVABSposLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.MVABSposLCD.setLineWidth(1)
        self.MVABSposLCD.setDigitCount(7)
        self.MVABSposLCD.setProperty(u"value", 888.888)

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

        self.MVRelposLCD = QLCDNumber(self.widget)
        self.MVRelposLCD.setObjectName(u"MVRelposLCD")
        self.MVRelposLCD.setGeometry(QRect(340, 177, 131, 61))
        self.MVRelposLCD.setFrameShape(QFrame.Shape.StyledPanel)
        self.MVRelposLCD.setFrameShadow(QFrame.Shadow.Raised)
        self.MVRelposLCD.setLineWidth(1)
        self.MVRelposLCD.setDigitCount(7)
        self.MVRelposLCD.setProperty(u"value", 888.888)

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

        self.MVlabel = QLabel("MV", self.widget)
        self.MVlabel.setObjectName(u"MVlabel")
        self.MVlabel.setGeometry(QRect(390, -3, 41, 41))
        self.MVlabel.setFont(toplabelfont)

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

        self.MVmanualenter = QPlainTextEdit(self.widget)
        self.MVmanualenter.setObjectName(u"MVmanualenter")
        self.MVmanualenter.setGeometry(QRect(420, 310, 91, 40))
        self.MVmanualenter.setFont(manualenterfont)

        self.DVmanualenter = QPlainTextEdit(self.widget)
        self.DVmanualenter.setObjectName(u"DVmanualenter")
        self.DVmanualenter.setGeometry(QRect(420, 360, 91, 40))
        self.DVmanualenter.setFont(manualenterfont)

        self.APlabel = QLabel("AP", self.widget)
        self.APlabel.setObjectName(u"APlabelmanual")
        self.APlabel.setGeometry(QRect(370, 260, 41, 40))
        self.APlabel.setFont(toplabelfont)

        self.MVlabel = QLabel("MV", self.widget)
        self.MVlabel.setObjectName(u"MVlabelmanual")
        self.MVlabel.setGeometry(QRect(370, 310, 41, 40))
        self.MVlabel.setFont(toplabelfont)

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
        self.checkBox.setGeometry(QRect(545, 270, 98, 20))
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

#THREAD POOL WAS HERE


    #grabs the plaintext from the text boxes only if the checkbox is selected
    def plaintextgrab(self):
        APcooord = self.APmanualenter.toPlainText()
        MVcooord = self.MVmanualenter.toPlainText()
        DVcooord = self.DVmanualenter.toPlainText()
        if self.checkBox.isChecked():
            print(f"I want to go to AP:{APcooord}, MV:{MVcooord}, DV:{DVcooord}")
            # RUN THE FUNCTION  TO DO THE CALC AND MOVE
            self.checkBox.setChecked(False)

    def updatepositionLCD(self, stepAP, stepMV, stepDV, ABS_AP, ABS_MV, ABS_DV, REL_AP, REL_MV, REL_DV):
        # print("lcds should update")
        self.APstepLCD.display(stepAP)
        self.MVstepLCD.display(stepMV)
        self.DVstepLCD.display(stepDV)
        self.APABSposLCD.display(ABS_AP)
        self.MVABSposLCD.display(ABS_MV)
        self.DVABSposLCD.display(ABS_DV)
        self.APRelposLCD.display(REL_AP)
        self.MVRelposLCD.display(REL_MV)
        self.DVRelposLCD.display(REL_DV)

#    def copy_folder_from_onedrive(self):
#       os.system('rclone copy onedrive:scans D:/aa')

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

    def selectlistcoordinates(self):
        selected_items = self.listWidget.selectedItems()
        selected_text = selected_items[0].text()
        # Assuming the format is "Item,Value,Extra"
        name, APlist, MVlist, DVlist = selected_text.split(' ')
        self.APmanualenter.setPlainText(APlist)
        self.MVmanualenter.setPlainText(MVlist)
        self.DVmanualenter.setPlainText(DVlist)

    def drilloffset(self):
        self.drilloffsetcheck.toggle()

    def needleoffset(self):
        self.needleoffsetcheck.toggle()

    def probeoffset(self):
        self.fiberoffsetcheck.toggle()

app = QApplication(sys.argv)
window = MainWindow()


maininstancesendcontrol = mainprogram()

# start the threads that need to keep the buttons and such working
threadpool = QThreadPool()
threadpool.start(maininstancesendcontrol.intializethesystem_andrun)

maininstancesendcontrol.receive_frommaincontrol(window)


window.show()

app.exec()