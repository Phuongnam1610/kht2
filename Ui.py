from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QObject, QThread,pyqtSignal
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QCheckBox, QLineEdit, QGridLayout, QPushButton, QHBoxLayout

from PyQt5 import QtWidgets
from datetime import datetime
from MultiThread import *
import functools
import sys
class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        vbox = QVBoxLayout()

        buttonLayout = QGridLayout()

        # Tạo các button
        self.button1 = QPushButton("Chay Tool")
        self.button2 = QPushButton("To Chau ")
        self.button3 = QPushButton("Nutx  ")
        

        # Thêm các button vào buttonLayout
        buttonLayout.addWidget(self.button1, 0, 0)
        buttonLayout.addWidget(self.button2, 0, 1)
        buttonLayout.addWidget(self.button3, 0, 2)
        # buttonLayout.addWidget(self.button4, 1, 0)
        # buttonLayout.addWidget(self.button5, 1, 1)
        # buttonLayout.addWidget(self.button6, 1, 2)
        # buttonLayout.addWidget(self.button7, 3, 0)
        # buttonLayout.addWidget(self.button8, 3, 1)
        # buttonLayout.addWidget(self.button9, 3, 2)
        # buttonLayout.addWidget(self.button10, 4, 0)
        # buttonLayout.addWidget(self.button11, 4, 1)
        # buttonLayout.addWidget(self.button12, 4, 2)
        # buttonLayout.addWidget(self.button13, 5, 0)
        # Thêm buttonLayout vào vbox
        vbox.addLayout(buttonLayout)


        
        self.button1.clicked.connect(functools.partial(self.ev, 1))
        self.button2.clicked.connect(functools.partial(self.ev, 1))
        self.button3.clicked.connect(functools.partial(self.ev, 3))
        # self.button4.clicked.connect(functools.partial(self.ev, 4))
        # self.button5.clicked.connect(functools.partial(self.ev,6))
        # self.button6.clicked.connect(functools.partial(self.ev,5))
        # self.button7.clicked.connect(functools.partial(self.ev, 8))
        # self.button8.clicked.connect(functools.partial(self.ev, 7))
        # self.button9.clicked.connect(functools.partial(self.ev, 9))
        # self.button10.clicked.connect(functools.partial(self.ev,10))
        # self.button11.clicked.connect(functools.partial(self.ev,11))
        # self.button12.clicked.connect(functools.partial(self.ev,12))
        # self.button13.clicked.connect(functools.partial(self.ev,13))

        self.setLayout(vbox)
        self.setWindowTitle('ADB Device List')
        self.show()
      
        
    def ev(self,i):
        stoptool()
        Ham(i)
        
    def start_work(self,i):        
            self.worker_thread.i=i
            self.worker_thread.start()
            
    def stop_work(self):
            self.worker_thread.terminate()

       

def countdown():
    seconds=3600
    while seconds > 0:
        minutes, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(minutes, secs)
        print(f"Remaining time: {timer}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
class ThreadCountDown(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        countdown()
        pass

        

class WorkerThread(QThread):
    def __init__(self) -> None:
        self.i=0
        super().__init__()

    def run(self):
        Ham(self.i)
 
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    sys.exit(app.exec_())

    