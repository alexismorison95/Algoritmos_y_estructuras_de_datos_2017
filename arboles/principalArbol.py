# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 01:47:39 2018

@author: Mona Thinkpad
"""

import sys


from PyQt4 import QtGui, uic, QtCore
from PyQt4.QtGui import QTableWidgetItem, QHeaderView, QPixmap, QColor

from archivos import abrir, leer, crearDatNCV, crearDatCliente, guardarid, cerrar
from arbolinConAVL import cargarArbolNCV, cargarArbolCliente, busquedaCliente

from altaBajaModif import AltaBajaModif

from ayuda import Ayuda

menu = uic.loadUiType("interfaz/principalArbol.ui")[0] 
        
#crearDatNCV(archNCV)
#crearDatCliente(archCliente)

class Ventana(QtGui.QMainWindow,menu):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self) 
        self.setWindowTitle("Estadística de Ventas")
        self.setWindowIcon(QtGui.QIcon('bar-chart.png'))
        self.arbolNCV = None
        self.arbolCliente = None  
        
        self.barras()
        self.ayuda()
        
        #self.tabla.setColumnCount(7)        
        #self.tabla.setHorizontalHeaderLabels(['NCV', 'Vendedor', 'IDCliente', 'Nombre', 'Activo', 'Importe','Pagado'])
        
        self.tabla.setColumnWidth(0, 70);   
        self.tabla.setColumnWidth(3, 150);
        
        stylesheet = "::section{Background-color:lightblue;border-radius:40px;}"
        self.tabla.verticalHeader().setStyleSheet(stylesheet)
       
        
        
        self.generarArboles()
        
        #self.membrete.setPixmap(QPixmap("fcyt.png"))
        self.inicializacion()
        
        self.vendedorCombo.setEnabled(False)
        self.clienteCombo.setEnabled(False)
        self.vendedorNumeroRadio.clicked.connect(self.activarVCombo)
        self.vendedorTodosRadio.clicked.connect(self.desactivarVCombo)
        self.clienteNumeroRadio.clicked.connect(self.activarCCombo)
        self.clienteTodosRadio.clicked.connect(self.desactivarCCombo)
        
        self.generarReportePush.clicked.connect(self.generarReporte)
        
        self.groupBox_7.setEnabled(False)
        self.groupBox_10.setEnabled(False)
        
        self.tabla.clicked.connect(self.altaBajaModif)
    
       
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
        
        
    def inordenNCV(self, arbol, lista, archivo):
        if(arbol != None):
            lista = self.inordenNCV(arbol.izq, lista, archivo)
            reg = leer(archivo, arbol.nrr)
            lista.append(reg)
            lista = self.inordenNCV(arbol.der, lista, archivo)
        return lista
        
        
    def postordenNCV(self, arbol, lista, archivo):
        if(arbol != None):
            lista = self.postordenNCV(arbol.der, lista, archivo)
            reg = leer(archivo, arbol.nrr)
            lista.append(reg)       
            lista = self.postordenNCV(arbol.izq, lista, archivo)
        return lista
        
       
    def listaSeleccionados(self):
        radioButtonsSaldo=[self.saldoTotalRadio,self.saldoPagoRadio,self.saldoImpagoRadio]
        radioButtonsVendedor=[self.vendedorTodosRadio,self.vendedorNumeroRadio]
        radioButtonsCliente=[self.clienteTodosRadio,self.clienteNumeroRadio]
        seleccionados=[]
        for i in radioButtonsSaldo:
            if (i.isChecked()):
                seleccionados.append('saldo'+i.text())
        for i in radioButtonsVendedor:
            if (i.isChecked()):
                seleccionado = i.text()
                if (seleccionado == 'Número'):
                    vendedor = self.vendedorCombo.currentText()
                    vendedorLista = vendedor.split() 
                    try:
                        seleccionados.append(vendedorLista[0])
                    except:
                        self.error()
                else:
                    seleccionados.append('vendedor'+i.text())
        for i in radioButtonsCliente:
            if i.isChecked():
                seleccionado =i.text()
                if (seleccionado == 'Número'):
                    cliente = self.clienteCombo.currentText()
                    clienteLista = cliente.split()
                    try:                    
                        seleccionados.append(clienteLista[0])
                    except:
                        self.error()
                else:
                    seleccionados.append('cliente'+i.text())
        return seleccionados


    def error(self):
        msg = QtGui.QMessageBox()
        msg.setWindowTitle("Error")
        msg.setWindowIcon(QtGui.QIcon('error_15261.ico'))
        msg.setIcon(QtGui.QMessageBox.Critical)
        msg.setText("Seleccione una persona")
        msg.exec()
        
        
    def cargarFila(self,seleccionados,fila,lista,i):
        archCliente = abrir('Cliente')
        
        if (seleccionados[1]=='vendedorTodos'):
            if (seleccionados[2]=='clienteTodos'):
                self.tabla.insertRow(fila)
                
                self.tabla.setItem(fila, 0, QTableWidgetItem(str(lista[i].ncv)))
                self.tabla.setItem(fila, 1, QTableWidgetItem(str(lista[i].idVendedor)))
                self.tabla.setItem(fila, 2, QTableWidgetItem(str(lista[i].idCliente)))
                self.tabla.setItem(fila, 5, QTableWidgetItem(str(lista[i].importe)))
                if (lista[i].pagado):
                    self.tabla.setItem(fila, 6, QTableWidgetItem('PAGADO'))
                    self.tabla.item(fila,6).setBackground(QColor("lightgreen"))
                else:
                    self.tabla.setItem(fila, 6, QTableWidgetItem('IMPAGO'))
                    self.tabla.item(fila,6).setBackground(QColor("red"))
                pos = busquedaCliente(self.arbolCliente,lista[i].idCliente)
                reg = leer(archCliente,pos)
                self.tabla.setItem(fila, 3, QTableWidgetItem(reg.nomCliente))
                if (reg.activo):
                    self.tabla.setItem(fila, 4, QTableWidgetItem('ACTIVO'))
                    self.tabla.item(fila,4).setBackground(QColor("lightgreen"))
                else:
                    self.tabla.setItem(fila, 4, QTableWidgetItem('BAJA'))
                    self.tabla.item(fila,4).setBackground(QColor("red")) 
            else:
                if (lista[i].idCliente==int(seleccionados[2])):
                    self.barrasCliente(lista[i].idCliente)
                    self.tabla.insertRow(fila)
                
                    self.tabla.setItem(fila, 0, QTableWidgetItem(str(lista[i].ncv)))
                    self.tabla.setItem(fila, 1, QTableWidgetItem(str(lista[i].idVendedor)))
                    self.tabla.setItem(fila, 2, QTableWidgetItem(str(lista[i].idCliente)))
                    self.tabla.setItem(fila, 5, QTableWidgetItem(str(lista[i].importe)))
                    if (lista[i].pagado):
                        self.tabla.setItem(fila, 6, QTableWidgetItem('PAGADO'))
                        self.tabla.item(fila,6).setBackground(QColor("lightgreen"))
                    else:
                        self.tabla.setItem(fila, 6, QTableWidgetItem('IMPAGO'))
                        self.tabla.item(fila,6).setBackground(QColor("red"))
                    pos = busquedaCliente(self.arbolCliente,lista[i].idCliente)
                    reg = leer(archCliente,pos)
                    self.tabla.setItem(fila, 3, QTableWidgetItem(reg.nomCliente))
                    if (reg.activo):
                        self.tabla.setItem(fila, 4, QTableWidgetItem('ACTIVO'))
                        self.tabla.item(fila,4).setBackground(QColor("lightgreen"))
                    else:
                        self.tabla.setItem(fila, 4, QTableWidgetItem('BAJA'))
                        self.tabla.item(fila,4).setBackground(QColor("red"))
                
        elif (lista[i].idVendedor==int(seleccionados[1])):
            self.barrasVendedor(lista[i].idVendedor)
            if (seleccionados[2]=='clienteTodos'):
                self.tabla.insertRow(fila)
                
                self.tabla.setItem(fila, 0, QTableWidgetItem(str(lista[i].ncv)))
                self.tabla.setItem(fila, 1, QTableWidgetItem(str(lista[i].idVendedor)))
                self.tabla.setItem(fila, 2, QTableWidgetItem(str(lista[i].idCliente)))
                self.tabla.setItem(fila, 5, QTableWidgetItem(str(lista[i].importe)))
                if (lista[i].pagado):
                    self.tabla.setItem(fila, 6, QTableWidgetItem('PAGADO'))
                    self.tabla.item(fila,6).setBackground(QColor("lightgreen"))
                else:
                    self.tabla.setItem(fila, 6, QTableWidgetItem('IMPAGO'))
                    self.tabla.item(fila,6).setBackground(QColor("red"))
                pos = busquedaCliente(self.arbolCliente,lista[i].idCliente)
                reg = leer(archCliente,pos)
                self.tabla.setItem(fila, 3, QTableWidgetItem(reg.nomCliente))
                if (reg.activo):
                    self.tabla.setItem(fila, 4, QTableWidgetItem('ACTIVO'))
                    self.tabla.item(fila,4).setBackground(QColor("lightgreen"))
                else:
                    self.tabla.setItem(fila, 4, QTableWidgetItem('BAJA'))
                    self.tabla.item(fila,4).setBackground(QColor("red"))
            else:
                if (lista[i].idCliente==int(seleccionados[2])):
                    self.barrasCliente(lista[i].idCliente)
                    self.tabla.insertRow(fila)
                
                    self.tabla.setItem(fila, 0, QTableWidgetItem(str(lista[i].ncv)))
                    self.tabla.setItem(fila, 1, QTableWidgetItem(str(lista[i].idVendedor)))
                    self.tabla.setItem(fila, 2, QTableWidgetItem(str(lista[i].idCliente)))
                    self.tabla.setItem(fila, 5, QTableWidgetItem(str(lista[i].importe)))
                    if (lista[i].pagado):
                        self.tabla.setItem(fila, 6, QTableWidgetItem('PAGADO'))
                        self.tabla.item(fila,6).setBackground(QColor("lightgreen"))
                    else:
                        self.tabla.setItem(fila, 6, QTableWidgetItem('IMPAGO'))
                        self.tabla.item(fila,6).setBackground(QColor("red"))
                    pos = busquedaCliente(self.arbolCliente,lista[i].idCliente)
                    reg = leer(archCliente,pos)
                    self.tabla.setItem(fila, 3, QTableWidgetItem(reg.nomCliente))
                    if (reg.activo):
                        self.tabla.setItem(fila, 4, QTableWidgetItem('ACTIVO'))
                        self.tabla.item(fila,4).setBackground(QColor("lightgreen"))
                    else:
                        self.tabla.setItem(fila, 4, QTableWidgetItem('BAJA'))
                        self.tabla.item(fila,4).setBackground(QColor("red"))
        cerrar(archCliente)                
            
    
    def generarReporte(self):        
        self.inicializarBarras()
        self.tabla.setColumnCount(0)  
        self.tabla.setColumnCount(7)        
        self.tabla.setHorizontalHeaderLabels(['NCV', 'Vendedor', 'IDCliente', 'Nombre', 'Activo', 'Importe','Pagado'])
        
        self.tabla.setColumnWidth(0, 70);   
        self.tabla.setColumnWidth(3, 150);
        
        #self.tabla.setSortingEnabled(False)
        
        self.tabla.setRowCount(0)
        lista = []
        
        archNCV = abrir('NCV')
        
        if self.inordenRadio.isChecked():       
            lista = self.inordenNCV(self.arbolNCV, lista, archNCV)           
        else: 
            lista = self.postordenNCV(self.arbolNCV, lista, archNCV)
        
        cerrar(archNCV)
        
        seleccionados=self.listaSeleccionados()
        #print(seleccionados)
                
        for i in range(len(lista)):
            fila=self.tabla.rowCount()
            #self.tabla.insertRow(fila)
            
            if (seleccionados[0]=='saldoTotal'):
                self.cargarFila(seleccionados,fila,lista,i)
                
            elif (seleccionados[0]=='saldoPago'):
                if (lista[i].pagado):
                    self.cargarFila(seleccionados,fila,lista,i) 
                    
            else: #saldoImpago
                if (lista[i].pagado==False):
                    self.cargarFila(seleccionados,fila,lista,i)
            
        #self.tabla.setSortingEnabled(True)

             
    def activarVCombo(self):
        self.vendedorCombo.setEnabled(True)
        
    def desactivarVCombo(self):
        self.vendedorCombo.setEnabled(False)
    
    def activarCCombo(self):
        self.clienteCombo.setEnabled(True)
        
    def desactivarCCombo(self):
        self.clienteCombo.setEnabled(False)    
    
    
    def generarArboles(self):   
                
        archNCV = abrir('NCV')
        archCliente = abrir('Cliente')
        
        self.arbolNCV = None
        self.arbolNCV = cargarArbolNCV(archNCV)
        self.arbolCliente = None
        self.arbolCliente = cargarArbolCliente(archCliente)
        
        cerrar(archNCV)
        cerrar(archCliente)
        
        
        #inorden(self.arbolCliente)
    def barras(self):
        self.eTotalBar.reset()
        self.ePagoBar.reset()
        self.eImpagoBar.reset()
        
        self.vTotalBar.reset()
        self.vPagoBar.reset()
        self.vImpagoBar.reset()
        
        self.cTotalBar.reset()
        self.cPagoBar.reset()
        self.cImpagoBar.reset()
        
        self.eTotalBar.setAlignment(QtCore.Qt.AlignCenter)
        self.ePagoBar.setAlignment(QtCore.Qt.AlignCenter)
        self.eImpagoBar.setAlignment(QtCore.Qt.AlignCenter)
        
        self.vTotalBar.setAlignment(QtCore.Qt.AlignCenter)
        self.vPagoBar.setAlignment(QtCore.Qt.AlignCenter)
        self.vImpagoBar.setAlignment(QtCore.Qt.AlignCenter)
        
        self.cTotalBar.setAlignment(QtCore.Qt.AlignCenter)
        self.cPagoBar.setAlignment(QtCore.Qt.AlignCenter)
        self.cImpagoBar.setAlignment(QtCore.Qt.AlignCenter)
        
        
    def barrasVendedor(self,idVendedor):
        archNCV = abrir('NCV')
        archCliente = abrir('Cliente')
        
        self.groupBox_7.setEnabled(True)
        total = 0
        pago = 0
        impago = 0
        for i in range (len(archNCV)):
            reg = leer(archNCV,i)
            if (reg.idVendedor==idVendedor):
                total +=reg.importe
                if (reg.pagado):
                    pago+=reg.importe
                else:
                    impago+=reg.importe
        self.vendedorTotalPrecio.setText('TOTAL $ '+str(total))
        self.vendedorPagoPrecio.setText('PAGO $ '+str(pago))
        self.vendedorImpagoPrecio.setText('IMPAGO $ '+str(impago))
        
        self.vTotalBar.setValue(100)
        self.vPagoBar.setValue(101*pago/total)
        self.vImpagoBar.setValue(101*impago/total)
        
        cerrar(archNCV)
        cerrar(archCliente)
        
        
    def barrasCliente(self,idCliente):
        archNCV = abrir('NCV')
        
        self.groupBox_10.setEnabled(True)
        total = 0
        pago = 0
        impago = 0
        for i in range (len(archNCV)):
            reg = leer(archNCV,i)
            if (reg.idCliente==idCliente):
                total +=reg.importe
                if (reg.pagado):
                    pago+=reg.importe
                else:
                    impago+=reg.importe
        self.clienteTotalPrecio.setText('TOTAL $ '+str(total))
        self.clientePagoPrecio.setText('PAGO $ '+str(pago))
        self.clienteImpagoPrecio.setText('IMPAGO $ '+str(impago))
        
        self.cTotalBar.setValue(100)
        self.cPagoBar.setValue(101*pago/total)
        self.cImpagoBar.setValue(101*impago/total)
        
        cerrar(archNCV)
        
    
    def inicializarBarras(self):
        self.groupBox_7.setEnabled(False)
        self.groupBox_10.setEnabled(False)        
        
        self.vTotalBar.reset()
        self.vPagoBar.reset()
        self.vImpagoBar.reset()
        
        self.cTotalBar.reset()
        self.cPagoBar.reset()
        self.cImpagoBar.reset()
        
        self.vendedorTotalPrecio.setText('')
        self.vendedorPagoPrecio.setText('')
        self.vendedorImpagoPrecio.setText('')
         
        self.clienteTotalPrecio.setText('')
        self.clientePagoPrecio.setText('')
        self.clienteImpagoPrecio.setText('')
        
                   
    def inicializacion(self):
        archNCV = abrir('NCV')
        archCliente = abrir('Cliente')
        
        total = 0
        pago = 0
        impago = 0
        for i in range (len(archNCV)):
            reg = leer(archNCV,i)
            total +=reg.importe
            if (reg.pagado):
                pago+=reg.importe
            else:
                impago+=reg.importe
        self.empresaTotalPrecio.setText('TOTAL $ '+str(total))
        self.empresaPagoPrecio.setText('PAGO $ '+str(pago))
        self.empresaImpagoPrecio.setText('IMPAGO $ '+str(impago))
        
        self.eTotalBar.setValue(100)
        self.ePagoBar.setValue(101*pago/total)
        self.eImpagoBar.setValue(101*impago/total)
        
        for j in range (len(archCliente)):
            reg = leer(archCliente,j)
            self.clienteCombo.addItem(str(reg.idCliente)+' '+reg.nomCliente)
        
        cerrar(archNCV)
        cerrar(archCliente)
        
            
    def altaBajaModif(self):
        #print('entro')   
        #print(self.tabla.currentRow())
        #print(self.tabla.item(self.tabla.currentRow(), 2).text())
        idSeleccionado = self.tabla.item(self.tabla.currentRow(), 2).text()
        j = self.tabla.currentRow()
        self.tabla.clearSelection()
        for i in range (0,7):
            self.tabla.item(j,i).setBackground(QColor("cyan"))
        idCliente=abrir('id')
        guardarid(idCliente,int(idSeleccionado))
               
        dial = AltaBajaModif()       
        dial.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dial.setModal(True)   
        dial.exec_()
        
        self.generarArboles()
        #print(leer(archNCV,len(archNCV)-1).ncv)
        self.clienteCombo.clear()
        
        archCliente = abrir('Cliente')

        for j in range (len(archCliente)):
            reg = leer(archCliente,j)
            self.clienteCombo.addItem(str(reg.idCliente)+' '+reg.nomCliente)
        
        cerrar(archCliente)
        
        self.inicializacion()
        self.generarReporte()

        

app = QtGui.QApplication(sys.argv)
principal = Ventana()
principal.show()
app.exec_()