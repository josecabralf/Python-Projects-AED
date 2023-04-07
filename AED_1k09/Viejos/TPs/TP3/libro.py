class Libro:
    def __init__(self, cod, tit, gen, idioma, precio):
        self.codigo = cod
        self.titulo = tit
        self.genero = gen
        self.idioma = idioma
        self.precio = precio


def to_string(libro):
    r = ""
    r += "{:<25}".format("ISBN: " + libro.codigo)
    r += "{:<30}".format("Título: " + libro.titulo)
    r += "{:<15}".format("Género: " + str(libro.genero))
    r += "{:<15}".format("Idioma: " + str(libro.idioma))
    r += "{:<20}".format("Precio: " + str(libro.precio))

    return r
