
class nodopila():
    info,sig = None, None
    

class PilaD():
    def __init__(self):
       self.Tope = None
       self.Tam = 0
        
def crearpilaD(P):
    P.Tope = None
    P.Tam = 0

def apilar(P,x):
    Dir = nodopila()
    Dir.info = x
    Dir.sig = P.Tope
    P.Tope = Dir
    P.Tam = P.Tam + 1

def desapilar(P):
    x = P.Tope.info
    aux = P.Tope
    P.Tope = P.Tope.sig      
    P.Tam = P.Tam - 1
    return x

def pilaVacia(P):
    return (P.Tope == None)

def pilallena(P):
    return(False)

def tam(P):
    return P.Tope + 1

def tope(P):
    return P.Tope     


