"""
Este es un archivo que contiene funciones relacionadas estrictamente con los procesos de generación y validación de
códigos ISBN 10.
"""
import random


def guion_isbn_random(v):
    """
    Esta función inserta 3 "-" de forma semi-aleatoria, en un vector v que contiene los dígitos de un código ISBN 10
    :param v: Vector con dígitos de un ISBN 10 válido
    :return: Vector v con "-" agregados
    """
    v.insert(len(v)-1, "-")
    # Generacion de Guiones
    g1 = random.randint(1, 7)
    v.insert(g1, "-")
    g2 = random.randint(g1+2, 9)
    v.insert(g2, "-")


def isbn_to_string(v):
    """
    Esta función transforma un código ISBN, cuyos caracteres están almacenados en un vector, en un string, y retorna el
    string creado.
    :param v: vector con caracteres del ISBN (números y "-")
    :return: Código ISBN en formato string
    """
    isbn = ""
    for i in range(len(v)):
        isbn += str(v[i])
    return isbn


def gen_isbn():
    """
    Esta función genera un ISBN de 10 dígitos, separados en 4 grupos con "-", de manera aleatoria y lo retorna.
    :return: Código ISBN en formato string
    """
    v = [0] * 9

    control = 10

    while control > 9:
        acu = 0
        # Generación de Nros
        for i in range(len(v)):
            v[i] = random.randint(0, 9)
            acu += (10-i) * v[i]

        # Digito Control
        control = 11 - (acu % 11)
        if control == 11:
            control = 0

    v.append(control)
    guion_isbn_random(v)
    isbn = isbn_to_string(v)
    return isbn


def sacar_guiones(string):
    """
    Esta función elimina los guiones de un código ISBN 10, añadiendo los dígitos individualmente en un vector y
    retornándolo.
    :param string: Código ISBN 10
    :return: Vector con los dígitos del ISBN
    """
    v = []
    for car in string:
        if car != "-":
            v.append(int(car))
    return v


def validar_isbn(mensaje="Ingrese el código ISBN: "):
    """
    Esta función asegura que un código ISBN 10 ingresado por teclado sea válido, y lo retorna
    :param mensaje: Mensaje mostrado indicando qué se debe ingresar por teclado
    :return: Código ISBN 10 ingresado por teclado
    """
    validez = False

    while not validez:
        # Se supone que ingresa el ISBN con los "-" separadores
        isbn = str(input(mensaje))
        # Sacar guiones
        v = sacar_guiones(isbn)

        acu = 0
        for i in range(len(v)):
            acu += (10-i) * v[i]

        if acu % 11 == 0:
            validez = True
        else:
            print("ERROR... Ese ISBN no es válido")
    return isbn
