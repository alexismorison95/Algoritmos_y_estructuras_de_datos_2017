# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 17:04:20 2017

@author: Mona Thinkpad
"""


import TDAColaDinamica



def listaSemaforos():
    lista=[]
    for i in range(0,4):
        x=TDAColaDinamica.T_Dato()
        x.id=i+1
        if (i%2==0):
            x.tiempoverde=6 #6segundos a pares
        else:
            x.tiempoverde=8
        lista.append(x)
    return lista
    
def encolarLista(lista):
    cola = TDAColaDinamica.cola()
    for i in range(0,len(lista)):
        TDAColaDinamica.insertarencola(cola,lista[i])
    return cola


