import libro
import ISBN
import random


def validar_entre(inf, sup, mensaje):
    """
    Esta función valida que un valor númerico ingresado por teclado se encuentre entre un límite inferior y uno
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


def validar_mayor_que(inf, mensaje="Ingrese un nro: "):
    """
    Esta función valida que un valor númerico ingresado por teclado sea mayor que un valor constante
    :param inf: Límite inferior
    :param mensaje: Mensaje mostrado indicando qué se debe ingresar por teclado
    :return: Valor ingresado por teclado
    """
    valor = int(input(mensaje))
    while valor <= inf:
        print('¡Valor invalido!')
        valor = int(input(mensaje))
    return valor


def carga_manual(libros):
    """
    Esta función permite la carga manual del vector con cada uno de los campos que componen a cada uno de sus elementos
    :param libros: Vector a cargar
    :return: Vector con datos cargados manualmente
    """
    print("\nCarga Manual")
    for i in range(len(libros)):
        isbn = ISBN.validar_isbn()
        titulo = input("Ingrese titulo: ")
        genero = validar_entre(0, 9, "Ingrese género (entre 0 y 9): ")
        idioma = validar_entre(1, 5, "Ingrese idioma (entre 1 y 5): ")
        precio = validar_mayor_que(0, "Ingrese el precio:")

        libros[i] = libro.Libro(isbn, titulo, genero, idioma, precio)


def carga_automatica(libros):
    """
    Esta función permite la carga automática del vector con cada uno de los campos que componen a cada uno de sus
    elementos
    :param libros: Vector a cargar
    :return: Vector con datos cargados automáticamente
    """
    for i in range(len(libros)):
        isbn = ISBN.gen_isbn()
        titulo = "Libro " + str(i)
        genero = random.randint(0, 9)
        idioma = random.randint(1, 5)
        precio = random.randint(100, 5000)

        libros[i] = libro.Libro(isbn, titulo, genero, idioma, precio)


def opcion1():
    """
    Esta función realiza la opción 1 del menú de opciones: permite carga manual o automática de los datos a procesar, a
    elección del usuario.
    :return: Vector "libros" cargado
    """
    op = validar_entre(1, 2, "\nIngrese el tipo de carga a realizar: \n1. Manual\n2. Automática\nOpción: ")
    n = validar_mayor_que(0, "Ingrese la cantidad de libros ofrecidos: ")
    libros = [None] * n
    if op == 1:
        carga_manual(libros)
    else:
        carga_automatica(libros)

    return libros


def titulo_sort(v):
    """
    Esta función ordena un arreglo en orden ascendente acorde al campo títulos.
    :param v: Arreglo a ordenar
    :return: Arreglo ordenado
    """
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].titulo < v[j].titulo:
                v[i], v[j] = v[j], v[i]


def opcion2(libros, generos, idiomas):
    """
    Esta función realiza la opción 2 del menú de opciones: primero ordena acorde a los títulos en forma ascendente, y
    posteriormente los muestra reemplazando la numeración de género e idioma, con su genero e idioma correspondiente.
    :param libros: Arreglo a procesar
    :param generos: Arreglo conteniendo los géneros en formato string
    :param idiomas: Arreglo conteniendo los idiomas en formato string
    :return: -
    """
    titulo_sort(libros)
    for i in range(len(libros)):
        r = ""
        r += "{:<25}".format("ISBN: " + libros[i].codigo)
        r += "{:<20}".format("Título: " + libros[i].titulo)
        r += "{:<25}".format("Género: " + generos[libros[i].genero])
        r += "{:<20}".format("Idioma: " + idiomas[libros[i].idioma - 1])
        r += "{:<20}".format("Precio: " + str(libros[i].precio))
        print(r)


def contador_genero(libros):
    """
    Esta función genera un arreglo contador para contar cuantos libros hay de cada genero.
    :param libros: Arreglo conteniendo los libros a procesar
    :return: Arreglo contador
    """
    c = [0] * 10
    for i in range(len(libros)):
        c[libros[i].genero] += 1
    return c


def buscar_mayor(v):
    """
    Esta función recorre un arreglo e identifica el mayor número en el mismo, y devuelve su posición
    :param v: Arreglo a recorrer
    :return: Posición del número mayor
    """
    mayor = 0
    for i in range(1, len(v)):
        if v[i] > v[mayor]:
            mayor = i
    return mayor


def mostrar_generos(generos, c):
    """
    Esta función muestra en pantalla cada género junto a la cantidad de libros que hay del mismo.
    :param generos: Arreglo conteniendo los géneros en formato string
    :param c: Arreglo contador de generos
    :return: -
    """
    for i in range(len(generos)):
        print(generos[i], ":", c[i])


def opcion3(libros, generos):
    """
    Esta función realiza la opción 3 del menú de opciones: primero genera un arreglo contador, luego muestra los géneros
     con sus respectivas cantidades, luego busca el género con mayor cantidad de libros, lo muestra en pantalla y lo devuelve.
    :param libros: Arreglo conteniendo los libros a procesar
    :param generos: Arreglo conteniendo los géneros en formato string
    :return: Genero con mayor cantidad de libros
    """
    c = contador_genero(libros)
    mostrar_generos(generos, c)
    mayor_genero = buscar_mayor(c)

    print("El género con mayor cantidad de libros ofrecidos: ", generos[mayor_genero])
    return mayor_genero


def buscar_mayor_idioma(libros, idioma):
    """
    Esta función busca el libro de  mayor precio para un idioma específico.
    :param libros: Arreglo conteniendo los libros a procesar
    :param idioma: Idioma solicitado para clasificar los libros
    :return: Posición del libro de mayor precio para el idioma solicitado
    """
    mayor = 0
    for i in range(1, len(libros)):
        if libros[i].idioma == idioma:
            if libros[mayor].precio < libros[i].precio:
                mayor = i
    return mayor


def opcion4(libros):
    """
    Esta función realiza la opción 4 del menú de opciones: primero se pide y valida el ingreso de un idioma i, luego se
    busca el libro de mayor precio para ese idioma y finalmente se imprime en pantalla dicho libro con sus datos.
    :param libros: Arreglo conteniendo los libros a procesar
    :return: -
    """
    i = validar_entre(1, 5, "Cargue el idioma deseado (1 a 5): ")
    mayor = buscar_mayor_idioma(libros, i)
    print(libro.to_string(libros[mayor]))


def linear_search_isbn(v, x):
    """
    Esta función busca un ISBN 10 en un arreglo de manera lineal.
    :param v: Arreglo
    :param x: ISBN 10 a buscar
    :return: Posición del primer elemento encontrado o -1 en caso de no encontrarlo
    """
    r = -1
    for i in range(len(v)):
        if x == v[i].codigo:
            r = i
            return r

    return r


def opcion5(libros):
    """
    Esta función realiza la opción 5 del menú de opciones: primero se pide y valida un código ISBN 10 y luego se lo
    busca en el arreglo libros. En caso de existir, se aumenta el precio del libro un 10% y en caso contrario
    se avisa al usuario.
    :param libros: Arreglo conteniendo los libros a procesar
    :return: -
    """
    isbn = ISBN.validar_isbn("Ingrese el código ISBN del libro buscado: ")
    pos = linear_search_isbn(libros, isbn)
    if pos == -1:
        print("El libro buscado no está disponible")
    else:
        print("Libro encontrado...Precio actualizado")
        libros[pos].precio = round(libros[pos].precio * 1.1, 2)

        print(libro.to_string(libros[pos]))


def precio_sort(v):
    """
    Esta función ordena el arreglo acorde al campo precio de mayor a menor.
    :param v: Arreglo a ordenar
    :return: -
    """
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].precio < v[j].precio:
                v[i], v[j] = v[j], v[i]


def opcion6(libros, genero):
    """
    Esta función realiza la opción 6 del menú de opciones: primero ordena los libros por precio de mayor a menor y
    luego imprime aquellos del género más popular
    :param libros: Arreglo conteniendo los libros a procesar
    :param genero: Género más popular
    :return: -
    """
    n = len(libros)

    precio_sort(libros)
    for i in range(n):
        if libros[i].genero == genero:
            print(libro.to_string(libros[i]))


def opcion7(libros):
    """
    Esta función realiza la opción 7 del menú de opciones: primero crea un arreglo con los libros exigidos por un
    estudiante y los busca, almacenandolos en encontrados o no_encontrados para cada caso. Finalmente, muestra los
    libros que están disponibles, los que no y calcula el precio total.
    :param libros: Arreglo conteniendo los libros a procesar
    :return: -
    """
    n = validar_mayor_que(0, "Ingrese la cantidad de libros a buscar: ")
    v = [""] * n
    for i in range(n):
        v[i] = ISBN.validar_isbn("Ingrese el código ISBN del libro " + str(i + 1) + ": ")

    encontrados = []
    no_encontrados = []

    for i in range(n):
        pos = linear_search_isbn(libros, v[i])
        if pos != -1:
            encontrados.append(pos)
        else:
            no_encontrados.append(v[i])

    s = len(encontrados)
    t = len(no_encontrados)
    suma = 0

    if t != 0:
        print("Los siguiente libros no fueron encontrados:")
        for i in range(t):
            print(no_encontrados[i])
    if s != 0:
        print("Los siguiente libros fueron encontrados:")
        for i in range(s):
            print(libros[encontrados[i]].codigo, " | ", libros[encontrados[i]].titulo,
                  " | ", libros[encontrados[i]].precio)
            suma += libros[encontrados[i]].precio
        print("El precio total a pagar: $", str(suma))


def test():
    print("Sistema de Gestión de Libros\n")

    generos = ["Autoayuda", "Arte", "Ficción", "Computación", "Economía", "Escolar", "Sociedad", "Gastronomía",
               "Infantil", "Otros"]
    idiomas = ["Español", "Inglés", "Francés", "Italiano", "Otros"]

    op = -1
    existe = False
    opc3 = False

    while op != 8:
        print("Menu de opciones:")
        print("1- Generación y Carga")
        print("2- Mostrar")
        print("3- Conteo y género más popular")
        print("4- Búsqueda del mayor")
        print("5- Búsqueda por ISBN")
        print("6- Consulta de un género")
        print("7- Consulta de precio por grupo")
        print("8- Salir")

        op = int(input("Ingrese la opción deseada: "))

        if op == 1:
            libros = opcion1()
            existe = True

        elif op == 2:
            if not existe:
                print("\nNo hay listado para mostrar, generelo con la opción 1")
            else:
                print("\nListado de libros")
                opcion2(libros, generos, idiomas)

        elif op == 3:
            if not existe:
                print("\nNo hay listado con el que trabajar, generelo con la opción 1")
            else:
                print("\nConteo y género más popular")
                mayor_genero = opcion3(libros, generos)
                opc3 = True

        elif op == 4:
            if not existe:
                print("\nNo hay listado con el que trabajar, generelo con la opción 1")
            else:
                print("\nDeterminar el libro de mayor precio para un idioma i")
                opcion4(libros)

        elif op == 5:
            if not existe:
                print("\nNo hay listado con el que trabajar, generelo con la opción 1")
            else:
                print("\nBúsqueda por ISBN")
                opcion5(libros)

        elif op == 6:
            if not existe:
                print("\nNo hay listado con el que trabajar, generelo con la opción 1")
            elif not opc3:
                print("\nEs necesario obtener el género más numeroso primero, obténgalo con la opción 3")
            else:
                print("\nConsulta del género más numeroso")
                opcion6(libros, mayor_genero)

        elif op == 7:
            if not existe:
                print("\nNo hay listado con el que trabajar, generelo con la opción 1")
            else:
                print("\nConsulta de precio por grupo")
                opcion7(libros)
        elif op == 8:
            print("\nBye Bye...")
        else:
            print("\nValor no válido...Intente de nuevo\n")

        print()


if __name__ == "__main__":
    test()
