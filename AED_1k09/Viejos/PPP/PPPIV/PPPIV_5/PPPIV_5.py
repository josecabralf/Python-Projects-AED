"""
5. Colegio Profesiones (Tipo Parcial 4)
Un colegio o asociación de profesionales mantiene información sobre sus distintos miembros. Por cada miembro se
registran los campos siguientes: número de dni del profesional (un número entero), nombre del profesional (una cadena),
importe que paga al colegio por mes, tipo de afiliación (un valor entre 0 y 4 incluidos, por ejemplo de la forma 0:
vitalicio, 1: transitorio, 2: indirecto, etc.) y un número que identifica el tipo de trabajo que desempeña (un número
entero entre 0 y 14 incluidos, para indicar (por ejemplo): 0: empleado, 1: jefe o director, 2: administrativo, etc.) Se
pide definir un tipo registro Profesional con los campos que se indicaron, y un programa completo con menú de opciones
para hacer lo siguiente:

1- Cargar los datos de n registros de tipo Profesional en un arreglo de registros (cargue n por teclado). Puede cargar
los datos manualmente, o puede generarlos aleatoriamente. El arreglo debe crearse de forma que siempre quede ordenado
de menor a mayor, según el dni de los profesionales. Se considerará incorrecta la solución basada en cargar el arreglo
completo y ordenarlo al final.

2- Mostrar el arreglo creado en el punto 1, a razón de un registro por línea.

3- Buscar en el arreglo creado en el punto 1 un profesional con dni igual a un valor doc (doc es cargado por teclado).
Si no existe, informar con un mensaje. Si existe mostrar todos sus datos, al final agregar un mensaje que indique que
tiene el importe desactualizado, si es menor a un valor imp (tambien cargado por teclado)

4- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todos los profesionales cuyo
tipo de trabajo sea 3, 4 o 5 y cuyo importe pagado mensual sea mayor a un valor x que se carga por teclado.

5- Mostrar el archivo creado en el punto 3, a razón de un registro por línea en la pantalla.

6- Buscar en el arreglo creado en el punto 1 un registro en el cual el nombre del profesional sea igual a nom (cargar
nom por teclado). Si existe, mostrar por pantalla todos los datos de ese registro. Si no existe, informar con un
mensaje. La búsqueda debe detenerse al encontrar el primer registro que coincida con el patrón pedido.

7- Usando el arreglo creado en el punto 1, determine la cantidad de profesionales de cada posible tipo d afiliación por
cada posible tipo de trabajo (o sea, 5 * 15 = 75 contadores en una matriz de conteo). Muestre sólo los resultados que
sean diferentes de 0.
"""
import pickle
import random
import os
import profesionales


def menu():
    cad = "\nMENÚ DE OPCIONES:\n" \
          "1. Crear arreglo\n" \
          "2. Mostrar arreglo\n" \
          "3. Buscar dni\n" \
          "4. Crear Archivo\n" \
          "5. Mostrar archivo\n" \
          "6. Buscar profesional por nombre y mostrarlo\n" \
          "7. Cantidad de profesionales de cada afiliacion por cada tipo de trabajo\n" \
          "8. Salir\n" \
          "Opción: "
    return cad


def validar_entre(inf, sup, mensaje):
    valor = int(input(mensaje))
    while valor < inf or valor > sup:
        print('Valor Invalido!!')
        valor = int(input(mensaje))
    return valor


def add_in_order(v, prof):
    """
    Agregar elemento en orden, binario
    :param v: Vector al que se agrega
    :param prof: Elemento agregado
    :return: -
    """
    izq, der = 0, len(v) - 1
    pos = 0

    while izq <= der:
        med = (izq + der) // 2
        if v[med].dni == prof.dni:
            pos = med
            break
        if prof.dni < v[med].dni:
            der = med - 1
        else:
            izq = med + 1
    if izq > der:
        pos = izq

    v[pos:pos] = [prof]


