"""
En una empresa de telefonía celular unos de sus mejores ingresos es la venta de paquetes de gigas para navegar por
internet para sus respectivas líneas. Dichos planes, por política de la empresa se venden en las oficinas de ventas
oficiales y se acreditan dichos gigas al día siguiente, para la cual las oficinas envían un listado de las líneas que
han comprado dichos planes (Para el programa a hacer no importa el tamaño del paquete o el costo).

Para poder acreditar el paquete, el teléfono no debe figurar en un listado de celulares que se encuentran bloqueados o
denunciados por motivos de falta de pago. Dicho listado se encuentra ordenado.(-)

Para facilitar la identificación por áreas geográficas en vez de comenzar con los cuatro dígitos habituales para la
característica , comienza con un numero entre 1 y 10 que representan la característica de cada región(de nuevo se
simplifica el modelo del negocio). Por lo que el formato del número sería por ejemplo 1-548745487 o 5-587946185 (-)

Usted debe realizar un programa que, permita validar si a dicho numero telefónico se le puede asignar el paquete o no.
Para ello implementar un menú de opciones con las siguientes operaciones

1) - Cargar por única vez el listado de números de telefonía celular bloqueados (-)
2) - Cargar el listado de números telefónicos a los que se le deben asignar un paquete de gigas (-)
3) - Calcular el porcentaje de números telefónicos que no se les asignara un paquete por encontrarse bloqueados (-)
4) - Determinar la cantidad de paquetes que se han vendido para cada característica.
"""
import random


def validar_mayor_que(inf, mensaje="Ingrese un nro: "):
    valor = int(input(mensaje))
    while valor < inf:
        print('¡Valor invalido!')
        valor = int(input(mensaje))
    return valor


def selection_sort(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]


def generar_telefonos(n):
    telefonos = [""] * n
    for i in range(n):
        telefonos[i] = str(random.randint(1, 10)) + "-"
        for j in range(9):
            telefonos[i] += str(random.randint(0, 9))
    return telefonos


def binary_search(v, x):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c]:
            return c
        if x < v[c]:
            der = c - 1
        else:
            izq = c + 1

    return -1


def es_valido(numero, bloqueados):
    pos = binary_search(bloqueados, numero)
    return pos == -1


def validar_numeros(telefonos, bloqueados):
    cantidad = 0
    for numero in telefonos:
        if not es_valido(numero, bloqueados):
            cantidad += 1
    return cantidad


def porcentaje(subtotal, total):
    porc = 0
    if total > 0:
        porc = round((subtotal / total) * 100, 2)
    return porc


def cantidad_por_caracteristica(telefonos, bloqueados):
    vc = [0] * 10
    for n in telefonos:
        if es_valido(n, bloqueados):
            pos = n.index("-")
            caracteristica = int(n[0:pos]) - 1
            vc[caracteristica] += 1
    return vc


def test():
    # Cargar telefonos bloqueados (automatico)
    n = validar_mayor_que(0, "Ingrese la cantidad de números en el listado de bloqueados: ")
    bloqueados = generar_telefonos(n)
    selection_sort(bloqueados)

    # Cargar telefonos para paquetes
    n = validar_mayor_que(0, "Ingrese la cantidad de números en el listado a procesar: ")
    telefonos = generar_telefonos(n)
    selection_sort(telefonos)

    # Calcular porcentaje
    cantidad = validar_numeros(telefonos, bloqueados)
    porc = porcentaje(cantidad, len(telefonos))
    print("El porcentaje de nros que no tendrán paquete por encontrarse bloqueados es:", str(porc), "%")

    # Cantidad de paquetes por característica
    cantidad = cantidad_por_caracteristica(telefonos, bloqueados)
    for i in range(len(cantidad)):
        print("La cantidad de nros para la característica", str(i+1), "fue:", str(cantidad[i]))


if __name__ == "__main__":
    test()
