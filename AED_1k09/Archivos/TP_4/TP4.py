"""
1- Cargar: Cargar el contenido del archivo en un vector de registros de libros, que siempre debe mantenerse ordenado por
isbn (Omitir la primera línea del archivo, que contiene el nombre de los campos)

2- Sumar revisión: El usuario puede optar por buscar el libro por ISBN o por título. Según el criterio elegido se debe
ingresar por teclado el ítem a buscar. Si existe en el vector el libro con el criterio buscado,  mostrar sus datos y
sumar una revisión al mismo. Si no existe mostrar un mensaje por pantalla.

3- Mayor revisiones: Buscar en el vector el libro con mayor cantidad de revisiones. Informar si su rating es mayor,
menor o igual al rating promedio de su mismo idioma.

4- Popularidad 2000: A partir del vector, generar una matriz donde cada fila sea un idioma y cada columna un año de
publicación. La celda debe contener el libro que tenga mayor rating para ese idioma y año (si hubiera varios, elegir
sólo uno) sólo para los libros publicados entre el año 2000 y el 2020 (ambos incluídos).

5- Publicaciones por década: A partir del vector, generar un vector de conteo donde cada celda representa una década
entre 1900 y 2000. La celda debe indicar cuántos libros se publicaron en esa década. Mostrar todas las cantidades
mayores a cero. Informar además cuál fue la década con más publicaciones. Si varias tuvieran la misma cantidad,
informar todas.

6- Guardar populares: Si la matriz de la opción 4 ya fue generada, almacenar su contenido registros por registro
(omitiendo las celdas vacías) en un archivo binario llamado populares.dat e informar la cantidad de registros grabados.
Si la matriz aún no fue generada, informarlo.

7- Mostrar archivo: Listar el contenido del archivo generado en el punto anterior.
"""
import pickle
import os
import registro


def menu():
    cad = "MENÚ DE OPCIONES:\n" \
          "1. Cargar\n" \
          "2. Sumar Revisión\n" \
          "3. Mayor revisiones\n" \
          "4. Popularidad 2000\n" \
          "5. Publicaciones por década\n" \
          "6. Guardar populares\n" \
          "7. Mostrar archivo\n" \
          "8. Salir\n" \
          "Opción: "
    return cad


def menu_busqueda():
    cad = "\nDesea buscar el libro según:\n" \
          "1. Título\n" \
          "2. ISBN\n" \
          "Opción: "
    return cad


def validar_entre(inf, sup, mensaje):
    """
    Esta función valida que un valor númerico entero ingresado por teclado se encuentre entre un límite inferior y uno
    superior.
    :param inf: Límite inferior
    :param sup: Límite superior
    :param mensaje: Mensaje mostrado indicando qué se debe ingresar por teclado
    :return: Valor ingresado por teclado
    """
    valor = int(input(mensaje))
    while valor < inf or valor > sup:
        print('Valor Invalido!!')
        valor = int(input(mensaje))
    return valor


def add_in_order(v, libro):
    """
    Agregar libro a un vector en orden según ISBN a partir del algoritmo de búsqueda binaria
    :param v: Vector al que se agrega el libro
    :param libro: Elemento agregado
    :return: -
    """
    izq, der = 0, len(v) - 1
    pos = 0

    while izq <= der:
        med = (izq + der) // 2
        if v[med].isbn == libro.isbn:
            pos = med
            break
        if libro.isbn < v[med].isbn:
            der = med - 1
        else:
            izq = med + 1
    if izq > der:
        pos = izq

    v[pos:pos] = [libro]


def cargar_archivo(fd):
    """
    Esta función permite generar un arreglo de registros de tipo libro, a partir de un archivo de texto con codificación
    utf8.
    :param fd: dirección del archivo
    :return: arreglo con registros de tipo libro
    """
    v = []
    m = open(fd, "rt", encoding="utf8")
    m.readline()
    for linea in m:
        cadenas = linea.split(',')
        tit = cadenas[0]
        rev = int(cadenas[1])
        year = int(cadenas[2])
        idi = int(cadenas[3])
        rat = float(cadenas[4])
        # Eliminar salto de linea con .rstrip()
        isbn = cadenas[5].rstrip()
        lib = registro.Libro(tit, rev, year, idi, rat, isbn)
        add_in_order(v, lib)
    return v


def busqueda_titulo(v, x):
    """
    Esta función sirve para buscar un libro según su título en un arreglo con registros de tipo libro, a partir del
    algoritmo de búsqueda secuencial.
    :param v: arreglo con registros de tipo libro
    :param x: título del libro buscado
    :return: posición del libro en el arreglo, -1 en caso de no encontrarlo
    """
    pos = -1
    for i in range(len(v)):
        if x == v[i].titulo:
            pos = i
            return pos
    return pos


