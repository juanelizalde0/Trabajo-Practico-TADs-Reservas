from datetime import date,datetime,timedelta
from TADReservas import *
from TADAgenda import *

def recorrerFecha(agenda,cant,f):          #recorre la agenda buscando una reserva con la misma fecha que se le dio, si la encuentra devuelve esa reserva, sino devuelve None
    for i in range (0,cant):
        r=recuperarReserva(agenda,i)
        if(f==verFecha(r)):  
            return r                       #devuelve la reserva (r) si encuentra una reserva con la misma fecha (f) que se le dio
    return None                            #devuelve None si no hay ninguna reserva con esa fecha en el sistema

def cargarDatos():                              #separe el cargar datos de cargar fecha para simplificar a la hora de llamar desde la main
    act=input("\nActividad de la reserva: ")
    p=input("Nivel de prioridad: ")

    return act, p

def cargarFecha(agenda,modo):           #pide al usuario que ingrese una fecha, dependiendo del modo, si es 'nueva' se fija que esa fecha no este reservada, y si es 'existente' se fija que esa fecha ya este reservada y devuelve la reserva para ahorrar dsp el proceso de recuperarla 
    while True:
        dia = int(input("Dia: "))
        mes = int(input("Mes: "))
        anio = int(input("Año: "))
        hora = int(input("Hora: "))
        minuto = int(input("Minuto: "))
        fecha=datetime(anio,mes,dia,hora,minuto)
        
        cant = cantidadReservas(agenda)
        r = recorrerFecha(agenda, cant, fecha)          
        if modo == 'nueva':                         #si en el main le doy el modo 'nueva' es porque es una fecha que quiero cargar, y no modificar o eliminar
            if r is None:                           #para cargarla se tiene que fijar si esa fecha ya esta reservada, recorrerFecha devuelve None es porque no hay ninguna reserva con esa fecha
                return fecha                        #entonces devuelve la fecha para ya asi cargar la reserva con esa
            else:
                print("\nLa fecha ya esta reservada, ingresa otra\n")
        elif modo == 'existente':                   #si en el main le doy el modo 'existente' es porque es una reserva que quiero modificar o eliminar
            if r is not None:                       #si esa reserva devuelve algo distinto a None es porque encontro la reserva con esa fecha
                return r                            #devuelvo la reserva para ya asi modificar o eliminar sin tener que volver a recuperarla desde la main y verificar esta misma
            else:
                print("\nLa fecha no se encuentra en nuestro sistema, ingresa otra\n")

def ordenarFechas(aux):
    cant = cantidadReservas(aux)

    for i in range(cant):
        for j in range(0, cant - i - 1):
            r1 = recuperarReserva(aux, j)
            r2 = recuperarReserva(aux, j+1)

            if verFecha(r1) > verFecha(r2):
                aux[j], aux[j+1] = aux[j+1], aux[j]

    return aux
                 
        
    