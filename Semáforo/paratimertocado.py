# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 20:20:24 2017

@author: Mona Thinkpad
"""
import sys
from PyQt4 import QtGui, QtCore

s = 0

 
class Main(QtGui.QMainWindow):
 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()
 
    def initUI(self):
 
        self.timer = QtCore.QTimer(self)
 
        self.lcd = QtGui.QLCDNumber(self)
        self.lcd.setDigitCount(1)
 
        self.time = QtGui.QTimeEdit(self)
        self.timer.timeout.connect(self.Time)
 
        self.set = QtGui.QPushButton("Set",self)
        self.set.clicked.connect(self.Set)
 
        self.stop = QtGui.QPushButton("Stop",self)
        self.stop.clicked.connect(lambda: self.timer.stop())
 
        grid = QtGui.QGridLayout(self)
 
        grid.addWidget(self.lcd,3,0)
        grid.addWidget(self.time,0,0)
        grid.addWidget(self.set,1,0)
        grid.addWidget(self.stop,2,0)
 
        centralwidget = QtGui.QWidget()
 
        self.setCentralWidget(centralwidget)
 
        centralwidget.setLayout(grid)
 
#---------Window settings --------------------------------
         
        self.setGeometry(300,300,280,170)
 
    def Set(self):
        global t,s
         
        t=6
        #t = self.time.time()
        self.lcd.display(t)
 
        self.timer.start(1000)
 
       # h = t.hour()
        #m = t.minute()
        #s = t.second()
         
        s=t
        
    def Time(self):
        global t,s
 
        if s > 0:
            s -=1
        """else:
            if m > 0:
                m -= 1
                s = 59
            elif m == 0 and h > 0:
                h -= 1
                m = 59
                s = 59
            else:
                self.timer.stop()
                
                stop = QtGui.QMessageBox.warning(self,"Time is up","Time is up")"""
 
        time = ("{0}".format(s))
 
        self.lcd.setDigitCount(len(time))
        self.lcd.display(time)
 
def main():
    app = QtGui.QApplication(sys.argv)
    main= Main()
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()