def busqueda_isbn(v, x):
    """
    Esta función sirve para buscar un libro según su código ISBN en un arreglo con registros de tipo libro, a partir
    del algoritmo de búsqueda binaria.
    :param v: arreglo con registros de tipo libro
    :param x: código ISBN del libro buscado
    :return: posición del libro en el arreglo, -1 en caso de no encontrarlo
    """
    izq, der = 0, len(v) - 1
    pos = -1

    while izq <= der:
        med = (izq + der) // 2
        if v[med].isbn == x:
            pos = med
            return pos
        if x < v[med].isbn:
            der = med - 1
        else:
            izq = med + 1

    return pos


def promedio(acu, cont):
    """
    Esta función sirve para calcular promedio
    :param acu: acumulador, suma de las cantidades a promediar
    :param cont: contador, número de sumandos
    :return: promedio
    """
    prom = 0
    # Evitar n/0
    if cont > 0:
        prom = round(acu / cont, 2)
    return prom


def may_men_ig(x, y):
    """
    Esta función compara dos magnitudes rating (x e y), siendo rating un campo de un registro de tipo libro, y define
    si x es mayor, menor o igual a y
    :param x: Magnitud 1
    :param y: Magnitud 2
    :return: String con la palabra "Mayor" si x > y, "Menor" si x < y, o "Igual" si x = y
    """
    if x.rating > y[x.idioma - 1]:
        return "Mayor"
    elif x.rating < y[x.idioma - 1]:
        return "Menor"
    else:
        return "Igual"


# Se decidió no modularizar para evitar recorrer el arreglo 2 veces (1 para buscar may, otra para el rating promedio)
# Así se recorre el arreglo una sola vez y se tiene ambos resultados, ahorrando tiempo y procesamiento
def opcion3(v):
    """
    Esta función lleva a cabo la opción 3 del menú de opciones. Recorre el arreglo secuencialmente para encontrar
    el libro con mayor cantidad de revisiones y para calcular el rating promedio de cada idioma. Tras esto, compara
    el rating del libro con mayor número de revisiones con el promedio de su idioma e informa si este primero es
    mayor, menor o igual al promedio.
    :param v: arreglo con registros de tipo libro
    :return: -
    """
    cont = [0]*27
    acu = [0]*27
    proms = [0]*27
    may = None

    for i in range(1, len(v)):

        cont[v[i].idioma - 1] += 1
        acu[v[i].idioma - 1] += v[i].rating

        if may is None:
            may = v[i]
        elif v[i].revisiones > may.revisiones:
            may = v[i]

    for i in range(len(proms)):
        proms[i] = promedio(acu[i], cont[i])

    print("\nEl libro con más revisiones fue: ")
    print(registro.to_string(may))
    print("Rating promedio del idioma {}: {}\n".format(may.idioma, proms[may.idioma-1]))
    print("Su rating comparado al promedio de su idioma fue: " + may_men_ig(may, proms) + "\n")


def generar_matriz(v, filas, columnas):
    """
    Esta función genera una matriz que almacena registros de tipo libros, cuyo rating sea el mayor entre los libros
    de un idioma y año de publicación (entre 2000 y 2020) determinados.
    :param v: arreglo con registros de tipo libro
    :param filas: cantidad de filas que debe tener la matriz
    :param columnas: cantidad de columnas que debe tener la matriz
    :return: matriz
    """
    mat = [[0] * columnas for i in range(filas)]
    for lib in v:
        if 2000 <= lib.year <= 2020:
            f = lib.idioma - 1
            c = lib.year - 2000
            if mat[f][c] == 0:
                mat[f][c] = lib
            elif mat[f][c].rating < lib.rating:
                mat[f][c] = lib
    return mat


def generar_archivo(mat, fd_b):
    """
    Esta función crea un archivo binario a partir de una matriz que contiene registros de tipo libro.
    :param mat: matriz con registros de tipo libro
    :param fd_b: nombre deseado para el archivo
    :return: -
    """
    m = open(fd_b, "wb")
    cont = 0
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if mat[f][c] != 0:
                pickle.dump(mat[f][c], m)
                cont += 1
                m.flush()
    print("\nArchivo creado! Se grabaron {} libros\n".format(cont))
    m.close()


