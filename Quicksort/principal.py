# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 01:05:34 2017

@author: Mona Thinkpad
"""

import sys

from PyQt4 import QtGui, uic, QtCore
from PyQt4.QtGui import QTableWidgetItem, QHeaderView, QPixmap, QAbstractItemView
from test import CargarEnLista, QuickSortIterativoAZ, QuickSortIterativoZA 
from test import LevantarArchivo, bbrecursivaZA, bbrecursivaAZ
from Archivo import abrir
from ayuda import Ayuda
import random
import time

menu = uic.loadUiType("interfaceGrafica/ppalQuicksort.ui")[0] 

#arch = abrir("pruebaordenar")


class Ventana(QtGui.QMainWindow,menu):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self) 
        self.setWindowTitle("Quicksort Iterativo")
        self.setWindowIcon(QtGui.QIcon('personas.ico'))
        
        self.membrete.setPixmap(QPixmap("logoWeb3.png"))
        
        self.ayuda()
        
        self.barra.reset()
        self.barra.setAlignment(QtCore.Qt.AlignCenter)
        
        header = self.tabla.horizontalHeader()
        header.setResizeMode(QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)
        self.tabla.setRowCount(0)
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        self.listAux = []
        self.listMona = []
        self.cargarLista.clicked.connect(self.levantarARam)  
        self.desordenar.clicked.connect(self.desordenado)
        self.AZ.clicked.connect(self.ascendente)
        self.ZA.clicked.connect(self.descendente)
        
        self.desordenar.setEnabled(False)        
        self.AZ.setEnabled(False)
        self.ZA.setEnabled(False)
        self.busquedab.setEnabled(False)
        self.aceptar.setEnabled(False)
        
        
        self.orden.setStyleSheet('color: grey')       
        self.bb.setStyleSheet('color: grey')
        
        self.aceptar.clicked.connect(self.busquedaAprox)
        
        self.az = False
        self.za = False
        


    def deseleccionar(self):
        self.tabla.selectRow(0)
        self.tabla.clearSelection()
    
       
    def busquedaAprox(self):
        encontrados=[]
        buscado=self.busquedab.text().title()
        #print(mona)
    
        for i in self.listAux:
            if(len(i) >= len(buscado) and i[0:len(buscado)] == buscado):
                encontrados.append(i)
        #print(encontrados)
        self.cargarTabla(encontrados)
                
        #self.origen.setCompleter(QtGui.QCompleter(self.lista,self.origen)) #mona
        """
    def bbAZZA(self):
        if (self.busquedab.text()!= ""):
            #mona
            #buscado = self.busquedab.text()+'\n'    
            if (self.az):
                pos = bbrecursivaAZ(self.listAux,buscado.title(),0,len(self.listAux)-1)
                    
            elif (self.za):
                pos = bbrecursivaZA(self.listAux,buscado.title(),0,len(self.listAux)-1)
                
            if (pos == -1):
                self.errorBusqueda("Nombre no encontrado") 
            else:
                
                self.tabla.selectRow(pos)
               # print(pos)
               #print(self.listAux[pos])  
        else:
            self.errorBusqueda("Ingrese nombre a buscar")
        self.busquedab.setText('')         
        """
             
        
        
        

    def ayuda(self):
        menu = QtGui.QAction("Leéme", self)
        menu.triggered.connect(self.metodo)
        
        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&Ayuda')
        fileMenu.addAction(menu)
        
    #esta seria la ventana que se abre
    def metodo(self):
        dial = Ayuda()
        dial.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dial.setModal(True)        
        dial.exec_()
        
    
    def errorBusqueda(self,mensaje):
        msg = QtGui.QMessageBox()
        msg.setWindowTitle("Error")
        msg.setWindowIcon(QtGui.QIcon('error_15261.ico'))
        msg.setIcon(QtGui.QMessageBox.Critical)
        msg.setText(mensaje)
        msg.exec()
            
            
    def cargarTabla(self,lista):
        self.tabla.setRowCount(0) #pone las filas en cero resetea la tabla        
        for i in range(0,len(lista)):
            self.tabla.insertRow(i)
            self.tabla.setItem(i, 0, QTableWidgetItem(str(lista[i])))
        self.barra.reset()
        
        self.desordenar.setEnabled(True)        
        self.AZ.setEnabled(True)
        self.ZA.setEnabled(True)
        self.busquedab.clear()
        
        self.orden.setStyleSheet('')   
        
    
    
    def levantarARam(self):
        #aux = CargarEnLista(arch,self.barra)
        lista = LevantarArchivo()
        self.listAux = lista
        self.cargarTabla(self.listAux)
        self.barra.reset()
        
        self.busquedab.setEnabled(False)      
        self.bb.setStyleSheet('color: grey')
        self.aceptar.setEnabled(False)        
        
        self.az = False
        self.za = False
        
        self.busquedab.clear()
        
        self.deseleccionar()
        
        
    def ascendente(self):
        
        self.az = True
        self.za = False        
        
        self.listAux = QuickSortIterativoAZ(self.listAux,self.barra)
        self.cargarTabla(self.listAux)
        
        
        self.busquedab.setEnabled(True)      
        self.bb.setStyleSheet('')
        self.aceptar.setEnabled(True)
            
        self.deseleccionar()
        self.busquedab.clear()
            
    
    def descendente(self):
        
        self.za = True
        self.az = False        
        
        self.cargarTabla(QuickSortIterativoZA(self.listAux,self.barra))
        
        self.busquedab.setEnabled(True)      
        self.bb.setStyleSheet('')
        self.aceptar.setEnabled(True)
        
        self.deseleccionar()
        self.busquedab.clear()


    def desordenado(self):
        v = 1
        for i in reversed(range(1, len(self.listAux))):
            self.barra.setValue(v*101//len(self.listAux))
            v+=1
            j = random.randint(0,3107)
            aux = self.listAux[i]
            self.listAux[i] = self.listAux[j]
            self.listAux[j] = aux
        self.cargarTabla(self.listAux)
        
        self.busquedab.setEnabled(False)      
        self.bb.setStyleSheet('color: grey')
        self.aceptar.setEnabled(False)
        
        self.az = False
        self.za = False
        
        self.deseleccionar()
        self.busquedab.clear()

app = QtGui.QApplication(sys.argv)
principal = Ventana()
principal.show()
app.exec_()
