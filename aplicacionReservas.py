from TADReservas import *   
from TADAgenda import *
from funcionesReservas import * 
agenda=crearAgenda()
while True:
    print("1. Alta de reserva")
    print("2. Modificacion de reserva")
    print("3. Cancelacion de reserva")
    print("4. Listado general de reservas")
    print("5. Reorganizacion y depuracion por fecha")
    print("6. Generacion de hoja de ruta")
    print("0. Salir")
    opcion=int(input(""))

    match opcion:
        case 1:
            reserva=crearReserva()
            act,p,fecha=cargarDatos(agenda)
            cargarReserva(reserva,act,p,fecha)
            agregarReserva(agenda,reserva)

        case 2:
            cant=cantidadReservas(agenda)
            print("Ingrese la fecha de la reserva que desea modificar:")
            dia = int(input("Día: "))
            mes = int(input("Mes: "))
            anio = int(input("Año: "))
            hora = int(input("Hora: "))
            minuto = int(input("Minuto: "))
            f=datetime(anio,mes,dia,hora,minuto)
            r=recorrerFecha(agenda,cant,f)
            if(r!=None):
                mod=input("Que desea modificar Todo - Actividad - Prioridad - Fecha")
                if(mod=="Todo"):
                    act,p,fecha=cargarDatos(agenda)
                    modReserva(r,act,p,fecha)

        


