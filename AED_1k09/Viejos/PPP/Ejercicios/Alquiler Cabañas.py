"""
9. Inmobiliaria de Cabañas
Una empresa dedicada al alquiler de cabañas de veraneo desea almacenar la información referida a los n alquileres de la
temporada estival en un arreglo de registros (cargar n por teclado). Por cada alquiler, se pide guardar el nombre y dni
de la persona que hizo la reserva, monto del alquiler y un código entre 0 y 9 que indica el tipo de cabaña alquilada
(suponiendo que por ejemplo, el 0 indica que se alquiló una cabaña de tipo Común, el 1 Premiun, el 2 Super Premiun, y
así hasta el código 9).

Se pide desarrollar un programa en Python controlado por un menú de opciones. Ese menú debe permitir gestionar las
siguientes tareas a partir del arreglo pedido en el párrafo anterior, siempre usando funciones que acepten parámetros
y/o retornen valores en cada situación en que se considere apropiado:

1. Cargar el arreglo de alquileres. Validar que el código de tipo de cabaña esté efectivamente entre 0 y 9. (no
realizar otra validación más que la solicitada).
2. Determinar la cantidad de alquileres que registraron un monto mayor a x, siendo x un valor pasado por parámetro.
3. Determinar y mostrar el monto total recaudado por cada tipo de cabaña posible (un acumulador que indique el monto
total recaudado por el alquiler de las cabañas de tipo 0, otro para las cabañas de tipo 1, etc.).
4. Mostrar los datos de todos los alquileres en orden de mayor a menor por el dni de las personas que realizaron la
reserva.
5. Mostrar un informe con todos los alquileres que registraron el menor monto (note que podría haber más de un alquiler
con el mismo monto menor).
"""""""""""


def validar_entre(inf, sup, mensaje="Ingrese un número: "):
    n = inf - 1
    while n > sup or n < inf:
        n = int(input(mensaje))
        if n > sup or n < inf:
            print("ERROR: Esa opción no es válida... ")
    return n


def validar_mayor_que(inf, mensaje="Ingrese un nro: "):
    n = inf
    while n <= inf:
        n = int(input(mensaje + str(inf) + ": "))
        if n <= inf:
            print("ERROR! Debe ser mayor a" + str(inf))
    return n


def menu():
    cadena = "\nMenu de Opciones\n" \
             "================================\n" \
             "1) Cargar el arreglo de alquileres\n" \
             "2) Cantidad de alquileres que registraron un monto mayor a x\n" \
             "3) Monto total recaudado por cada tipo de cabaña posible\n" \
             "4) Datos de todos los alquileres\n" \
             "5) informe con todos los alquileres que registraron el menor monto\n" \
             "6) Salir\n" \
             "Ingrese su opcion: "
    return int(input(cadena))


def cargar_alquileres(alquileres, n):
    pass


def principal():
    alquileres = []
    opcion = -1
    while opcion != 6:
        opcion = menu()

        if opcion == 1:
            n = validar_mayor_que(0, "Ingrese el número de alquileres: ")
            cargar_alquileres(alquileres, n)
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass

if __name__ == "__main__":
    principal()
