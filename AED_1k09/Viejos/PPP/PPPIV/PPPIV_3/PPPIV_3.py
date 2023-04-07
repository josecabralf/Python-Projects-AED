"""
Desarrollar un programa controlado por menu de opciones, que permita gestionar un arreglo de registro de tipo libro
(ISBN, título, y autor) con las siguientes opciones:

a.) Crear y cargar un arreglo v de n registros de tipo Libro.

b.) Mostrar el arreglo.

c.) Crear un archivo libros.dat que contenga todos los registros del arreglo v. Si el archivo ya existía, eliminar su
contenido y comenzar desde cero.

d.) Mostrar el contenido del archivo libros.dat.

e.) Crear nuevamente el archivo libros.dat, de forma que ahora contenga sólo los datos de los libros cuyo código sea
menor que x, cargando el código x por teclado. Si el archivo ya existía, eliminar su contenido y comenzar desde cero.

f.) A partir del archivo libros.dat, volver a crear en memoria el arreglo v, de forma que contenga todos los registros
del archivo. Reemplace el arreglo creado en el punto a.) por el que se le pide crear ahora.

g.) A partir del archivo libros.dat, volver a crear en memoria el arreglo v, que contenga sólo los registros de los
libros cuyo código sea mayor a x (cargue x por teclado). Reemplace el arreglo creado en el punto a.) por el que se le
pide crear ahora.
"""
import Libro
import random
import pickle
import os


def menu():
    cad = "\nMENÚ DE OPCIONES:\n" \
          "1. Crear arreglo\n" \
          "2. Mostrar arreglo\n" \
          "3. Crear archivo completo\n" \
          "4. Mostrar archivo\n" \
          "5. Crear archivo: código menor x\n" \
          "6. Crear arreglo a partir de archivo completo\n" \
          "7. Crear arreglo a partir de archivo: código mayor a x\n" \
          "8. Salir\n" \
          "Opción: "
    return cad


def add_in_order(v, lib):
    """
    Agregar elemento en orden, binario
    :param v: Vector al que se agrega
    :param lib: Elemento agregado
    :return: -
    """
    izq, der = 0, len(v) - 1
    pos = 0

    while izq <= der:
        med = (izq + der) // 2
        if v[med].codigo == lib.codigo:
            pos = med
            break
        if lib.codigo < v[med].codigo:
            der = med - 1
        else:
            izq = med + 1
    if izq > der:
        pos = izq

    v[pos:pos] = [lib]


def gen_automatica():
    n = int(input("Ingrese el nro de libros que quiere generar: "))
    v = []
    for i in range(n):
        cod = random.randint(0, 9999)
        tit = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + random.choice("abcdefghijklmnopqrstuvwxyz")
        aut = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        lib = Libro.Libro(tit, cod, aut)
        add_in_order(v, lib)

    return v


def mostrar_arreglo(v):
    for i in range(len(v)):
        print(Libro.to_string(v[i]))


def crear_archivo(v):
    archivo = open("Libros.dat", "wb")
    for i in range(len(v)):
        pickle.dump(v[i], archivo)
        archivo.flush()
    archivo.close()


def mostrar_archivo():
    if not os.path.exists("Libros.dat"):
        print("No existe el archivo")
        return

    tam = os.path.getsize("Libros.dat")
    archivo = open("Libros.dat", "rb")

    while archivo.tell() < tam:
        libro = pickle.load(archivo)
        print(Libro.to_string(libro))

    archivo.close()


def crear_archivo_menor_x(v):
    x = int(input("Ingrese el valor de x: "))
    archivo = open("Libros.dat", "wb")
    for i in range(len(v)):
        if v[i].codigo < x:
            pickle.dump(v[i], archivo)
    archivo.flush()
    archivo.close()


def arreglo_archivo():
    if not os.path.exists("Libros.dat"):
        print("No existe el archivo")
        return

    v = []
    tam = os.path.getsize("Libros.dat")

    archivo = open("Libros.dat", "rb")

    while archivo.tell() < tam:
        libro = pickle.load(archivo)
        v.append(libro)
    return v


def arreglo_archivo_mayor_x():
    if not os.path.exists("Libros.dat"):
        print("No existe el archivo")
        return

    x = int(input("Ingrese el valor de x: "))
    v = []

    tam = os.path.getsize("Libros.dat")
    archivo = open("Libros.dat", "rb")

    while archivo.tell() < tam:
        libro = pickle.load(archivo)
        if libro.codigo > x:
            v.append(libro)

    return v


def test():
    op = -1
    v1 = []
    while op != 8:
        op = int(input(menu()))
        if op == 1:
            v1 = gen_automatica()
        elif op == 2:
            mostrar_arreglo(v1)
        elif op == 3:
            crear_archivo(v1)
        elif op == 4:
            mostrar_archivo()
        elif op == 5:
            crear_archivo_menor_x(v1)
        elif op == 6:
            v1 = arreglo_archivo()
        elif op == 7:
            v1 = arreglo_archivo_mayor_x()


if __name__ == "__main__":
    test()
