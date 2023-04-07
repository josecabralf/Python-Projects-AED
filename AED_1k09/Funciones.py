# Calcular Promedio de Letras por Palabras
def promedio(total, cantidad):
    prom = 0
    # Evitar n/0
    if cantidad > 0:
        prom = round(total / cantidad, 2)
    return prom


# Porcentaje
def porcentaje(subtotal, total):
    porc = 0
    if total > 0:
        porc = round((subtotal / total) * 100, 2)
    return porc


# Ingresar Texto --- Corroborar final con "."
def ingreso_texto():
    texto = input("Ingrese su texto (finalice con un punto):")
    texto.lower()

    if texto[-1] != ".":
        texto = texto + "."

    return texto


def es_digito(car):
    return car in "0123456789"


def es_vocal(car):
    return car in "aeiouáéíóú"


# Ejemplo de menú standard
def menu():
    cadena = "\nMenu de Opciones\n" \
             "================================\n" \
             "1) Cargar el arreglo de alquileres\n" \
             "2) Cantidad de alquileres que registraron un monto mayor a x\n" \
             "3) Monto total recaudado por cada tipo de cabaña posible\n" \
             "4) Datos de todos los alquileres\n" \
             "5) informe con todos los alquileres que registraron el menor monto\n" \
             "6) Salir\n" \
             "Ingrese su opcion: "
    return int(input(cadena))


# Validar mayor que inf
def validar_mayor_que(inf, mensaje="Ingrese un nro: "):
    valor = int(input(mensaje))
    while valor <= inf:
        print('¡Valor invalido!')
        valor = int(input(mensaje))
    return valor


# Valida entre inf y sup
def validar_entre(inf, sup, mensaje):
    valor = int(input(mensaje))
    while valor < inf or valor > sup:
        print('Valor Invalido!!')
        valor = int(input(mensaje))
    return valor


def validar_mayor_igual_que(desde, mensaje):
    valor = int(input(mensaje))
    while valor < desde:
        print('¡Valor invalido!')
        valor = int(input(mensaje))
    return valor
