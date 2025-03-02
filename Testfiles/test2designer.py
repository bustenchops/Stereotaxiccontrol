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

loader = QUiLoader()

app = QApplication(sys.argv)
window = loader.load("test2designer.ui", None)
window.show()
app.exec()