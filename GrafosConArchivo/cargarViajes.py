# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:47:24 2017

@author: Alexis
"""

from PyQt4 import QtGui, uic
from tpentrerios import grafo
from archivoG import abrir

menu = uic.loadUiType("interfaz/cargarViaje.ui")[0]


fileVertices = abrir("vertices")

sePuedeGuardar = False

class CargarViaje(QtGui.QDialog, menu):
    
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle("Cargar Viaje")
        self.setWindowIcon(QtGui.QIcon('maps_22147.ico'))
        self.cancelar.clicked.connect(self.hide)

        self.grafo = grafo()        
        self.grafo.iniVertices(fileVertices)  
        
        self.lista = []
        act = self.grafo.cab
        while(act != None):
            self.lista.append(act.info.ciudad)
            act = act.sig

        self.origen.setPlaceholderText('Ingrese una ciudad de origen')
        self.destino.setPlaceholderText('Ingrese una ciudad de destino')
        self.importe.setPlaceholderText('Ingrese importe')
        self.distancia.setPlaceholderText('Ingrese distancia')
       
        self.origen.setCompleter(QtGui.QCompleter(self.lista,self.origen)) #pongo inicial y me muestra los que coinciden
        self.origen.textChanged.connect(self.cargarO)
        
        self.destino.setCompleter(QtGui.QCompleter(self.lista,self.destino))
        self.destino.textChanged.connect(self.cargarD)
         
        self.importe.textChanged.connect(self.importeV)
        self.distancia.textChanged.connect(self.distanciaV)
    
        self.aceptar.clicked.connect(self.guardarV)
        
        self.distanciaBool = False
        self.importeBool = False
        self.origenBool = False
        self.destinoBool = False
     
          
    def esInt(self,value):
        try:
            int(value)
            return True
        except:
            return False
    
    
    def esFloat(self,value):
        try:
            float(value)
            return True
        except:
            return False
    
    
    def distanciaV(self):
        if(self.distancia.text() != ""):
            if(self.esFloat(self.distancia.text())):
                self.distancia.setStyleSheet("border: 2px solid lightgreen;")
                self.distanciaBool = True
            else:
                self.distancia.setStyleSheet("border: 2px solid red;")
                self.distanciaBool = False
        else:
            self.distancia.setStyleSheet("")
            self.distanciaBool = False
    
        
    def importeV(self):
        if(self.importe.text() != ""):
            if(self.esFloat(self.importe.text())):
                self.importe.setStyleSheet("border: 2px solid lightgreen;")
                self.importeBool = True
            else:
                self.importe.setStyleSheet("border: 2px solid red;") 
                self.importeBool = False
        else:
            self.importe.setStyleSheet("")
            self.importeBool = False
    

              
    def cargarO(self):
        if(self.origen.text() != ""):
            pos = self.grafo.buscarVertice(self.origen.text())
            if((pos == None) or (self.destino.text() == self.origen.text())):
                self.origen.setStyleSheet("border: 2px solid red;")
                self.origenBool = False
            else:
                self.origen.setStyleSheet("border: 2px solid lightgreen;")
                self.origenBool = True
        else:
            self.origen.setStyleSheet("")
            self.origenBool = False
    
            
    def cargarD(self):
        if(self.destino.text() != ""):
            pos = self.grafo.buscarVertice(self.destino.text())
            if((pos == None) or (self.destino.text() == self.origen.text())):
                self.destino.setStyleSheet("border: 2px solid red;")
                self.destinoBool = False
            else:
                self.destino.setStyleSheet("border: 2px solid lightgreen;") 
                self.destinoBool = True
        else:
            self.destino.setStyleSheet("")
            self.destinoBool = False
     
           
    def guardarV(self):
        if(len(self.origen.text().strip())>0 and len(self.destino.text().strip())>0 and len(self.importe.text().strip())>0 and len(self.distancia.text().strip())>0):
            if(self.origenBool and self.destinoBool and self.importeBool and self.distanciaBool):            
                
                print("guardo el viaje")
                msg = QtGui.QMessageBox()
                msg.setWindowTitle("Éxito")
                msg.setWindowIcon(QtGui.QIcon('maps_22147.ico'))
                msg.setText("Viaje guardado correctamente      ")
                msg.exec()
            else:
                msg = QtGui.QMessageBox()
                msg.setWindowTitle("Error")
                msg.setWindowIcon(QtGui.QIcon('maps_22147.ico'))
                msg.setIcon(QtGui.QMessageBox.Critical)
                msg.setText("Algún campo es incorrecto")
                msg.exec()
        else:
            msg = QtGui.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setWindowIcon(QtGui.QIcon('maps_22147.ico'))
            msg.setIcon(QtGui.QMessageBox.Critical)
            msg.setText("Debe completar todos los campos")
            msg.exec()
                
                
                
                
                
                
                
                