# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 00:05:51 2017

@author: Mona Thinkpad
"""

import sys, time
from PyQt4 import QtCore, QtGui

class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.spinbox = QtGui.QSpinBox(self)
        self.spinbox.setValue(5)
        self.lcdnumber = QtGui.QLCDNumber(self)
        self.button = QtGui.QPushButton('Start', self)
        self.button.clicked.connect(self.handleButton)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.spinbox)
        layout.addWidget(self.lcdnumber)
        layout.addWidget(self.button)

    def handleButton(self): #manejar el boton
        for tick in range(self.spinbox.value(), -1, -1): #instante
            self.lcdnumber.display(tick)
            self.button.setEnabled(not tick)
            # continuamente procesa eventos por un segundo
            start = time.time()
            while time.time() - start < 1:
                QtGui.qApp.processEvents()
                time.sleep(0.02)

    def start_btn_clicked(self):
        x = self.Minute_spinBox.value()
        for i in range(x,0,-1):
            time.sleep(1)
            app.processEvents() # solo esta línea permite mostrar 'i'
            self.lcdNumber.display(i)


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.setGeometry(500, 300, 300, 200)
    window.show()
    sys.exit(app.exec_())