class Pedido:
    def __init__(self, nro_ped, cod, desc, imp, cat):
        self.numero = nro_ped
        self.codigo = cod
        self.descripcion = desc
        self.importe = imp
        self.categoria = cat


def to_string(pedido):
    r = ""

    r += "{:<15}".format("Numero: " + str(pedido.numero))
    r += "{:<15}".format("Codigo: " + str(pedido.codigo))
    r += "{:<25}".format("Descripción: " + str(pedido.descripcion))
    r += "{:<20}".format("Importe: " + str(pedido.importe))
    r += "{:<15}".format("Categoria: " + str(pedido.categoria))

    return r


def selection_sort_importes(pedidos):
    n = len(pedidos)
    for i in range(n-1):
        for j in range(i+1, n):
            if pedidos[i].importe > pedidos[j].importe:
                pedidos[i], pedidos[j] = pedidos[j], pedidos[i]


def linear_search_numero(pedidos, nro):
    r = -1
    for i in range(len(pedidos)):
        if nro == pedidos[i].numero:
            return i
    return r
