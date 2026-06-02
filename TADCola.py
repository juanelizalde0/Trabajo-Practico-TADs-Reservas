def crearCola():
    return[]
    
def esVacia(cola):
    return len(cola)==0 

def encolar(cola,elemento1,elemento2):
    cola.append((elemento1,elemento2))      #estaria guardando una tupla porque el append hace un solo espacio en la cola

def desencolar(cola):
    if not esVacia(cola):
        return cola.pop(0)
    else:
        return None
    
def tamanio(cola):
    return len(cola)    

def copiarCola(cola1,cola2):
    aux=crearCola()
    while not esVacia(cola2):
        elem1,elem2=desencolar(cola2)
        encolar(aux,elem1,elem2)
    while not esVacia(aux):
        elem1,elem2=desencolar(aux)
        encolar(cola1,elem1,elem2)
        encolar(cola2,elem1,elem2) 
