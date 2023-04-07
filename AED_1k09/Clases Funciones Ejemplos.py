import random
# Iniciar Clase


class Libro:
    def __init__(self, cod, tit, gen, idioma, precio):
        self.codigo = cod
        self.titulo = tit
        self.genero = gen
        self.idioma = idioma
        self.precio = precio


# Pasarla a string. "libro" es un vector.
def to_string(libro):
    r = ""
    r += "{:<25}".format("ISBN: " + libro.codigo)
    r += "{:<30}".format("Título: " + libro.titulo)
    r += "{:<15}".format("Género: " + str(libro.genero))
    r += "{:<15}".format("Idioma: " + str(libro.idioma))
    r += "{:<20}".format("Precio: " + str(libro.precio))

    return r


# Hacer Carga manual en un vector
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


# Hacer Carga automática en un vector
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


# Carga
def add_in_order(p, paciente):
    """
    Agregar elemento en orden, binario
    :param p: Vector al que se agrega
    :param paciente: Elemento agregado
    :return: -
    """
    izq, der = 0, len(p) - 1
    pos = 0

    while izq <= der:
        med = (izq + der) // 2
        if p[med].nombre == paciente.nombre:
            pos = med
            break

        if paciente.nombre < p[med].nombre:
            der = med - 1
        else:
            izq = med + 1

    if izq > der:
        pos = izq

    p[pos:pos] = [paciente]


def cargar_arreglo_ordenado():
    p = []
    n = int(input("Ingrese el nro de pacientes a cargar: "))

    for i in range(n):
        hc = random.randint(0, 9999)
        nom = random.choice("QWERTYUIOPASDFGHJKLZXCVBNM")
        dias = random.randint(1, 365)
        cod = random.randint(0, 9)
        paciente = Paciente(hc, nom, dias, cod)
        add_in_order(p, paciente)

    return p


# Matriz
# Generar Matriz de Conteo
def generar_matriz(v, filas, columnas):
    mat = [[0] * columnas for i in range(filas)]
    for prof in v:
        f = prof.afiliacion
        c = prof.tipo
        mat[f][c] += 1
    return mat


# Mostrar Matriz de Conteo
def mostrar_matriz(mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if mat[f][c] > 0:
                print("Para el tipo de afiliación {} y el tipo de trabajo {} hay {} profesionales"
                      .format(f, c, mat[f][c]))
