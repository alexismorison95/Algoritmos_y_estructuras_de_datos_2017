import shelve 


def abrir(ruta):
    return shelve.open(ruta)
    
def cerrar(archivo):
    archivo.close()
    
def guardar(archivo, reg):
    archivo[str(len(archivo))] = reg
    
def leer(archivo, pos):
    try:
        return archivo[str(pos)]
    except:
        return None

def modificar(archivo, pos, reg):
    archivo[str(pos)] = reg
    

