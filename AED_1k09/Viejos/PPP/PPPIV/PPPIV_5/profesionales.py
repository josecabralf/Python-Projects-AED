class Profesional:
    def __init__(self, dni, nom, imp, af, tr):
        self.dni = dni
        self.nombre = nom
        self.importe = imp
        self.afiliacion = af
        self.trabajo = tr


def to_string(prof):
    r = ""
    r += "{:<20}".format("DNI: " + str(prof.dni))
    r += "{:<20}".format("Nombre: " + prof.nombre)
    r += "{:<20}".format("Importe: $" + str(prof.importe))
    r += "{:<18}".format("Afiliación: " + str(prof.afiliacion))
    r += "{:<14}".format("Trabajo: " + str(prof.trabajo))
    return r
