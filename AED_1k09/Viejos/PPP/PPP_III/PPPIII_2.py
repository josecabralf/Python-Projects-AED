"""
Una compañía de servicios de limpieza desea un programa para procesar los datos de los trabajos ofrecidos. Por cada
trabajo se tienen los siguientes datos: el número de identificación del trabajo, la descripción o nombre del mismo, el
tipo de trabajo (un valor de 0 a 3, 0:interior, 1:exterior, 2:piletas, 3:tapizados), el importe a cobrar por ese trabajo
 y la cantidad de personal afectado para prestar ese servicio. Se desea almacenar la información referida a los n
 trabajos en un arreglo de registros de trabajos (definir el Trabajo y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones, que permita gestionar las siguientes
tareas:

1- Cargar el arreglo pedido con los datos de los n trabajos. Valide que el número identificador del trabajo sea
positivo y que el importe a cobrar sea mayor a cero. Puede hacer la carga en forma manual, o puede generar los datos
en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe
programar.

2- Mostrar todos los datos de todos los trabajos, en un listado ordenado de mayor a menor según los importes a cobrar.

3- Determinar y mostrar los datos del trabajo que tenga la mayor cantidad de personal afectado (no importa si hay
varios trabajos con la misma cantidad máxima de personal: se pide mostrar uno y sólo uno cuya cantidad de personal
sea máxima).

4- Determinar si existe un trabajo cuya descripción sea igual a d, siendo d un valor que se carga por teclado. Si
existe, mostrar sus datos. Si no existe, informar con un mensaje. Si existe más de un registro que coincida con esos
parámetros de búsqueda, debe mostrar sólo el primero que encuentre.

5- Determinar y mostrar la cantidad de trabajos por tipo.

"""
import random


class Trabajo:
    def __init__(self, numero, nombre, tipo, importe, personal):
        self.nro = numero
        self.nom = nombre
        self.tipo = tipo
        self.imp = importe
        self.per = personal


def validar_mayor_que(inf, mensaje="Ingrese un nro: "):
    valor = int(input(mensaje))
    while valor <= inf:
        print('¡Valor invalido!')
        valor = int(input(mensaje))
    return valor


def validar_entre(inf, sup, mensaje):
    valor = int(input(mensaje))
    while valor < inf or valor > sup:
        print('Valor Invalido!!')
        valor = int(input(mensaje))
    return valor


def nombres():
    nom = ["Limpieza", "Pulido", "Aspiradora", "Hidrolavado", "Mantenimiento"]
    return nom


def menu():
    cad = "\nMENÚ DE OPCIONES:\n" \
          "1. Cargar Trabajos\n" \
          "2. Mostrar Trabajos Cargados \n" \
          "3. Trabajo con más personal\n" \
          "4. Encontrar trabajo con descripción d\n" \
          "5. Trabajos por tipo\n" \
          "6. Salir\n" \
          "Opción: "
    return cad


def carga_automatica(trabajos):
    for i in range(len(trabajos)):
        nro = random.randint(0, 9999)
        nom = random.choice(nombres())
        tipo = random.randint(0, 3)
        importe = random.randint(500, 9999)
        personal = random.randint(1, 9)
        trabajos[i] = Trabajo(nro, nom, tipo, importe, personal)


def opcion1():
    n = validar_mayor_que(0, "\nIngrese el nro de trabajos a procesar: ")
    trabajos = [None] * n
    carga_automatica(trabajos)
    return trabajos


def selection_sort_imp(trabajos):
    n = len(trabajos)
    for i in range(n-1):
        for j in range(i+1, n):
            if trabajos[i].imp < trabajos[j].imp:
                trabajos[i], trabajos[j] = trabajos[j], trabajos[i]


def write(trabajos):
    for i in range(len(trabajos)):
        r = ""
        r += "{:<15}".format("Nro: " + str(trabajos[i].nro))
        r += "{:<30}".format("Descripción: " + trabajos[i].nom)
        r += "{:<10}".format("Tipo: " + str(trabajos[i].tipo))
        r += "{:<15}".format("Importe: " + str(trabajos[i].imp))
        r += "{:<15}".format("Personal: " + str(trabajos[i].per))
        print(r)


def opcion2(trabajos):
    print()
    selection_sort_imp(trabajos)
    write(trabajos)


def buscar_mayor(trabajos):
    mayor = 0
    for i in range(1, len(trabajos)):
        if trabajos[i].per > trabajos[mayor].per:
            mayor = i
    return mayor


def write_el(trabajos):
    r = ""
    r += "{:<15}".format("Nro: " + str(trabajos.nro))
    r += "{:<30}".format("Descripción: " + trabajos.nom)
    r += "{:<10}".format("Tipo: " + str(trabajos.tipo))
    r += "{:<15}".format("Importe: " + str(trabajos.imp))
    r += "{:<15}".format("Personal: " + str(trabajos.per))
    print(r)


def opcion3(trabajos):
    pos = buscar_mayor(trabajos)
    write_el(trabajos[pos])


def linear_search_d(trabajos, d):
    r = -1
    for i in range(len(trabajos)):
        if d == trabajos[i].nom:
            r = i
            return r
    return r


def opcion4(trabajos):
    d = str(input("\nIngrese la descripción buscada: "))
    pos = linear_search_d(trabajos, d)
    if pos == -1:
        print("No existe un trabajo con la descripción buscada")
    else:
        print("Existe un trabajo con la descripción buscada:")
        write_el(trabajos[pos])


def opcion5(trabajos):
    tipos = [0] * 4
    for i in range(len(trabajos)):
        tipos[trabajos[i].tipo] += 1
    for i in range(len(tipos)):
        print("Trabajo Tipo", str(i), ":", str(tipos[i]))


def test():
    print("SERVICIOS DE LIMPIEZA:")
    print("="*60)

    op = -1
    existe = False
    trabajos = []

    while op != 6:
        op = validar_entre(1, 6, menu())

        if op == 1:
            trabajos = opcion1()
            existe = True
        elif op == 2:
            if existe:
                opcion2(trabajos)
            else:
                print("Error... No hay trabajos que procesar. Carguelos con la opción 1!")
        elif op == 3:
            if existe:
                opcion3(trabajos)
            else:
                print("Error... No hay trabajos que procesar. Carguelos con la opción 1!")
        elif op == 4:
            if existe:
                opcion4(trabajos)
            else:
                print("Error... No hay trabajos que procesar. Carguelos con la opción 1!")
        elif op == 5:
            if existe:
                opcion5(trabajos)
            else:
                print("Error... No hay trabajos que procesar. Carguelos con la opción 1!")

    print("\nFin!")


if __name__ == "__main__":
    test()
