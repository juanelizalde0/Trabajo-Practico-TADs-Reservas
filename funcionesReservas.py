from datetime import date,datetime,timedelta
from TADReservas import *
from TADAgenda import *
from TADCola import*


def recorrerFecha(agenda,cant,f,opcion):          #recorre la agenda buscando una reserva con la misma fecha que se le dio, si la encuentra devuelve esa reserva, sino devuelve None
    for i in range (0,cant):
        r=recuperarReserva(agenda,i)
        if opcion=="fecha completa":
            if f==verFecha(r):  
                return r                           #devuelve la reserva (r) si encuentra una reserva con la misma fecha(con hora) (f) que se le dio
        elif opcion=="Solo dia":                     
            if(f.date()==verFecha(r).date()):
                return r                            #devuelve la reserva (r) si encuentra una reserva con wl mismo dia/mes/año (f) que se le dio
    return None                                     #devuelve None si no hay ninguna reserva con esa fecha en el sistema

def cargarDatos():                              #separe el cargar datos de cargar fecha para simplificar a la hora de llamar desde la main
    act=input("\nActividad de la reserva: ")
    p=input("Nivel de prioridad (normal, socio, torneo): ").lower()

    return act, p

def cargarFecha(agenda,modo):           #pide al usuario que ingrese una fecha, dependiendo del modo, si es 'nueva' se fija que esa fecha no este reservada, y si es 'existente' se fija que esa fecha ya este reservada y devuelve la reserva para ahorrar dsp el proceso de recuperarla 
    while True:
        dia = int(input("Dia: "))
        mes = int(input("Mes: "))
        anio = int(input("Año: "))
        hora = int(input("Hora: "))
        minuto = int(input("Minuto: "))
        fecha=datetime(anio,mes,dia,hora,minuto)
        
        cant=cantidadReservas(agenda)
        r=recorrerFecha(agenda, cant, fecha, "fecha completa")          
        if modo=='nueva':                         #si en el main le doy el modo 'nueva' es porque es una fecha que quiero cargar, y no modificar o eliminar
            if r is None:                           #para cargarla se tiene que fijar si esa fecha ya esta reservada, recorrerFecha devuelve None es porque no hay ninguna reserva con esa fecha
                return fecha                        #entonces devuelve la fecha para ya asi cargar la reserva con esa
            else:
                print("\nLa fecha ya esta reservada, ingresa otra\n")
        elif modo=='existente':                   #si en el main le doy el modo 'existente' es porque es una reserva que quiero modificar o eliminar
            if r is not None:                       #si esa reserva devuelve algo distinto a None es porque encontro la reserva con esa fecha
                return r                            #devuelvo la reserva para ya asi modificar o eliminar sin tener que volver a recuperarla desde la main y verificar esta misma
            else:
                print("\nLa fecha no se encuentra en nuestro sistema, ingresa otra\n")

def ordenarFechas(aux):
    cant = cantidadReservas(aux)
    for i in range(cant):                           #recorre toda la agenda y por cada reserva compara su fecha con la siguiente, hace eso mismo la cantidad de reservas que haya en la agenda
        for j in range(cant - 1 - i):            #recorre hasta la penultima y a esa le resta la cantidad de veces que ya hizo el proceso para no volver a comparar las que ya quedaron ordenadas
            r1 = recuperarReserva(aux, j)
            r2 = recuperarReserva(aux, j+1)

            if verFecha(r1) > verFecha(r2):
                aux[j], aux[j+1] = aux[j+1], aux[j]
    return aux

def imprimirReservas(agendaaux):
    cant=cantidadReservas(agendaaux)
    for i in range (0,cant):
        r=recuperarReserva(agendaaux,i)
        print(f"{verActividad(r)} | {verPrioridad(r)} | {verFecha(r)}\n")    

