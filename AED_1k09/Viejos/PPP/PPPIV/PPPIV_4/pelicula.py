class Pelicula:
    def __init__(self, id, tit, imp, tipo, pais):
        self.identificacion = id
        self.titulo = tit
        self.importe_p = imp
        self.tipo = tipo
        self.pais = pais


def to_string(pelicula):
    r = ""
    r += "{:<35}".format("Nro. de Identificación: " + str(pelicula.identificacion))
    r += "{:<15}".format("Título: " + pelicula.titulo)
    r += "{:<20}".format("Importe: $" + str(pelicula.importe_p))
    r += "{:<10}".format("Tipo: " + str(pelicula.tipo))
    r += "{:<20}".format("País: " + str(pelicula.pais))
    return r
