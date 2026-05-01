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
            r=crearReserva()
            act,p=cargarDatos()
            f=cargarFecha(agenda,'nueva')
            cargarReserva(r,act,p,f)
            agregarReserva(agenda,r)
            print(f"\nReserva cargada: {verActividad(r)} | {verPrioridad(r)} | {verFecha(r)}\n")

        case 2:
            cant=cantidadReservas(agenda)
            print("\nIngrese la fecha de la reserva que desea modificar:\n")
            r=cargarFecha(agenda,'existente')     
            mod=input("\nQue desea modificar? (todo - actividad - prioridad - fecha): ").lower()
            if(mod == 'todo'):
                print(f"\nReserva actual: {verActividad(r)} | {verPrioridad(r)} | {verFecha(r)}")
                act,p=cargarDatos()
                f=cargarFecha(agenda,'nueva')
                modReserva(r,act,p,f)
                print(f"\nReserva modificada: {verActividad(r)} | {verPrioridad(r)} | {verFecha(r)}\n")
            elif(mod=='actividad'):
                print(f"\nReserva actual: {verActividad(r)} | {verPrioridad(r)} | {verFecha(r)}")
                act=input("Ingrese la nueva actividad: ")
                modAct(r,act)
                print(f"\nReserva modificada: {verActividad(r)} | {verPrioridad(r)} | {verFecha(r)}\n")
            elif(mod=='prioridad'):
                print(f"\nReserva actual: {verActividad(r)} | {verPrioridad(r)} | {verFecha(r)}")
                p=input("Ingrese la nueva prioridad: ")
                modPrior(r,p)
                print(f"\nReserva modificada: {verActividad(r)} | {verPrioridad(r)} | {verFecha(r)}\n")
            elif(mod=='fecha'):
                print(f"\nReserva actual: {verActividad(r)} | {verPrioridad(r)} | {verFecha(r)}")
                f=cargarFecha(agenda,'nueva')
                modFecha(r,f)  
                print(f"\nReserva modificada: {verActividad(r)} | {verPrioridad(r)} | {verFecha(r)}\n")
        case 3: 
            cant=cantidadReservas(agenda)
            print("\nIngrese la fecha de la reserva que desea cancelar:\n")
            r=cargarFecha(agenda,'existente')
            print(f"\nSe cancelo la reserva: {verActividad(r)} | {verPrioridad(r)} | {verFecha(r)}")
            eliminarReserva(agenda,r)
        case 4:
            print("\nLISTADO GENERAL DE RESERVAS: \nACTIVIDAD | PRIORIDAD | FECHA\n")
            cant=cantidadReservas(agenda)
            for i in range (0,cant):
                r=recuperarReserva(agenda,i)
                print(f"{verActividad(r)} | {verPrioridad(r)} | {verFecha(r)}\n")    
            
    

        


