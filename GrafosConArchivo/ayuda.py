# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 13:09:21 2018

@author: Alexis
"""
import os
from PyQt4 import QtCore, QtGui, uic


menu = uic.loadUiType("interfaz/ayuda.ui")[0]

class Ayuda(QtGui.QDialog, menu):
    
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle("Información")
        self.setWindowIcon(QtGui.QIcon('admin_user_man_22187.ico'))
        
        self.pushButton.clicked.connect(self.cerrarVentana)
   
        
    def cerrarVentana(self):
        self.hide()