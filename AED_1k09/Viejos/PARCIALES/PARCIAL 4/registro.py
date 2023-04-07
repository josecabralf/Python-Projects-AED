class Empleo:
    def __init__(self, nro, desc, mont, city, tipo):
        self.numero = nro
        self.descripcion = desc
        self.monto = mont
        self.ciudad = city
        self.tipo = tipo


def to_string(emp):
    r = ""
    r += "{:<31}".format("Nro. de Identificación: " + str(emp.numero))
    r += "{:<16}".format("Descripción: " + emp.descripcion)
    r += "{:<13}".format("Monto: " + str(emp.monto))
    r += "{:<12}".format("Ciudad: " + str(emp.ciudad))
    r += "{:<10}".format("Tipo: " + str(emp.tipo))
    return r

