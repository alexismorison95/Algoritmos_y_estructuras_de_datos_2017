# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 21:57:02 2017

@author: Alexis
"""

from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QTableWidgetItem, QHeaderView, QColor
from tpentrerios import grafo
from archivoG import abrir,cerrar
from cargarViajes import CargarViaje


menu = uic.loadUiType("interfaz/admin.ui")[0]

fileVertices = abrir("vertices")
fileAristas = abrir("aristas")

#cerrar(fileVertices)

class Administracion(QtGui.QDialog, menu):
    
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle("Administración")
        self.setWindowIcon(QtGui.QIcon('admin_user_man_22187.ico'))
        
        self.grafo = grafo()
        self.grafo.iniVertices(fileVertices)
        self.grafo.iniAristas(fileAristas)
        
        
        self.cerrar.clicked.connect(self.cerrarVentana)
        
        self.listaC.verticalHeader().hide()
        self.listaC.setColumnCount(2)
        self.listaC.setHorizontalHeaderLabels(['ID', 'NOMBRE'])
        
        header = self.listaC.horizontalHeader()
        header.setResizeMode(QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)
        
        self.listaC.setSortingEnabled(True)
        
        self.iniCiudades()
        
        self.nombreC.setPlaceholderText('Ingrese nombre de ciudad')
        
        self.guardar.clicked.connect(self.guardarCiudad)
        
        self.cargarV.clicked.connect(self.viajes)
        
        self.listaV.verticalHeader().hide()
        self.listaV.setColumnCount(2)
        self.listaV.setHorizontalHeaderLabels(['CIUDAD', 'SE CONECTA CON'])
        header = self.listaV.horizontalHeader()
        header.setResizeMode(QHeaderView.ResizeToContents)
        header.setStretchLastSection(False)
        self.listaV.setSortingEnabled(True)
        
        
        self.iniViajes()
        self.listaV.resizeRowsToContents()
        
        self.nombreC.deselect()
    
    
    
    def cerrarVentana(self):
        #cerrar(fileVertices)
        self.hide()
    
    
    def esFloat(self,value):
        try:
            float(value)
            return True
        except:
            return False
            
    
    def guardarCiudad(self):
        if(len(self.nombreC.text().strip())>0):
            if(self.grafo.buscarVertice(self.nombreC.text()) != None):
                msg = QtGui.QMessageBox()
                msg.setWindowTitle("Error")
                msg.setWindowIcon(QtGui.QIcon('admin_user_man_22187.ico'))
                msg.setIcon(QtGui.QMessageBox.Critical)
                msg.setText("Ya existe la ciudad")
                msg.exec()
            else:
                if(self.esFloat(self.nombreC.text())):
                    self.nombreC.setStyleSheet("border: 1px solid red;")
                else:
                    print("cargo la ciudad: "+self.nombreC.text())
                    if(self.grafo.cargarCiudadQT(fileVertices,self.nombreC.text())):
                        msg = QtGui.QMessageBox()
                        msg.setWindowTitle("Éxito")
                        msg.setWindowIcon(QtGui.QIcon('admin_user_man_22187.ico'))
                        msg.setText("Éxito")
                        msg.exec()
                            
                        self.nombreC.clear()
                        self.nombreC.setPlaceholderText('Ingrese nombre de ciudad')
                        self.nombreC.setStyleSheet("")

                            #cerrar(fileVertices)
                        self.grafo = grafo()
                            #fileVertices = abrir("vertices")
                        self.grafo.iniVertices(fileVertices)
                        self.grafo.iniAristas(fileAristas)
                            
                        self.iniCiudades()
                    else:
                        msg = QtGui.QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setWindowIcon(QtGui.QIcon('admin_user_man_22187.ico'))
                        msg.setText("Falló el guardado")
                        msg.exec()
        else:
            msg = QtGui.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setWindowIcon(QtGui.QIcon('admin_user_man_22187.ico'))
            msg.setIcon(QtGui.QMessageBox.Critical)
            msg.setText("Debe completar el campo")
            msg.exec()
    
    
    def viajes(self): #abre ventana para cargar viajes
        dial = CargarViaje()
        dial.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dial.setModal(True)        
        dial.exec_()
        
        
    def iniViajes(self): #inicializa tabla de viajes cargados
        row = 0
        aux = self.grafo.cab
        self.listaV.setRowCount(0)
        while(aux != None):
            nomb = str(aux.info.ciudad.capitalize())
            act = aux.cab
            conexion = ""
            while(act != None):
                if(act.sig != None):
                    conexion += act.info.CD.capitalize()+" \n"
                else:
                    conexion += act.info.CD.capitalize()
                act = act.sig
            self.listaV.insertRow(row) #tabla de viajes
            self.listaV.setItem(row, 0, QTableWidgetItem(nomb))
            self.listaV.setItem(row, 1, QTableWidgetItem(conexion))
            row += 1
            aux = aux.sig
                
            
    def iniCiudades(self):    #inicializa tabla de ciudades cargadas
        row = 0
        aux = self.grafo.cab
        self.listaC.setRowCount(0)
        while(aux != None):
            self.listaC.insertRow(row)
            self.listaC.setItem(row, 0, QTableWidgetItem(str(aux.info.idCiudad)))
            self.listaC.setItem(row, 1, QTableWidgetItem(str(aux.info.ciudad.capitalize())))
            row += 1
            aux = aux.sig
        
        #cambia color de fondo de una celda y texto
        #self.listaC.item(1,1).setBackground(QColor("red"))
        
        #self.listaC.item(2,1).setBackground(QColor("#A3CE5D"))
        #self.listaC.item(1,1).setTextColor(QColor("white"))
        
        
        
