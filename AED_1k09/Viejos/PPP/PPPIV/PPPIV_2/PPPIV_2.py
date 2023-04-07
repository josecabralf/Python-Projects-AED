"""
Una empresa dedicada al alquiler de cabañas de veraneo desea almacenar la información referida a los n alquileres de la
temporada estival en un arreglo de registros (cargar n por teclado).

Por cada alquiler, se pide guardar el DNI de la persona que hizo la reserva, monto del alquiler y un código entre 0 y 9
que indica el tipo de cabaña alquilada.

Se pide desarrollar un programa en Python que permita:

Cargar el arreglo pedido (validar tipo de cabaña).
Trasladar a un archivo los alquileres que registraron un monto mayor a x, siendo x un valor pasado por parámetro.
Usando los datos del archivo, determinar y mostrar el monto total recaudado por cada tipo de cabaña posible.
"""
from cabaña import *
import random
import pickle
import os.path


def add_in_order(v, cab):
    """
    Agregar elemento en orden, binario
    :param v: Vector al que se agrega
    :param cab: Elemento agregado
    :return: -
    """
    izq, der = 0, len(v) - 1
    pos = 0

    while izq <= der:
        med = (izq + der) // 2
        if v[med].documento == cab.documento:
            pos = med
            break
        if cab.documento < v[med].documento:
            der = med - 1
        else:
            izq = med + 1
    if izq > der:
        pos = izq

    v[pos:pos] = [cab]


def generar_vector(n):
    v = []
    for pos in range(n):
        doc = random.randint(1000000, 50000000)
        monto = random.uniform(1000, 7500)
        tipo = random.randrange(10)
        cab = Cabaña(doc, monto, tipo)
        add_in_order(v, cab)

    return v


def generar_archivo(vector, monto, archivo):
    arch = open(archivo, 'wb')
    for cab in vector:
        if cab.monto > monto:
            pickle.dump(cab, arch)
    arch.flush()
    arch.close()


def leer_archivo(archivo):
    size = os.path.getsize(archivo)
    if size < 0:
        return None

    arch = open(archivo, 'rb')
    vc = [0] * 10
    while arch.tell() < size:
        cab = pickle.load(arch)
        vc[cab.tipo] += cab.monto
    arch.close()
    return vc


def principal():
    menu = 'Menu de Opciones \n' \
           '===================================== \n' \
           '1 - Cargar Arreglo de Reservas \n' \
           '2 - Grabar Archivo por Monto \n' \
           '3 - Mostrar Archivo \n' \
           '4 - Salir\n' \
           'Ingrese la opcion: '

    nombre_archivo = 'reservas.dat'
    opcion = 0
    vector = []

    while opcion != 4:
        opcion = int(input(menu))

        if opcion == 1:
            n = int(input('Ingrese la cantidad de elementos a generar: '))
            vector = generar_vector(n)

        elif opcion == 2:
            monto = float(input('Ingrese el monto minimo para guardar: '))
            generar_archivo(vector, monto, nombre_archivo)

        elif opcion == 3:
            listado = leer_archivo(nombre_archivo)
            if not listado is None:
                for i in range(len(listado)):
                    print('Tipo de Cabaña ', i, 'recaudo $', listado[i])
            else:
                print('El Archivo no tiene Registros')

principal()