def cargarFecha2(agenda, modo):
    while True:
        dia=int(input("Dia:"))
        mes=int(input("Mes:"))
        anio=int(input("Año:"))
        fecha=datetime(anio, mes, dia)

        cant = cantidadReservas(agenda)
        r = recorrerFecha(agenda, cant, fecha, "Solo dia")         #recorro la agenda buscando una reserva con ese dia/mes/anio, si la encuentra devuelve esa reserva, sino devuelve None
        
        if modo=='trasladar':
            if r is None:
                print("\nLa fecha no se encuentra en nuestro sistema, ingresa otra\n")
            else:
                print(f"Fecha |{verFecha(r).date()}| encontrada en la agenda.")
                print("Ingrese la nueva fecha a la que desea trasladar las reservas")
                dia=int(input("Dia:"))
                mes=int(input("Mes:"))
                anio=int(input("Año:"))
                fechanueva=datetime(anio, mes, dia)
                return fecha, fechanueva

        elif modo=='cancelar':
            if r is None:
                print("\nLa fecha no se encuentra en nuestro sistema, ingresa otra\n")
            else: 
                print(f"Fecha |{verFecha(r).date()}| encontrada en la agenda.")
                return fecha
        elif modo=='existente':
            if r is None:
                print("\nLa fecha no se encuentra en nuestro sistema, ingresa otra\n")
            else: 
                return fecha
        

def trasladarFecha(agenda, f, fN):
    cant=cantidadReservas(agenda)
    for i in range (cant):
        r=recuperarReserva(agenda, i)
        if verFecha(r).date()==f.date():
            hora=verFecha(r).time()
            fechaCompletaN=datetime.combine(fN.date(), hora)
            modFecha(r, fechaCompletaN)

def cancelarFecha(agenda, f):
    agendaux=agenda.copy()   
    cant=cantidadReservas(agendaux)                          #con esta copia no modifico la agenda original
    for i in range (cant):                                   #al recorrer con una agende auxiliar, no se modifica la cantidad del for ni el orden. entonces no se rompe
            r=recuperarReserva(agendaux, i)                  #al eliminar reservas de la original, voy a seguir el recorrido por la auxiliar y no voy a saltearme ninguna posicion
            if verFecha(r).date()==f.date():
                eliminarReserva(agenda, r)
def imprimirDatos(r,modo):                                  #esta funcion esta hecha para optimizar el codigo y repetir lo mismo tantas veces
    if modo=='modificada':
        print(f"\nReserva modificada: {verActividad(r)} | {verPrioridad(r)} | {verFecha(r)}\n")
    elif modo=='actual':
        print(f"\nReserva actual: {verActividad(r)} | {verPrioridad(r)} | {verFecha(r)}\n")

def encolarFecha(agenda,f):
    cant=cantidadReservas(agenda)
    cola=crearCola()
    for i in range (cant):                      
        r=recuperarReserva(agenda, i)                       
        if verFecha(r).date()==f.date():                        
            encolar(cola,verActividad(r),verPrioridad(r))
    return cola
    
def ordenarCola(cola):
    normal = crearCola()
    socio = crearCola()
    torneo = crearCola()

    while not esVacia(cola):
        act, prioridad=desencolar(cola)

        if prioridad=='normal':
            encolar(normal,act,prioridad)
        
        elif prioridad=='socio':
            encolar(socio,act,prioridad)
        
        elif prioridad=='torneo':
            encolar(torneo,act,prioridad)
    
    while not esVacia(torneo):
        a,p=desencolar(torneo)
        encolar(cola,a,p)
    while not esVacia(socio):
        a,p=desencolar(socio)
        encolar(cola,a,p)
    while not esVacia(normal):
        a,p=desencolar(normal)
        encolar(cola,a,p)
    
    return cola

def escribirCola(cola,f):
    print("\n-------------------HOJA DE RUTA PARA EL DIA",f.date(),"-------------------\n")
    while not esVacia(cola): 
        actividad, prioridad=desencolar(cola)
        print(f"{actividad} | {prioridad}\n")
        
