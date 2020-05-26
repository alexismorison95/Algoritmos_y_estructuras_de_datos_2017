import PD

def orden_stock(lista): 
    li = 0
    lf = len(lista) -1   
    QuickSortStock(lista,li, lf)
    
def orden_id(lista): 
    li = 0
    lf = len(lista) -1   
    QuickSortID(lista,li, lf)

def orden_tipo(lista): 
    li = 0
    lf = len(lista) -1   
    QuickSortTipo(lista,li, lf)
def orden_marca(lista): 
    li = 0
    lf = len(lista) -1   
    QuickSortMarca(lista,li, lf)
def orden_año(lista): 
    li = 0
    lf = len(lista) -1   
    QuickSortAño(lista,li, lf)
def orden_modelo(lista): 
    li = 0
    lf = len(lista) -1   
    QuickSortModelo(lista,li, lf)
def orden_importe(lista): 
    li = 0
    lf = len(lista) -1   
    QuickSortImporte(lista,li, lf)
def orden_color(lista): 
    li = 0
    lf = len(lista) -1   
    QuickSortColor(lista,li, lf)
    

def QuickSortID(Lista,li,lf):
    pila = PD.PilaD()
    PD.crearpilaD(pila)
    PD.apilar(pila,[li,lf])
    while(not PD.pilavacia(pila)):
        x = PD.desapilar(pila)
        li, lf = x[0], x[1]
        pivot= lf 
        i= li 
        j= lf - 1
        while (i <= j) : 
            while (Lista[i].idAuto < Lista[pivot].idAuto):
                i= i + 1
            while Lista[j].idAuto > Lista[pivot].idAuto:
                j= j - 1
            if (i <= j):
                aux= Lista[i]
                Lista[i]= Lista[j]
                Lista[j]= aux               
                i= i + 1
                j= j - 1
        aux=Lista[i]
        Lista[i]=Lista[lf]
        Lista[lf]=aux
        if (i<lf):
            PD.apilar(pila,[(i),lf])
        if (j>li):    
            PD.apilar(pila,[li,(j)])
    
def QuickSortTipo(Lista,li,lf):
    pila = PD.PilaD()
    PD.crearpilaD(pila)
    PD.apilar(pila,[li,lf])
    while(not PD.pilavacia(pila)):
        x = PD.desapilar(pila)
        li, lf = x[0], x[1]
        pivot= lf 
        i= li 
        j= lf - 1
        while (i <= j) : 
            while (Lista[i].tipo < Lista[pivot].tipo):
                i= i + 1
            while Lista[j].tipo > Lista[pivot].tipo:
                j= j - 1
            if (i <= j):
                aux= Lista[i]
                Lista[i]= Lista[j]
                Lista[j]= aux               
                i= i + 1
                j= j - 1
        aux=Lista[i]
        Lista[i]=Lista[lf]
        Lista[lf]=aux
        if (i<lf):
            PD.apilar(pila,[(i),lf])
        if (j>li):    
            PD.apilar(pila,[li,(j)])
    
def QuickSortMarca(Lista,li,lf):
    pila = PD.PilaD()
    PD.crearpilaD(pila)
    PD.apilar(pila,[li,lf])
    while(not PD.pilavacia(pila)):
        x = PD.desapilar(pila)
        li, lf = x[0], x[1]
        pivot= lf 
        i= li 
        j= lf - 1
        while (i <= j) : 
            while (Lista[i].marca < Lista[pivot].marca):
                i= i + 1
            while Lista[j].marca > Lista[pivot].marca:
                j= j - 1
            if (i <= j):
                aux= Lista[i]
                Lista[i]= Lista[j]
                Lista[j]= aux               
                i= i + 1
                j= j - 1
        aux=Lista[i]
        Lista[i]=Lista[lf]
        Lista[lf]=aux
        if (i<lf):
            PD.apilar(pila,[(i),lf])
        if (j>li):    
            PD.apilar(pila,[li,(j)])
    
