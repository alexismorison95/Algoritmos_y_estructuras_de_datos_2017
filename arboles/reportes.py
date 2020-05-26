# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 03:54:01 2018

@author: Mona Thinkpad
"""


from PyQt4 import QtCore, QtGui, uic


menu = uic.loadUiType("interfaz/reportes.ui")[0]

class Reporte(QtGui.QDialog, menu):
    
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle("Reportes")
        #self.setWindowIcon(QtGui.QIcon('admin_user_man_22187.ico'))
        
   