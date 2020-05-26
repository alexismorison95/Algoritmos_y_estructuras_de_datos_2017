# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 20:59:42 2017

@author: Alexis
"""
import sys

from PyQt4 import QtGui, uic, QtCore
from PyQt4.QtGui import QTableWidgetItem, QHeaderView, QPixmap, QAbstractItemView
from passW import Contra
from ayuda import Ayuda
from tpentrerios import grafo
from archivoG import abrir, cerrar


menu = uic.loadUiType("interfaz/main.ui")[0] 


fileVertices = abrir("vertices")
fileAristas = abrir("aristas")




class Ventana(QtGui.QMainWindow,menu):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self) 
        self.setWindowTitle("Viajes Mona Alexis")
        self.setWindowIcon(QtGui.QIcon('bus_icon-icons.com_76529.ico'))
               
        self.cargarMapaDefecto() #sinrutas
        
        self.label_4.setPixmap(QPixmap("logoWeb1.png"))
        
        self.grafo = grafo()  
        
        self.grafo.iniVertices(fileVertices)
        self.grafo.iniAristas(fileAristas)
   
        #cargo las ciudades disponibles en combobox
        aux = self.grafo.cab
        while(aux != None):          
            self.origen.addItem(aux.info.ciudad)
            aux = aux.sig

        self.origen.currentIndexChanged.connect(self.cargarDestino)
        
        #cargo la tabla
        self.tableWidget.setColumnCount(3)        
        self.tableWidget.setHorizontalHeaderLabels(['CIUDADES', 'PRECIO', 'DISTANCIA'])
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)        
                
        
        header = self.tableWidget.horizontalHeader() #ajusta columas depende cargue
        header.setResizeMode(QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)
        
        self.tableWidget.setSortingEnabled(True) #permite ordenar en tabla
        
        if(self.tableWidget.rowCount() == 0):
            self.pushButton_3.setEnabled(False)
            self.pushButton_4.setEnabled(False)
               
        self.buscarViaje.clicked.connect(self.buscarCaminos)
        self.tableWidget.clicked.connect(self.seleccionado) #marca camino seleccionado
        self.pushButton_3.clicked.connect(self.ordenarPrecio)
        self.pushButton_4.clicked.connect(self.ordenarDistancia)
        
        self.ayuda()
        
        
    def ayuda(self):          
        self.statusBar()

        mainMenu = self.menuBar()
 
        menu1 = QtGui.QAction("Administrador", self)
        menu1.triggered.connect(self.admini)
        fileMenu1 = mainMenu.addMenu('&Permiso')
        fileMenu1.addAction(menu1)
        
        menu = QtGui.QAction("Leéme", self)
        menu.triggered.connect(self.metodo)
        fileMenu = mainMenu.addMenu('&Ayuda')
        fileMenu.addAction(menu)
        
               
    #esta seria la ventana que se abre
    def metodo(self):
        dial = Ayuda()
        dial.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dial.setModal(True) #ventana visible       
        dial.exec_()
        
    def admini(self):
        dial = Contra()
        dial.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dial.setModal(True) #ventana visible       
        dial.exec_()
    
    
    def ordenarDistancia(self):
        self.tableWidget.sortItems(2)
    
    
    def ordenarPrecio(self):
        self.tableWidget.sortItems(1)
        
        
    def actualizar(self):
        self.origen.clear() #limpia comboBox
        
        self.grafo = None
        self.grafo = grafo()
        
        fileVertices = abrir("vertices")
        fileAristas = abrir("aristas")
        
        self.grafo.iniVertices(fileVertices)
        self.grafo.iniAristas(fileAristas)
        
        aux = self.grafo.cab 
        self.origen.addItem("")
        while(aux != None): 
            #print(aux.info.ciudad)
            self.origen.addItem(aux.info.ciudad)
            aux = aux.sig
        self.destino.clear()
        
                
    def cargarMapaDefecto(self):        
        center ="center=rosario del tala entre rios" #centro del mapa
        zoom = "&zoom=7"
        size = "&size=405x390"                         
        imgformat = "&format=png"
        maptype="&maptype=roadmap" #rutas nacionales
        sensor = "&sensor=false" #ubucacion gps
        self.visor.load(QtCore.QUrl("https://maps.googleapis.com/maps/api/staticmap?"+center+zoom
                        +size+imgformat+maptype+sensor))
        
    
    def cargarDestino(self):
        self.destino.clear()
        aux = self.grafo.cab
        while(aux != None):
            if(aux.info.ciudad != self.origen.currentText()):
                self.destino.addItem(aux.info.ciudad)
            aux = aux.sig
    
    
    def cargarMapa(self,caminoElegido):
        center ="center=rosario del tala entre rios" #centro del mapa
        zoom = "&zoom=7"
        size = "&size=405x390"         
        lista_vertices = []  
        #cargo los vertices y las aristas en 2 vectores
        aux = self.grafo.cab
        while(aux != None):
            if(aux.info.ciudad in caminoElegido):
                lista_vertices.append(aux.info.ciudad)
            aux = aux.sig
        marcas = "|"
        marcas = marcas.join(lista_vertices)           
        viajes = caminoElegido
        markers = "&markers=" + "color:red|"+ marcas
        path = "&path=weight:4"+ viajes
        imgformat = "&format=png"
        maptype="&maptype=roadmap"
        sensor = "&sensor=false"
        self.visor.load(QtCore.QUrl("https://maps.googleapis.com/maps/api/staticmap?"+center+zoom
                        +size+markers+path+imgformat+maptype+sensor))
     
     
    def buscarCaminos(self): #muestra en tabla cminos encontrados           
        if(self.origen.currentText()==''):
            msg = QtGui.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setWindowIcon(QtGui.QIcon('error_15261.ico'))
            msg.setText("Debe seleccionar Ciudades      ")
            msg.exec()
        else:
            self.cargarMapaDefecto()
            self.tableWidget.setRowCount(0)
            lista = self.grafo.caminos(self.origen.currentText(),self.destino.currentText())
            #print(len(lista))
            if(len(lista) == 0): #no existe camino
                msg = QtGui.QMessageBox()
                msg.setWindowTitle("Error")
                msg.setWindowIcon(QtGui.QIcon('error_15261.ico'))
                msg.setText("No hay viajes entre "+self.origen.currentText().capitalize()+" y "+self.destino.currentText().capitalize()+"       ")
                msg.exec()
            else: 
                self.pushButton_3.setEnabled(True)
                self.pushButton_4.setEnabled(True)
                for i in range(0,len(lista)):
                    self.tableWidget.insertRow(i)
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(str(lista[i].camino)))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(str(lista[i].importe)))
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(str(lista[i].distancia)))
    
    
    def seleccionado(self): #dibuja camino seleccionado
        string = ""
        for item in self.tableWidget.selectedItems():
            string+= item.text()
        #print(string)
        self.cargarMapaDefecto()
        self.cargarMapa(string)
        


app = QtGui.QApplication(sys.argv)
principal = Ventana()
principal.show()
app.exec_()