#Crea una reserva vacia
def crearReserva():
    reserva=['','',0,0]
    return reserva

#Carga una reserva con sus respectivos datos
def cargarReserva(reserva, act, prior, fecha):
    reserva[0]=act
    reserva[1]=prior
    reserva[2]=fecha

#Funciones para modificar parametros de una reserva
def modReserva(reserva,nuevaA,nuevaP,nuevaFecha):
    reserva[0]=nuevaA
    reserva[1]=nuevaP
    reserva[2]=nuevaFecha
def modAct(reserva, actN):
    reserva[0]=actN

def modPrior(reserva, priorN):
    reserva[1]=priorN

def modFecha(reserva, fechaN):
    reserva[2]=fechaN
               
#Funciones para ver parametros de una reserva
def verActividad(reserva):
    return reserva[0]

def verPrioridad(reserva):
    return reserva[1]

def verFecha(reserva):
    return reserva[2]