def gen_profesionales(n):
    v = []
    tit = ["Sr", "Sra"]
    for i in range(n):
        dni = random.randint(10000000, 99999999)
        nom = random.choice(tit) + " " + random.choice("QWERTYUIOPASDFGHJKLZXCVBNM")
        imp = random.randint(100, 5000)
        af = random.randint(0, 4)
        tr = random.randint(0, 14)
        prof = profesionales.Profesional(dni, nom, imp, af, tr)
        add_in_order(v, prof)
    return v


def mostrar(v):
    for prof in v:
        print(profesionales.to_string(prof))


def buscar_dni(v, dni):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if dni == v[c].dni:
            return c
        if dni < v[c].dni:
            der = c - 1
        else:
            izq = c + 1
    return -1


def validar_prof(prof, x):
    val = False
    if prof.importe > x and (prof.trabajo == 3 or prof.trabajo == 4 or prof.trabajo == 5):
        val = True
    return val


def crear_archivo(v, fd, x):
    m = open(fd, "wb")
    for i in range(len(v)):
        if validar_prof(v[i], x):
            pickle.dump(v[i], m)
            m.flush()
    m.close()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("No existe el archivo!")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)

    while m.tell() < tam:
        prof = pickle.load(m)
        print(profesionales.to_string(prof))
    m.close()


def buscar_nom(v, nom):
    pos = -1
    for i in range(len(v)):
        if nom == v[i].nombre:
            pos = i
            return pos
    return pos


def generar_matriz(v, filas, columnas):
    mat = [[0] * columnas for i in range(filas)]
    for prof in v:
        f = prof.afiliacion
        c = prof.trabajo
        mat[f][c] += 1
    return mat


def mostrar_matriz(mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if mat[f][c] > 0:
                print("Para el tipo de afiliación {} y el tipo de trabajo {} hay {} profesionales"
                      .format(f, c, mat[f][c]))


def test():
    op = -1
    v = []
    existe_v = False
    fd = "Profesionales.dat"

    while op != 8:
        op = validar_entre(1, 8, menu())

        if op == 1:
            n = int(input("\nIngrese el nro de profesionales a generar: "))
            v = gen_profesionales(n)
            existe_v = True
        elif op == 2:
            if existe_v:
                print("\nProfesionales:\n")
                mostrar(v)
            else:
                print("\nNo existe arreglo. Creelo con la opción 1!\n")
        elif op == 3:
            if existe_v:
                doc = int(input("\nIngrese el dni a buscar: "))
                imp = int(input("Ingrese el importe: "))
                pos = buscar_dni(v, doc)
                if pos != -1:
                    print("\nProfesional encontrado!")
                    print(profesionales.to_string(v[pos]))
                    if v[pos].importe < imp:
                        print("Tiene el importe desactualizado!\n")
                else:
                    print("\nNo se ha hallado profesional con ese documento!\n")
            else:
                print("\nNo existe arreglo. Creelo con la opción 1!\n")
        elif op == 4:
            x = int(input("Ingrese el importe mínimo: "))
            crear_archivo(v, fd, x)
            print("\nArchivo creado!\n")
        elif op == 5:
            print("\nProfesionales:\n")
            mostrar_archivo(fd)
        elif op == 6:
            if existe_v:
                nom = str(input("\nIngrese el nombre a buscar: "))
                pos = buscar_nom(v, nom)
                if pos != -1:
                    print("\nProfesional encontrado!")
                    print(profesionales.to_string(v[pos]))
                else:
                    print("\nNo se ha hallado profesional con ese nombre!\n")
            else:
                print("\nNo existe arreglo. Creelo con la opción 1!\n")
        elif op == 7:
            if existe_v:
                mat = generar_matriz(v, 5, 15)
                print("\nResultados:\n")
                mostrar_matriz(mat)
            else:
                print("\nNo existe arreglo. Creelo con la opción 1!\n")

    print("Fin del Programa!")


if __name__ == "__main__":
    test()
