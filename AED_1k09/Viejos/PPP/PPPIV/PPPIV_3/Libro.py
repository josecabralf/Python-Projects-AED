import random


class Libro:
    def __init__(self, tit, cod, aut):
        self.titulo = tit
        self.codigo = cod
        self.autor = aut


def to_string(libro):
    r = ""
    r += "{:<16}".format("Código: " + str(libro.codigo))
    r += "{:<14}".format("Título: " + libro.titulo)
    r += "{:<14}".format("Autor: " + libro.autor)
    return r
