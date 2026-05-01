from datetime import date,datetime,timedelta
from TADReservas import *
from TADAgenda import *

def recorrerFecha(agenda,cant,f):
    for i in range (0,cant):
        r=recuperarReserva(agenda,i)
        if(f==verFecha(r)):  
            return r  
    return None

def cargarDatos():
    act=input("\nActividad de la reserva: ")
    p=input("Nivel de prioridad: ")

    return act, p

def cargarFecha(agenda,modo):
    while True:
        dia = int(input("Dia: "))
        mes = int(input("Mes: "))
        anio = int(input("Año: "))
        hora = int(input("Hora: "))
        minuto = int(input("Minuto: "))
        fecha=datetime(anio,mes,dia,hora,minuto)
        
        cant = cantidadReservas(agenda)
        r = recorrerFecha(agenda, cant, fecha)
        if modo == 'nueva':
            if r is None:
                return fecha
            else:
                print("\nLa fecha ya esta reservada, ingresa otra\n")
        elif modo == 'existente':
            if r is not None:
                return r
            else:
                print("\nLa fecha no se encuentra en nuestro sistema, ingresa otra\n")
    