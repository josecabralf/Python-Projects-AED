"""
El Comité Argentnio de Atletismo llevo a cabo una prueba atletica de Triatlón, nos solicito un programa que valide lo
anotado por los jueces del evento, para dicho propósito se deben cargar los datos de los tres atletas con mejor
promedio. De cada atleta se conocen Nombre, Tiempo Natacion, Tiempo Ciclismo, Tiempo Corriendo (todo en minutos para
simplificar los calculos).

Usted debe:

Informar tiempo promedio de cada competidor
Determinar el podio, indicando el nombre del primer, segundo y tercer mejor promedio
"""


import random


class Atleta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.natacion = random.randint(10, 20)
        self.ciclismo = random.randint(10, 40)
        self.pedestre = random.randint(10, 25)


def write(atleta):
    print('El Atleta ', atleta.nombre, ' - ',
          'Natacion: ', str(atleta.natacion), ' - ',
          'Ciclismo: ', str(atleta.ciclismo), ' - ',
          'Pedestre: ', str(atleta.pedestre))


def determinar_promedio(atleta):
    suma = atleta.ciclismo + atleta.natacion + atleta.pedestre
    return suma / 3


def test():
    nombre = input('Ingrese el nombre del atleta 1: ')
    atleta1 = Atleta(nombre)
    write(atleta1)
    nombre = input('Ingrese el nombre del atleta 2: ')
    atleta2 = Atleta(nombre)
    write(atleta2)
    nombre = input('Ingrese el nombre del atleta 3: ')
    atleta3 = Atleta(nombre)
    write(atleta3)

    prom1 = determinar_promedio(atleta1)
    prom2 = determinar_promedio(atleta2)
    prom3 = determinar_promedio(atleta3)
    print('El Atleta ', atleta1.nombre, ' hizo ', prom1, ' minutos')
    print('El Atleta ', atleta2.nombre, ' hizo ', prom2, ' minutos')
    print('El Atleta ', atleta3.nombre, ' hizo ', prom3, ' minutos')

    # Determinar el podio, indicando el nombre del primer,
    # segundo y tercer mejor promedio
    if prom1 < prom2 and prom1 < prom3:
        primero = atleta1
        if prom2 < prom3:
            segundo = atleta2
            tercero = atleta3
        else:
            segundo = atleta3
            tercero = atleta2
    elif prom2 < prom3:
        primero = atleta2
        if prom1 < prom3:
            segundo = atleta1
            tercero = atleta3
        else:
            segundo = atleta3
            tercero = atleta1
    else:
        primero = atleta3
        if prom1 < prom2:
            segundo = atleta1
            tercero = atleta2
        else:
            segundo = atleta2
            tercero = atleta1

    print('Podio')
    print('Primero ', end='')
    write(primero)
    print('Segundo ', end='')
    write(segundo)
    print('Tercero ', end='')
    write(tercero)


if __name__ == "__main__":
    test()
