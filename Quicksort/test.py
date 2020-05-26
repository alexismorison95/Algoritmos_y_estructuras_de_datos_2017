from Archivo import abrir, cerrar, guardar, leer
from PD import PilaD, apilar, desapilar, pilavacia
#from principal import Ventana


def LevantarArchivo():
    archivo = open('apeynom.txt')
    #arch = abrir("pruebaordenar")
    linea = archivo.readline()
    lista = []
        
    while linea:
        lista.append(linea)
        linea = archivo.readline()
    #cerrar(arch)
    return lista
 
def CargarEnLista(arch,barra):
    #arch = abrir("pruebaordenar")
    lista = []
    for i in range(0,len(arch)):
        barra.setValue(i*101//len(arch))
        regi = leer(arch,i)
        lista.append(regi.apeynom)
    #cerrar(arch)
    return lista    


def ListarLista(lista):
    print("LISTA")
    for i in range(0, len(lista)):
        print(lista[i])
        
       
def ListaDesordenada():
    arch = abrir("pruebaordenar")
    
    print("LISTA DESORDENADA")
    for i in range (0,len(arch)):
        print(leer(arch,i).apeynom)
    cerrar(arch)    
        
def QuickSortIterativoAZ(lista,barra):
    posini = 0
    posfin = len(lista)-1    
    pila = PilaD()
    apilar(pila,[posini,posfin])
    v = 1
    while(not pilavacia(pila)):        
        x = desapilar(pila)
        posini, posfin = x[0], x[1]
        pivot = posfin
        i = posini 
        j = posfin - 1
        while (i <= j) : 
            while (lista[i] < lista[pivot]):
                i+= 1
            while lista[j] > lista[pivot]:
                j-= 1
            if (i <= j):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux             
                i+= 1
                j-= 1        
        aux = lista[i]
        lista[i] = lista[posfin]
        lista[posfin] = aux
        
        if (i < posfin):
            apilar(pila,[(i),posfin])
        if (j > posini):    
            apilar(pila,[posini,(j)])
        barra.setValue(v*101//len(lista))
        v+=1
    return lista            

def QuickSortIterativoZA(lista,barra):
    #lista = lista1
    posini = 0
    posfin = len(lista)-1    
    pila = PilaD()
    apilar(pila,[posini,posfin])
    v = 1
    while(not pilavacia(pila)):
        x = desapilar(pila)
        posini, posfin = x[0], x[1]
        pivot= posfin 
        i= posini 
        j= posfin - 1
        while (i <= j) : 
            while (lista[i] > lista[pivot]):
                i+= 1
            while lista[j] < lista[pivot]:
                j-= 1
            if (i <= j):
                aux= lista[i]
                lista[i]= lista[j]
                lista[j]= aux               
                i+= 1
                j-= 1
        aux=lista[i]
        lista[i]=lista[posfin]
        lista[posfin]=aux
        if (i<posfin):
            apilar(pila,[(i),posfin])
        if (j>posini):    
            apilar(pila,[posini,(j)])
        barra.setValue(v*101//len(lista))
        v+=1
    return lista

def quicksortRecursivoAZ(L,first,last):
    # definimos los índices y calculamos el pivote
    i = first
    j = last  
    #pivote = (L[i] + L[j]) / 2
    pivote = L[i]
    # iteramos hasta que i no sea menor que j
    while(i < j):
        # iteramos mientras que el valor de L[i] sea menor que pivote
        while(L[i] < pivote):
            # Incrementamos el índice
            i+=1
        # iteramos mientras que el valor de L[j] sea mayor que pivote
        while(L[j] > pivote):
            # decrementamos el índice
            j-=1
        # si i es menor o igual que j significa que los índices se han cruzado
        if(i <= j):
            # creamos una variable temporal para guardar el valor de L[j]
            x = L[j]
            # intercambiamos los valores de L[j] y L[i]
            L[j] = L[i]
            L[i] = x
            # incrementamos y decrementamos i y j respectivamente
            i+=1
            j-=1

    # si first es menor que j mantenemos la recursividad
    if(first < j):
        L = quicksortRecursivoAZ(L, first, j)
    # si last es mayor que i mantenemos la recursividad
    if(last > i):
        L = quicksortRecursivoAZ(L, i, last)

    # devolvemos la lista ordenada
    return L   
    
def quicksortRecursivoZA(L,first,last):
    # definimos los índices y calculamos el pivote
    i = first
    j = last  
    #pivote = (L[i] + L[j]) / 2
    pivote = L[i]
    # iteramos hasta que i no sea menor que j
    while(i < j):
        # iteramos mientras que el valor de L[i] sea menor que pivote
        while(L[i] > pivote):
            # Incrementamos el índice
            i+=1
        # iteramos mientras que el valor de L[j] sea mayor que pivote
        while(L[j] < pivote):
            # decrementamos el índice
            j-=1
        # si i es menor o igual que j significa que los índices se han cruzado
        if(i <= j):
            # creamos una variable temporal para guardar el valor de L[j]
            x = L[j]
            # intercambiamos los valores de L[j] y L[i]
            L[j] = L[i]
            L[i] = x
            # incrementamos y decrementamos i y j respectivamente
            i+=1
            j-=1

    # si first es menor que j mantenemos la recursividad
    if(first < j):
        L = quicksortRecursivoZA(L, first, j)
    # si last es mayor que i mantenemos la recursividad
    if(last > i):
        L = quicksortRecursivoZA(L, i, last)

    # devolvemos la lista ordenada
    return L  
    
    
def bbrecursivaAZ(vector,buscado,pri,ult):
    if pri>ult:
        return -1
    else:
        med=(pri+ult)//2
        if vector[med]==buscado:
            return med
                
        elif vector[med]<buscado:
            return bbrecursivaAZ(vector,buscado,med+1,ult)
        else:
            return bbrecursivaAZ(vector,buscado,pri,med-1)    
      
          
def bbrecursivaZA(vector,buscado,pri,ult):
    if pri>ult:
        return -1
    else:
        med=(pri+ult)//2
        if vector[med]==buscado:
            return med
                
        elif vector[med]<buscado:
            return bbrecursivaZA(vector,buscado,pri,med-1)
        else:
            return bbrecursivaZA(vector,buscado,med+1,ult)  

def busquedabinaria(listavector,buscado,limite):
    pos=-1
    pri=0
    ult=limite
    while (pos==-1) or (pri<=ult):
        med =(pri+ult)//2
        if listavector[med]==buscado:
            pos=med
        elif listavector[med]>buscado:
            ult=med-1
        else:
            pri=med+1
    return pos          


def bbrecursivaTabla(tabla,buscado,pri,ult):
    if pri>ult:
        return -1
    else:
        med=(pri+ult)//2
        if tabla.item(0,med).text()==buscado:
            return med
                
        elif tabla.item(0,med).text()<buscado:
            return bbrecursivaTabla(tabla,buscado,med+1,ult)
        else:
            return bbrecursivaTabla(tabla,buscado,pri,med-1) 
            

 
#LevantarArchivo()
#ListaDesordenada()
"""lista = CargarEnLista()
QuickSortIterativoAZ(lista)
print("ordenada")
ListarLista(lista)"""

