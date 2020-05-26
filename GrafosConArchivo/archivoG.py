# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 20:52:17 2017

@author: Alexis
"""

import shelve

def abrir(ruta):
    return shelve.open(ruta)
    
def cerrar(archivo):
    archivo.close()

def guardar(archivo,regG):
    archivo[str(len(archivo))]=regG

def modificar(archivo,regG,pos):
    try:
        archivo[str(pos)]=regG
        return True
    except:
        return False

def leer(archivo,nrr):
    try:
        return archivo[str(nrr)]
    except:
        return None