def QuickSortAño(Lista,li,lf):
    pila = PD.PilaD()
    PD.crearpilaD(pila)
    PD.apilar(pila,[li,lf])
    while(not PD.pilavacia(pila)):
        x = PD.desapilar(pila)
        li, lf = x[0], x[1]
        pivot= lf 
        i= li 
        j= lf - 1
        while (i <= j) : 
            while (Lista[i].año < Lista[pivot].año):
                i= i + 1
            while Lista[j].año > Lista[pivot].año:
                j= j - 1
            if (i <= j):
                aux= Lista[i]
                Lista[i]= Lista[j]
                Lista[j]= aux               
                i= i + 1
                j= j - 1
        aux=Lista[i]
        Lista[i]=Lista[lf]
        Lista[lf]=aux
        if (i<lf):
            PD.apilar(pila,[(i),lf])
        if (j>li):    
            PD.apilar(pila,[li,(j)])
    
def QuickSortModelo(Lista,li,lf):
    pila = PD.PilaD()
    PD.crearpilaD(pila)
    PD.apilar(pila,[li,lf])
    while(not PD.pilavacia(pila)):
        x = PD.desapilar(pila)
        li, lf = x[0], x[1]
        pivot= lf 
        i= li 
        j= lf - 1
        while (i <= j) : 
            while (str(Lista[i].modelo) < str(Lista[pivot].modelo)):
                i= i + 1
            while str(Lista[j].modelo) > str(Lista[pivot].modelo):
                j= j - 1
            if (i <= j):
                aux= Lista[i]
                Lista[i]= Lista[j]
                Lista[j]= aux               
                i= i + 1
                j= j - 1
        aux=Lista[i]
        Lista[i]=Lista[lf]
        Lista[lf]=aux
        if (i<lf):
            PD.apilar(pila,[(i),lf])
        if (j>li):    
            PD.apilar(pila,[li,(j)])
   
def QuickSortImporte(Lista,li,lf):
    pila = PD.PilaD()
    PD.crearpilaD(pila)
    PD.apilar(pila,[li,lf])
    while(not PD.pilavacia(pila)):
        x = PD.desapilar(pila)
        li, lf = x[0], x[1]
        pivot= lf 
        i= li 
        j= lf - 1
        while (i <= j) : 
            while (float(Lista[i].importe) < float(Lista[pivot].importe)):
                i= i + 1
            while float(Lista[j].importe) > float(Lista[pivot].importe):
                j= j - 1
            if (i <= j):
                aux= Lista[i]
                Lista[i]= Lista[j]
                Lista[j]= aux               
                i= i + 1
                j= j - 1
        aux=Lista[i]
        Lista[i]=Lista[lf]
        Lista[lf]=aux
        if (i<lf):
            PD.apilar(pila,[(i),lf])
        if (j>li):    
            PD.apilar(pila,[li,(j)])
                
def QuickSortColor(Lista,li,lf):
    pila = PD.PilaD()
    PD.crearpilaD(pila)
    PD.apilar(pila,[li,lf])
    while(not PD.pilavacia(pila)):
        x = PD.desapilar(pila)
        li, lf = x[0], x[1]
        pivot= lf 
        i= li 
        j= lf - 1
        while (i <= j) : 
            while (Lista[i].detalle < Lista[pivot].detalle):
                i= i + 1
            while Lista[j].detalle > Lista[pivot].detalle:
                j= j - 1
            if (i <= j):
                aux= Lista[i]
                Lista[i]= Lista[j]
                Lista[j]= aux               
                i= i + 1
                j= j - 1
        aux=Lista[i]
        Lista[i]=Lista[lf]
        Lista[lf]=aux
        if (i<lf):
            PD.apilar(pila,[(i),lf])
        if (j>li):    
            PD.apilar(pila,[li,(j)])
                
def QuickSortStock(Lista,li,lf):
    pila = PD.PilaD()
    PD.crearpilaD(pila)
    PD.apilar(pila,[li,lf])
    while(not PD.pilavacia(pila)):
        x = PD.desapilar(pila)
        li, lf = x[0], x[1]
        pivot= lf 
        i= li 
        j= lf - 1
        while (i <= j) : 
            while (float(Lista[i].stock) < float(Lista[pivot].stock)):
                i= i + 1
            while float(Lista[j].stock) > float(Lista[pivot].stock):
                j= j - 1
            if (i <= j):
                aux= Lista[i]
                Lista[i]= Lista[j]
                Lista[j]= aux               
                i= i + 1
                j= j - 1
        aux=Lista[i]
        Lista[i]=Lista[lf]
        Lista[lf]=aux
        if (i<lf):
            PD.apilar(pila,[(i),lf])
        if (j>li):    
            PD.apilar(pila,[li,(j)])