def mostrar_archivo(fd):
    """
    Esta función muestra los datos de un archivo binario que contiene registros de tipo libro.
    :param fd: dirección del archivo
    :return: -
    """
    if not os.path.exists(fd):
        print("No existe el archivo!")
        return

    m = open(fd, "rb")
    tam = os.path.getsize(fd)
    while m.tell() < tam:
        lib = pickle.load(m)
        print(registro.to_string(lib))
    m.close()


def publicaciones_dec(v):
    """
    Genera un vector contador que almacena la cantidad de libros publicados en cada una de las décadas entre los años
    1900 y 2000
    :param v: arreglo con registros de tipo libro
    :return:vector contador
    """
    vd = [0]*10
    for lib in v:
        if 1900 <= lib.year < 2000:
            vd[(lib.year - 1900) // 10] += 1
    return vd


def mostrar_vc_publicados(vc):
    """
    Esta función muestra la cantidades almacenadas en un vector de conteo de libros publicados en cada decada entre
    el año 1900 y el 2000
    :param vc: vector de conteo con la cantidad de libros publicados en cada decada entre el año 1900 y el 2000
    :return: -
    """
    for i in range(len(vc)):
        # Mostrar solo los != 0
        if vc[i] != 0:
            print("El nro. de libros publicados en la decada de {} fue {}".format((i*10 + 1900), vc[i]))


def buscar_mayor_vc(vc):
    """
    Esta función busca la/s mayores cantidades dentro de un vector, y almacena sus posiciones dentro de dicho vector
    en un arreglo may
    :param vc: vector con cantidades
    :return: posiciones de las mayores cantidades
    """
    may = [0]
    for i in range(1, len(vc)):
        if vc[i] > may[0]:
            may = [i]
        elif vc[i] == may[0]:
            may.append(i)
    return may


def test():
    """
    Esta función lleva a cabo el programa manejado por menú de opciones propuesto por el enunciado
    :return:
    """
    op = -1
    fd = "libros.csv"
    fd_b = "populares.dat"
    exist_v = False
    exist_mat = False
    v = []
    mat = []

    while op != 8:
        op = validar_entre(1, 8, menu())

        if op == 1:
            v = cargar_archivo(fd)
            exist_v = True
            print("\nArreglo Cargado!\n")
        elif op == 2:
            if exist_v:
                op = validar_entre(1, 2, menu_busqueda())
                if op == 1:
                    # Busqueda por título
                    x = str(input("\nIngrese el título del libro a buscar: "))
                    pos = busqueda_titulo(v, x)
                    if pos != -1:
                        # Mostrar libro
                        print("Se ha encontrado el libro buscado: Se le ha sumado una revisión")
                        v[pos].revisiones += 1
                        print(registro.to_string(v[pos]))
                        print()
                    else:
                        print("No se ha encontrado el libro buscado")
                else:
                    # Busqueda por ISBN
                    x = str(input("\nIngrese el ISBN del libro a buscar: "))
                    pos = busqueda_isbn(v, x)
                    if pos != -1:
                        # Mostrar libro
                        print("Se ha encontrado el libro buscado: Se le ha sumado una revisión")
                        v[pos].revisiones += 1
                        print(registro.to_string(v[pos]))
                        print()
                    else:
                        print("No se ha encontrado el libro buscado\n")
            else:
                print("\nERROR... No existe arreglo! Pruebe cargarlo con la opción 1\n")
        elif op == 3:
            if exist_v:
                opcion3(v)
            else:
                print("\nERROR... No existe arreglo! Pruebe cargarlo con la opción 1\n")
        elif op == 4:
            if exist_v:
                mat = generar_matriz(v, 27, 21)
                print("\nMatriz Generada!\n")
                exist_mat = True
            else:
                print("\nERROR... No existe arreglo! Pruebe cargarlo con la opción 1\n")
        elif op == 5:
            if exist_v:
                print("\nPublicaciones por década:\n")
                vc_dec = publicaciones_dec(v)
                mostrar_vc_publicados(vc_dec)
                x = buscar_mayor_vc(vc_dec)
                print("\nLa/s decadas con más publicaciones fueron: ")
                for dec in x:
                    print("Decada del {}\n".format(dec*10 + 1900))
            else:
                print("\nERROR... No existe arreglo! Pruebe cargarlo con la opción 1\n")
        elif op == 6:
            if exist_mat:
                generar_archivo(mat, fd_b)
            else:
                print("\nERROR... No existe matriz! Pruebe crearla con la opción 4\n")
        elif op == 7:
            print("\nLibros:")
            mostrar_archivo(fd_b)
            print()


if __name__ == "__main__":
    test()
