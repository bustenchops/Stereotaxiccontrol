# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLCDNumber, QMainWindow,
    QMenuBar, QRadioButton, QSizePolicy, QStatusBar,
    QWidget,QLabel)

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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

        self.APmanualenter = QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName(u"APmanualenter")
        self.plainTextEdit.setGeometry(QRect(420, 260, 91, 40))
        self.plainTextEdit.setFont(font1)

        self.plainTextEdit_2 = QPlainTextEdit(self.widget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(420, 310, 91, 40))
        self.plainTextEdit_2.setFont(font1)
        self.plainTextEdit_2.setLineWidth(1)
        self.plainTextEdit_3 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(420, 360, 91, 40))
        self.plainTextEdit_3.setFont(font1)
        self.plainTextEdit_3.setLineWidth(1)





        self.menubar = QMenuBar()
        self.menubar.setGeometry(QRect(0, 0, 800, 33))

        self.statusbar = QStatusBar()
        self.setCentralWidget(self.widget)





app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()