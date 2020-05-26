# -*- coding: utf-8 -*-
"""
Created on Tue May  1 01:38:10 2018

@author: Mona Thinkpad
"""

from PyQt4 import QtCore, QtGui, uic
from archivos import abrir, leer, modificar, regNCV, guardar
from arbolinConAVL import cargarArbolNCV, cargarArbolCliente

menu = uic.loadUiType("interfaz/altaBajaModificacion.ui")[0]
archivoId = abrir('id')
archCliente = abrir('Cliente')
archNCV = abrir('NCV')


class AltaBajaModif(QtGui.QDialog, menu):
    
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle("Alta-Baja-Modificación")
        self.setWindowIcon(QtGui.QIcon('bar-chart.png'))

        self.nuevoNombre.setEnabled(False)

        self.cerrar.clicked.connect(self.hide)
        self.idBuscar=leer(archivoId,0)
        self.pos=None
        self.registro=None
        self.inicializar()
        self.nombreCheckBox.clicked.connect(self.modifNombreChecked)
        self.guardar.clicked.connect(self.guardarRegistro)
        self.cargarVentaBox.clicked.connect(self.inicializarVenta)

    def modifNombreChecked(self):
        if (self.nombreCheckBox.isChecked()):
            self.nuevoNombre.setEnabled(True)
        else:
            self.nuevoNombre.setEnabled(False)
            
           
    def inicializar(self):
        for i in range (len(archCliente)):
            reg=leer(archCliente,i)
            if (reg.idCliente==self.idBuscar):
                self.registro=reg
                self.pos=i
        self.clienteLabel.setText('Cliente: '+self.registro.nomCliente)
        if (self.registro.activo):
            self.activoButton.setChecked(True)
        else:
            self.bajaButton.setChecked(True)
    
    def isFloat(self):
        try:
            float(self.importeLine.text())
            return True
        except:
            return False
    
    def guardarRegistro(self):
        if ((self.nombreCheckBox.isChecked()) and (self.nuevoNombre.text()!='')):
            self.registro.nomCliente=self.nuevoNombre.text().title()
        if ((self.activoButton.isChecked()) and (self.registro.activo!=True)):
            self.registro.activo=True
        elif ((self.bajaButton.isChecked()) and (self.registro.activo)):
            self.registro.activo=False
        modificar(archCliente,self.pos,self.registro)
        if (self.cargarVentaBox.isChecked()):
            if (self.importeLine.text()!='') and (self.isFloat()):
                regNuevo=regNCV()
                regNuevo.ncv=len(archNCV)+100
                regNuevo.idVendedor=self.registro.idVendedor
                regNuevo.idCliente=self.registro.idCliente
                regNuevo.importe=float(self.importeLine.text())
                if (self.pagadoButton.isChecked()):
                    regNuevo.pagado=True
                else:
                    regNuevo.pagado=False
                guardar(archNCV,regNuevo)
                print('len de archivo NCV en guardar registro: '+str(len(archNCV)))
        
                """self.arbolNCV = None
                self.arbolNCV = cargarArbolNCV(archNCV)
                self.arbolCliente = None
                self.arbolCliente = cargarArbolCliente(archCliente)"""
                
                
                #print('len  NCV en guardar registro generar arboles: '+str(len(archNCV)))
                #print(regNuevo.ncv,regNuevo.idCliente,  regNuevo.idVendedor, regNuevo.importe, regNuevo.pagado)
                self.hide()
            else:
                self.error('Debe ingresar importe válido')
                self.importeLine.clear()
                    
        else:
            self.hide()
        #archNCV.close()
        #archCliente.close()
            
        
        

    def error(self,mensaje):
        msg = QtGui.QMessageBox()
        msg.setWindowTitle("Error")
        msg.setWindowIcon(QtGui.QIcon('error_15261.ico'))
        msg.setIcon(QtGui.QMessageBox.Critical)
        msg.setText(mensaje)
        msg.exec()
     
    def inicializarVenta(self):
        if (self.activoButton.isChecked()):
            self.cargarVentaBox.setChecked(True)
            self.ncvLabel.setText('NCV: '+str(len(archNCV)+100))
            self.vendedorLabel.setText('Id Vendedor: '+str(self.registro.idVendedor))
        else:
            self.error('El cliente debe estar ACTIVO')
            self.cargarVentaBox.setChecked(False)
            
            
            
    