class Cabaña:
    def __init__(self, documento, monto, tipo):
        self.documento = documento
        self.monto = monto
        self.tipo = tipo


def to_string(cabaña):
    cadena = 'Reseva por Documento: {:<10}'.format(cabaña.documento)
    cadena += ' Moto a pagar: ${:<10.2f}'.format(cabaña.monto)
    cadena += ' Tipo Cabaña: ${:<5}'.format(cabaña.tipo)
    return cadena
