"""
Una agencia de empleo desea un programa para procesar los datos de los empleos que tiene disponobles. Para cada empleo
se registran los siguientes datos: número de identificación del empleo (un entero), descripción del empleo (una cadena),
monto a pagar por ese empleo, ciudad en que se ofrece (un valor entre 0 y 29 por ejemplo: 0: Córdoba 1: Santa Fe, etc.)
y tipo de empleo (un valor entre 0 y 19 por ejemplo: 0: industrial, 1: doméstico, etc.). Se pide definir un tipo
registro Empleo con los campos que se indicaron, y un programa completo con menú de opciones para hacer lo siguiente:

1- Cargar los datos de n registros de tipo Empleo en un arreglo de registros (cargue n por teclado). Puede cargar los
datos manualmente, o puede generarlos aleatoriamente (pero si hace carga manual, TODA la carga debe ser manual, y si la
hace automática entonces TODA debe ser automática). Valide todos los campos que sean necesarios. El arreglo debe crearse
de forma que siempre quede ordenado de menor a mayor, según el número de identificación de los empleao, y para hacer
esto debe aplicar el algoritmo de inserción ordenada con búsqueda binaria. Se considerará directamente incorrecta la
solución basada en cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero
con búsqueda secuencial.

2- Mostrar el vector completo, a razón de un registro por línea, pero muestre solo los registros cuya ciudad sea un
valor entre 0 y 10, ambos incluidos.

3- Usando el arreglo creado en el punto 1, determine la cantidad de empleos ofrecidos para cada posible ciudad y por
cada posible tipo (o sea, 30 * 20 contadores en una matriz de conteo). Muestre sólo los contadores con valores que
estén comprendido entre un rango de valores a y b (ambos incluidos) (los valores de a y b se cargan por teclado.

4- A partir del arreglo creado en el punto 1, crear un archivo de registros en el cual se copien los datos de todos los
registros cuyo monto a pagar sea mayor a un valor p (ingresado por teclado) pero que no sean de un tipo mayor a 15.

5- Mostrar el archivo creado en el punto 4, a razón de un registro por línea en la pantalla. Muestre al final del
listado una línea adicional indicando la cantidad de registros que se mostraron.
"""
import pickle
import random
import os
import registro


def menu():
    cad = "MENÚ DE OPCIONES:\n" \
          "1. Cargar Datos\n" \
          "2. Mostrar Datos de Ciudades 0-10\n" \
          "3. Empleos por Ciudad y Tipo\n" \
          "4. Crear Archivo con Monto a pagar mayor a p y tipo menor a 15\n" \
          "5. Mostrar archivo\n" \
          "6. Salir\n" \
          "Opción: "
    return cad


def validar_entre(inf, sup, mensaje):
    valor = int(input(mensaje))
    while valor < inf or valor > sup:
        print('Valor Invalido!!')
        valor = int(input(mensaje))
    return valor


def validar_mayor_que(inf, mensaje="Ingrese un nro: "):
    valor = int(input(mensaje))
    while valor <= inf:
        print('¡Valor invalido!')
        valor = int(input(mensaje))
    return valor


def add_in_order(v, emp):
    izq, der = 0, len(v) - 1
    pos = 0
    while izq <= der:
        med = (izq + der) // 2
        if v[med].numero == emp.numero:
            pos = med
            break
        if emp.numero < v[med].numero:
            der = med - 1
        else:
            izq = med + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [emp]


def gen_empleos(n):
    v = []
    for i in range(n):
        nro = random.randint(10000, 99999)
        # Se asume que cada letra tiene un significado
        desc = random.choice("QWERTYUIOPASDFGHJKLZXCVBNM")
        mont = random.randint(1000, 9999)
        city = random.randint(0, 29)
        tipo = random.randint(0, 19)
        emp = registro.Empleo(nro, desc, mont, city, tipo)
        add_in_order(v, emp)
    return v


def validar_ciudad(emp):
    val = False
    if 0 <= emp.ciudad <= 10:
        val = True
    return val


def generar_matriz(v, filas, columnas):
    mat = [[0] * columnas for i in range(filas)]
    for emp in v:
        f = emp.ciudad
        c = emp.tipo
        mat[f][c] += 1
    return mat


def mostrar_mat(mat, a, b):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if a <= mat[f][c] <= b:
                print("Para la ciudad {} y el tipo de empleo {} hay {} empleos"
                      .format(f, c, mat[f][c]))


def crear_archivo(v, fd, p):
    m = open(fd, "wb")
    for emp in v:
        if emp.monto > p and emp.tipo <= 15:
            pickle.dump(emp, m)
            m.flush()
    m.close()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("\nNo existe el archivo! Pruebe crearlo con la opción 4!\n")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)
    cont = 0
    print("\nEmpleos: ")
    while m.tell() < tam:
        emp = pickle.load(m)
        print(registro.to_string(emp))
        cont += 1
    print("Se mostraron {} empleos\n".format(cont))
    m.close()


def test():
    op = -1
    exist_v = False
    v = []
    fd = "Empleos.dat"

    while op != 6:
        op = validar_entre(1, 6, menu())
        if op == 1:
            n = validar_mayor_que(0, "\nIngrese el nro. de empleos a generar:")
            v = gen_empleos(n)
            print("Empleos generados!\n")
            exist_v = True
        elif op == 2:
            if exist_v:
                print("\nEmpleos :")
                for emp in v:
                    if validar_ciudad(emp):
                        print(registro.to_string(emp))
                print()
            else:
                print("\nERROR... No hay empleos para procesar. Agreguelos con la opción 1!\n")
        elif op == 3:
            if exist_v:
                mat = generar_matriz(v, 30, 20)
                a = validar_mayor_que(-1, "\nDetermine el límite inferior: ")
                b = validar_mayor_que(a, "Determine el límite superior: ")
                print("\nEmpleos: ")
                mostrar_mat(mat, a, b)
                print()
            else:
                print("\nERROR... No hay empleos para procesar. Agreguelos con la opción 1!\n")
        elif op == 4:
            if exist_v:
                p = validar_mayor_que(0, "\nDetermine el valor del monto mínimo p: ")
                crear_archivo(v, fd, p)
                print("Archivo creado!\n")
            else:
                print("\nERROR... No hay empleos para procesar. Agreguelos con la opción 1!\n")
        elif op == 5:
            mostrar_archivo(fd)

    print("\nHasta luego!")


if __name__ == "__main__":
    test()
