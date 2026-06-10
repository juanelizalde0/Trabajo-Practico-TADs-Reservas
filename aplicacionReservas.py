from TADReservas import *   
from TADAgenda import*
from funcionesReservas import* 
from TADCola import* 
from tabulate import* #en la terminal escribir pip install tabulate

agenda=crearAgenda()

while True:
    encabezados=["\033[1mOpcion\033[0m", "\033[1mMENU DE GESTION DE RESERVAS \033[0m"]
    datos=[
    ["1." , "Alta de reserva"],
    ["2." , "Modificacion de reserva"],
    ["3." , "Cancelacion de reserva"],
    ["4." , "Listado general de reservas"],
    ["5." , "Reorganizacion y depuracion por fecha"],
    ["6." , "Generacion de hoja de ruta"],
    ["0." , "Salir"]]
    tabla = tabulate(datos, headers=encabezados, tablefmt="fancy_grid")
    print(tabla)
    opcion=int(input("\nOpcion: "))

    match opcion:
        case 1:
            limpiarPantalla()
            while True:
                r=crearReserva()
                act,p=cargarDatos()
                f=cargarFecha(agenda,'nueva')
                cargarReserva(r,act,p,f)
                agregarReserva(agenda,r)
                print("\nReserva cargada con exito ...\n")
                a=input("Desea cargar otra reserva? (s/n): ").lower()
                if a=='n':
                    limpiarPantalla()
                    break
                    

        case 2:
            limpiarPantalla()
            cant=cantidadReservas(agenda)
            imprimirReservas(agenda,"l")
            while True:
                print("\nIngrese la fecha de la reserva que desea modificar:\n")
                r=cargarFecha(agenda,'existente')                    #ya aca recibe la reserva entonces no hace falta volver a recuperarla.
                mod=input("\nQue desea modificar? (todo - actividad - prioridad - fecha): ").lower()
                if(mod=='todo'):
                    act,p=cargarDatos()
                    f=cargarFecha(agenda,'nueva')
                    modReserva(r,act,p,f)
                    imprimirReservas(agenda,"mod")
                elif(mod=='actividad'):
                    act=input("Ingrese la nueva actividad: ")
                    modAct(r,act)
                    imprimirReservas(agenda,"mod")
                elif(mod=='prioridad'):
                    p=input("Ingrese la nueva prioridad: ")
                    modPrior(r,p)
                    imprimirReservas(agenda,"mod")
                elif(mod=='fecha'):
                    f=cargarFecha(agenda,'nueva')
                    modFecha(r,f)  
                    imprimirReservas(agenda,"mod")
                a=input("Desea modificar alguna otra reserva? (s/n): ").lower()
                if a=="n":
                    limpiarPantalla()
                    break
            
        case 3: 
            limpiarPantalla()
            while True:
                cant=cantidadReservas(agenda)
                print("Ingrese la fecha de la reserva que desea cancelar:\n")
                r=cargarFecha(agenda,'existente')
                print("\nReserva cancelada con exito...\n")
                eliminarReserva(agenda,r)
                a=input("\nDesea cancelar otra reserva? (s/n): ")
                if a=="n":
                    break
            
        case 4:
            limpiarPantalla()
            agendaaux=agenda.copy()                             #con esta copia no modifico la agenda original
            agendaaux=ordenarFechas(agendaaux)                  #la ordeno en una auxiliar y la imprimo ordenada
            imprimirReservas(agendaaux,"l")

        case 5:
            limpiarPantalla()
            while True:
                opt=input("A.Trasladar reservas\nB.Cancelar reservas\n").lower()
                if opt=='a': 
                    f,fN= cargarFecha2(agenda,'trasladar')
                    trasladarFecha(agenda,f,fN)
                    print("\nReservas trasladadas con exito...\n")
                elif opt=='b':
                    f=cargarFecha2(agenda,"cancelar")
                    cancelarFecha(agenda,f)
                a=input("\nDesea hacer otra reorganizacion o depuracion? (s/n): ")
                if a=='n':
                    limpiarPantalla() 
                    break

        case 6: 
            limpiarPantalla()
            print("Ingrese una fecha para generar la hoja de ruta: ")
            f=cargarFecha2(agenda,'existente')                              #cargo y verifico con la funcion
            cola=encolarFecha(agenda,f)                                     #encolo todas las de la fecha   
            cola=ordenarCola(cola)                                          #funcion para ordenar por prioridad la cola
            limpiarPantalla()                                                
            escribirCola(cola,f)    

        case 0:
            limpiarPantalla()
            print("se cerro el sistema...")
            break
                                      
    

        


