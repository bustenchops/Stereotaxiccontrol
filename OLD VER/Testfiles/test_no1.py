from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLCDNumber, QMainWindow,
    QMenuBar, QRadioButton, QSizePolicy, QStatusBar,
    QWidget)
from PySide6.QtUiTools import QUiLoader



import sys
import time
import traceback

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.centralwidget = QWidget()

        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QRect(480, 60, 92, 20))
        font1 = QFont()
        font1.setPointSize(12)
        self.radioButton.setFont(font1)


        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QRect(450, 100, 151, 81))
        font2 = QFont()
        font2.setPointSize(24)
        self.lcdNumber.setFont(font2)
        self.lcdNumber.setFrameShape(QFrame.Shape.StyledPanel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

app = QApplication(sys.argv)
window = MainWindow()
app.exec()