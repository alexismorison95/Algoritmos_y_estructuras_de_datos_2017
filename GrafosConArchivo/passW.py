# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 05:20:22 2018

@author: Mona Thinkpad
"""

from PyQt4 import QtCore, QtGui, uic
from admin import Administracion

menu = uic.loadUiType("interfaz/contra.ui")[0]

#cerrar(fileVertices)

class Contra(QtGui.QDialog, menu):
    
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle("Administrador")
        self.setWindowIcon(QtGui.QIcon('admin_user_man_22187.ico'))
        
        self.lineEditContra.setEchoMode(2)
        
        self.aceptar.clicked.connect(self.verificar)
        self.cancelar.clicked.connect(self.hide)
        
        
    def verificar(self):
        if(str(self.lineEditContra.text())=='1234'):
            self.hide()
            dial = Administracion()
            dial.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            dial.setModal(True) #ventana visible       
            dial.exec_()
        else:
            msg = QtGui.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setWindowIcon(QtGui.QIcon('admin_user_man_22187.ico'))
            msg.setIcon(QtGui.QMessageBox.Critical)
            msg.setText("Contraseña incorrecta")
            msg.exec()
            
            self.lineEditContra.clear()