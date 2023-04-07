"""
4. Productora (Tipo Parcial 4)
Una empresa de producciones cinematográficas mantiene información sobre las distintas películas que tiene en desarrollo.
Por cada película se registran los datos siguientes: número de identificación de la película (un número entero), título
(una cadena), importe invertido en su producción, tipo de película (un valor entre 0 y 9 incluidos, de la forma 0:
acción, 1: comedia, 2: drama, etc.) y un número para identificar el pais de origen de la película (un número entero
entre 0 y 19 incluidos) Se pide definir un tipo registro Pelicula con los campos que se indicaron, y un programa
completo con menú de opciones para hacer lo siguiente:

1- Cargar los datos de n registros de tipo Pelicula en un arreglo de registros (cargue n por teclado). Puede cargar los
datos manualmente, o puede generarlos aleatoriamente. El arreglo debe crearse de forma que siempre quede ordenado de
menor a mayor, según el título de las películas.

2- Mostrar el arreglo creado en el punto 1, a razón de un registro por línea.

3 - Buscar en el arreglo creado en el punto 1 un registro en el cual el titulo de la pelicula sea igual a nom (cargar
nom por teclado). Si existe, mostrar por pantalla los datos, previamente modicar el importe con un valor imp (cargar
imp por teclado). Si no existe, informar con un mensaje. La busqueda debe detenerse al encontrar el primer registro que
coincida con el titulo

4- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todas las películas cuyo pais
de origen no sea el 10 y cuyo importe invertido sea menor a un valor x que se carga por teclado.

5- Mostrar el archivo creado en el punto 3, a razón de un registro por línea en la pantalla.

6- Buscar en el arreglo creado en el punto 1 un registro en el cual el número de identificación de la película sea igual
a num (cargar num por teclado). Si existe, mostrar por pantalla todos los datos de ese registro. Si no existe, informar
con un mensaje. La búsqueda debe detenerse al encontrar el primer registro que coincida con el patrón pedido.

7- Usando el arreglo creado en el punto 1, determine la cantidad de películas de cada posible tipo por cada posible pais
 de origen (o sea, 10 * 20 = 200 contadores en una matriz de conteo). Muestre sólo los resultados que sean diferentes de
  0.
"""
import pickle
import random
import pelicula
import os


def menu():
    cad = "\nMENÚ DE OPCIONES:\n" \
          "1. Crear arreglo\n" \
          "2. Mostrar arreglo\n" \
          "3. Buscar nom y cambiar imp\n" \
          "4. Crear Archivo\n" \
          "5. Mostrar archivo\n" \
          "6. Buscar num y mostrarlo\n" \
          "7. Cantidad de peliculas de cada tipo por cada país\n" \
          "8. Salir\n" \
          "Opción: "
    return cad


def validar_entre(inf, sup, mensaje):
    valor = int(input(mensaje))
    while valor < inf or valor > sup:
        print('Valor Invalido!!')
        valor = int(input(mensaje))
    return valor


def add_in_order(v, pel):
    """
    Agregar elemento en orden, binario
    :param v: Vector al que se agrega
    :param pel: Elemento agregado
    :return: -
    """
    izq, der = 0, len(v) - 1
    pos = 0

    while izq <= der:
        med = (izq + der) // 2
        if v[med].titulo == pel.titulo:
            pos = med
            break
        if pel.titulo < v[med].titulo:
            der = med - 1
        else:
            izq = med + 1
    if izq > der:
        pos = izq

    v[pos:pos] = [pel]


def auto_gen_pelicula(n):
    v = []

    for i in range(n):
        ide = random.randint(10000, 99999)
        tit = random.choice("QWERTYUIOPASDFGHJKLZXCVBNM") + random.choice("qwertyuiopasdfghjklzcxvbnm")
        imp = random.randint(10000, 50000)
        tip = random.randint(0, 9)
        pais = random.randint(0, 19)
        peli = pelicula.Pelicula(ide, tit, imp, tip, pais)
        add_in_order(v, peli)

    print("Arreglo generado!")
    print()

    return v


def write(v):
    for i in range(len(v)):
        print(pelicula.to_string(v[i]))


def buscar_tit(v, nom):
    izq, der = 0, len(v) - 1
    while izq <= der:
        med = (izq + der) // 2
        if nom == v[med].titulo:
            return med
        if nom < v[med].titulo:
            der = med - 1
        else:
            izq = med + 1

    return -1


def validar_pelicula(pel, x):
    val = False
    if pel.pais != 10 and pel.importe_p < x:
        val = True
    return val


def crear_archivo(v, fd):
    x = int(input("Ingrese el importe máximo: "))

    m = open(fd, "wb")
    for i in range(len(v)):
        if validar_pelicula(v[i], x):
            pickle.dump(v[i], m)
            m.flush()
    m.close()

    print("Archivo creado!")
    print()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("No existe el archivo!")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    while m.tell() < tam:
        pel = pickle.load(m)
        print(pelicula.to_string(pel))
    m.close()


def buscar_id(v, num):
    pos = -1

    for i in range(len(v)):
        if num == v[i].identificacion:
            pos = i
            return pos

    return pos


def generar_mat(v):
    mat = [[0]*20 for i in range(10)]
    for i in range(len(v)):
        f = v[i].tipo
        c = v[i].pais
        mat[f][c] += 1
    return mat


def mostrar_matriz(mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if mat[f][c] > 0:
                print("Para el tipo de pelicula {} y el país {} hay {} peliculas".format(f, c, mat[f][c]))


def test():
    op = -1
    v = []
    fd = "Peliculas.dat"
    exist_v = False

    while op != 8:
        op = validar_entre(0, 8, menu())

        if op == 1:
            n = int(input("\nIngrese el nro de peliculas a generar: "))
            v = auto_gen_pelicula(n)
            exist_v = True
        elif op == 2:
            if exist_v:
                write(v)
            else:
                print("\nNo existe arreglo. Creelo con la opción 1!\n")
        elif op == 3:
            if exist_v:
                nom = input("\nIngrese el titulo de la película a buscar: ")
                pos = buscar_tit(v, nom)
                if pos != -1:
                    v[pos].importe_p = int(input("Ingrese el nuevo importe: "))
                else:
                    print("\nNo se encontró la pelicula buscada!\n")
            else:
                print("\nNo existe arreglo. Creelo con la opción 1!\n")
        elif op == 4:
            if exist_v:
                crear_archivo(v, fd)
            else:
                print("\nNo existe arreglo. Creelo con la opción 1!\n")
        elif op == 5:
            mostrar_archivo(fd)
        elif op == 6:
            if exist_v:
                num = int(input("\nIngrese el nro. de identificación de la película buscada: "))
                pos = buscar_id(v, num)
                if pos != -1:
                    print("Datos de la película buscada:")
                    print(pelicula.to_string(v[pos]))
                else:
                    print("\nNo se encontró la pelicula buscada!\n")
            else:
                print("\nNo existe arreglo. Creelo con la opción 1!\n")
        elif op == 7:
            if exist_v:
                mat = generar_mat(v)
                mostrar_matriz(mat)
            else:
                print("\nNo existe arreglo. Creelo con la opción 1!\n")

    print("Hasta luego!")


if __name__ == "__main__":
    test()
