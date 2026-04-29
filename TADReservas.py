#Crea una reserva vacia
def CrearReserva():
    return = ['','', ,]
#Carga una reserva con sus respectivos datos
def CargarReserva(reserva, act, prior, fecha, hora):
    reserva[0]=act
    reserva[1]=prior
    reserva[2]=fecha
    reserva[3]=hora
#Funciones para modificar parametros de una reserva
def ModAct(reserva, actN):
    reserva[0]=actN

def ModPrior(reserva, priorN):
    reserva[1]=priorN

def ModFecha(reserva, fechaN):
    reserva[2]=fechaN

def ModHora(reserva, horaN):
    reserva[3]=horaN
               
#Funciones para ver parametros de una reserva
def VerActividad(reserva):
    return reserva[0]

def VerPrioridad(reserva):
    return reserva[1]

def VerFecha(reserva):
    return reserva[2]

def VerHora(reserva):
    return reserva[3]
