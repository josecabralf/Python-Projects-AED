class Libro:
    def __init__(self, tit, rev, year, idi, rat, isbn):
        self.titulo = tit
        self.revisiones = rev
        self.year = year
        self.idioma = idi
        self.rating = rat
        self.isbn = isbn


def to_string(libro):
    r = ""
    r += "Título: " + libro.titulo + " | "
    r += "Revisiones: " + str(libro.revisiones) + " | "
    r += "Año: " + str(libro.year) + " | "
    r += "Idioma: " + str(libro.idioma) + " | "
    r += "Rating: " + str(round(libro.rating, 2)) + " | "
    r += "ISBN: " + libro.isbn + " | "
    return r
