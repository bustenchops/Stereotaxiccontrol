from PySide6.QtCore import QRunnable, Slot
import time
class threadtesting(QRunnable):

    @Slot()
    def counterup(self):
        self.counter = 0

        while True:
            print(self.counter)
            time.sleep(0.01)
            self.counter +=1
