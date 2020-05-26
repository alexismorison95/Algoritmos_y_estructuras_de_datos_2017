# -*- coding: utf-8 -*-

from archivos import leer,abrir, cerrar

class nodoArbolNCV():
    def __init__(self, info=None, nrr=None, izq=None, der=None): #agregar altura
        self.info=info
        self.nrr=nrr        
        self.izq=izq
        self.der=der
        self.altura=0

class nodoArbolCliente():
    def __init__(self, info=None, idVendedor=None, nrr=None, izq=None, der=None): #agregar altura
        self.info=info
        self.idVendedor=idVendedor
        self.nrr=nrr        
        self.izq=izq
        self.der=der
        self.altura=0
        

def altura(raiz): 
	if(raiz):
		return raiz.altura
	else:
		return -1

def actualizarAltura(raiz):
	if (not raiz): return
	raiz.altura = max(altura(raiz.izq), altura(raiz.der)) +1

def rotarS(raiz, a_izq):  
	#Rotar simple
	n2 = None
	if (a_izq):#rotacion izquierda
		n2 = raiz.izq
		raiz.izq = n2.der
		n2.der = raiz
	else:#rotacion derecha
		n2 = raiz.der
		raiz.der = n2.izq
		n2.izq = raiz
	actualizarAltura(raiz)
	actualizarAltura(n2)
	return n2 #no hay pasaje por referencia en python (de manera limpia)

def rotarD(raiz, a_izq): #rotar doble
	if(a_izq):
		raiz.izq = rotarS(raiz.izq, False)
		raiz = rotarS(raiz, True)
	else:
		raiz.der = rotarS(raiz.der, True)
		raiz = rotarS(raiz, False)
	#/* la actualización de las alturas se realiza en las rotaciones simples */
	return raiz
	
def balancear(raiz):
	if (not raiz): return
	if altura(raiz.izq) - altura(raiz.der) == 2:#podria almacenar el resultado de la diferencia pero asi se entiende mas
		#desequilibrio hacia la izquierda
		if altura(raiz.izq.izq) >= altura(raiz.izq.der):
			#desequilibrio simple a la izq
			raiz = rotarS(raiz, True)
		else:
			#desequilibrio doble a la izquierda
			raiz = rotarD(raiz, True)
	elif altura(raiz.der) - altura(raiz.izq) == 2:
		#desequilibrio hacia la derecha
		if altura(raiz.der.der) >= altura(raiz.der.izq): 
			#desequilibrio simple hacia la derecha
			raiz = rotarS(raiz, False)
		else:
			#desequilibrio doble hacia la derecha
			raiz = rotarD(raiz, False)
	return raiz

#este insertar esta mejor y mas simple
def insertarNCV(nodo, dato, pos):  
	if (not nodo):
         nodo = nodoArbolNCV(dato,pos,None,None)
	else:
		#la magia de la recursividad hace todo aca
		if (dato < nodo.info):
			nodo.izq = insertarNCV(nodo.izq, dato,pos)
		else:
			nodo.der = insertarNCV(nodo.der, dato,pos)
		nodo = balancear(nodo)
		actualizarAltura(nodo)
	return nodo


def insertarCliente(nodo, idCliente, idVendedor, pos):  
	if (not nodo):
         nodo = nodoArbolCliente(idCliente, idVendedor ,pos,None,None)
	else:
		#la magia de la recursividad hace todo aca
		if (idCliente < nodo.info):
			nodo.izq = insertarCliente(nodo.izq, idCliente, idVendedor, pos)
		else:
			nodo.der = insertarCliente(nodo.der, idCliente, idVendedor, pos)
		nodo = balancear(nodo)
		actualizarAltura(nodo)
	return nodo

def arbolvacio(raiz):
    return raiz.info == None


def remplazar(raiz):
    aux = None
    if raiz.der==None:
        aux = raiz
        raiz = None
    else:
        raiz.der, aux = remplazar(raiz.der)
    return raiz, aux
    
    
def eliminar_nodo(raiz, clave):
    x = None
    if raiz!=None:
        if clave<raiz.info:
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif clave>raiz.info:
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info            
            if raiz.izq == None:
                raiz = raiz.der
            elif raiz.der == None:
                raiz = raiz.izq
            else:
                raiz.izq, aux = remplazar(raiz.izq)
                raiz.info, raiz.nrr = aux.info, aux.nrr
    return raiz, x
    

def busquedaCliente(raiz, clave):
    pos = None
    if raiz!=None:
        if raiz.info == clave:
            pos = raiz.nrr
        elif clave < raiz.info:
            pos = busquedaCliente(raiz.izq, clave)
        else:
            pos = busquedaCliente(raiz.der, clave)
    return pos
    

def busquedaNCV(raiz, clave):
    pos = None
    if raiz!=None:
        if raiz.nrr == clave:
            pos = raiz.nrr
        elif clave < raiz.info:
            pos = busquedaNCV(raiz.izq, clave)
        else:
            pos = busquedaNCV(raiz.der, clave)
    return pos
    
        
def inorden(raiz):
    if raiz!=None:
        inorden(raiz.izq)
        print (str(raiz.nrr)+" "+str(raiz.info))
        inorden(raiz.der)
                
def preorden(raiz):
    if raiz!=None:
        print (raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)

def postorden(raiz):
    if raiz!=None:
        postorden(raiz.der)
        print (raiz.info)        
        postorden(raiz.izq)


def cargarArbolNCV(file):
    raiz = None
    for i in range(0,len(file)):
        r = leer(file,i)
        raiz = insertarNCV(raiz, r.ncv, i) 
  
    return raiz

def cargarArbolCliente(file):
    raiz = None
    for i in range(0,len(file)):
        r = leer(file,i)
        raiz = insertarCliente(raiz, r.idCliente, r.idVendedor, i)
    return raiz


space = 5
v_space = 1
def mostrar(nodo, lvl=0): #este mostrar muestra el arbol de costado
	if (not nodo):
		print ("")
		return
	
	nlvl = lvl+ 1
	mostrar(nodo.der, nlvl)
	print((" "*space*lvl) + str(nodo.info))

	mostrar(nodo.izq, nlvl)
 
#PRINCIPAL
 
"""raiz = None
for i in range(1,16):
    raiz = insertar(raiz, i, i)

#raiz, x = eliminar_nodo(raiz, 8)

print("listado pre orden")
preorden(raiz)
print("")

print("in orden")
inorden(raiz)
print("")

print("post orden")
postorden(raiz)
print("")

mostrar(raiz)"""


"""arch = abrir("prueba")

raizNCV = cargarArbolNCV(arch)

raizCliente = cargarArbolCliente(arch)


print("in orden")
inorden(raizCliente)
print("")

mostrar(raizCliente)

pos = busquedaNCV(raizNCV, 2)
r = leer(arch,pos.nrr)
print(r.cliente)"""
