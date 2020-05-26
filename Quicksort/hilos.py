# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 16:26:20 2018

@author: Alexis
"""

from threading import Thread
import threading

def qsort(lista,first,last):

    print(lista[first:last])

    i = first
    j = last
    pivot = lista[(first+last)//2]
    #temp = 0
    while(i <= j):
         while(pivot > lista[i]):
             i = i+1
         while(pivot < lista[j]):
             j = j-1
         if(i <= j):
             aux = lista[i]     
             lista[i] = lista[j]
             lista[j] = aux
             
             i+=1
             j-=1

    lthread = None
    rthread = None

    if (first < j):
        lthread = Thread(target = lambda: qsort(lista,first,j))
        lthread.start()

    if (i < last):
        rthread = Thread(target = lambda: qsort(lista,i,last))
        rthread.start()
        
    if lthread is not None: lthread.join()
    if rthread is not None: rthread.join()

    return lista


#ls = [1,3,6,9,1,2,3,8,6]
#res = qsort(ls, 0, len(ls) - 1)
#print(res)