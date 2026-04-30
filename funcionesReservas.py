from datetime import date,datetime,timedelta
from TADReservas import *
from TADAgenda import *

def recorrerFecha(agenda,cant,f):
    for i in range (0,cant):
        r=recuperarReserva(agenda,i)
        if(f==verFecha(r)):  
            return r  
    return None

def cargarDatos(agenda):
    act=input("Actividad de la reserva: ")
    p=input("Nivel de prioridad: ")

    while True:
        dia = int(input("Dia: "))
        mes = int(input("Mes: "))
        anio = int(input("Año: "))
        hora = int(input("Hora: "))
        minuto = int(input("Minuto: "))

        fecha = datetime(anio,mes,dia,hora,minuto)

        cant = cantidadReservas(agenda)
        si = recorrerFecha(agenda, cant, fecha)

        if si is None:
            break
        else:
            print("\nLa fecha ya esta reservada, ingresa otra\n")

    print("fecha cargada:", fecha)
    return act, p, fecha