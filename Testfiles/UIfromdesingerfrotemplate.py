# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test2designerDFhffQ.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLCDNumber,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(170, 37, 141, 61))
        self.lcdNumber.setFrameShape(QFrame.Shape.StyledPanel)
        self.lcdNumber.setFrameShadow(QFrame.Shadow.Raised)
        self.lcdNumber.setLineWidth(1)
        self.lcdNumber.setDigitCount(7)
        self.lcdNumber.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber.setProperty(u"value", 188.889000000000010)
        self.lcdNumber.setProperty(u"intValue", 189)
        self.lcdNumber_2 = QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setGeometry(QRect(340, 37, 131, 61))
        self.lcdNumber_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.lcdNumber_2.setFrameShadow(QFrame.Shadow.Raised)
        self.lcdNumber_2.setLineWidth(1)
        self.lcdNumber_2.setDigitCount(7)
        self.lcdNumber_2.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber_2.setProperty(u"value", 188.889000000000010)
        self.lcdNumber_2.setProperty(u"intValue", 189)
        self.lcdNumber_3 = QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        self.lcdNumber_3.setGeometry(QRect(500, 37, 131, 61))
        self.lcdNumber_3.setAutoFillBackground(True)
        self.lcdNumber_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.lcdNumber_3.setFrameShadow(QFrame.Shadow.Raised)
        self.lcdNumber_3.setLineWidth(1)
        self.lcdNumber_3.setSmallDecimalPoint(False)
        self.lcdNumber_3.setDigitCount(7)
        self.lcdNumber_3.setMode(QLCDNumber.Mode.Dec)
        self.lcdNumber_3.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber_3.setProperty(u"value", -88.887000000000000)
        self.lcdNumber_3.setProperty(u"intValue", -89)
        self.lcdNumber_4 = QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")
        self.lcdNumber_4.setGeometry(QRect(170, 107, 141, 61))
        self.lcdNumber_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.lcdNumber_4.setFrameShadow(QFrame.Shadow.Raised)
        self.lcdNumber_4.setLineWidth(1)
        self.lcdNumber_4.setDigitCount(7)
        self.lcdNumber_4.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber_4.setProperty(u"value", 188.889000000000010)
        self.lcdNumber_4.setProperty(u"intValue", 189)
        self.lcdNumber_5 = QLCDNumber(self.centralwidget)
        self.lcdNumber_5.setObjectName(u"lcdNumber_5")
        self.lcdNumber_5.setGeometry(QRect(340, 107, 131, 61))
        self.lcdNumber_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.lcdNumber_5.setFrameShadow(QFrame.Shadow.Raised)
        self.lcdNumber_5.setLineWidth(1)
        self.lcdNumber_5.setDigitCount(7)
        self.lcdNumber_5.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber_5.setProperty(u"value", 188.889000000000010)
        self.lcdNumber_5.setProperty(u"intValue", 189)
        self.lcdNumber_6 = QLCDNumber(self.centralwidget)
        self.lcdNumber_6.setObjectName(u"lcdNumber_6")
        self.lcdNumber_6.setGeometry(QRect(500, 107, 131, 61))
        self.lcdNumber_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.lcdNumber_6.setFrameShadow(QFrame.Shadow.Raised)
        self.lcdNumber_6.setLineWidth(1)
        self.lcdNumber_6.setDigitCount(7)
        self.lcdNumber_6.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber_6.setProperty(u"value", 188.889000000000010)
        self.lcdNumber_6.setProperty(u"intValue", 189)
        self.lcdNumber_7 = QLCDNumber(self.centralwidget)
        self.lcdNumber_7.setObjectName(u"lcdNumber_7")
        self.lcdNumber_7.setGeometry(QRect(170, 177, 141, 61))
        self.lcdNumber_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.lcdNumber_7.setFrameShadow(QFrame.Shadow.Raised)
        self.lcdNumber_7.setLineWidth(1)
        self.lcdNumber_7.setDigitCount(7)
        self.lcdNumber_7.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber_7.setProperty(u"value", 188.889000000000010)
        self.lcdNumber_7.setProperty(u"intValue", 189)
        self.lcdNumber_8 = QLCDNumber(self.centralwidget)
        self.lcdNumber_8.setObjectName(u"lcdNumber_8")
        self.lcdNumber_8.setGeometry(QRect(340, 177, 131, 61))
        self.lcdNumber_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.lcdNumber_8.setFrameShadow(QFrame.Shadow.Raised)
        self.lcdNumber_8.setLineWidth(1)
        self.lcdNumber_8.setDigitCount(7)
        self.lcdNumber_8.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber_8.setProperty(u"value", 188.889000000000010)
        self.lcdNumber_8.setProperty(u"intValue", 189)
        self.lcdNumber_9 = QLCDNumber(self.centralwidget)
        self.lcdNumber_9.setObjectName(u"lcdNumber_9")
        self.lcdNumber_9.setGeometry(QRect(500, 177, 131, 61))
        self.lcdNumber_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.lcdNumber_9.setFrameShadow(QFrame.Shadow.Raised)
        self.lcdNumber_9.setLineWidth(1)
        self.lcdNumber_9.setSmallDecimalPoint(False)
        self.lcdNumber_9.setDigitCount(7)
        self.lcdNumber_9.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber_9.setProperty(u"value", 188.889000000000010)
        self.lcdNumber_9.setProperty(u"intValue", 189)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 47, 111, 41))
        self.label.setTextFormat(Qt.TextFormat.AutoText)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 107, 111, 61))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 177, 111, 61))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, -3, 41, 41))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(390, -3, 41, 41))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(550, -3, 41, 41))
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(140, 273, 211, 101))
        font = QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 380, 161, 31))
        self.pushButton.setFont(font)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(160, 243, 171, 31))
        self.pushButton_2.setFont(font)
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(420, 260, 91, 40))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.plainTextEdit.setFont(font1)
        self.plainTextEdit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.plainTextEdit.setLineWidth(1)
        self.plainTextEdit_2 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(420, 310, 91, 40))
        self.plainTextEdit_2.setFont(font1)
        self.plainTextEdit_2.setLineWidth(1)
        self.plainTextEdit_3 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(420, 360, 91, 40))
        self.plainTextEdit_3.setFont(font1)
        self.plainTextEdit_3.setLineWidth(1)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(370, 260, 41, 40))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(370, 310, 41, 40))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(370, 360, 41, 40))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(540, 310, 101, 81))
        font2 = QFont()
        font2.setPointSize(14)
        self.pushButton_3.setFont(font2)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(550, 270, 78, 20))
        font3 = QFont()
        font3.setPointSize(11)
        self.checkBox.setFont(font3)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(652, 140, 111, 16))
        self.label_10.setFont(font)
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(662, 170, 92, 20))
        self.radioButton.setFont(font)
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(662, 200, 92, 20))
        self.radioButton_2.setFont(font)
        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(662, 230, 92, 20))
        self.radioButton_3.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Step position:</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">ABS pos:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">REL pos:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">AP</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">MV</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">DV</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Arm Coordinates", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Load Preset File", None))
        self.plainTextEdit.setDocumentTitle("")
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-00.000", None))
        self.plainTextEdit_2.setDocumentTitle("")
        self.plainTextEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"+00.000", None))
        self.plainTextEdit_3.setDocumentTitle("")
        self.plainTextEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"000.000", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">AP</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">MV</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">DV</span></p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Engage", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Current Offset", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Drill", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Syringe", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Probe", None))
    # retranslateUi

