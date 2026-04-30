from TADReservas import *

def crearAgenda():
    agenda=[]
    return agenda

def agregarReserva(agenda,reserva):
    agenda.append(reserva)

def eliminarReserva(agenda,reserva):
    agenda.remove(reserva)

def recuperarReserva(agenda,pos):
    return agenda[pos]

def cantidadReservas(agenda):
    return len(agenda)  