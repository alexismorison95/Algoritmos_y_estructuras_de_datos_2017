# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 20:54:44 2017

@author: Alexis
"""


from archivoG import abrir
from tpentrerios import grafo



#defino los archivos y los abro
fileVertices = abrir("vertices")
fileAristas = abrir("aristas")

#defino el grafo
g = grafo()

#g.cargarCiudad(fileVertices)
#g.cargarViaje(fileAristas)

#cargo el grafo desde el archivo
g.iniVertices(fileVertices)
g.iniAristas(fileAristas)
g.listarGrafo()


#buscador que nos puede servir
pos = g.buscador("rios")
if(pos!=None):
    for i in range(0,len(pos)):
        print(pos[i])


#lista = g.dijkstra("paraná","colon")

lista = g.caminos("parana entre rios","concepcion del uruguay entre rios")

g.listarCaminos(lista)

#v = g.burbujaI(lista)
#print("")
#print("")
#print("Caminos ordenados por precio")
#g.listarCaminos(v)






#cerrar(fileVertices) 
#cerrar(fileAristas)       



