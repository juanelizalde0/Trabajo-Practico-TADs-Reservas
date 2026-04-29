from TADReservas import* 

while True:
    print("1. Alta de reserva\n")
    print("2. Modificacion de reserva")
    print("3. Cancelacion de reserva")
    print("4. Listado general de reservas")
    print("5. Reorganizacion y depuracion por fecha")
    print("6. Generacion de hoja de ruta")
    print("0. Salir")

    if opcion == "1":
        act=input("Actividad de la reserva: ")
        p=input("Nivel de prioridad: ")
        d=("Dia: ")
        m=("Mes: ")
        a=("Año: ")

