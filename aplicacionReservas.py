from TADReservas import *   
from TADAgenda import*
from funcionesReservas import* 
from TADCola import* 
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
            r=crearReserva()
            act,p=cargarDatos()
            f=cargarFecha(agenda,'nueva')
            cargarReserva(r,act,p,f)
            agregarReserva(agenda,r)
            print(f"\nReserva cargada: {verActividad(r)} | {verPrioridad(r)} | {verFecha(r)}\n")

        case 2:
            cant=cantidadReservas(agenda)
            print("\nIngrese la fecha de la reserva que desea modificar:\n")
            r=cargarFecha(agenda,'existente')                    #ya aca recibe la reserva entonces no hace falta volver a recuperarla.
            mod=input("\nQue desea modificar? (todo - actividad - prioridad - fecha): ").lower()
            if(mod == 'todo'):
                imprimirDatos(r,'actual')
                act,p=cargarDatos()
                f=cargarFecha(agenda,'nueva')
                modReserva(r,act,p,f)
                imprimirDatos(r,'modificada')
            elif(mod=='actividad'):
                imprimirDatos(r,'actual')
                act=input("Ingrese la nueva actividad: ")
                modAct(r,act)
                imprimirDatos(r,'modificada')
            elif(mod=='prioridad'):
                imprimirDatos(r,'actual')
                p=input("Ingrese la nueva prioridad: ")
                modPrior(r,p)
                imprimirDatos(r,'modificada')
            elif(mod=='fecha'):
                imprimirDatos(r,'actual')
                f=cargarFecha(agenda,'nueva')
                modFecha(r,f)  
                imprimirDatos(r,'modificada')
        case 3: 
            cant=cantidadReservas(agenda)
            print("\nIngrese la fecha de la reserva que desea cancelar:\n")
            r=cargarFecha(agenda,'existente')
            print(f"\nSe cancelo la reserva: {verActividad(r)} | {verPrioridad(r)} | {verFecha(r)}")
            eliminarReserva(agenda,r)
        case 4:
            agendaaux=agenda.copy()                             #con esta copia no modifico la agenda original
            agendaaux=ordenarFechas(agendaaux)                  #la ordeno en una auxiliar y la imprimo ordenada
            print("\n-------------------LISTADO GENERAL DE RESERVAS ORDENADO POR FECHA------------------- \nACTIVIDAD | PRIORIDAD | FECHA\n")
            imprimirReservas(agendaaux)
        case 5:
            opt=input("A.Trasladar reservas\nB.Cancelar reservas\n").lower()
            if opt=='a': 
                f,fN= cargarFecha2(agenda,'trasladar')
                trasladarFecha(agenda,f,fN)
                print("\nReservas trasladadas\n")
            elif opt=='b':
                f=cargarFecha2(agenda,"cancelar")
                cancelarFecha(agenda,f)
                print("\nReservas canceladas\n")
        case 6: 
            print("\nIngrese una fecha para generar la hoja de ruta: ")
            f=cargarFecha2(agenda,'existente')                              #cargo y verifico con la funcion
            cola=encolarFecha(agenda,f)                                     #encolo todas las de la fecha   
            cola=ordenarCola(cola)                                          #funcion para ordenar por prioridad la cola
            escribirCola(cola,f)      
        case 0:
            break
                                      
    

        


