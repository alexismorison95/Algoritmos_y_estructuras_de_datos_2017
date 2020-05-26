# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:14:15 2017

@author: Alexis
"""

import shelve
import random


class regNCV():
    ncv, idVendedor, idCliente, importe, pagado = 0,0,0,0,False

class regCliente():
    idCliente, nomCliente, activo, idVendedor = 0, '', None, 0
       

def abrir(ruta):
    return shelve.open(ruta)
    
def cerrar(archivo):
    archivo.close()
    
def guardar(archivo, reg):
    archivo[str(len(archivo))] = reg

def guardarid(archivo, reg):
    archivo['0'] = reg
    
def leer(archivo, pos):
    try:
        return archivo[str(pos)]
    except:
        return None

def modificar(archivo, pos, reg):
    archivo[str(pos)] = reg

"""
def cargarArchivoRandom(f):
    for i in range(0,10):
        r=regNCV()
        #r.ncv=10000+len(f)
        r.ncv=len(f)+1
        for j in range(0,20):
            r.cliente += chr(random.randint(65,90))
        r.importe=random.random()*10000
        r.pagado= True if random.randint(0,1)==1 else False
        r.vendedor=random.randint(1,5)
        r.activo=True
        guardar(f,r)      
    cerrar(f)"""
    



def crearDatNCV(archivo):
    archNCV = open('NCV1.txt')
    contenido = archNCV.readlines()   #vector con contenido     

    for i in range(len(contenido)):
        reg = regNCV()
        datos = contenido[i].split(';')
        reg.ncv = int(datos[0])
        reg.idVendedor = int(datos[1])
        reg.idCliente = int(datos[2])
        reg.importe = float(datos[3])
        if (datos[4]=='True\n'):
            reg.pagado = True
        else:
            reg.pagado = False
          
        print(str(reg.ncv)+'  '+str(reg.idVendedor)+'   '+str(reg.pagado))        
        guardar(archivo,reg)
    cerrar(archivo)   
        
def crearDatCliente(archivo):
    archCliente = open('Cliente1.txt')
    contenido = archCliente.readlines()   #vector con contenido    
    
    for i in range(len(contenido)):
        reg = regCliente()
        datos = contenido[i].split(';')
        reg.idCliente = int(datos[0])
        reg.nomCliente = datos[1]
        if (datos[2]=='True'):        
            reg.activo = True
        else:
            reg.activo = False
        reg.idVendedor = int(datos[3])
        print(str(reg.idCliente)+'  '+str(reg.idVendedor)+'   '+str(reg.activo))
        guardar(archivo,reg)        
    cerrar(archivo)
    
        
    

#cargarArchivoRandom(arch)    

        
        
        
        
        
    
    
    