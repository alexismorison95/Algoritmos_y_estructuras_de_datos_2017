# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:42:12 2017

@author: Mona Thinkpad
"""

from archivoG import guardar,leer
from PD import PilaD, apilar, desapilar, pilaVacia, crearpilaD

class regVertice():
    ciudad,gps,idCiudad = None,None,0    


class regArista():
    idViaje,CO,CD,importe,empresa,distancia = 0,None,None,0,None,None  
    
class regCamino():
    camino, importe, distancia = None, None, None
    
   
class nodoVertice():
    sig,cab,info,nrr = None,None,regVertice(),0
    
    def cargarNodoVertice(self): #devuelve nodo cargado
        #self.info.idCiudad = int(input("Ingrese ID de ciudad: "))
        self.info.ciudad = input("Ingrese nombre de Ciudad: ")
        self.info.gps = input("Ingrese coordenadas GPS: ")
    
    
    def buscarArista(self,buscado): #por ciudad de destino
        pos = None
        act = self.cab
        while ((act != None) and (act.info.CD != buscado)):
            act = act.sig
        if (act != None):
            pos = act
        return pos 
  

class nodoArista():
    sig,info,nrr = None,regArista(),0   

    def cargarNodoArista(self): #devuelve nodo cargado
        self.info.idViaje = int(input("Ingrese ID de viaje: "))
        self.info.empresa = input("Ingrese Empresa: ")
        self.info.CO = input("Ingrese Ciudad Origen: ")
        self.info.CD = input("Ingrese Ciudad Destino: ")
        self.info.importe = float(input("Ingrese Importe: "))
        self.info.distancia = float(input("Ingrese Distancia: "))      

  
class grafo():
    def __init__(self):
        self.cab = None
        self.tam = 0
    
    
    def buscarVertice(self,buscado): #por ciudad
        pos = None
        act = self.cab
        while ((act != None) and (act.info.ciudad != buscado)):
            act = act.sig
        if (act != None):
            pos = act
        return pos 
    
    
    def buscarArista(self,buscado): #por ciudad de destino
        pos = None
        act = self.cab
        while ((act != None) and (act.info.CD != buscado)):
            act = act.sig
        if (act != None):
            pos = act
        return pos 
    
    
    def insertarVertice(self,nodo): #por ciudad
        if((self.cab == None) or (nodo.info.ciudad < self.cab.info.ciudad)):
            nodo.sig = self.cab
            self.cab = nodo
        else:
            ant = self.cab
            act = self.cab.sig
            while ((act != None) and (act.info.ciudad < nodo.info.ciudad)):
                ant = ant.sig
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        self.tam += 1
    
    
    def insertarArista(self,nodo): #por ciudad de destino, puede haber cd repetidas 
        v = self.buscarVertice(nodo.info.CO)
        if(v != None):
            if(self.buscarVertice(nodo.info.CD) != None):
                if((v.cab == None) or (nodo.info.CD < v.cab.info.CD)):
                    nodo.sig = v.cab
                    v.cab = nodo
                else:
                    ant = v.cab
                    act = v.cab.sig
                    while((act != None) and (act.info.CD < nodo.info.CD)):
                        ant = ant.sig
                        act = act.sig
                    nodo.sig = act
                    ant.sig = nodo
                    
        
    def listarGrafo(self):
        if(self.cab == None):
            print("No hay nada cargado")
        else:
            act = self.cab
            while(act != None):
                print("")
                print("Ciudad: "+act.info.ciudad)
                act2 = act.cab
                string = "Se conecta con: "
                string2 = "Precio: "
                string3 = "Distancia: "
                while(act2 != None):         
                    string+= act2.info.CD+", "  
                    string2+= str(act2.info.importe)+", " 
                    string3+= str(act2.info.distancia)+", " 
                    act2 = act2.sig
                print(string)
                print(string2)
                print(string3)
                print("--------------------------------")
                act = act.sig
    
    
    #cargo los vertices desde el archivo        
    def iniVertices(self,file):     
        for i in range(0,len(file)):
            regv = leer(file,i)
            nodo = nodoVertice()
            nodo.info = regv
            nodo.nrr = i
            self.insertarVertice(nodo)      
            
    
    #cargo las aristas desde el archivo
    def iniAristas(self,file):     
        for i in range(0,len(file)):
            rega = leer(file,i)
            nodo = nodoArista()
            nodo.info = rega
            nodo.nrr = i
            self.insertarArista(nodo)       
    
    
    #cargo una ciudad y guardo en arch
    def cargarCiudad(self,fileVertices):        
        nodo = nodoVertice()
        nodo.cargarNodoVertice()
        nodo.info.idCiudad = self.tam+1
        nodo.nrr = len(fileVertices)
        self.insertarVertice(nodo)
        guardar(fileVertices,nodo.info)
    
    def cargarCiudadQT(self,fileVertices,ciudad):
        try:
            nodo = nodoVertice()
            nodo.info.ciudad = ciudad
            nodo.info.idCiudad = self.tam+1
            #nodo.nrr = len(fileVertices)
            self.insertarVertice(nodo)
            guardar(fileVertices,nodo.info)
            return True
        except:
            return False
        
        
    #cargo un viaje y lo guardo en arch     
    def cargarViaje(self,fileAristas):        
        nodo = nodoArista()
        nodo.cargarNodoArista()
        nodo.nrr = len(fileAristas)
        self.insertarArista(nodo)
        guardar(fileAristas,nodo.info)  
    
    
    #buscador que puede servir
    def buscador(self,buscado):
        aux = self.cab
        pos = []
        while(aux != None):
            if(buscado in aux.info.ciudad):
                pos.append(aux.info.ciudad)
            aux = aux.sig
        return pos
     
     
    #origen y destino son strings    
    """def caminoDirecto(self,importe, origen, destino):        
        pos = self.buscarVertice(origen)
        arista = None
        if(pos != None):
            print('existe la ciudad: ',origen)
            arista = pos.cab
            while((arista != None) and (arista.info.CD != destino)):
                arista = arista.sig 
        return arista 
        
    
    #recorrido es el vector con las ciudades
    #distancia ?
    #origen es un string
    #destino es un string
    def caminos(self,recorrido,importe,origen,destino):
        paso = self.caminoDirecto(importe,origen, destino) 
        #print(actual.clave)
        #print(recorrido)
        if(paso != None):
                recorrido.append(origen)
                recorrido.append(destino)
                #print(recorrido)
                return (recorrido, importe + paso.info.importe)
        else:
            if(self.buscarVertice(origen) != None):
                arista = self.buscarVertice(origen).cab
                while(arista != None):
                    self.caminos(recorrido,importe,arista.info.CD,destino)
                    arista = arista.sig
    
    
    #origen y destino son strings
    def dijkstra(self, origen , destino):
        vert = self.buscarVertice(origen)
        if((vert != None) and (self.buscarVertice(destino) != None)): 
            listaCaminos = []
            importe = 0
            paso = self.caminoDirecto(importe,vert.info.ciudad, destino) 
            if(paso != None):
                listaCaminos.append(([vert.info.ciudad,destino],paso.info.importe))
            else:
                arista = vert.cab
                while(arista != None):
                    listaCaminos.append(self.caminos([origen],arista.info.importe,arista.info.CD,destino))
                    arista = arista.sig
        return listaCaminos"""

    
    
    def CaminosFinales (self, origen, destino):
        
        caminosHechos=[]     
        camHechosimporte=[]
        camHechosdistancia=[]
        caminoCtrl = None   #string con barritas
        
        caminoAux, caminoMax, caminoDirecto, importeDirecto, importeAux, importeMax = origen, origen, origen, 0, 0, 0  
        distanciaDirecto, distanciaAux, distanciaMax = 0, 0, 0
        cabecvertice = self.cab  #cabecera de vertice                
        while(cabecvertice != None):
            
            verticeInicial = cabecvertice.info.ciudad #verticeinicial con string con ciudad
            cabecarista = cabecvertice.cab       #cabecera arista  
            
            while (cabecarista != None):
                verticefinal = cabecarista.info.CD #vertice final string con CD
                                
                if((origen==verticeInicial) and (destino==verticefinal)):
                    caminoDirecto = origen +'|'+verticefinal
                    importeDirecto = int(cabecarista.info.importe)
                    distanciaDirecto = int(cabecarista.info.distancia)
                   # if(importeMax < importeDirecto): and (distanciaMax < distanciaDirecto)):                                          
                    caminoMax = caminoDirecto
                    importeMax = importeDirecto
                    distanciaMax = distanciaDirecto
                    if(caminoDirecto not in caminosHechos):                        
                        caminosHechos.append(caminoDirecto)
                        camHechosimporte.append(importeDirecto)
                        camHechosdistancia.append(distanciaDirecto)
    
                        
                elif (origen==verticeInicial) and (destino!= verticefinal):
                    #limpio las variables auxiliares                    
                    caminoAux= origen
                    importeAux= 0 
                    distanciaAux= 0
                    #
                    caminoAux += '|'+verticefinal
                    importeAux += int(cabecarista.info.importe) 
                    distanciaAux += int(cabecarista.info.distancia)
                    con =0
                    caminoCtrl, importeCtrl, distanciaCtrl = self.caminosParciales(con,verticefinal, destino,caminosHechos,camHechosimporte,camHechosdistancia,caminoCtrl,caminoAux, caminoMax, importeAux, importeMax, distanciaAux, distanciaMax)
                        
                cabecarista = cabecarista.sig
            cabecvertice = cabecvertice.sig     

        return caminosHechos, camHechosimporte, camHechosdistancia
        
    
    def caminosParciales (self, con,origen, destino,caminosHechos,camHechosimporte,camHechosdistancia,caminoCtrl,caminoAux, caminoMax, importeAux, importeMax, distanciaAux, distanciaMax):
        if(con<10):        
            import copy        
            caminoparcial = copy.copy(caminoAux) #string
            importeparcial = importeAux
            distanciaparcial = distanciaAux
            cabecvertice = self.cab
            while(cabecvertice != None):
                verticeinicial = cabecvertice.info.ciudad
                cabecarista = cabecvertice.cab          
                
                while(cabecarista != None):
                    verticefinal = cabecarista.info.CD
                    if((origen==verticeinicial) and (destino==verticefinal)): #camino directo
                        caminoCtrl = caminoAux +'|'+verticefinal
                        importeAux += int(cabecarista.info.importe)
                        distanciaAux += int(cabecarista.info.distancia)
                            
                       # if(importeMax < importeAux): and (distanciaMax < distanciaAux)):
                        caminoMax = caminoCtrl
                        importeMax = importeAux
                        distanciaMax = distanciaAux
                        if(caminoCtrl not in caminosHechos):
                            caminosHechos.append(caminoCtrl)
                            camHechosimporte.append(importeAux) 
                            camHechosdistancia.append(distanciaAux)
                                
                            
                    elif((origen == verticeinicial) and (destino != verticefinal)): #si no es directo
                        caminoAux += '|'+verticefinal
                        importeAux += int(cabecarista.info.importe)  
                        distanciaAux += int(cabecarista.info.distancia)
                        con+=1
                        caminoCtrl, importeCtrol, distanciaCtrl = self.caminosParciales(con,verticefinal, destino,caminosHechos,camHechosimporte,camHechosdistancia,caminoCtrl,caminoAux, caminoMax, importeAux, importeMax, distanciaAux, distanciaMax)
                            
                        
                    caminoAux = copy.copy(caminoparcial)
                    importeAux = importeparcial
                    distanciaAux = distanciaparcial
                    cabecarista = cabecarista.sig
                    
                cabecvertice = cabecvertice.sig
            
        return caminoMax, importeMax, distanciaMax 
    
    
    def soluciones(self,origen,destino):
        pos = self.buscarVertice(origen) #busca vertice origen
        sol = []                         #lista de soluciones
        solucion = [origen]              #camino de origen a destino | agrega origen
        pre = []
        dist = []
        precio = []
        precio.append(0)
        distancia = []
        distancia.append(0)



        if((pos != None) and (self.buscarVertice(destino) != None)):#existe origen y destino
            visitados = [origen]         #vertices tratados
            pila = PilaD()               #pila para vertices pendientes
            crearpilaD(pila)
            apilar(pila,pos.cab)         #apila 1er arista de sublista origen              
            
            while(not pilaVacia(pila)):  #mientras queden vertices por tratar
                pos = desapilar(pila)    #desapila vertice a tratar              
                
                while((pos != None) and (pos.info.CD in visitados)):
                    pos = pos.sig
                     
                if(pos!=None):
                    if (pos.info.CD not in visitados) and (pos.info.CD!=destino):                
                        visitados.append(pos.info.CD) #agregar nombre CD a tratados

                    if(pos.info.CD==destino): #si la arista es el verice destino
                        solucion.append(pos.info.CD) #agrega CD destino a solucion
                        precio.append(pos.info.importe)  #precio
                        distancia.append(pos.info.distancia) #distancia
                        
                        sol.append("")
                        pre.append(0)
                        dist.append(0)
                        
                        for i in range(0,len(solucion)):
                            sol[len(sol)-1] += "|"+str(solucion[i])    #agrega camino a sol                    
                            pre[len(pre)-1] += precio[i]
                            dist[len(dist)-1] += distancia[i]
                        
                        #pre.append("precio "+str(len(pre))+": "+str(precio))#precio
                        #dist.append("distancia "+str(len(dist))+": "+str(distancia))#distancia
                        solucion.pop() # elimina ultimo valor de la solucion
                        precio.pop()
                        distancia.pop()
                        apilar(pila,pos.sig)
                    else:
                        apilar(pila,pos.sig)
                        aux = self.buscarVertice(pos.info.CD)
                        solucion.append(aux.info.ciudad)
                        precio.append(pos.info.importe)  #precio
                        distancia.append(pos.info.distancia) #distancia
                        apilar(pila,aux.cab)
                else:
                    solucion.pop()  #elimina ultimo valor de la solucion
                    precio.pop()  #precio
                    distancia.pop()  #distancia
                   
                    visitados.pop() #elimina de visitado para poder utilizar por otro cammino
            
        return sol, pre, dist
        
      
    def caminos(self,origen,destino): #devuelve un vector con caminos precio y distancia
        res = [] #resultados
        
        caminos,precios, distancias = self.soluciones(origen,destino)
        
        for i in range(0,len(caminos)):
            reg = regCamino()
            reg.camino = caminos[i]
            reg.importe = precios[i]
            reg.distancia = distancias[i] 
            res.append(reg)

        return res
     
     
    def listarCaminos(self,vec):
        for i in range(0,len(vec)):
            print("")
            print(vec[i].camino+"  Precio: "
                        +str(vec[i].importe)+"  Distancia: "+str(vec[i].distancia))
        
    
    def burbujaI(self,v): #por importe
        for i in range(1,len(v)):
            for j in range (0, len(v)-i):
                if(v[j].importe > v[j+1].importe):
                    aux = v[j]
                    v[j] = v[j+1]
                    v[j+1] = aux
        return v
     
     
    def burbujaD(self,v): #por distancia
        for i in range(1,len(v)):
            for j in range (0, len(v)-i):
                if(v[j].distancia > v[j+1].distancia):
                    aux = v[j]
                    v[j] = v[j+1]
                    v[j+1] = aux
        return v
        
    
    

            
            
               
                    
                        
                
                
                
                
                    
                    
                    
                    
                

                
                
                
                    
                    
                    
                    
                    
            
                    
            
            
            
            
            
            
            
            
            
            
            

       