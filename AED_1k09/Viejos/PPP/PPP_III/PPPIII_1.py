"""
12. Hipódromo
Desarrollar un programa que permita obtener estadísticas para el Hipódromo.
Para comenzar, se debe cargar un vector de n registros (n se ingresa por teclado). Cada registro representa una apuesta
realizada para una cierta carrera, con los siguientes datos: número de ticket, caballo elegido (un número del 0 al 9,
validar) y monto a apostar.
Luego, implementar un menú con las siguientes opciones:

1.	Determinar el monto total de apuestas para cada caballo

2.	Buscar un ticket cuyo número se ingresa por teclado. Si no existe, informarlo. Si existe, multiplicar por 10 el
monto apostado y mostrar los datos de la apuesta.

3.	Contar cuántas apuestas se realizaron para un cierto número de caballo, que se ingresa por teclado

4.	Mostrar los datos del ticket con mayor monto apostado
"""
import random


class Apuestas:
    def __init__(self, numero, caballo, monto):
        self.nro = numero
        self.cab = caballo
        self.mon = monto


def validar_entre(inf, sup, mensaje):
    valor = int(input(mensaje))
    while valor < inf or valor > sup:
        print('Valor Invalido!!')
        valor = int(input(mensaje))
    return valor


def menu():
    cad = "\nMENÚ DE OPCIONES:\n" \
          "1. Determinar el monto total de apuestas para cada caballo\n" \
          "2. Busqueda de Ticket \n" \
          "3. Cantidad de apuestas por caballo\n" \
          "4. Ticket con mayor monto apostado\n" \
          "5. Salir\n" \
          "Opción: "
    return cad


# Hacer Carga automática en un vector
def carga_automatica(apuestas):
    for i in range(len(apuestas)):
        nro = random.randint(0, 9999)
        cab = random.randint(0, 9)
        mon = random.randint(50, 1000)
        apuestas[i] = Apuestas(nro, cab, mon)


def validar_mayor_que(inf, mensaje="Ingrese un nro: "):
    valor = int(input(mensaje))
    while valor <= inf:
        print('¡Valor invalido!')
        valor = int(input(mensaje))
    return valor


def selection_sort(apuestas):
    n = len(apuestas)
    for i in range(n-1):
        for j in range(i+1, n):
            if apuestas[i].nro > apuestas[j].nro:
                apuestas[i], apuestas[j] = apuestas[j], apuestas[i]


# Pasarla a string. "libro" es un vector.
def write(apuestas):
    for i in range(len(apuestas)):
        r = ""
        r += "{:<25}".format("Nro: " + str(apuestas[i].nro))
        r += "{:<20}".format("Caballo: " + str(apuestas[i].cab))
        r += "{:<20}".format("Monto: " + str(apuestas[i].mon))
        print(r)


def write_el(apuesta):
    r = ""
    r += "{:<25}".format("Nro: " + str(apuesta.nro))
    r += "{:<20}".format("Caballo: " + str(apuesta.cab))
    r += "{:<20}".format("Monto: " + str(apuesta.mon))
    print(r)


def opcion1(apuestas):
    caballos = [0] * 10
    for i in range(len(apuestas)):
        caballos[apuestas[i].cab] += apuestas[i].mon
    for i in range(len(caballos)):
        if caballos[i] != 0:
            print("Apuestas Caballo", str(i), ":", str(caballos[i]))


def busqueda_ticket(ticket, apuestas):
    r = -1
    for i in range(len(apuestas)):
        if ticket == apuestas[i].nro:
            r = i
            return r
    return r


def opcion2(apuestas):
    nro = validar_mayor_que(0, "Ingrese el nro de ticket: ")
    pos = busqueda_ticket(nro, apuestas)

    if pos == -1:
        print("No se ha encontrado el ticket buscado")
    else:
        apuestas[pos].mon *= 10
        write_el(apuestas[pos])


def opcion3(apuestas):
    caballo = validar_entre(0, 9, "Ingrese el nro. de caballo: ")
    cont = 0
    for i in range(len(apuestas)):
        if caballo == apuestas[i].cab:
            cont += 1
    print("La cantidad de apuestas realizadas para el caballo", str(caballo), "fue: ", str(cont))


def buscar_mayor(apuestas):
    mayor = 0
    for i in range(1, len(apuestas)):
        if apuestas[i].mon > apuestas[mayor].mon:
            mayor = i
    return mayor


def opcion4(apuestas):
    pos = buscar_mayor(apuestas)
    print("El ticket con mayor monto apostado fue: ")
    write_el(apuestas[pos])


def test():
    print("ESTADÍSTICAS DEL HIPÓDROMO:")
    print("="*60)
    op = -1

    n = validar_mayor_que(0, "Ingrese el nro de apuestas a procesar: ")
    apuestas = [None] * n
    carga_automatica(apuestas)
    selection_sort(apuestas)
    write(apuestas)

    while op != 5:
        op = validar_entre(1, 5, menu())

        if op == 1:
            opcion1(apuestas)
        elif op == 2:
            opcion2(apuestas)
        elif op == 3:
            opcion3(apuestas)
        elif op == 4:
            opcion4(apuestas)

    print("Fin.")


if __name__ == "__main__":
    test()
