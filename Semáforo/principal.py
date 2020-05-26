# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 21:04:54 2017

@author: Alexis
"""

import sys, time

from PyQt4 import QtGui, uic, QtCore
from PyQt4.QtGui import QPixmap, QPushButton
import TDAColaDinamica
import semaforoMona
from ayuda import Ayuda


menu = uic.loadUiType("interfaz/principal.ui")[0]

class Ventana(QtGui.QMainWindow,menu):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self) 
        
        self.setWindowTitle("Semáforos")
        self.setWindowIcon(QtGui.QIcon('traffic_light_15645.ico'))
        
        self.ayuda()
        
        callesFondo = QPixmap("controlled-crossroads.jpg")
        self.fondo.setPixmap(callesFondo)
        
        membrete = QPixmap("logoWeb3.png")
        self.logo.setPixmap(membrete)
        
        semaforoGrande = QPixmap("apagadograndeprueba.png")
        self.semaforoActivo.setPixmap(semaforoGrande)
        
        self.lista = None
        self.cola = None        
        
        self.lineEdit.setFrame(False)
        self.lineEdit.setReadOnly(True)        
        
        self.lcdNumber.setDigitCount(1)
        
        self.semActivo = None     
        
        self.semaforo1.setPixmap(QPixmap("rojoOE.png"))
        self.semaforo2.setPixmap(QPixmap("rojoSN.png"))
        self.semaforo3.setPixmap(QPixmap("rojoEO.png"))
        self.semaforo4.setPixmap(QPixmap("rojoNS.png"))
        
        self.corriendo = False
        
        self.boton_apagar.setEnabled(False)
        
        self.boton_iniciar.clicked.connect(self.empezar)
        
        self.boton_apagar.clicked.connect(self.apagar)
        
        self.groupBox.setAlignment(0x0004)        
        self.groupBox_2.setAlignment(0x0004)
        
        self.listaBotones = {}
        for i in range (0,4):
            self.boton = QPushButton("Semáforo "+str(i+1))
            self.prioridades.addWidget(self.boton)
            self.boton.clicked.connect(self.botonClickeado)
            self.listaBotones[i] = self.boton
            self.boton.setEnabled(False)
        
        self.existePrioridad = False        
        self.prioridadInsertar = None  
        
        
    def ayuda(self):
        menu = QtGui.QAction("Leeme", self)
        menu.triggered.connect(self.metodo)
        
        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&Ayuda')
        fileMenu.addAction(menu)
    
    def metodo(self):
        dial = Ayuda()
        dial.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dial.setModal(True)        
        dial.exec_()
        
        
    def botonClickeado(self):
        if self.sender() is self.listaBotones[0]:
            print("apreto semaforo1")
            self.existePrioridad = True
            self.prioridadInsertar = self.lista[0]
            
        elif self.sender() is self.listaBotones[1]:
            print("apreto semaforo2")
            self.existePrioridad = True
            self.prioridadInsertar = self.lista[1]
            
        elif self.sender() is self.listaBotones[2]:
            print("apreto semaforo3")
            self.existePrioridad = True
            self.prioridadInsertar = self.lista[2]
            
        elif self.sender() is self.listaBotones[3]:
            print("apreto semaforo4")
            self.existePrioridad = True
            self.prioridadInsertar = self.lista[3]
            
        for i in range(0,4):
            self.listaBotones[i].setEnabled(False)
        self.lineEdit.deselect()
            
        
        
    def todoRojo(self):
        self.semaforo1.setPixmap(QPixmap("rojoOE.png"))
        self.semaforo2.setPixmap(QPixmap("rojoSN.png"))
        self.semaforo3.setPixmap(QPixmap("rojoEO.png"))
        self.semaforo4.setPixmap(QPixmap("rojoNS.png"))
        semaforoGrande = QPixmap("apagadograndeprueba.png")
        self.semaforoActivo.setPixmap(semaforoGrande)

    
    def empezar(self):
        self.lista = semaforoMona.listaSemaforos()       
        self.cola = semaforoMona.encolarLista(self.lista)
        
        self.boton_iniciar.setEnabled(False)
        self.boton_apagar.setEnabled(True)
        for i in range (0,4):
            self.listaBotones[i].setEnabled(True)
        self.corriendo = True
        self.ciclo()
        
        
    def ciclo(self):
        while(self.corriendo):
            if (self.existePrioridad):
                TDAColaDinamica.insertarPrioridad(self.cola,self.prioridadInsertar)
                self.atender()
                self.existePrioridad = False
                for i in range(0,4):
                    self.listaBotones[i].setEnabled(True)
            else:
                TDAColaDinamica.insertarencola(self.cola,self.atender())
            
            
    def apagar(self):
        self.corriendo = False
        self.boton_iniciar.setEnabled(True)
        self.boton_apagar.setEnabled(False)
        for i in range (0,4):
            self.listaBotones[i].setEnabled(False)        
        
        self.lineEdit.setText("")
        self.todoRojo()   
        self.lcdNumber.display(0)
        QtGui.qApp.processEvents()
        
 
    def atender(self):
        x=TDAColaDinamica.eliminarDeCola(self.cola)
        self.lineEdit.setText(str(x.id))
          
        if(x.id == 1):
            self.semActivo = self.semaforo1
            self.semActivo.setPixmap(QPixmap("amarilloOE.png"))
        elif(x.id == 2):
            self.semActivo = self.semaforo2
            self.semActivo.setPixmap(QPixmap("amarilloSN.png"))
        elif(x.id == 3):
            self.semActivo = self.semaforo3
            self.semActivo.setPixmap(QPixmap("amarilloEO.png"))
        elif(x.id == 4):
            self.semActivo = self.semaforo4
            self.semActivo.setPixmap(QPixmap("amarilloNS.png"))            
        
        semaforoGrande = QPixmap("amarillograndeprueba.png")
        self.semaforoActivo.setPixmap(semaforoGrande)
        x.color="amarillo"
        self.cicloAmarillo()
        
        if(self.corriendo):
            
            if(x.id == 1):
                self.semActivo = self.semaforo1
                self.semActivo.setPixmap(QPixmap("verdeOE.png"))
            elif(x.id == 2):
                self.semActivo = self.semaforo2
                self.semActivo.setPixmap(QPixmap("verdeSN.png"))
            elif(x.id == 3):
                self.semActivo = self.semaforo3
                self.semActivo.setPixmap(QPixmap("verdeEO.png"))
            elif(x.id == 4):
                self.semActivo = self.semaforo4
                self.semActivo.setPixmap(QPixmap("verdeNS.png"))
            
            x.color="verde"           
            semaforoGrande = QPixmap("verdegrandeprueba.png")
            self.semaforoActivo.setPixmap(semaforoGrande)
            self.cicloVerde(x.tiempoverde)
            x.color="rojo"
            
            if(x.id == 1):
                self.semActivo.setPixmap(QPixmap("rojoOE.png"))
            elif(x.id == 2):
                self.semActivo.setPixmap(QPixmap("rojoSN.png"))
            elif(x.id == 3):
                self.semActivo.setPixmap(QPixmap("rojoEO.png"))
            elif(x.id == 4):
                self.semActivo.setPixmap(QPixmap("rojoNS.png"))            
            
            return x
        
        
            
    
    def cicloVerde(self,tiempo):
        for tictac in range(tiempo, 0, -1): #instante
            start = time.time()
            while ((time.time() - start < 1) and (self.corriendo == True)):
                self.lcdNumber.display(tictac)                
                QtGui.qApp.processEvents() #actualiza el grafico de la ventana
        
        
    def cicloAmarillo(self):
        for tictac in range(1, 0, -1): #instante
            start = time.time()
            while ((time.time() - start < 1) and (self.corriendo == True)):
                self.lcdNumber.display(tictac)                
                QtGui.qApp.processEvents() #actualiza el grafico de la ventana
    


app = QtGui.QApplication(sys.argv)
principal = Ventana()
principal.show()
app.exec_()

