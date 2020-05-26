# -*- coding: utf-8 -*-
class T_Dato():
    id,tiempoverde,color = None,None,"rojo"

class NodoCola():
    info, sig = T_Dato, None

class cola():
    def __init__ (self):
        self.frente = None
        self.final = None
        self.tam = 0

def crearcola (q):
    q.frente = None
    q.final = None
    q.tam = 0

def insertarencola(q, x): 
    aux = NodoCola()
    aux.info = x
    aux.sig = None
    if q.frente == None:
        q.frente = aux
    else:
        q.final.sig = aux
    q.final = aux
    q.tam += 1
    
def eliminarDeCola(q):
    x=q.frente.info
    q.frente=q.frente.sig
    if (q.frente ==None):
        q.final=None
    q.tam-=1 #descremento el tamanio
    return x

   
def colavacia(q):
    return (q.frente == None)

def colallena(pila):
    return (False)
    
def tamanioCola(q):
    return q.tam
    
def insertarPrioridad(q,x):
    aux=NodoCola()
    aux.info=x
    aux.sig=q.frente
    q.frente=aux
    q.tam+=1